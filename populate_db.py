#!/usr/bin/env python

# thanks to http://stackoverflow.com/a/4576110

import nltk.data
import sys
import random
import sqlite3
import codecs

# globals

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# functions

def shuffled_sentences(path):
    fp = codecs.open(path, encoding='utf8')
    data = fp.read()
    sentences = [sentence.replace('\n',' ').replace('\r',' ') for sentence in tokenizer.tokenize(data)]
    random.shuffle(sentences)
    return sentences

# "main"

cur.execute('insert into users (id, user, name) values (?, ?, ?)', (None, 'mshelley', 'Mary Shelley'))
for s in shuffled_sentences('books/mary_shelley_frankenstein.txt'):
    cur.execute('insert into tweets (id, user_id, body) values (?, ?, ?)', (None, 1, s))

con.commit()
con.close()

