#!/usr/bin/python
# -*- coding: UTF-8 -*-

from converter import Converter

DEFAULT_LOCALE = "es_ES"
DIRECTORY_SUFIX = ".lproj"
FILE_NAME = "Localizable.strings"


class iOSConverter(Converter):

    def __init__(self, translation, directory):
        Converter.__init__(self, translation, directory)

    def _add_sentences(self, lines, locale):
        sections = self.translation.get_sections()
        for section in sections:
            self._add_section(lines, section, locale)
            for sentence in section.get_sentences():
                self._add_sentence(lines, sentence, locale)

    def _add_section(self, lines, section, locale):
        name = section.get_name().upper()
        description = section.get_description()
        lines.append('\n/*\n')
        lines.append('* %s\n' % name)
        lines.append('* %s\n' % description)
        lines.append('*/\n')

    def _add_sentence(self, lines, sentence, locale):
        language_key = sentence.get_language_by_locale(DEFAULT_LOCALE)
        language_value = sentence.get_language_by_locale(locale)
        key = language_key.get_value()
        value = language_value.get_value()
        lines.append('"%s" = "%s";\n' % (key, value))

    def _get_directory_for_locale(self, locale):
        language = self._get_language_from_locale(locale)
        return language + DIRECTORY_SUFIX

    def _get_file_name(self):
        return FILE_NAME
