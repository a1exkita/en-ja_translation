with open('subword_extract.bpe', 'rt') as fin:
    with open('ns_subword_extract.bpe', 'wt') as fout:
        for line in fin:
            fout.write(line.replace('\\ ', ''))