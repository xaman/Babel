#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Language(object):

    def __init__(self):
        self.locale = ''
        self.value = ''

    def get_locale(self):
        return self.locale

    def set_locale(self, locale):
        self.locale = locale

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return "Language{locale=%s, value=%s}" % (self.locale, self.value)
