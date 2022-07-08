#!/usr/bin/env python3
#通过公式近似pi值并与math.pi值比较
import math

def factorial(a):
	i=1
	result=1
	while i<=a:
		result*=i
		i=i+1
	return result

C=math.sqrt(8)/9801

#sum=0
#for k in range(0,200):
#	sum+=factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))
#approximate_pi=1/(C*sum)
#print("通过公式近似所得结果(k=200)：%.15f" % approximate_pi)
#print("math.pi值为：%.15f" % math.pi)
#print("二者之间的差值为：%.15f"%(approximate_pi-math.pi))

for n in range(10,300,10):
	sum=0
	for k in range(0,n):
		sum+=factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))
	approximate_pi=1/(C*sum)
	print("通过公式近似所得结果(k="+str(n)+")：%.15f" % approximate_pi)
	print("math.pi值为：%.15f" % math.pi)
	print("二者之间的差值为：%.15f"%(approximate_pi-math.pi))