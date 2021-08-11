name = ''
li = list()
while name != '끝':
    name = input('우리 반 친구의 이름을 입력해 주세요. 다 입력했으면 끝이라고 입력하세요. :')
    if name == '끝':
        continue
    
    li.append(name)

print(li)