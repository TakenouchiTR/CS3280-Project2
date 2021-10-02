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
        text += "<a href='tel:1234567890'></a>"
        text += "<a href='mailto:example@example.com'></a>"
        text += "<a href='/dir/page.html'></a>"
        text += "<a href='#id'></a>"
        text += "<a href='javascript:void(0);'></a>"
        response.text = text
        return response