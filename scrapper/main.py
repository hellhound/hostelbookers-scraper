#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Application class
"""
from controllers import CityScrapperController
class Application(object):
    def __init__(self):
        self._root_controller = CityScrapperController()

    def main(self):
        self._root_controller.render()

if __name__ == '__main__':
    app = Application()
    app.main()
