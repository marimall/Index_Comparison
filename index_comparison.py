## imports

import pandas as pd
from scipy.spatial.distance import hamming 
import argparse

### functions

def check_pairs(df):
    return df[df.duplicated()]



def hamming_of_seqs(index, max_dist):
    pairs = []
    for i in index.copy():
        seq = index[i]
        index.pop(i)
        for l in index:
            mis1 = hamming(list(seq), list(index[l])) * len(seq)
            if mis1 <= max_dist:
                pairs.append([i , seq , l, index[l], mis1])
    return pd.DataFrame(pairs, columns = ["Index_1", "Sequence_1","Index_2","Sequence_2", "Diff_Bases"])


### input csv file

parser = argparse.ArgumentParser(description='Find similar indexes',  epilog = "author: Maria Malliarou <maria.malliarou.ger@gmail.com> v1.1" )

parser.add_argument('--input_file',  type = str, required = True, help = "Please provide your excel file. It shoud have four columns named as p7_name, p7_sequence, p5_name, p5_sequence" ) 
parser.add_argument('--max_bases', type = int, default = 2 , help = "Please provide the maximum number of similar bases. Default is 2" ) 



args = parser.parse_args()



indexes = pd.read_excel(args.input_file) # comment if csv

#indexes = pd.read_csv(args.input_file, delimiter = "\t") ## uncomment if csv and change the delimiter if you have other than tab


assert (indexes["p7_sequence"].apply(len) == len(indexes.iloc[0]["p7_sequence"])).all(),"Your p7 indexes do not have the same length"

assert (indexes["p5_sequence"].apply(len) == len(indexes.iloc[0]["p5_sequence"])).all(),"Your p5 indexes do not have the same length"

if not check_pairs(indexes).empty:
    print("There are duplicated pairs in your file which are: \n")
    print(check_pairs(indexes))
    print("\n")
    
p7 = dict(zip(indexes["p7_name"], indexes["p7_sequence"]))
p7_seqs = hamming_of_seqs(p7, args.max_bases)
p5 = dict(zip(indexes["p5_name"], indexes["p5_sequence"]))
p5_seqs = hamming_of_seqs(p5, args.max_bases)

if p7_seqs.empty:
    print(f"There are no p7 indexes with less than {args.max_bases} similar bases \n")
else:
    print(f"The p7 sequences similar for less than {args.max_bases} are: \n")
    print(p7_seqs)

if p5_seqs.empty:
    print(f"There are no p5 indexes with less than {args.max_bases} similar bases \n")
else:
    print(f"The p5 sequences similar for less than {args.max_bases} are: \n")
    print(p5_seqs)