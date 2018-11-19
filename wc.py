#! /usr/bin/python
def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print lines, words, chars
with open('/etc/passwd') as fd:
    s = fd.read()
wordCount(s)
