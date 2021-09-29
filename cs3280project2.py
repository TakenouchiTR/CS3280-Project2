#!/usr/bin/env python3
import sys
import http.server
import socket
import utils

__author__ = 'CS3280'
__version__ = 'Fall 2021'
__pylint__ = 'v1.8.3'

class Project2Server(http.server.BaseHTTPRequestHandler):
    pass

def main():
    """
    Entry point for the script
    """
    server_address_tuple = ('localhost', 3280)
    server = http.server.HTTPServer(server_address_tuple, Project2Server)
    server.serve_forever()

if __name__ == "__main__":
    main()