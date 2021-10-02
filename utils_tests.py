#!/usr/bin/env python3
"""
Tests for the utils.py lirary
"""
import unittest
import requests
import utils

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

class FakeResponse:
    #pylint: disable=too-few-public-methods
    """
    A fake response object used for providing a consistent input to
    the utils module.
    """
    text = ""

    def get(url):
        #pylint: disable=unused-argument
        #pylint: disable=no-self-argument
        #pylint: disable=no-self-use
        """
        Creates a FakeResponse with multiple anchor tags as the text
        Args: url - Unused variable to match the requests get() function
        Return: A FakeResponse with text for testing
        """
        response = FakeResponse()
        text = "<a href='https://www.example.com'></a>"
        text += "<a href='www.example.org'></a>"
        text += "<a href='tel:1234567890'></a>"
        text += "<a href='mailto:example@example.com'></a>"
        text += "<a href='/dir/page.html'></a>"
        text += "<a href='#id'></a>"
        text += "<a href='javascript:void(0);'></a>"
        response.text = text
        return responseclass TestGetLinksFromUrl(unittest.TestCase):
    """
    Tests for the get_links_from_url() function
    """
    def test_valid_response_text(self):
        """
        Checks if a valid response is scraped correctly
        """
        url = "https://www.example.com"
        links = utils.get_links_from_url(url, FakeResponse)
        expected_links = [
            "www.example.com",
            "www.example.org",
            "tel:1234567890",
            "mailto:example@example.com",
            "/dir/page.html",
            "#id",
            "javascript:void(0);",
        ]

        self.assertEqual(links, expected_links)

    def test_request_handler_lacks_get_function(self):
        """
        Checks that an AttributeError is raised if request_handler
        lacks a get() function
        """
        url = "https://www.example.com"
        with self.assertRaises(AttributeError):
            utils.get_links_from_url(url, True)

    def test_none_for_url(self):
        """
        Checks that a MissingSchema exception is raised if None is used
        as the url
        """
        with self.assertRaises(requests.exceptions.MissingSchema):
            utils.get_links_from_url(None)

    def test_empty_string(self):
        """
        Checks that a MissingSchema exception is raised if an empty string
        is used for the url
        """
        with self.assertRaises(requests.exceptions.MissingSchema):
            utils.get_links_from_url("")

    def test_url_without_protocol(self):
        """
        Checks that a MissingSchema exception is raised if the url is missing
        the protocol
        """
        url = "www.example.com"
        with self.assertRaises(requests.exceptions.MissingSchema):
            utils.get_links_from_url(url)

class TestGetStyleForLink(unittest.TestCase):
    """
    Tests for the get_style_for_link() function
    """
    def test_absolute_href(self):
        """
        Checks for a valid return for an absolute url
        """
        url = "www.example.com"
        expected = ""
        actual = utils.get_style_for_link(url)

        self.assertEqual(expected, actual)

    def test_phone_href(self):
        """
        Checks for a valid return for a phone url
        """
        url = "tel:1234567890"
        expected = " style='color: #faa;'"
        actual = utils.get_style_for_link(url)

        self.assertEqual(expected, actual)

    def test_email_href(self):
        """
        Checks for a valid return for an absolute url
        """
        url = "mailto:example@example.com"
        expected = " style='color: #f9f;'"
        actual = utils.get_style_for_link(url)

        self.assertEqual(expected, actual)

    def test_relative_href(self):
        """
        Checks for a valid return for an absolute url
        """
        url = "/dir/page.html"
        expected = " style='color: goldenrod;'"
        actual = utils.get_style_for_link(url)

        self.assertEqual(expected, actual)

    def test_id_href(self):
        """
        Checks for a valid return for an absolute url
        """
        url = "#id"
        expected = " style='color: #9f9;'"
        actual = utils.get_style_for_link(url)

        self.assertEqual(expected, actual)

    def test_javascript_href(self):
        """
        Checks for a valid return for an absolute url
        """
        url = "javascript:void(0);"
        expected = " style='color: #aaf;'"
        actual = utils.get_style_for_link(url)

        self.assertEqual(expected, actual)
