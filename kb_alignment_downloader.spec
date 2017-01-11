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

    funcdef export_rna_seq_alignment_as_excel(ExportParams params) returns (ExportOutput output) authentication required;

    funcdef export_rna_seq_alignment_as_tsv(ExportParams params) returns (ExportOutput output) authentication required;
};
