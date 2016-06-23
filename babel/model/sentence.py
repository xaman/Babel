#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Sentence(object):

    def __init__(self):
        self.id = ''
        self.languages = []

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_languages(self):
        return self.languages

    def set_languages(self, languages):
        self.languages = languages

    def add_language(self, language):
        self.languages.append(language)

    def __str__(self):
        return "%s" % self.id
