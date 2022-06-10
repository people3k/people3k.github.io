import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

with open('../data/p3k14c_refs.bib') as f:
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(f, parser=parser)

print('|Source|Author(s)|Year|Title|')
print('|------|---------|----|-----|')
for entry in bib_database.entries:
    source  = entry['ID']
    authors = entry['author']
    year    = entry['year']
    title   = entry['title']
    if 'howpublished' in entry.keys():
        url = entry['howpublished'][3:]
        title += ' [{}]({})'.format(url,url)
    print(f'|{source}|{authors}|{year}|{title}|')
