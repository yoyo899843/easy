#!/usr/bin/python
import os
import cPickle
import sys
import base64

s = raw_input(":")
print cPickle.loads(base64.b64decode(s))
