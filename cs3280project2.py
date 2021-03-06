#!/usr/bin/env python3
"""
This script runs an HTTP server that accepts a url as a resource, then
retrieves all of the links from the anchor tags of the webpage.
"""
import http.server
import socket
import utils

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

class Project2Server(http.server.BaseHTTPRequestHandler):
    """
    HTTP server made for handling requests to gather links on webpages
    """
    URL_QUERY = "pages?"

    def do_GET(self):
        #pylint: disable=invalid-name
        """
        Overrides do_GET()
        Handles GET requests to the server
        Args: None
        Return: None
        """
        try:
            resource = self.path[1:]

            if not resource.startswith(self.URL_QUERY):
                self.log_message("resource: %s", self.path)
                self.send_error(404, f"Expecting {self.URL_QUERY}<url>")

            query = self.get_query_from_resource(resource)
            body = create_message_body(query)

            self.complete_response(body)

        except ValueError as exception:
            self.send_error(500, str(exception))
        #Prevents the terminal from being filled with error messages
        except socket.error:
            pass

    def get_query_from_resource(self, resource):
        """
        Gets the query from the request's resource
        Args: resource - the resource from the request
        Return: The resource's query
        """
        start_index = len(self.URL_QUERY)
        return resource[start_index:]

    def complete_response(self, body):
        """
        Attaches the response body and sends it to the requester.
        Args: body - The response page's HTML
        Return: None
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(body, "UTF-8"))

def create_message_body(query):
    """
    Creates the HTML for the response.
    Args: query - The queried URL
    Return: The response page's HTML
    """

    links = utils.get_links_from_url(query)

    body = "<!DOCTYPE html>\n"
    body += "<html>\n<head>\n<head>\n"
    body += "<body style='color: #ccc; background-color: #111'>\n"

    body += "<h1>"
    body += f"Links found in <a style='color: #66f' href='{query}'>{query}</a>:"
    body += "</h1>\n"

    body += "<ul>\n"
    for link in links:
        style = utils.get_style_for_link(link)
        body += f"<li><span{style}>{link}</span></li>\n"
    body += "</ul>\n"

    body += "</body></html>"

    return body

def main():
    """
    Entry point for the script
    """
    server_address_tuple = ("localhost", 3280)
    server = http.server.HTTPServer(server_address_tuple, Project2Server)
    server.serve_forever()

if __name__ == "__main__":
    main()
