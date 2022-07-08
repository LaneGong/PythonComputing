#!/usr/bin/env python3

while True:
	time1 = input('请输入时间24小时制(格式：小时 分钟 秒)：')
	time2= time1.split()
	list1=[int(i)for i in time2]
	if list1[0]>=0 and list1[0]<=23 and list1[1]>=0 and list1[1]<=59 and list1[2]>=0 and list1[2]<=59:
		break
	else:
		print('输入不合法，请重新输入！')
	
if list1[2]==59:
	if list1[1]==59:
		if list1[0]==23:
			print('当前时间的下一秒为：00:00:00')
		else:
			list1[0]+=1
			print('当前时间的下一秒为：'+str(list1[0])+':'+'00:00')
	else:
		list1[1]+=1
		print('当前时间的下一秒为：'+str(list1[0])+':'+str(list1[1])+':00')
else:
	list1[2]+=1
	print('当前时间的下一秒为：'+str(list1[0])+':'+str(list1[1])+':'+str(list1[2]))

