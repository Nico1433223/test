import os
lines=[]
f=open('./file.txt')
for line in f.readlines():
    line.strip()
    lines.append(line)
f.close()
def fun():
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                for a in range(1,7):
                    for b in range(1,7):
                        for c in range(1,7):
                            lines[5]=str(i)+' '+str(j)+' '+str(k)+' '+str(a)+' '+str(b)+' '+str(c)+'\n'
                            s=''.join(lines)
                            f=open('./file.txt','w+')
                            f.write(s)
                            f.close()
                            command='./bomb file.txt'
                            r = os.popen(command) #执行该命令
                            info=r.read() #读取命令的输出结果
                            if 'BOOM!' not in info:
                                return [i,j,k,a,b,c]
print(fun()) 
