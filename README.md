# Index_Comparison
Check whether your forward and reverse indexes are similar based on a maximum number of similar bases provided by the user.

Usage:

python3 index_comparison.py --input_file <your_excel_file> --max_bases <int, default = 2>

The excel file should have four columns named as p7_name, p7_sequence, p5_name, p5_sequence. Check test file to view the format.
Although the code will throw an error otherwise, always make sure that you have the same number of nucleotides in all of your indexes.
All indexes need to be all either uppercase or lowcase and STRICTLY in English.

NOTE: This code does not save any result, it just prints the pairs in your terminal. In case you want to save ii ni a text file, just type

python3 index_comparison.py --input_file <your_excel_file> --max_bases <int, default = 2> > output.txt
