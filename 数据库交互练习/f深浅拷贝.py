import copy
a = [1,2,3,4,['a','b']]
b = a  #引用，除非直接给ａ重新复制，否则a变则ｂ变，ｂ变则ａ变。
c = copy.copy(a)  #浅复制，只会拷贝父对象，不会拷贝父对象中的子对象，所以若a的子对象则ｃ变，但是父对象变ｃ不会变
d = copy.deepcopy(a)  #深拷贝,完全拷贝，完全独立于原对象，ａ变也不变
a.append(5)
a[4].append('c')
print(a)
print(b)
print(c)
print(d)