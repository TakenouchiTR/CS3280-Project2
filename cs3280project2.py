#!/usr/bin/env python3
import sys
import http.server
import socket
import utils

__author__ = 'CS3280'
__version__ = 'Fall 2021'
__pylint__ = 'v1.8.3'

def main():
    result = utils.get_links("https://www.westga.edu")
    for line in result:
        print(line)

if __name__ == "__main__":
    main()