
def time() :
    import time
    heures = 0
    minutes = 0
    secondes = 0
    while True:
        print(f"\r{heures:02}:{minutes:02}:{secondes:02}", end="")
        
        
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
time()

