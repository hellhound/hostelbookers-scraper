# -*- coding:utf-8 -*-
"""
Controllers
"""
from pprint import pprint
from utils import CuscoHostelsBuilder

class CityScrapperController(object):
    def __init__(self):
        self._hostels = CuscoHostelsBuilder.build_hostels()

    def _get_first_summary(self):
        output_format = u"""
        1.
        Have reviews = %i
        Doesn't have reviews = %i
        """
        have_reviews = len([h for h in self._hostels if h.reviews > 0])
        doesnt_have_reviews = len(self._hostels) - have_reviews
        output = output_format % (have_reviews, doesnt_have_reviews)
        return output

    def _get_total_reviews(self):
        reduce_func = lambda x, y: x + y
        total_reviews = reduce(reduce_func, [h.reviews for h in self._hostels])
        return total_reviews

    def _get_second_summary(self):
        output_format = u"""
        2.
        Total Reviews = %i
        """
        total_reviews = self._get_total_reviews()
        output = output_format % total_reviews
        return output

    def _get_third_summary(self):
        title_format = u"""
        3.
        Hostel distribution by total reviews
        """
        output_format = u"""
        =================================================== 
        Name: %s
        Percentage: %.2f
        =================================================== 
        """
        total_reviews = float(self._get_total_reviews())
        distribution = u'\n'.join(
            [output_format % (
                h.name,
                100. * h.reviews / total_reviews)
            for h in self._hostels])
        return title_format + distribution

    def _get_forth_summary(self):
        output_format_more_than_1 = u"""
        4.
        Min, max qualification range = (%s: %.2f, %s: %.2f)
        """
        output_format_for_1 = u"""
        4.
        Min, max qualification range = (%s: %.2f)
        """
        rated_hostels = [h for h in self._hostels if h.qualification > 0]
        sorting_func = lambda h: h.qualification
        sorted_hostels = sorted(rated_hostels, key=sorting_func)
        if len(sorted_hostels) > 1:
            hostel_min = sorted_hostels[0]
            hostel_max = sorted_hostels[-1]
            output = output_format_more_than_1 % (
                hostel_min.name, hostel_min.qualification,
                hostel_max.name, hostel_max.qualification)
        elif len(sorted_hostels) > 0:
            hostel = sorted_hostels[0]
            output = output_format_for_1 % (
                hostel.name, hostel.qualification)
        else:
            output = u''
        return output

    def render(self):
        print self._get_first_summary()
        print self._get_second_summary()
        print self._get_third_summary()
        print self._get_forth_summary()
