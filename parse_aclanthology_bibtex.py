import bibtexparser
from bibtexparser.bparser import BibTexParser
import pickle
from config import anthology_bib, parsed_anthology_bib


def read_and_parse_bibliography():
    parser = BibTexParser(common_strings=False) # set common_strings = True if want to parse months

    with open(anthology_bib) as bibtex_file:
        text = bibtex_file.read()

    lines = text.split('\n')
    processed_text = ''
    new_text_len = 0
    min_year = 2000
    for line in lines:
        l = line.strip()
        if not (l.startswith('month') or l.startswith('doi') or l.startswith('pages') or l.startswith('ID') or 
                l.startswith('publisher') or l.startswith('booktitle') or l.startswith('address') or 
                l.startswith('ENTRYTYPE')):
            processed_text += (line + '\n')
            new_text_len+=1
        if l.startswith('year'):
            year = int(l[8:12])
            if year < min_year:
                print(f'Stop, year: {year}')
                break
    print('Finish text processing')
    print(f'The number of new lines: {new_text_len}')

    new_bib_database = bibtexparser.loads(processed_text, parser)
    print('Finish parsing')
    
    with open(parsed_anthology_bib, 'w') as bibtex_file:
        bibtexparser.dump(new_bib_database, bibtex_file)
    
    return new_bib_database


def read_parsed_bib():
    with open(parsed_anthology_bib) as bibtex_file:
        bib_db = bibtexparser.load(bibtex_file)
    return bib_db


def read_and_store_abstracts_in_pickle():
    with open(anthology_bib) as bibtex_file:
        text = bibtex_file.read()

    papers = []

    lines = text.split('\n')
    new_paper = {}
    for line in lines:
        l = line.strip()
        if l.startswith('@inproceedings'):
            new_paper = {}
        elif l.startswith('year'):
            year = int(l[8:12])
            new_paper['year'] = year
        elif l.startswith('url'):
            url = l.split('"')[1]
            new_paper['url'] = url
        elif l.startswith('abstract'):
            abstract = l.split(' = ')[1][:-2]
            new_paper['abstract'] = abstract.replace('"', '')
        elif l.startswith('}'):
            papers.append(new_paper)
    with open('papers.pickle', 'wb') as f:
        pickle.dump(papers, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    # read_and_parse_bibliography()
    # read_parsed_bib()
    read_and_store_abstracts_in_pickle()