
import time
debut=time.time()
tour=[]

while True :
    action = input('entre')
    if action == '1':
        tour.append(time.time()-debut)
        print(tour[:])
    

print(tour[:])