# Kindle EBook Clippings Parser, Data Analysis and Markdown Exporter

Part of [QS Ledger](https://github.com/markwk/qs_ledger/)

This set of scripts and notebooks allows you to parse the highlights from a kindle ebook device (like a Paperwhite), to do some simple data analysis and export individual book highlights into separate text files. 

![Data Analysis Example of Highlights](https://github.com/markwk/qs_ledger/raw/master/kindle/kindle_highlights_data_analysis_example.png)

### How to Use: Parser and Data Analysis

Review [QS Ledger's Readme for more generic installation instructions](https://github.com/markwk/qs_ledger/).

1. Connect your kindle ereader device to your computer and collect your "My Clippings.txt" file. Save that file into the data directory. 
2. Open [kindle_clippings_parser.ipynb](https://github.com/markwk/qs_ledger/blob/master/kindle/kindle_clippings_parser.ipynb) in jupyter notebook or jupyter labs, configure and run. This will parse your clippings file into a data frame and export it to several CSV files. 
3. For data analysis, open and run [kindle_clippings_data_analysis.ipynb](https://github.com/markwk/qs_ledger/blob/master/kindle/kindle_clippings_data_analysis.ipynb) for a breakdown of highlights across different time dimensions. 

### How to Use: Markdown Text File Exporter

[kindle_highlights_markdown_exporter.ipynb](https://github.com/markwk/qs_ledger/blob/master/kindle/kindle_highlights_markdown_exporter.ipynb) is an optional notebook that will generates a separate markdown file for each your books with their clippings and highlights. This can be useful for knowledge management and personal research. 

To use, open the notebook and first edit `export_directory` reference to a local directory on your machine. Then run the notebook.  
