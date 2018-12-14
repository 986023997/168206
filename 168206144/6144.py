start='hit'
end='cog'
adict=['hot','dot','dog','lot','log']

def find(star,end,paths):
    if start==end:
        return "star=end"
    else:
        visted=[]
        visted.append(start)
        for word in visted:
            
            words=word
            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):
                    word=words[:i]+chr(j)+word[i+1:]

                    
                    if word in paths:
                        if word not in visted:
                            visted.append(word)
                    if word==end:
                        visted.append(word)
                        return visted
                       
visteds=find(start,end,adict)
for i in range(len(visteds)):
    print(visteds[i])

