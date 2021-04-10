class Product:
    def __init__(self,pn,pt,pp,qh,rq):
        self.pn=pn
        self.pt = pt
        self.pp = pp
        self.qh = qh
        self.rq = rq

def FAS(lop,lon):
    c=0
    for i in lop:
        for j in lon:
            if(i.pn.lower() == j.lower()):
                print(j.lower(),i.qh)
                c+=1
    if c==0:
        print("Product Not Found")

def Update(lop,adq,producttyp):
    c=0
    for i in lop:
        if(i.pt.lower()==producttyp.lower()):
            c+=1
            if(i.qh <= i.rq):
                i.qh=i.qh+adq
    if c==0:
        print("Product Not Found")
    else:
        for i in lop:
            print(i.pn.lower(),i.qh)

if __name__=="__main__":
    lop=[]
    for i in range(5):
        pn=input()
        pt=input()
        pp=int(input())
        qh=int(input())
        rq=int(input())
        lop.append(Product(pn,pt,pp,qh,rq))
    n=int(input())
    lon=[]
    for i in range(n):
        pn=input()
        lon.append(pn)
    qon=int(input())
    producttyp = input()
    f1=FAS(lop,lon)
    f2=Update(lop,qon,producttyp)
