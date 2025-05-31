import time
import sys

start=time.time()
try:
    while True:
        ecoule=time.time()-start
        sys.stdout.write(f"{ecoule:.1f}")
        sys.stdout.flush()
        time.sleep(0.01)
except KeyboardInterrupt:
    print('chrono stop')

