#!/usr/bin/python
# -*- coding: UTF-8 -*-

import config
import logger.logger as logger
from converter import Converter
from android_converter import AndroidConverter
from ios_converter import iOSConverter

EXPORT_TO_ANDROID = 1
EXPORT_TO_IOS = 2
EXPORT_TO_WEB = 3


def export(translation):
    option = _get_export_option()
    directory = _get_export_directory()
    _export(translation, option, directory)


def _get_export_option():
    print 'Options:'
    print '1) Export to Android (strings.xml)'
    print '2) Export to iOS (Localizable.strings)'
    print '3) Export to I20N (strings.i20n)'
    option = int(raw_input("Select an option: "))
    if option > 0 and option < 3:
        return option
    else:
        logger.error("The option is not valid")
        _get_export_option()


def _get_export_directory():
    directory = raw_input("Select output directory [%s]: " % config.OUTPUT_DIR)
    return config.OUTPUT_DIR if len(directory) == 0 else directory


def _export(translation, option, directory):
    converter = None
    if (option == EXPORT_TO_ANDROID):
        converter = AndroidConverter(translation, directory)
    else:
        converter = iOSConverter(translation, directory)
    converter.convert()
