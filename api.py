#!/usr/bin/env python

# trivial "twitter"-like API.

# API endpoints:

# GET /tweets/pages/1
# GET /tweets/:id
# POST /tweets/:id/like
# GET /users
# GET /users/:id/tweets
# POST /users/:id/tweets


from bottle import route, run

@route('/')
def get_index():
    return "Tweets API running..."

@route('/tweets/pages/<pagenum>')
def get_page(pagenum):
    return "page %s" % pagenum

run(host='localhost', port=8080, debug=True)
