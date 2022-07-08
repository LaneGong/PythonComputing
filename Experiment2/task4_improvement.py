#!/usr/bin/env python3
import time
from nltk.corpus import words#导入NLYK的单词语料库
#该语料库通过nltk.down()下载
#import nltk
#nltk.down()

#dictionary = dict.fromkeys(words.words(), None)#创建字典索引，方便后续判断是否为英语单词，字典也是利用哈希表会比list更快

def make_word_list():
	with open('words.txt') as text:
		word_list = [x.strip() for x in text if 'a' in x or 'i' in x]#改进1：初筛，将不合法的直接去除，获得有效样本量
	return word_list

def isword(newword):
	try:
		x = dictionary[newword]
		return True
	except KeyError:
		return False
	
def cuttable_word(word,cuttable,uncuttable):
	if len(word)>1:#改进2:递归过程的修改
		for i in range(len(word)):
			newword = word[:i] + word[i+1:]#拼接过程的简化
			if (newword in cuttable) or (isword(newword) and newword not in uncuttable and cuttable_word(newword,cuttable,uncuttable)):#判断条件改进
				break
		else:#利用for-else语法改进结构
			return False
		return True
#	else:
#		return True if cuttable_word(newword,cuttable,uncuttable) else False
			

if __name__ == '__main__':
	starttime=time.time()
	word_list = make_word_list()
	dictionary = dict.fromkeys(word_list, None)
	cuttable={'a','i'}#配合新的递归结构可解决原方法中单个字符判断问题，不用单独拎出来考虑
	uncuttable=set()
	maxlength=1
	result='a'
	for word in word_list:
		if len(word)>=maxlength:#改进3：只有当当前字符长度大于我找到的最长可缩减单词长度时我才进行判断，大大减少了样本数量，提高了运行效率
			if cuttable_word(word,cuttable,uncuttable):#只要他是，则当前一定是他最长
				maxlength=len(word)
				result=word
				cuttable.add(word)
			else:
				uncuttable.add(word)
	print('最大长度可缩减词为：'+result+'({})'.format(maxlength))
	print('耗时：{}s'.format(time.time()-starttime))
