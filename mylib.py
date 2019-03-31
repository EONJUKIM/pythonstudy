def add_txt(t1, t2):
    return t1 +':'+t2

def reverse(x,y,z):
    return z,y,x

import mylib

ret1 = mylib.add_txt('대한민국','1등')
ret2 = mylib.reverse(1,2,3,)
print(Ret1)    #'대한민국:1등'이 출력됨
print(ret2)    #(3,2,1)이 출력됨