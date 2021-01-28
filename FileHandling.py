import sys
import time
from typing import Counter
import BotCode



def RaiseCounter():
    with open("Counting.txt", "r+", encoding="utf-8") as CountingFile:
        data = list(map(int, CountingFile.readlines()))
        
        data.sort

        for i in range(0, len(data)): 
            if i == (len(data)-1):
                CountingFile.write(str(data[i] + 1))
    
    
    
