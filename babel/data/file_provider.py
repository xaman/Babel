#!/usr/bin/python
# -*- coding: UTF-8 -*-

import config
import file_reader
import logger.logger as logger
from directory import Directory


def get_content():
    file_name = _get_selected_file()
    if (file_name is not None):
        path = config.INPUT_DIR + "/" + file_name
        return file_reader.read(path)


def _get_selected_file():
    files = _get_files()
    if (len(files) > 0):
        _print_files_list(files)
        return _select_file(files)
    else:
        logger.error("The input folder has not files\n")


def _get_files():
    dir = Directory(config.INPUT_DIR)
    return dir.get_files()


def _print_files_list(files):
    print "Input files: "
    position = 0
    for file in files:
        print str(position) + ") " + file
        position += 1


def _select_file(files):
    try:
        position = int(raw_input("Select a file position: "))
        if position >= 0 and position < len(files):
            return files[position]
        else:
            logger.error("The file position is not valid")
            _select_file(files)
    except KeyboardInterrupt:
        pass
