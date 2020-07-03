# English-Japanese Translation

## 🚀 Procedure
1. Extract Japanese and English sentences from xml files with extract.py
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
4. Remove useless spaces from Japanese bpe sentences file with remove_space.py
5. Combine the English sentences file with the Japanese bped sentences file with form.py

  
