#!/usr/bin/env python

# trivial "twitter"-like API.

from __future__ import with_statement
import bottle
import sqlite3
from json import dumps as json_dumps, loads as json_lds

__author__ = 'Jason Pepas'
__version__ = '0.0.1'
__license__ = 'MIT'


# functions

errors = {
    404001: (404001, "No such tweet."),
    404002: (404002, "No such page."),
}

resources = [
    ("/", ["GET"]),
    ("/spec", ["GET"]),
    ("/tweets/{tweet_id}", ["GET"]),
    ("/tweets/pages/{pagenum}", ["GET"]),
#    ("/tweets/{tweet_id}/like", ["POST"]),
#    ("/users", ["GET"]),
#    ("/users/{user}/tweets", ["GET"]),
#    ("/users/{user}/tweets", ["POST"]),
]


@bottle.error(404)
def error404(error):
    bottle.response.content_type = 'application/json'
    try:
        (code, message) = error.body
        return json_dumps({"schema":"api_error1", "code":code, "message":message})
    except:
        return error.body


@bottle.route('/')
def get_index():
    return resources_as_dict()

def resources_as_dict():
    return {"schema":"resources1", "resources": [{"url":url, "methods": methods} for (url,methods) in resources]}


@bottle.route('/spec')
def get_spec():
    bottle.response.content_type = 'text/plain'
    with open('spec.yaml') as f:
        return f.read()


@bottle.route('/tweets/<tweet_id>')
def get_tweet(tweet_id):
    tweet = db_query_tweet(tweet_id)
    if tweet is None:
        bottle.abort(404, errors[404001])
    d = db_tweet_as_dict(tweet)
    return d

def db_tweet_as_dict(tweet):
    (tweet_id, user, name, body, timestamp) = tweet
    return {"schema":"tweet1", "tweet_id":tweet_id, "user":user, "name":name, "body":body, "timestamp":timestamp}

def db_query_tweet(tweet_id):
    return cur.execute("""
        select tweets.id, users.user, users.name, tweets.body, tweets.timestamp
        from tweets
        join users on tweets.user_id = users.id
        where tweets.id = ?
        limit 1
        """, (tweet_id,)).fetchone()


@bottle.route('/tweets/pages/<pagenum>')
def get_tweet_page(pagenum):
    (index, offset) = pagenum_to_index_and_offset(pagenum)
    count = pagesize
    tweets = db_query_tweets(index, count)
    if len(tweets) == 0:
        bottle.abort(404, errors[404002])
    d = db_tweets_as_dict(tweets)
    return d

def pagenum_to_index_and_offset(pagenum):
    pagenum = int(pagenum)
    index = (pagenum - 1) * pagesize
    offset = index * pagesize
    return (index, offset)  

def db_tweets_as_dict(tweets):
    return { "schema":"tweets1", "tweets": [ {"schema":"tweet1", "tweet_id":tweet_id, "user":user, "name":name, "body":body, "timestamp":timestamp} for (tweet_id, user, name, body, timestamp) in tweets] }

def db_query_tweets(index, count):
    return cur.execute("""
        select tweets.id, users.user, users.name, tweets.body, tweets.timestamp
        from tweets
        join users on tweets.user_id = users.id
        order by tweets.id
        limit ?
        offset ?
        """, (count, index)).fetchall()


if __name__ == "__main__":
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    pagesize = 50
    bottle.run(host='localhost', port=8080, debug=True)
