#!/usr/bin/python
# -*- coding: UTF-8 -*-


import json
from model.translation import Translation
from model.section import Section
from model.sentence import Sentence
from model.language import Language

VERSION = "version"
DESCRIPTION = "description"
SECTIONS = "sections"
NAME = "name"
SENTENCES = "sentences"
ID = "id"


def parse(content):
    json = _convert_to_json(content)
    if (json is not None):
        return _parse_translation(json)


def _convert_to_json(content):
    return json.loads(content)


def _parse_translation(json):
    translation = Translation()
    translation.set_version(json[VERSION])
    translation.set_description(json[DESCRIPTION])
    for section_json in json[SECTIONS]:
        section = _parse_section(section_json)
        translation.add_section(section)
    return translation


def _parse_section(json):
    section = Section()
    section.set_name(json[NAME])
    section.set_description(json[DESCRIPTION])
    for sentence_json in json[SENTENCES]:
        sentence = _parse_sentence(sentence_json)
        section.add_sentence(sentence)
    return section


def _parse_sentence(json):
    sentence = Sentence()
    sentence.set_id(json[ID])
    language = None
    for key in json.keys():
        if key != ID:
            language = Language()
            language.set_locale(key)
            language.set_value(json[key])
            sentence.add_language(language)
    return sentence
