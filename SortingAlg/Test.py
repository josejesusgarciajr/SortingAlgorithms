'''
Created on Mar 7, 2019

@author: jginvincible
'''
from RadixSort import RadixSort

print("Testing Radix Sort")
list = [1, 30, 6, 8, 9, 29, 69, 400, 111, 69, 100000, 200]
radix = RadixSort(list)
# how to get sorted list
sortedList = radix.getSortedList()

# you could also simply print sorted list
print(sortedList)
radix.printSorted()