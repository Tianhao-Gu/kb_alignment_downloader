# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from pprint import pprint
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
    GIT_COMMIT_HASH = "0b06f733280f51d57bc68ea2378c53447eef4338"

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

    def export_rna_seq_alignment_as_excel(self, ctx, params):
        """
        :param params: instance of type "ExportParams" (input and output
           structure functions for standard downloaders) -> structure:
           parameter "input_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment_as_excel
        params['download_type'] = 'excel'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment_as_excel

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment_as_excel return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def export_rna_seq_alignment_as_tsv(self, ctx, params):
        """
        :param params: instance of type "ExportParams" (input and output
           structure functions for standard downloaders) -> structure:
           parameter "input_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_rna_seq_alignment_as_tsv
        print '--->\nRunning uploadmethods.upload_fastq_file\nparams:'
        params['download_type'] = 'tsv'
        print json.dumps(params, indent=1)

        alignment_downloader = RNASeqAlignmentDownloader(self.config)
        output = alignment_downloader.download_rna_seq_alignment(params)
        #END export_rna_seq_alignment_as_tsv

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_rna_seq_alignment_as_tsv return value ' +
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
