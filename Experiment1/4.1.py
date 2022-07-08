#!/usr/bin/env python3


txt = open("news.txt", "r", encoding='UTF-8').read()
txt = txt.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
	txt = txt.replace(ch, " ")
list1 = txt.split()
counts = {}
for i in list1:
	counts[i] = counts.get(i, 0) + 1 
	
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(len(items)):
	word, count = items[i]
	print("{0:<10}{1:>5}".format(word, count))