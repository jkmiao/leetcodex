#!/usr/bin/env python
# coding=utf-8
"""
    
   __author__: jkmiao
   create_time: 2016-12-26
   description:  
   Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

   Note:
   The number of people is less than 1,100.

   Example

   Input:
       [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

   Output:
       [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""

class Solution(object):
    
    def reconstructQueue(self, people):
        """
        还有错误，未能解决！！！
        """

        def people_compare(x, y):
            if x[0]==y[0]:
                return x[1]>y[1]
            return x[0]<y[0]

        people = sorted(people, cmp=people_compare)
        result = []
        for p in people[1:]:
            idx = p[1]
            result.insert(idx, p)
        return result


    def insert_sort(self, people):
        count = len(people)
        for i in range(count):
            current = people[i]
            j = i-1
            while j>=0:
                if people[j] > current:
                    people[j+1] = people[j]
                    people[j] = current
                j-=1
        return people
    
    def quick_sort(self, lists, left, right):
        # 快速排序
        if left >= right:
            return lists
        key = lists[left]
        low = left
        high = right
        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            while left < right and lists[left] <= key:
                left += 1
            lists[left], lists[right] = lists[right], lists[left]
        
        lists[left] = key
        
        self.quick_sort(lists, low, left - 1)
        self.quick_sort(lists, left + 1, high)
        
        return lists


if __name__=="__main__":
    

    a = [[7,0], [4,4], [7,1], [5,0], [6,1],[5,2]]
    print 'a: ', a
    test = Solution()
    print test.reconstructQueue(a)
