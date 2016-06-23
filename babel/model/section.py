#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Section(object):

    def __init__(self):
        self.name = ''
        self.description = ''
        self.sentences = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_sentences(self):
        return self.sentences

    def set_sentences(self, sentences):
        self.sentences = sentences

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def __str__(self):
        return "Section{name=%s, description=%s}" % (self.name, self.description)
