class Product:
    def __init__(self,productName,productType,unitPrice,qtyinHand):
        self.productName = productName
        self.productType = productType
        self.unitPrice = unitPrice
        self.qtyinHand =qtyinHand

class Store:
    def __init__(self,productList):
        self.productList = productList
    
    def purchaseProduct(self,name,quantity):
        bill=0
        for p in self.productList:
            if(p.productName.lower() == name.lower()and p.qtyinHand==0):
                return None
            elif(p.productName.lower()==name.lower() and p.qtyinhand>=quantity):
                bill = p.unitPrice*quantity
                p.qtyinHand=p.qtyinHand-quantity
                return bill
            elif(p.productName.lower()==name.lower() and p.qtyinhand<quantity):
                bill=p.unitPrice*p.qtyinHand
                p.qtyinHand=0
                return bill
        return None

n=int(input())   
productList=[]

for i in range(n):
    productName = input()
    productType= input()
    unitPrice=int(input())
    qtyinHand = int(input())
    productList.append(Product(productName,productType,unitPrice,qtyinHand))

obj = Store(productList)
name = input()
quantity = int(input())
bill = obj.purchaseProduct(name,quantity)

if(bill==None):
    print('Product not Available')
    for p in obj.productList:
        print(p.productName,end=' ')
        print(p.qtyinHand)
else:
    print(bill)
    for p in obj.productList:
        print(p.productName,end=' ')
        print(p.qtyinHand)

