import pandas as pd
import os

def merge_tsv_files(tsv_files):
    data = []

    for tsv_file in tsv_files:
        df = pd.read_csv(tsv_file, sep='\t', header=None, names=['text'])
        target_label = os.path.basename(tsv_file).replace('_test.tsv', '')
        
        for index, row in df.iterrows():
            data.append({ 'textid': None, 'text': row['text'],'condition': target_label,'target':  None })
    
    final_df = pd.DataFrame(data)
    final_df['textid'] = range(1, len(final_df) + 1)
    final_df = final_df[['textid', 'text', 'condition', 'target']]
    final_df.to_csv('test_data_16.tsv', sep='\t', index=False)


names = ['AbstractAlgebra', 'Algebra','Calculus', 'DiscreteMathematics', 'Geometry',  'LinearAlgebra', 'Logic', 'NumberTheory', 'Topology' ]

tsv_files = []
for name in names:
    s = name + '_test.tsv'
    tsv_files.append(s)
merge_tsv_files(tsv_files)
