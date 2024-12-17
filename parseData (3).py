import json
import csv

# open json, returns dictionary
def load_data(fpath):
    with open(fpath, 'r') as file:
        data = json.load(file)
    return data

def main():
    fpath = 'naturalproofs_proofwiki.json'
    data = load_data(fpath) 
    dataset = data['dataset']   # get dataset part
    theorems = dataset['theorems']
    seen_categories = set()
    for theorem in theorems:
        theorem_contents_string = ""
        toplevel_categories = theorem['toplevel_categories'] # get the toplevel_categories 
        contents = theorem['contents'] # get the contents of theorem
        for content in contents:   # format multi lines of contents into one string
            theorem_contents_string += content + " "
        proofs = theorem['proofs']# get proofs 
        formatted_proofs = []
        for proof in proofs:
            proof_contents_string = ""
            proof_contents = proof['contents']
            for content in proof_contents: # format multi lines of contents into one string
                proof_contents_string += content + " "
            formatted_proofs.append(proof_contents_string)  # add proof_contents_string to formatted_proofs array 
        for category in toplevel_categories:
            seen_categories.add(category)
            with open(f"{category}.tsv", mode='a', newline='') as file:   # create TSV file for category
                writer = csv.writer(file, delimiter='\t')
                writer.writerow([theorem_contents_string])   # write theorem
                # writer.writerows([formatted_proofs])   # write proofs
                for proof in formatted_proofs:
                    writer.writerow([proof])

    definitions = dataset['definitions']
    for definition in definitions:
        categories = definition['categories']# get categories
        for i in range(len(categories)):   # remove the string 'Definitions/' if it appears at the beginning of the string
            categories[i] = categories[i].removeprefix("Definitions/")
        def_contents_string = ''
        contents = definition['contents']
        for content in contents:   # format multi lines of contents into one string
            def_contents_string += content + ' '
        for category in categories: 
            if category in seen_categories: #only add to file if category already exists (definitions have too many categories)
                with open(f"{category}.tsv", mode='a', newline='') as file:   # create TSV file for category
                    writer = csv.writer(file, delimiter='\t')
                    writer.writerow([def_contents_string])   # write theorem


if __name__ == "__main__":
    main()
