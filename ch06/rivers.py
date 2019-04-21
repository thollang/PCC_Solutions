rivers={
    'nile':'egypt',
    'mississippi':'united status',
    'fraser':'canada',
    'kuskokwim':'alaska',
    'yangtze':'china',
}
for k,v in rivers.items():
    print("The "+k.title()+" runs through "+v.title())

for k in rivers.keys():
    print(k)
for v in rivers.values():
    print(v)
