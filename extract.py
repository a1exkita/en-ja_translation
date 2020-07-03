import os
import xml.etree.ElementTree as ET


# def extract(en, ja):
#     tree_en, tree_ja = ET.parse(en), ET.parse(ja)
#     root_en, root_ja = tree_en.getroot(), tree_ja.getroot()
#     for i, doc in enumerate(root_en.find('srcset').findall('doc')):
#         for j, sentence in enumerate(doc.findall('seg')):
#             print(sentence.text, end='\t', file=output)
#             print(root_ja.find('refset').findall('doc')[i].findall('seg')[j].text, file=output)

# with open('extract', 'w') as output:
#     for filename in sorted(os.listdir('./')):
#         if filename.endswith("en.xml"):
#             en = filename
#             continue
#         elif filename.endswith('ja.xml'):
#             ja = filename
#             extract(en, ja)
#             continue

with open('extract.raw', 'w') as output:
    for filename in sorted(os.listdir('./')):
        if filename.endswith('ja.xml'):
            tree_ja = ET.parse(filename)
            root_ja = tree_ja.getroot()
            for doc in root_ja.find('refset').findall('doc'):
                for sentence in doc.findall('seg'):
                    print(sentence.text, file=output)

with open('extract_en.raw', 'w') as output:
    for filename in sorted(os.listdir('./')):
        if filename.endswith('en.xml'):
            tree_ja = ET.parse(filename)
            root_ja = tree_ja.getroot()
            for doc in root_ja.find('srcset').findall('doc'):
                for sentence in doc.findall('seg'):
                    print(sentence.text, file=output)

# with open('extract.raw', 'w') as output:
#     for filename in sorted(os.listdir('./corpus')):
#         if filename.endswith('ja.xml'):
#             tree_ja = ET.parse(filename)
#             root_ja = tree_ja.getroot()
#             for doc in root_ja.find('refset').findall('doc'):
#                 for sentence in doc.findall('seg'):
#                     print(sentence.text, file=output)

# with open('extract_en.raw', 'w') as output:
#     for filename in sorted(os.listdir('./corpus')):
#         if filename.endswith('en.xml'):
#             tree_ja = ET.parse(filename)
#             root_ja = tree_ja.getroot()
#             for doc in root_ja.find('srcset').findall('doc'):
#                 for sentence in doc.findall('seg'):
#                     print(sentence.text, file=output)