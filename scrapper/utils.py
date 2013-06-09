# -*-  coding:utf-8 -*-
"""
Scrapping utilities
"""
import re
from pyquery import PyQuery as pq

from models import Hostel

DEFAULT_URL = 'http://www.hostelbookers.com/results/loc/dd/dst/1881/arr/' \
    '2013-06-15/ngt/2/ppl/1/'
ROW_CLASS = '.propertyRow'
HOSTEL_NAME_CLASS = '.propertyTitle'
RATINGS_CLASS = '.rating'
RATINGS_REGEX = '[-+]?[0-9]*\.?[0-9]+'

def encode(text, encoding='utf-8'):
    """
    Encoding coercion
    """
    return text.encode(encoding, 'ignore') \
        if isinstance(text, unicode) else text

class CuscoHostelsBuilder(object):
    @classmethod
    def _get_pyquery(cls):
        return pq(url=DEFAULT_URL)

    @classmethod
    def _get_hostel(cls, query):
        name = query.find(HOSTEL_NAME_CLASS).text()
        try:
            qualification, reviews = re.findall(
                RATINGS_REGEX, query.find(RATINGS_CLASS).text())
        except (ValueError, TypeError):
            qualification = reviews = 0
        global count
        hostel = Hostel(name, qualification, reviews)
        return hostel

    @classmethod
    def _get_hostel_list(cls, query):
        rows = query(ROW_CLASS)
        length = len(rows)
        hostels = []
        for i in range(length):
            hostel = cls._get_hostel(rows.eq(i))
            hostels.append(hostel)
        return hostels

    @classmethod
    def build_hostels(cls):
        query = cls._get_pyquery()
        hostels = cls._get_hostel_list(query)    
        return hostels
