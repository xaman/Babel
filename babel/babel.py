#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import config
import data.file_provider as file_provider


DEFAULT_ENCODING = "UTF-8"


def _main():
    _configure_encoding()
    _print_welcome()
    print _get_input_file_content()


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
    return file_provider.get_content()


if __name__ == '__main__':
    _main()
