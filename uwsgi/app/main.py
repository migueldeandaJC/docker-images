#!/usr/bin/env python
def app(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    return ["uWSGI ready"]
