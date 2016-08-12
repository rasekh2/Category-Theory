list = []

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if i <= j and j <= k and k <= l:
                    list.append(str(i)+str(j)+str(k)+str(l))
                    
                    
#print list
#print len(list)
i = 1
#for s in list:
#    print 'Number:', i
#    print s[0] + "             " + s[1] + "\n\n" + "       " + s[2] + "\n\n" + "       " + s[3]
#    i+=1

newlist = []
for s in list:
    newlist.append((s,(s[0]+s[2],s[1]+s[3])))
    
#print newlist

nnewlist= []

for s in newlist:
    if s[1][0][0] == s[1][0][1] and s[1][1][0] == s[1][1][1]:
        nnewlist.append(s)
        
print nnewlist