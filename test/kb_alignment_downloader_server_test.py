# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_alignment_downloader.kb_alignment_downloaderImpl import kb_alignment_downloader
from kb_alignment_downloader.kb_alignment_downloaderServer import MethodContext


class kb_alignment_downloaderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        user_id = requests.post(
            'https://kbase.us/services/authorization/Sessions/Login',
            data='token={}&fields=user_id'.format(token)).json()['user_id']
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_alignment_downloader',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_alignment_downloader'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = kb_alignment_downloader(cls.cfg)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_kb_alignment_downloader_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def getDefaultParams(self):
        default_input_params = {
            'input_ref': '2778/3/1'
        }

        return default_input_params

    def test_contructor(self):
        print '------ Testing Contructor Method ------'
        ret = self.getImpl()
        self.assertIsNotNone(ret.config)
        self.assertIsNotNone(ret.config['SDK_CALLBACK_URL'])
        self.assertIsNotNone(ret.config['KB_AUTH_TOKEN'])
        print '------ Testing Contructor Method OK ------'

    def test_validate_upload_fastq_file_parameters(self):
        print '------ Testing validate_upload_fastq_file_parameters Method ------'
        invalidate_input_params = self.getDefaultParams()
        del invalidate_input_params['input_ref']
        with self.assertRaisesRegexp(ValueError, '"input_ref" parameter is required, but missing'):
            self.getImpl().export_rna_seq_alignment_as_excel(self.getContext(), invalidate_input_params)

        with self.assertRaisesRegexp(ValueError, '"input_ref" parameter is required, but missing'):
            self.getImpl().export_rna_seq_alignment_as_tsv(self.getContext(), invalidate_input_params)

        print '------ Testing validate_upload_fastq_file_parameters Method OK ------'

    def test_export_rna_seq_alignment_as_zip(self):
        print '------ Testing export_rna_seq_alignment_as_zip Method ------'
        params = self.getDefaultParams()
        ret = self.getImpl().export_rna_seq_alignment_as_zip(self.getContext(), params)
        self.assertTrue(ret[0].has_key('shock_id'))

        print '------ Testing export_rna_seq_alignment_as_zip Method OK ------'

    def test_export_rna_seq_alignment_accepted_bam(self):
        print '------ Testing export_rna_seq_alignment_accepted_bam Method ------'
        params = self.getDefaultParams()
        ret = self.getImpl().export_rna_seq_alignment_accepted_bam(self.getContext(), params)
        self.assertTrue(ret[0].has_key('shock_id'))

        print '------ Testing export_rna_seq_alignment_accepted_bam Method OK ------'

    def test_export_rna_seq_alignment_accepted_sam(self):
        print '------ Testing export_rna_seq_alignment_accepted_sam Method ------'
        params = self.getDefaultParams()
        ret = self.getImpl().export_rna_seq_alignment_accepted_sam(self.getContext(), params)
        self.assertTrue(ret[0].has_key('shock_id'))

        print '------ Testing export_rna_seq_alignment_accepted_sam Method OK ------'

    def test_export_rna_seq_alignment_accepted_unsorted_bam(self):
        print '------ Testing export_rna_seq_alignment_accepted_unsorted_bam Method ------'
        params = self.getDefaultParams()
        ret = self.getImpl().export_rna_seq_alignment_accepted_unsorted_bam(self.getContext(), params)
        self.assertTrue(ret[0].has_key('shock_id'))

        print '------ Testing export_rna_seq_alignment_accepted_unsorted_bam Method OK ------'
        









