#!/usr/bin/python
# -*- coding: UTF-8 -*-

from colors import Colors


def debug(message):
    print Colors.OKBLUE + message + Colors.ENDC


def error(message):
    print Colors.FAIL + message + Colors.ENDC
