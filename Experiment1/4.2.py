#!/usr/bin/env python3
from jieba import analyse
txt = open("education.txt", "r", encoding='UTF-8').read()
txt = txt.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
	txt = txt.replace(ch, " ")
list1 = txt.split()
counts = {}
for i in list1:
	counts[i] = counts.get(i, 0) + 1

keys=analyse.extract_tags(txt)
for i in keys:
	print("{0:<10}{1:>5}".format(i, counts[i]))