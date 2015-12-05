#!/usr/bin/env python

# trivial "twitter"-like API.

# API endpoints:

# GET /tweets/pages/:pagenum
# GET /tweets/:id
# POST /tweets/:id/like
# GET /users
# GET /users/:id/tweets
# POST /users/:id/tweets


from bottle import route, run
import sqlite3

# functions

@route('/')
def get_index():
    return endpoints

@route('/tweets/pages/<pagenum>')
def get_tweets_page(pagenum):
    (index, offset) = pagenum_to_index_and_offset(pagenum)
    count = pagesize
    tweets = db_query_tweets(index, count)
    json = db_tweets_as_json(tweets)
    return json

def pagenum_to_index_and_offset(pagenum):
    pagenum = int(pagenum)
    index = (pagenum - 1) * pagesize
    offset = index * pagesize
    return (index, offset)  

def db_tweets_as_json(tweets):
    # example output:
    # { "tweets": [ { "id":1, "user":"mshelley", "body":"Hello, world!" } ] }
    return { "tweets": [ {"id":tweet_id, "user":user, "body":body} for (tweet_id, user, body) in tweets] }

def db_query_tweets(index, count):
    return cur.execute("""
        select tweets.id, users.user, tweets.body
        from tweets
        join users on tweets.user_id = users.id
        limit ?
        offset ?""", (count, index))

# globals

base_url = "http://example.com"

endpoints = {"resources":[
    {"method":"GET", "url":"%s/" % base_url},
    {"method":"GET", "url":"%s/tweets/pages/:pagenum" % base_url},
    {"method":"GET", "url":"%s/tweets/:id" % base_url},
    {"method":"POST", "url":"%s/tweets/:id/like" % base_url},
    {"method":"GET", "url":"%s/users" % base_url},
    {"method":"GET", "url":"%s/users/:id/tweets" % base_url},
    {"method":"POST", "url":"%s/users/:id/tweets" % base_url},
]}

# main

if __name__ == "__main__":
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    pagesize = 50
    run(host='localhost', port=8080, debug=True)
