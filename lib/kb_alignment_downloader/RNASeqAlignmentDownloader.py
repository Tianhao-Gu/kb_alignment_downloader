
import os
from pprint import pprint
from DataFileUtil.DataFileUtilClient import DataFileUtil


def log(message):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(message)

class RNASeqAlignmentDownloader:

	def __init__(self, config):
		log('--->\nInitializing RNASeqAlignmentDownloader instance:\n config:')
		log(config)
		self.scratch = config['scratch']
		self.callback_url = config['SDK_CALLBACK_URL']
		self.token = config['KB_AUTH_TOKEN']


	"""
	download_rna_seq_alignment: RNASeq Alignment Downloader

	params: 
	input_ref: RNASeq-Alignment file ref ID
	download_type: download type for web source fastq file

	returns:
	shock_id: Shock ID of downloadable file in download_type format

	"""
	def download_rna_seq_alignment(self, params):
		log('--->\nrunning download_rna_seq_alignment:\nparams:\n')
		log(params)

		self.validate_download_rna_seq_alignment_parameters(params)

		if params.get('download_type') == 'excel':
			returnVal = self._download_rna_seq_alignment_as_excel(input_ref=params.get('input_ref'))
		elif params.get('download_type') == 'tsv':
			returnVal = self._download_rna_seq_alignment_as_tsv(input_ref=params.get('input_ref'))

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
		valid_download_types =  ['excel', 'tsv']
		if params['download_type'] not in valid_download_types:
			raise ValueError('download type: %s is not supported' % params['download_type'])


	"""
	_download_rna_seq_alignment_as_excel: download RNASeq Alignment file as excel

	params: 
	input_ref: RNASeq-Alignment file ref ID

	returns:
	shock_id: Shock ID of downloadable file in download_type format

	"""
	def _download_rna_seq_alignment_as_excel(self, input_ref):
		dfu = DataFileUtil(self.callback_url, token=self.token)

		returnVal = {"shock_id": '123456'}
		return returnVal

	"""
	_download_rna_seq_alignment_as_tsv: download RNASeq Alignment file as excel tsv

	params: 
	input_ref: RNASeq-Alignment file ref ID

	returns:
	shock_id: Shock ID of downloadable file in download_type format

	"""
	def _download_rna_seq_alignment_as_tsv(self, input_ref):
		dfu = DataFileUtil(self.callback_url, token=self.token)

		returnVal = {"shock_id": '123456'}
		return returnVal







