#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logger.logger as logger
from output.converter import Converter

DIRECTORY_PREFIX = "values"
FILE_NAME = "strings.xml"


class AndroidConverter(Converter):

    def __init__(self, translation, directory):
        Converter.__init__(self, translation, directory)

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
        lines.append('\n\t/*\n')
        lines.append('\t* %s\n' % name)
        lines.append('\t* %s\n' % description)
        lines.append('\t*/\n')

    def _add_sentence(self, lines, sentence, locale):
        language = sentence.get_language_by_locale(locale)
        id = sentence.get_id()
        value = language.get_value()
        if value:
            lines.append('\t<string name="%s">%s</string>\n' % (id, value))
        else:
            logger.error("Translation not found for '%s' in %s" % (id, locale))

    def _add_footer(self, lines):
        lines.append('\n</resources>\n')

    def _get_directory_for_locale(self, locale):
        language = self._get_language_from_locale(locale)
        directory_name = DIRECTORY_PREFIX
        if (language != self.default_language):
            directory_name += '-' + language
        return directory_name

    def _get_file_name(self):
        return FILE_NAME
