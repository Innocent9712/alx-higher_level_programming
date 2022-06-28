#!/usr/bin/python3
"""Simple Class with specified fields"""


class LockedClass:
    """accepts only this field"""
    __slots__ = {'first_name'}
