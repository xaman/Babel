#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys


def write(path, lines):
    if not _file_exists(path):
        _create_folders(path)
    with open(path, 'w') as file:
        for line in lines:
            file.write(line)


def _file_exists(path):
    return os.path.exists(os.path.dirname(path))


def _create_folders(path):
    try:
        os.makedirs(os.path.dirname(path))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
