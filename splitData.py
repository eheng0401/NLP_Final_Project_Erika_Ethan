import csv
import random

def read_tsv(fpath):
    with open(fpath, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        data = [row for row in reader]
    return data

def split_data(data):
    random.shuffle(data)
    train_idx = int(0.8 * len(data))
    val_idx = int(0.9 * len(data))
    train_data = data[:train_idx]
    val_data = data[train_idx:val_idx]
    test_data = data[val_idx:]

    return train_data, val_data, test_data

def write_tsv(data, file_path): #for testing data
    with open(file_path + '.tsv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(data)

def write_txt(data, file_path): #for train and val data
    with open(file_path, mode='w') as file:
        for row in data:
            file.write("\t".join(row) + "\n")

def split_file(filename):
    data = read_tsv(filename)
    train_data, val_data, test_data = split_data(data)
    train_txt_file = filename.removesuffix('.tsv') + '_train'
    val_txt_file = filename.removesuffix('.tsv') + '_val'
    write_txt(train_data, train_txt_file)
    write_txt(val_data, val_txt_file)

    test_file = filename.removesuffix('.tsv') + '_test'
    write_tsv(test_data, test_file)

def main():
    file_names =['AbstractAlgebra', 'Algebra','Calculus', 'DiscreteMathematics', 'Geometry',  'LinearAlgebra', 'Logic', 'NumberTheory', 'Topology' ]

    # print(len(file_names))   ->9

    for file in file_names:
        name = file + '.tsv'
        split_file(name)
    # split_file('AbstractAlgebra.tsv') tested on first

if __name__ == "__main__":
    main()












