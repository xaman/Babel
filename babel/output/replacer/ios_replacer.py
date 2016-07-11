#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from replacer import Replacer


class iOSReplacer(Replacer):

    def __init__(self):
        Replacer.__init__(self)

    def replace(self, sentence):
        sentence = self._replace_apostrophe(sentence)
        return sentence

    def _replace_apostrophe(self, sentence):
        return sentence.replace('\'', '\\\'')
