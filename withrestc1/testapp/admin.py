#program to check s2 conatins in s in same order or not, if yes return True else return False

def check_order(s,s1):
    l2=[]
    for x in s:
        if x not in l2:
            l2.append(x)
    s2="".join(s)
    for x in s2:
        if x.lower() not in s1.lower():
            return False
        else:
            return True
s='sdhncksdllivsdyssa'
#s2=list(set(s)) # don't use set because order will not confirm, it will come in same order or not
s1='divya'
print(check_order(s,s1))







