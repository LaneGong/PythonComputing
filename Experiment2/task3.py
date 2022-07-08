#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
import math

#step1:数据读入及差错判断
while True:
	m=int(input("请输入班级数m(m>=1000)："))
	if m<1000:
		print("班级数不符合要求，请重新输入！")
	else:
		while True:
			n=int(input("请输入每个班级同学的人数n："))
			if n<=0:
				print("人数不符合要求，请重新输入！")
			else:
				break
		break

#step2:利用random模块生成每个班级同学的生日并计算m个班级中存在相同生日情况的班级数 Q
Q=0
for Class in range(m):
	birth=[random.randint(1,365)for member in range(n)]
	if len(birth) != len(set(birth)):
		Q+=1


#step3:用 P=Q/M 作为对相同生日概率的估计
P=Q/m
print("{}个班级、每个班级{}人，相同生日的概率是{}".format(m,n,P))





"""
#step4:分析 M，N 和 P 之间的关系
#4.1 单个班级（m=1即试验次数为1），观察n和至少存在2人生日相同的概率p
Q=0
plist=[]
for n in range(100):
	p=1-math.factorial(365)/(365**n*math.factorial(365-n))
	plist.append(p)

data=DataFrame(plist,columns=["probability"])
data['number']=range(100)
data.plot(kind="scatter",x="number",y="probability",marker="o",color="b")
plt.axhline(0.5, linestyle='--', color='red', label='50% prob')
plt.show()



#4.2 大量试验统计性分析(n=23)，生日悖论的验证，m和p的关系
analysis={}
for num in range(1,1000):
	Q=0
	for Class in range(num):
		birth=[random.randint(1,365)for member in range(23)]
		if len(birth) != len(set(birth)):
			Q+=1
	P=Q/num
	analysis[num]=P
data1=DataFrame(list(analysis.values()),columns=["probability"])
data1['classes']=list(analysis.keys())
data1.plot(kind="scatter",x="classes",y="probability",marker="o",color="b")
plt.axhline(0.5, linestyle='--', color='red', label='50% prob')
plt.show()
"""