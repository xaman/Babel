#!/usr/bin/python
# -*- coding: UTF-8 -*-

import output.file_writer as file_writer


class Converter(object):

    def __init__(self, translation, directory):
        self.default_language = 'en'
        self.translation = translation
        self.directory = directory

    def convert(self):
        locales = self._get_locales()
        for locale in locales:
            self._convert_language(locale)

    def _get_locales(self):
        section = self.translation.get_sections()[0]
        sentence = section.get_sentences()[0]
        return sentence.get_locales()

    def _convert_language(self, locale):
        lines = []
        file_path = self._get_file_path(locale)
        self._add_header(lines)
        self._add_sentences(lines, locale)
        self._add_footer(lines)
        file_writer.write(file_path, lines)

    def _get_file_path(self, locale):
        language_directory = self._get_directory_for_locale(locale)
        file_name = self._get_file_name()
        return self.directory + '/' + language_directory + '/' + file_name

    def _get_directory_for_locale(self, locale):
        return NotImplemented

    def _get_file_name(self):
        return NotImplemented

    def _get_language_from_locale(self, locale):
        return locale[0:2]

    def _add_header(self, lines):
        return NotImplemented

    def _add_sentences(self, lines, locale):
        return NotImplemented

    def _add_footer(self, lines):
        return NotImplemented
