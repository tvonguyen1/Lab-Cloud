'''
Created on Feb 22, 2022

@author: nhatt
'''


class Error(Exception):
    """Base class for other exceptions"""
    pass


class nullValue(Error):
    """when there is missing field"""
    pass


class valueError(Error):
    """When there is unmatch data"""
    pass
