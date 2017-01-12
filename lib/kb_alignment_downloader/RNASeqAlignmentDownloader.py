
import os
import json
import shutil
import zipfile
from DataFileUtil.DataFileUtilClient import DataFileUtil


def log(message):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(message)

class RNASeqAlignmentDownloader:

	def __init__(self, config):
		log('--->\nInitializing RNASeqAlignmentDownloader instance:\n config: %s' % config)
		self.scratch = config['scratch']
		self.callback_url = config['SDK_CALLBACK_URL']
		self.token = config['KB_AUTH_TOKEN']
		self.dfu = DataFileUtil(self.callback_url, token=self.token)

	"""
	download_rna_seq_alignment: RNASeq Alignment Downloader

	params: 
	input_ref: RNASeq-Alignment file ref ID
	download_type: download type for web source fastq file

	returns:
	shock_id: Shock ID of downloadable file in download_type format

	"""
	def download_rna_seq_alignment(self, params):
		log('--->\nrunning RNASeqAlignmentDownloader.download_rna_seq_alignment:\nparams: %s' % params)

		# validate params 
		self.validate_download_rna_seq_alignment_parameters(params)

		returnVal = self._download_rna_seq_alignment(input_ref=params.get('input_ref'), download_type=params.get('download_type'))

		return returnVal

	"""
	validate_download_rna_seq_alignment_parameters: validates params passed to download_rna_seq_alignment method

	"""
	def validate_download_rna_seq_alignment_parameters(self, params):
				
		# check required parameters
		for p in ['input_ref', 'download_type']:
			if p not in params:
				raise ValueError('"' + p + '" parameter is required, but missing')	

		# check supportive download types
		valid_download_types =  ['zip', 'accepted_bam', 'accepted_sam', 'unsorted_bam']
		if params['download_type'] not in valid_download_types:
			raise ValueError('download type: %s is not supported' % params['download_type'])

	"""
	_download_rna_seq_alignment: download RNASeq Alignment's archive zip file or 'accepted_hits.bam', 'accepted_hits.sam' or 'accepted_hits_unsorted.bam' from RNASeq Alignment's archive file

	params: 
	input_ref: RNASeq-Alignment file ref ID
	download_type: download file type 
	               'zip' -> original archive zip file
	               'accepted_bam' -> unpacked 'accepted_hits.bam' file
	               'accepted_sam' -> unpacked 'accepted_hits.sam' file
	               'unsorted_bam' -> unpacked 'accepted_hits_unsorted.bam' file

	returns:
	shock_id: Shock ID of downloadable accepted_hits.bam file

	"""
	def _download_rna_seq_alignment(self, input_ref, download_type):
		
		# get object data
		object_data = self._get_object_data(input_ref)

		# get handle data
		handle = self._get_handle_data(object_data)

		# make tmp directory for downloading
		dstdir = os.path.join(self.scratch, 'tmp')
		if not os.path.exists(dstdir):
			os.makedirs(dstdir)

		# download original zip file and save to tmp directory
		handle_id = handle.get('hid')
		original_zip_file_path = self._download_original_zip_file(handle_id, dstdir)

		if download_type == 'zip':
			download_file_path = original_zip_file_path
		else:
			# unzip original zip file
			with zipfile.ZipFile(original_zip_file_path,"r") as zip_ref:
				zip_ref.extractall(dstdir + '/' + original_zip_file_path.rpartition('.')[0].rpartition('/')[-1])

			# get downlaod file name ('accepted_hits.bam', 'accepted_hits.sam' or 'accepted_hits_unsorted.bam')
			download_file_name = self._get_download_file_name(download_type)

			if download_file_name not in os.listdir(original_zip_file_path[:-4]):
				raise ValueError("%s is not available from %s\navailable files:\n%s" % 
								(download_file_name, original_zip_file_path.rpartition('/')[-1], os.listdir(original_zip_file_path[:-4])))
			else:	
				download_file_path = original_zip_file_path[:-4] + '/' + download_file_name

		log ('loading %s to shock' % download_file_path)
		shock_id = self._upload_to_shock(accepted_bam_file_path)

		log('--->\nremoving folder: %s' % dstdir)
		shutil.rmtree(dstdir)

		returnVal = {"shock_id": shock_id}

		return returnVal

	"""
	_get_object_data: get object_data using DataFileUtil

	"""
	def _get_object_data(self, input_ref):

		get_objects_params = {
			'object_refs': [input_ref],
			'ignore_errors': False
		}

		object_data = self.dfu.get_objects(get_objects_params)

		return object_data

	"""
	_get_handle_data: get Handle from object_data

	"""
	def _get_handle_data(self, object_data):

		try:
			handle = object_data.get('data')[0].get('data').get('file')
		except:
			raise ValueError("Unexpected object format. Refer to DataFileUtil.get_objects definition\nobject_data:\n%s" % json.dumps(object_data, indent=1))

		if handle is None:
			raise ValueError("object_data does have Handle(file key)\nobject_data:\n%s" % json.dumps(object_data, indent=1))
		elif handle.get('hid') is None:
			raise ValueError("Handle does have HandleId(hid key)\nhandle_data:\n%s" % json.dumps(handle, indent=1))
		else:
			return handle

	"""
	_download_original_zip_file: download original archive .zip file using DataFileUtil
	
	"""
	def _download_original_zip_file(self, handle_id, dstdir):

		shock_to_file_params = {
			'handle_id': handle_id,
			'file_path': dstdir
		}
		original_zip_file = self.dfu.shock_to_file(shock_to_file_params)

		original_zip_file_path = original_zip_file.get('file_path')

		return original_zip_file_path

	"""
	_upload_to_shock: upload target file to shock using DataFileUtil
	
	"""
	def _upload_to_shock(self, file_path):

		file_to_shock_params = {
			'file_path': file_path
		}
		shock_file = self.dfu.file_to_shock(file_to_shock_params)

		shock_id = shock_file.get('shock_id')

		return shock_id

	"""
	_get_download_file_name: translate download_type to actual file name
	
	"""
	def _get_download_file_name(self, download_type):

		if download_type == 'accepted_bam':
			file_name = 'accepted_hits.bam'
		elif download_type == 'accepted_sam':
			file_name = 'accepted_hits.sam'
		elif download_type == 'unsorted_bam':
			file_name = 'accepted_hits_unsorted.bam'

		return file_name






