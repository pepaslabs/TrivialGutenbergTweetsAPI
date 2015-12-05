#!/usr/bin/env python

# thanks to http://stackoverflow.com/a/4576110

import nltk.data
import sys
import random
import sqlite3
import codecs

# functions

def shuffled_sentences(path):
    fp = codecs.open(path, encoding='utf8')
    data = fp.read()
    sentences = [sentence.replace('\n',' ').replace('\r',' ').replace('  ',' ') for sentence in tokenizer.tokenize(data)]
    random.shuffle(sentences)
    return sentences

def process_book(book, user, name):
    print "processing", book
    cur.execute('insert into users (id, user, name) values (?, ?, ?)', (None, user, name))
    user_id = cur.lastrowid
    for s in shuffled_sentences(book):
        cur.execute('insert into tweets (id, user_id, body) values (?, ?, ?)', (None, user_id, s))


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

process_book('books/pride_and_prejudice.txt', 'jausten', 'Jane Austen')
process_book('books/alices_adventures_in_wonderland.txt', 'lcarroll', 'Lewis Carroll')
process_book('books/frankenstein.txt', 'mshelley', 'Mary Shelley')
process_book('books/adventures_of_huckleberry_finn.txt', 'mtwain', 'Mark Twain')
process_book('books/adventures_of_sherlock_holmes.txt', 'adoyle', 'Arthur Conan Doyle')
process_book('books/moby_dick.txt', 'hmelville', 'Herman Melville')
process_book('books/a_modest_proposal.txt', 'jswift', 'Jonathan Swift')
process_book('books/the_picture_of_dorian_gray.txt', 'owilde', 'Oscar Wilde')
process_book('books/metamorphosis.txt', 'fkafka', 'Franz Kafka')
process_book('books/a_tale_of_two_cities.txt', 'cdickens', 'Charles Dickens')

con.commit()
con.close()
