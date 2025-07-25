# concurrency.py
# Logan Till
# 2025-07-24

import multiprocessing
import time
import random
from datetime import datetime

def wait_and_print():
    wait_time = random.uniform(0, 5)
    time.sleep(wait_time)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {multiprocessing.current_process().name} finished at {current_time}")

if __name__ == "__main__":
      processes = []
      for i in range(3):
         process = multiprocessing.Process(target=wait_and_print, name=f"Process-{i+1}")
         processes.append(process)
         process.start()
   
      for process in processes:
         process.join()
