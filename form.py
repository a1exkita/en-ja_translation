import os

with open('ns_subword_extract.bpe') as ja:
    with open('extract_en.raw') as en:
        with open('tedcorpus.bpe.3000.en-ja', 'w') as ted:
            ja_lines = ja.readlines()
            en_lines = en.readlines()
            for i in range(len(ja_lines)):
                line = en_lines[i].strip() + '\t' + ja_lines[i]
                ted.write(line)