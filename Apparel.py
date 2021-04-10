class Apparel:
    def __init__(self,ab,t,p,d):
        self.ab = ab
        self.t = t
        self.p = p
        self.d =d
class Store:
    def __init__(self,li):
        self.li=li
    def checkaa(self,brand,type,apsize,c):
        st1,st2,st3=False,False,False
        demp=None
        for i in self.li:
            if(i.ab==brand and i.t==type):
                st1=True
                demp=i.d
        
        if demp is not None:
            if apsize in demp.keys():
                st2=True
                if c < demp[apsize]:
                    st3=True
                    demp[apsize] = c
                    if st1==True and st2==True and st3==True:
                        print("Size is Available")
                        for k,v in demp.items():
                            print(k,":",v)
                        return True
        return False

if __name__ =="__main__":
    li=[]
    n=int(input())
    for i in range(n):
        ab=input()
        t=input()
        p=int(input())
        count = int(input())
        d={}
        for i in range(count):
            k=input()
            v=int(input())
            d[k]=v
        li.append(Apparel(ab,t,p,d))
    brand = input()
    at = input()
    asize = input()
    c= int(input())
    s = Store(li)
    st = s.checkaa(brand,at,asize,c)
    if st == False:
        print("Size is not available")
    status = False
    for  i in li:
        if(i.ab==brand and i.t==at):
            status =True
            break
    if status == False:
        print("Apparel not Found")
    
'''# input 
Van huessan
shirt
1500
3
S
1
M
2
L
0
Louis Philip
Trousers
2800
2
S
2
M
2
Indian Terrain
Shorts
1000
3
S
3
M
7
L
2
Louis Philip
Shirts
L
1'''
#input 2
'''
3
Van huessan
shirt
1500
3
S
1
M
2
L
0
Louis Philip
Trousers
2800
2
S
2
M
2
Indian Terrain
Shorts
1000
3
S
3
M
7
L
2
Louis Philip
Trousers
M
1
'''

