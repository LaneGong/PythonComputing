
import time
start=time.perf_counter()

f=open("words.txt","r")
lines=f.read()
f.close()
words=set(lines.split())
results=set()
for word in words:
    rword = ''.join(reversed(word))
    if rword in words:
        print(word,rword)
        results.add(word+'  '+rword)
print('反序对个数',len(results))
end=time.perf_counter()
print("运行耗时",end-start)
