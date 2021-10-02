#!/usr/bin/env python3
"""
Utilities for project 2
Gets the HTML for a specified website and searches for all of the links within
anchor tags.
"""
from logging import exception
import re
import requests
import bs4

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

def get_links_from_url(url, request_handler = requests):
    """
    Retrieves all of the links from the website at the specified URL
    Args: url - The URL for the webpage to search
          request_handler - The module or class that will handle making requests.
    Return: The list of links from the website
    """
    href_regex = re.compile(r"(.*://)?(.*)")
    links = []

    response = request_handler.get(url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    tags = soup.find_all("a", href=True)

    for tag in tags:
        links.append(href_regex.match(tag["href"])[2])

    return links

def get_style_for_link(link):
    """
    Gets a special style for non-absolute links (relative, phone, etc).
    Args: link - The specified link to check
    Return: The appropriate style for non-absolute links; otherwise a blank string
    """
    style_patterns = [
        (r"^/", " style='color: goldenrod;'"),
        (r"^#", " style='color: #9f9;'"),
        (r"^tel:", " style='color: #faa;'"),
        (r"^mailto:", " style='color: #f9f;'"),
        (r"^javascript", " style='color: #aaf;'"),
    ]

    for pattern, style in style_patterns:
        regex = re.compile(pattern)
        if regex.match(link) is not None:
            return style
    return ""