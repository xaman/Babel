#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import logging.config
import config


DEFAULT_ENCODING = "UTF-8"


def _main():
    _configure_encoding()
    _configure_logging()


def _configure_encoding():
    reload(sys)
    sys.setdefaultencoding(DEFAULT_ENCODING)


def _configure_logging():
    try:
        logging.config.fileConfig(config.LOGGING_CONFIG)
    except AttributeError:
        pass


if __name__ == '__main__':
    _main()
