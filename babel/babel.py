#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import config
import input.importer as importer
import parser.json_parser as parser
import output.exporter as exporter


DEFAULT_ENCODING = "UTF-8"


def _main():
    try:
        _configure_encoding()
        _print_welcome()
        content = _get_input_file_content()
        translation = _parse_content(content)
        exporter.export(translation)
    except KeyboardInterrupt:
        pass


def _configure_encoding():
    reload(sys)
    sys.setdefaultencoding(DEFAULT_ENCODING)


def _print_welcome():
    print ''
    print '##########################'
    print '#    Welcome to Babel!   #'
    print '##########################'
    print ''


def _get_input_file_content():
    return importer.get_content()


def _parse_content(content):
    return parser.parse(content)

if __name__ == '__main__':
    _main()
