#!/usr/bin/python
# -*- coding: UTF-8 -*-

from output.converter import Converter

FOLDER_PREFIX = "values"
FILE_NAME = "strings.xml"


class AndroidConverter(Converter):

    def __init__(self, translation, folder):
        Converter.__init__(self, translation, folder)

    def _add_header(self, lines):
        lines.append('<?xml version="1.0" encoding="utf-8"?>\n')
        lines.append('<resources>\n')

    def _add_sentences(self, lines, locale):
        sections = self.translation.get_sections()
        for section in sections:
            self._add_section(lines, section, locale)
            for sentence in section.get_sentences():
                self._add_sentence(lines, sentence, locale)

    def _add_section(self, lines, section, locale):
        name = section.get_name().upper()
        description = section.get_description()
        lines.append('\n')
        lines.append('/*\n')
        lines.append('* %s\n' % name)
        lines.append('* %s\n' % description)
        lines.append('*/\n')

    def _add_sentence(self, lines, sentence, locale):
        language = sentence.get_language_by_locale(locale)
        id = sentence.get_id()
        value = language.get_value()
        lines.append('<string id="%s">%s</string>\n' % (id, value))

    def _add_footer(self, lines):
        lines.append('\n</resources>\n')

    def _get_folder_for_locale(self, locale):
        language = self._get_language_from_locale(locale)
        return FOLDER_PREFIX if language == self.default_language else FOLDER_PREFIX + '-' + language

    def _get_file_name(self):
        return FILE_NAME
