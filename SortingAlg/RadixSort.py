'''
Created on Mar 7, 2019

@author: jginvincible
'''

class RadixSort:
    def __init__(self, list):
        self.list = list
        '''
        Temp is a two demensional List
            Each Row is considered a bucket
            There are 10 buckets ranging from 0 to 9 (For each digit)
            the lenght of each bucket is the lenght of the list to be sorted
        '''
        self.temp = [[None for x in range(len(self.list))] for y in range(10)]
        self.sortedList = self.sort()
        
    def largestNumber(self): # finds the largest number in the list
        max = self.list[0]
        for number in self.list:
            if max < number:
                max = number
        return max
    
    def divisor(self, digit): # divisor is used as a step to get the index of the digit for the bucket later on
        if digit == 1:
            return 1
        if digit == 2:
            return 10
        if digit == 3:
            return 100
        if digit == 4:
            return 1000
        if digit == 5:
            return 10000
        if digit == 6:
            return 100000
        if digit == 7:
            return 1000000
        if digit == 8:
            return 10000000
        if digit == 9:
            return 100000000    
    
    def putInBucket(self, bucket, num):
        index = 0       # start at index 0
        while self.temp[bucket][index] != None:
            index += 1      # search until that bucket has a None value
        self.temp[bucket][index] = num  # insert at the None value
    
    def emptyBucket(self):      # emptys every singel bucket
        index = 0       # keep track of index to re-arrange the list
        r = len(self.list)
        for i in range(10):
            for j in range(r):
                if self.temp[i][j] == None:     # None means no more numbers in that bucket
                    break       # break to go to next bucket
                self.list[index] = self.temp[i][j]      # if number in bucket, add to list
                self.temp[i][j] = None              # rest temp to None
                index += 1          # increment index for next number
            if index == r:      # if sorted list is full no need to continue to check
                break 
               
    def sort(self):
                # largest Index is the range of the largest number
        largestIndex = len(str(self.largestNumber())) + 1
                # start from digit 1 to the largest Number digit
        for digit in range( 1, largestIndex):
            divide = self.divisor(digit) # divisor is used to return what do divide by to get the bucket later on
            for num in self.list:
                if num == None:     # if number is None no need to continue checking that row
                    break
                bucket = (num / divide) % 10        # this gives the bucket number to insert the number
                self.putInBucket(bucket, num)
            self.emptyBucket()
        return self.list
            
    def printSorted(self):
        print("SORTED LIST")
        print(self.list)
    
    def getSortedList(self):
        return self.sortedList

