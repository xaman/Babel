#!/usr/bin/python
# -*- coding: UTF-8 -*-


from os import listdir
from os.path import isfile, join


class Directory(object):

    def __init__(self, path):
        self.path = path if path.endswith('/') else path + '/'

    def get_path(self):
        return self.path

    def get_files(self):
        return [f for f in listdir(self.path) if isfile(join(self.path, f))]

    def __str__(self):
        return "%s" % self.path
