#!/usr/bin/python
# -*- coding: UTF-8 -*-

import config
import file_reader
import logger.logger as logger
from model.directory import Directory


def get_content():
    directory = _get_selected_directory()
    file_name = _get_selected_file(directory)
    if (file_name is not None):
        path = directory.get_path() + file_name
        content = file_reader.read(path)
        content = _escape_characters(content)
        return content


def _get_selected_directory():
    default = config.INPUT_DIR
    path = raw_input("Select input directory [%s]: " % default) or default
    return Directory(path)


def _get_selected_file(directory):
    files = directory.get_files()
    if (len(files) > 0):
        _print_files_list(files)
        return _select_file(files)
    else:
        logger.error("The input directory hasn't files\n")


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
    except ValueError, e:
        pass
    return _on_file_selection_error(files)


def _on_file_selection_error(files):
    logger.error("The file position is not valid")
    return _select_file(files)


def _escape_characters(input):
    input = input.replace('\\', '\\\\')
    return input
