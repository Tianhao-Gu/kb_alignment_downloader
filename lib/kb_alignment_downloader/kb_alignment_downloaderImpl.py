# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json
from kb_alignment_downloader.RNASeqAlignmentDownloader import RNASeqAlignmentDownloader
#END_HEADER


class kb_alignment_downloader:
    '''
    Module Name:
    kb_alignment_downloader

    Module Description:
    A KBase module: kb_alignment_downloader
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:Tianhao-Gu/kb_alignment_downloader.git"
    GIT_COMMIT_HASH = "071f0241585da7a85eccd704ff8fa0600888fd58"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass

    def export_rna_seq_alignment_accepted_bam(self, ctx, params):
        """
        Download 'accepted_hits.bam' file from RNASeq-Alignment archive zip file

        params: 
            input_ref: RNASeq-Alignment file ref ID

        returns:
            shock_id: Shock ID of downloadable file in download_type format
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment_accepted_bam
        print '--->\nRunning kb_alignment_downloader.export_rna_seq_alignment_accepted_bam\nparams:'
        params['download_type'] = 'accepted_bam'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment_accepted_bam

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment_accepted_bam return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def export_rna_seq_alignment_accepted_sam(self, ctx, params):
        """
        Download 'accepted_hits.sam' file from RNASeq-Alignment archive zip file
        
        params: 
            input_ref: RNASeq-Alignment file ref ID

        returns:
            shock_id: Shock ID of downloadable file in download_type format
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment_accepted_sam
        print '--->\nRunning kb_alignment_downloader.export_rna_seq_alignment_accepted_sam\nparams:'
        params['download_type'] = 'accepted_sam'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment_accepted_sam

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment_accepted_sam return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def export_rna_seq_alignment_accepted_unsorted_bam(self, ctx, params):
        """
        Download 'accepted_hits_unsorted.bam' file from RNASeq-Alignment archive zip file
        
        params: 
            input_ref: RNASeq-Alignment file ref ID

        returns:
            shock_id: Shock ID of downloadable file in download_type format
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment_accepted_unsorted_bam
        print '--->\nRunning kb_alignment_downloader.export_rna_seq_alignment_accepted_unsorted_bam\nparams:'
        params['download_type'] = 'unsorted_bam'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment_accepted_unsorted_bam

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment_accepted_unsorted_bam return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def export_rna_seq_alignment_as_zip(self, ctx, params):
        """
        Download original archive zip file from RNASeq-Alignment
        
        params: 
            input_ref: RNASeq-Alignment file ref ID

        returns:
            shock_id: Shock ID of downloadable file in download_type format
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment_as_zip
        print '--->\nRunning kb_alignment_downloader.export_rna_seq_alignment_as_zip\nparams:'
        params['download_type'] = 'zip'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment_as_zip

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment_as_zip return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def export_rna_seq_alignment(self, ctx, params):
        """
        Dynamically download RNASeq Alignment's archive zip file or 'accepted_hits.bam', 'accepted_hits.sam' or 'accepted_hits_unsorted.bam' from RNASeq Alignment's archive file

        params: 
            input_ref: RNASeq-Alignment file ref ID
            download_type: download file type 
                   'zip' -> original archive zip file
                   'accepted_bam' -> unpacked 'accepted_hits.bam' file
                   'accepted_sam' -> unpacked 'accepted_hits.sam' file
                   'unsorted_bam' -> unpacked 'accepted_hits_unsorted.bam' file
                   
        returns:
            shock_id: Shock ID of downloadable file in download_type format
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment
        print '--->\nRunning kb_alignment_downloader.export_rna_seq_alignment\nparams:'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
