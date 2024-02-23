weight = int(input("enter the peice"))
if weight > 2 and weight % 2 ==0:
    for i in range (2,weight//2+1,2):
        print("[",i,",",weight-i,"]",end= "")
else:
    print("error")