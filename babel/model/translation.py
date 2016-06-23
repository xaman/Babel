#!/usr/bin/python
# -*- coding: UTF-8 -*-


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
        print str(self)
        for section in self.sections:
            print "\t" + str(section)
            for sentence in section.get_sentences():
                print "\t\t" + str(sentence)
                for language in sentence.get_languages():
                    print "\t\t\t" + str(language)

    def __str__(self):
        return "%s\t%s" % (self.version, self.description)
