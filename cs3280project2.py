#!/usr/bin/env python3
import sys
import http.server
import socket
import utils

__author__ = 'CS3280'
__version__ = 'Fall 2021'
__pylint__ = 'v1.8.3'

class Project2Server(http.server.BaseHTTPRequestHandler):
    url_query = "url="

    def do_GET(self): #pylint: disable=invalid-name
        """
        Overrides do_GET()
        Handles GET requests to the server
        Args: None
        Return: None
        """
        try:
            resource = self.path[1:]
            print(resource)

            if not self.validate_resource(resource):
                self.log_message('resource: %s', self.path)
                self.send_error(404, 'Expecting {}<url>'.format(self.url_query))

            start_index = len(self.url_query)
            query = resource[start_index:].split('&')
            print(query)

            body = self.process_and_respond(query)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))

        except ValueError as exception:
            self.send_error(500, str(exception))
        #Prevents the terminal from being filled with error messages
        except socket.error:
            pass
    
    def validate_resource(self, resource):
        """
        Checks if the resource is in the valid format
        Args: resource - the resource from the request
        Return: True iff the resource starts with "url="; otherwise False
        """
        return resource.startswith(self.url_query)
    
    def get_query_from_resource(self, resource):
        """
        Gets the query from the request's resource
        Args: resource - the resource from the request
        Return: The resource's query
        """
        start_index = len(self.url_query)
        return resource[start_index:].split('&')


def main():
    """
    Entry point for the script
    """
    server_address_tuple = ('localhost', 3280)
    server = http.server.HTTPServer(server_address_tuple, Project2Server)
    server.serve_forever()

if __name__ == "__main__":
    main()