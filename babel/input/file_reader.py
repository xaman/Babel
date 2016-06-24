#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logger.logger as logger


def read(path):
    try:
        return open(path, 'r').read()
    except IOError, e:
        logger.error('Error reading file %s' % path)
