#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Kane'

from xml.parsers.expat import ParserCreate
import urllib2

class DefaultSaxHandler(object):
    _sp = '\n-----\n'
    _TARGET_TAG_NAME = 'description'
    _desc = ''

    def start_element(self, name, attrs):
        self._tag = name
        # print 'sax:start_element: %s, attrs: %s' % (name, str(attrs))

    def end_element(self, name):
        if name == self._TARGET_TAG_NAME:
            self._desc = self._desc + self._sp

        # print 'sax:end_element: %s' % name

    def char_data(self, text):
        if self._tag == self._TARGET_TAG_NAME:
            self._desc = self._desc + text

        # print 'sax:char_data: %s' % text

    def show_weather(self):
        print self._desc

handler = DefaultSaxHandler()
parser = ParserCreate()

parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

resp = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?u=c&w=2151330')
xml = resp.read()

parser.Parse(str(xml))
handler.show_weather()
