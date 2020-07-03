# English-Japanese Translation

## 🚀 Procedure
0. Download [TED](https://wit3.fbk.eu/archive/2017-01-trnted//texts/en/ja/en-ja.tgz) corpus and put "en-ja" file to the root directory
1. Extract Japanese and English sentences from xml files with extract.py
    - generates extract.raw and extract_en.raw
2. Do word segmentation for Japanese sentences by using Kytea
  ```
  git clone https://github.com/neubig/kytea.git
  cd kytea
  brew install automake # if not having it
  autoreconf -i
  ./configure
  make
  make install
  kytea --help # make sure it is installed
  kytea < extract.raw > extract.full -notags -nounk
  ```
3. Apply bpe to Japanese sentences by using subword-nmt
  ```
  pip install subword-nmt
  subword-nmt learn-bpe -s 3000 < extract.full > extract.bpe
  subwrod-nmt apply-bpe -c extract.bpe < extract.full > subword_extract.bpe
  ```
  - To check if it is applied,
  ```
  python check_bpe.py input output
  ```
4. Remove useless spaces from Japanese bpe sentences file with remove_space.py
    - generates ns_subword_extract.bpe
5. Combine the English sentences file with the Japanese bped sentences file with form.py
    - generates tedcorpus.bpe.3000.en-ja
  
