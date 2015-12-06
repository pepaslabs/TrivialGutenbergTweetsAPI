# TrivialGutenbergTweetsAPI
A trivial twitter-like API, populated with data from Project Gutenberg.

## Dependencies

`populate_db.py` needs the `nltk` python module:

```bash
sudo pip install nltk
```

More specifically, it needs the `punkt` tokenizer models which are part of `nltk`.  Fire up a `python` REPL, `import nltk` and call `download()`:

```python
$ python
import nltk
nltk.download()
```

This will present you with either a GUI or a terminal menu:
* GUI: Click on the "Models" tab, select `punkt`, then click "Download".
* terminal: enter `d` at the `Download>` prompt, then enter `punkt` at the `Identifier>` prompt.

## Bootstrapping

* Run `bootstrap.sh`.  This will:
  * Create an SQLite database (`db.sqlite3`)
  * Download 10 books from [gutenberg.com](https://www.gutenberg.org)
  * Parse each book into sentences and insert them into the database as (about 50,000) "tweets".
* Run `api.py`
* Point your web browser at http://localhost:8080

