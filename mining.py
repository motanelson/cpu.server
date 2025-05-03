
import time
import random
print ("\033c\033[43;30m\nenter simulator\n")
def floats():
    f=float(random.randrange(1,9)-5)
    return f
def collapseEvent():
    rets=random.randrange(1,1000)
    retss=rets>995
    return retss
def sims(n):
    totals=0
    money=float(0.0)
    rets=[]
    nn=0
    t=True
    gold=float(0.0)
    diamants=float(0.0)
    while t:
        print(str(totals)+" units")
        totals=totals+n
        if collapseEvent():
           print("collapse event all the mining as destroy")
           totals=0
        if totals>10:
            totals=0
            diamants=float(9.00+floats())
            gold=float(9.00+floats())
            
            print("gold=2 X "+str(float(gold))+" ="+str(float(gold*2.00)))
            print("diamants=8 X "+str(float(diamants))+" ="+str(float(diamants*8.00)))
            money=money+float(gold*8.00)+float(diamants*8.00)-float(110.00)
            print("expenses="+str(float(110.00)))
            print("money="+str(float(money)))
            print("8 units as diamants")
            print("2 units gold")
        time.sleep(1)
    
sims(1)