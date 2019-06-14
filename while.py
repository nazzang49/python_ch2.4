# while의 단점 = 초기값 / 조건식 / 증가식이 분리되어 있음
from builtins import print

count = 1
while count < 11:
    print(count, end=' ')
    # if count == 5:
    #     break
    count += 1
else:
    print('ok')

hap, i = 0, 1
while i <= 10:
    hap += i
    i += 1

print( '합: {0}'.format(hap))

# break / continue / else 활용
i = 0
while i < 10:
    i+=1
    if i < 5:
        continue
    if i >= 10:
        break
    print(i,end=' ')
else:
    print('ok')

