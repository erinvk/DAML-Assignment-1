# Tolstoy in English Translation: 46 Project Gutenberg Ebooks

A corpus of 46 English-language Project Gutenberg editions of works by Leo Tolstoy.

## 1. The Dataset

The corpus contains 46 items across 39 distinct works by Leo Tolstoy (1828–1910) distributed by Project Gutenberg, spanning novels, novellas, short stories and story collections, plays, essays, religious treatises, and one diary volume. Plain texts live in `data/` with metadata in `metadata.csv`, while header- and licence-stripped copies live in `data_cleaned/`.

Fifteen named translators appear across the corpus (including Aylmer Maude with 14 items and Isabel F. Hapgood with 5), while 6 items do not list a translator.

## 2. Motivation

I created this dataset because I wanted to focus on an author whose work is both famous and diverse. Tolstoy is one of the most translated authors in the world. His English translations were produced by a small number of translators with very different backgrounds: making this dataset useful for studying translator styles, genre variation, and Russian-to-English translation patterns. Several works appear in multiple editions or translations, such as *The Kingdom of God Is Within You* (4 items), *What to Do?* (3 items), *Resurrection* (2 items), and *Sevastopol Sketches* (2 items).

## 3. Selection criteria

From Project Gutenberg's catalogue, English `Text` entries listing Leo Tolstoy as first author yield 48 candidate ebooks, of which 46 are included (editions are kept per ebook, so multi-edition works appear more than once). 

Excluded entries were bibliographic indexes (https://www.gutenberg.org/ebooks/59195 *Index of the Project Gutenberg Works of Leon Tolstoy*), front-matter/TOC-only files (https://www.gutenberg.org/ebooks/26660 *Plays: Complete Edition*), multi-author anthologies (https://www.gutenberg.org/ebooks/5741) *Stories by Foreign Authors: Russian*, https://www.gutenberg.org/ebooks/62942 *Modern Short Stories*`), and `Sound` audio editions (https://www.gutenberg.org/ebooks/26581 *Master and Man*, https://www.gutenberg.org/ebooks/28920 *War and Peace, Book 01: 1805*).

The dataset represents only English editions available on Project Gutenberg and not Russian originals or standalone stories from collections.

## 4. Data collection process

Because Project Gutenberg was down at the time of collection (22 November 2026), I used the Wayback Machine's archived Tolstoy author page in Project Gutenberg (https://archive.org/details/gutenberg?tab=collection&query=Tolstoy&and%5B%5D=language%3A%22English%22) to identify ebook IDs by hovering over links, then fetched each plain-text file from the official mirror (https://gutenberg.pglaf.org/cache/epub/)<pg_id>/pg<pg_id>.txt)

## 5. Cleaning and preprocessing

`data/` stores the unmodified Project Gutenberg downloads, while `clean_data.py` writes header- and licence-stripped copies to `data_cleaned/` using the same filenames.

## 6. Structure and codebook

```
DAML-Assignment-1/
    README.md
    metadata.csv
    extract_data.py
    clean_data.py
    check_dataset.ipynb
    requirements.txt
    .gitignore
    data/
        tol_243_forged_coupon.txt
    data_cleaned/
        tol_243_forged_coupon.txt
```

### Codebook for `metadata.csv`

| Variable | Description | Type | Allowed values / missing values |
| --- | --- | --- | --- |
| `id` | Unique item ID | String | `tol_<pg_id>_<slug>` (lowercase letters, digits, underscores); required |
| `file` | Path to raw text file | String | `data/<id>.txt`; required |
| `source` | Source URL of the ebook | String | `https://www.gutenberg.org/ebooks/<pg_id>`; required |
| `licence` | Copyright or licence statement | String | `Public domain in the US (Project Gutenberg eBook #<pg_id>)`; required |
| `title` | Title in ebook header | String | Ebook title text; required |
| `author` | Author of the work | String | `Leo Tolstoy`; required |
| `translator` | Translator named in ebook | String | Translator name; empty if unnamed or editor-only (6 items) |
| `work` | Underlying literary work | Categorical | English work title grouping editions; required |
| `genre` | Genre of main text | Categorical | `novel`, `novella`, `short story`, `short stories`, `children's stories`, `drama`, `essay`, `treatise`, `diary`; required |
| `language` | Language of the text | Categorical | ISO 639-1 code (`en`); required |
| `pg_id` | Project Gutenberg ebook ID | Integer | Positive integer; required |
| `release_date` | Project Gutenberg release date | String | `YYYY-MM-DD` digitization date (1998–2026), not print/original date; required |

Missing values are left empty, and original/print publication dates are omitted.

## 7. Uses and limitations

This corpus can be used for translator attribution or style comparisons, translation studies around 1900, and teaching text preprocessing or stylometry. This dataset should not be used to make claims about Tolstoy's Russian prose, 21st-century English translations, or the true genre proportions of Tolstoy's entire output (which is skewed by Project Gutenberg digitization). Also, do not redistribute any data from the data_cleaned folder, as it does not contain the Project Gutenberg License in the headers/licences. 

A limitation is that the release dates in metadata.csv are from the 21st century for all but 2 works, while all translations were done in the 19th and 20th centuries, as translators worked between roughly 1885 and 1930.

## 8. Ethical and legal aspects

Tolstoy's Russian originals and pre-1931 translations are in the public domain in the US (and in life+70 jurisdictions such as the Netherlands, except Rose Strunsky's translation of The Journal of Leo Tolstoi—translator died 1963, protected until the end of 2033). Redistribution is permitted under the Project Gutenberg License when headers/licences remain intact (as in data/), and the dataset contains no personal or GDPR-sensitive data.

## 9. Licence and citation

The dataset structure, metadata.csv, scripts, notebook, documentation, and data_cleaned/ are released under the MIT License, while data remains subject to the Project Gutenberg License.

If you use this dataset, please cite it as:

Leung, E. Y.-L. (2026). Tolstoy in English Translation: 46 Project Gutenberg Ebooks [Dataset]. GitHub.
