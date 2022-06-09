v="rat"
m=str(input("Enter input string :- "))
k={}
p={}
for i in v:
    z=v.count(i)
    if i not in p:
        p[i]=z
for j in m:
    b=m.count(j)
    if j not in k:
        k[j]=b
print(p)
print(k)
if p.items()==k.items():
    print("given string is anagram")
else:
    print("given string is not anagram")


