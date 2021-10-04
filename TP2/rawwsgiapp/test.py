import pprint
import json

def app(environ, start_response):
    environ_str = str(environ)
    environ_b_str = str.encode(environ_str, 'utf8')
    hw_string = b'Hello World !'
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    yield hw_string
    yield environ_b_str