#!/usr/bin/env python3
import time
from nltk.corpus import words#导入NLTK的单词语料库
#该语料库通过nltk.down()下载
#import nltk
#nltk.down()

dictionary = dict.fromkeys(words.words(), None)#创建字典索引，方便后续判断是否为英语单词，字典也是利用哈希表会比list更快

def make_word_list():#接收文件，返回列表
	word_list = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		word_list.append(word)
	return word_list

def isword(newword):#判断单词是否属于合法英文单词
#	if newword in words.words():
#		return True
#	else:
#		return False
#	dictionary = dict.fromkeys(words.words(), None)
	try:
		x = dictionary[newword]
		return True
	except KeyError:
		return False

def cuttable_word(word,cuttable,uncuttable):#判断单词是否可缩减
	word=list(word)
	if 'a' not in word and 'i' not in word:#若单词中不含‘a’或‘i’，则一定不是可缩减，直接返回
		return False
	
	elif len(word)==2:#可缩减单词递归结束的标志，原先是下面这种，判断到最后一个字母，但会存在问题
		if ('a' in word) or ('i' in word):
			return True

#错误代码，比如at->t->进递归->False
#	elif len(word)==1:
#		if word=='a' or word=='i':
#			return True
		
	for i in range(len(word)):#删除某个字母
		newword=""#新字符串初始化
		for j in range(len(word)):
			if j != i:
				newword=newword+word[j]#拼凑
		if newword in cuttable:
			return True
		elif newword in uncuttable:
			return False
		if isword(newword):
			break
	
	if i==len(word)-1 and (not isword(newword)):#遍历结束且删除最后一个字母组成的新单词不合法说明不是
		return False
	else:
		return True if cuttable_word(newword,cuttable,uncuttable) else False#递归查找
	

#		if cuttable_word(newword):
#			return True
#		else:
#			return False

#错误代码，逐层退出递归覆盖原结果
#	else:
#		cuttable_word(newword)
	
		
if __name__ == '__main__':
	starttime=time.time()
	word_list = make_word_list()
	cuttable=set()#利用set()创建空集合
	uncuttable=set()
	maxlength_word=""
	for word in word_list:
		if cuttable_word(word,cuttable,uncuttable):#如果是可缩减
			#print(word)
			if len(word)>=len(maxlength_word):#进一步判断长度
				maxlength_word=word
			cuttable.add(word)#追加提供给判断子单词的依据
		else:
			uncuttable.add(word)
	print('最大长度可缩减词为：'+maxlength_word+'({})'.format(len(maxlength_word)))
	print('耗时：{}s'.format(time.time()-starttime))