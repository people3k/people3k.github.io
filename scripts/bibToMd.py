import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

with open('../data/p3k14c_refs.bib') as f:
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(f, parser=parser)

def formatAuthors(authorstr):
    authors = ''
    alist = authorstr.split(' and ')
    for a in alist:
        last,first = a.split(', ')
        authors += '{} {}, '.format(first,last)
    return authors[:-2]

print('|Source|Author(s)|Year|Title|')
print('|------|---------|----|-----|')
for entry in bib_database.entries:
    source  = entry['ID'].replace('_',' ')
    authors = entry['author'].replace('\n',' ')
    authors = formatAuthors(authors)
    year    = entry['year']
    title   = entry['title'].replace('\n',' ')
    if 'howpublished' in entry.keys():
        url = entry['howpublished'][3:]
        title += ' [{}]({})'.format(url,url)
    print(f'|**{source}**|{authors}|{year}|{title}|')
