# -*- coding:utf-8 -*-
"""
Models
"""
class Hostel(object):
    def __init__(self, name, qualification, reviews):
        self.name = name
        self.qualification = float(qualification)
        self.reviews = int(reviews)
