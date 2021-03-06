#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logger.logger as logger


class Translation(object):

    def __init__(self):
        self.version = ''
        self.description = ''
        self.sections = []

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_sections(self):
        return self.sections

    def set_sections(self, sections):
        self.sections = sections

    def add_section(self, section):
        self.sections.append(section)

    def print_value(self):
        logger.debug(str(self))
        for section in self.sections:
            logger.debug("\t" + str(section))
            for sentence in section.get_sentences():
                logger.debug("\t\t" + str(sentence))
                for language in sentence.get_languages():
                    logger.debug("\t\t\t" + str(language))

    def __str__(self):
        return "Translation{version=%s, description=%s}" % (self.version, self.description)
