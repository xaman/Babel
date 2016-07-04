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
        path = _get_path(directory, file_name)
        content = file_reader.read(path)
        content = _escape_characters(content)
        return content


def _get_selected_directory():
    directory = raw_input("Select input directory [%s]: " % config.INPUT_DIR)
    return directory if directory else config.INPUT_DIR


def _get_selected_file(directory):
    files = _get_files(directory)
    if (len(files) > 0):
        _print_files_list(files)
        return _select_file(files)
    else:
        logger.error("The input directory hasn't files\n")


def _get_path(directory, file_name):
    if not directory.endswith('/'):
        directory = directory + '/'
    return directory + file_name


def _get_files(directory):
    dir = Directory(directory)
    return dir.get_files()


def _print_files_list(files):
    print "Input files: "
    position = 0
    for file in files:
        print str(position) + ") " + file
        position += 1


def _select_file(files):
    position = int(raw_input("Select a file position: "))
    if position >= 0 and position < len(files):
        return files[position]
    else:
        logger.error("The file position is not valid")
        _select_file(files)


def _escape_characters(input):
    input = input.replace('\\', '\\\\')
    return input
