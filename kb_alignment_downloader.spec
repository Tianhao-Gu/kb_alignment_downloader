/*
A KBase module: kb_alignment_downloader
*/

module kb_alignment_downloader {

    /*  input and output structure functions for standard downloaders */
    typedef structure {
        string input_ref;
    } ExportParams;

    typedef structure {
        string shock_id;
    } ExportOutput;

    funcdef export_rna_seq_alignment_accepted_bam (ExportParams params) returns (ExportOutput output) authentication required;

    funcdef export_rna_seq_alignment_accepted_sam (ExportParams params) returns (ExportOutput output) authentication required;

    funcdef export_rna_seq_alignment_accepted_unsorted_bam (ExportParams params) returns (ExportOutput output) authentication required;

    funcdef export_rna_seq_alignment_as_zip (ExportParams params) returns (ExportOutput output) authentication required;

    /*  input structure function for dynamic downloader */
    typedef structure {
        string input_ref;
        string download_type;
    } GeneralExportParams;

    funcdef export_rna_seq_alignment (GeneralExportParams params) returns (ExportOutput output) authentication required;

};
