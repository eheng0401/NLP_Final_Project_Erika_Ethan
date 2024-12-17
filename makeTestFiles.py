import csv
import os

def fill_files(input_file, names, output_directory):
    with open(input_file, 'r', newline='') as infile:
        reader = list(csv.DictReader(infile, delimiter='\t'))
        headers = reader[0].keys()

    for name in names:
        output_file = os.path.join(output_directory, f"{name}_test_final.tsv")
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            for row in reader:
                if row['condition'] == name:
                    row['target'] = 'Positive'
                else:
                    row['target'] = 'Negative'
                writer.writerow(row)

if __name__ == "__main__":
    input_tsv_file = "test_data_16_no_empty.tsv"
    
    names = ['AbstractAlgebra', 'Algebra', 'Calculus', 'DiscreteMathematics', 'Geometry', 'LinearAlgebra', 'Logic', 'NumberTheory','Topology']
    fill_files(input_tsv_file, names, "test_tsv_files")
