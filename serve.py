#!/usr/bin/env python
 
import os
import sys
import argparse
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting


def parseArgs():
	parser = argparse.ArgumentParser(description="Run a static site development http server.")
	parser.add_argument('-s', '--serve', action='store_const', default=False, const=True, dest='serve', help='start the http server')
	parser.add_argument('-p', '--port', action='store', default=8000, metavar='PORT', dest='port', help='port number to run the http server on')
	return parser.parse_args()

def serve(port):
	os.chdir('public') 
	server = BaseHTTPServer.HTTPServer
	handler = CGIHTTPServer.CGIHTTPRequestHandler
	server_address = ("", port)
	handler.cgi_directories = [""]
	httpd = server(server_address, handler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		print 'goodbye'

def run():
	args = parseArgs()
	print options
	if options.serve == True:
		serve(8000)

if __name__ == "__main__":
	run()