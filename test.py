import os
command = './bomb ans.txt ' #可以直接在命令行中执行的命令
r = os.popen(command) #执行该命令
def fun():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for a in range(0,10):
                    for b in range(0,10):
                        for c in range(0,10):
                            command=str(i)+' '+str(j)+' '+str(k)+' '+str(a)+' '+str(b)+' '+str(c)
                            r = os.popen(command) #执行该命令
                            info=r.readlines() #读取命令的输出结果
                            for line in info:  #按行遍历
                                line = line.strip('\r\n')
                                if(line=='BOOM!'):
                                    return [i,j,k,a,b,c]
print(fun()) 
           

