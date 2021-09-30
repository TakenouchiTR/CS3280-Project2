#!/usr/bin/env python3
"""
Utilities for project 2
Gets the HTML for a specified website and searches for all of the links within
anchor tags.
"""
import bs4
import requests
import re

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

def get_links_from_url(url):
    """
    Retrieves all of the links from the website at the specified URL
    Args: url - The URL to search
    Return: The list of links from the website
    """
    href_regex = re.compile(r"(.*://)?(.*)")

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    tags = soup.find_all("a", href=True)
    links = []

    for tag in tags:
        if href_regex.match(tag["href"]) != None:
            links.append(href_regex.match(tag["href"])[2])
    
    return links