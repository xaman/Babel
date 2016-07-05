#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from replacer import Replacer


class AndroidReplacer(Replacer):

    def __init__(self):
        Replacer.__init__(self)
        self.argument_pattern = re.compile(ur'{[0-9]}')

    def replace(self, sentence):
        sentence = self._replace_apostrophe(sentence)
        return sentence

    def _replace_apostrophe(self, sentence):
        original = '\''
        replacement = '\\\'\\\'' if self._has_arguments(sentence) else '\\\''
        return sentence.replace(original, replacement)

    def _has_arguments(self, sentence):
        args = re.findall(self.argument_pattern, sentence)
        return args
