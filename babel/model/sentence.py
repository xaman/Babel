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

    def get_language_by_locale(self, locale):
        for language in self.languages:
            if locale == language.get_locale():
                return language

    def get_locales(self):
        locales = []
        for language in self.languages:
            locales.append(language.get_locale())
        return locales

    def __str__(self):
        return "Sentence{id=%s}" % self.id
