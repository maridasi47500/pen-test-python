#!/usr/bin/env python3
"""
License: MIT License
Copyright (c) 2023 Miel Donkers

Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import urllib
from urllib.parse import urlparse, parse_qs

from hello import Hello
from erreur import Erreur
from route import Route
from render import Render
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
ROUTE={"/":"hello#hi"}

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params=parse_qs(parsed_path.query) | {}
        if parsed_path.path.startswith("/echo"):
           message = '\n'.join([  'CLIENT VALUES:',
           'client_address=%s (%s)' % (self.client_address, self.address_string()),
           'command=%s' % self.command,
           'path=%s' % self.path,
           'real path=%s' % parsed_path.path,
           'query=%s' % parsed_path.query,
           'request_version=%s' % self.request_version,
           '',
           'HEADERS:',
           '%s' % self.headers,])
           self.send_response(200)
           self.end_headers()
           self.wfile.write(message.encode('utf-8'))
        else:
           logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
           self._set_response()

            #mytext="<nav><a href=\"hack\">hacks de python</a><a href=\"bibliohteque\">bibliotheue de python</a></nav><main><h1>hi</h1><p>vous êtes sur la page{}</p><p></p></main>".format(self.path)
           print(params)
           print("myparams")
           mytext=Route().get_route(myroute=self.path.split("?")[0],myparams=params)

           self.wfile.write(mytext)

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
