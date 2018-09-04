def maopao(list_num):
    for i in range(len(list_num)-1,0,-1):
        for j in range(0,i):
            if list_num[j] > list_num[j+1]:
                list_num[j],list_num[j+1] = list_num[j+1],list_num[j]
    return list_num

result = maopao([1,23,34,3,2,1,3,432,34,2])
print(result)