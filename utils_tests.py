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
    text = ""

    def get(url):
        response = FakeResponse()
        text = "<a href='https://www.example.com'></a>"
        text += "<a href='tel:1234567890'></a>"
        text += "<a href='mailto:example@example.com'></a>"
        text += "<a href='/dir/page.html'></a>"
        text += "<a href='#id'></a>"
        text += "<a href='javascript:void(0);'></a>"
        response.text = text
        return response