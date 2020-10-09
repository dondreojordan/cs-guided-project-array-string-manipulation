"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
​
The "pivot" index is where the sum of all the numbers on the left of that index is equal to the 
sum of all the numbers on the right of that index.
​
If the input array does not have a "pivot" index, then the function should return `-1`. 
If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
​
Example 1:
​
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers 
to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
​
Example 2:
​
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here
    # single-element arrays would just return index 0 
    # if there's no left side, consider the left side to be 0 
    # if there's no right side, consider the right side to be 0 
    # O(n^2) runtime, O(n) space  
    # # iterate over the nums 
    # for i in range(len(nums)): # O(n)
    #     # figure out the sum of the left side 
    #     # use slicing syntax to get everything up to but not including i 
    #     # O(n) 
    #     left = sum(nums[:i]) # O(i)
    #     # figure out the sum of the right side 
    #     # use slicing syntax to get everything after i 
    #     right = sum(nums[i+1:]) # O(n - i)
    #     # check if they're equal 
    #     if left == right:
    #         # if they're equal, return that index 
    #         return i 

    # # if we get through the entire loop, we didn't find an element 
    # # that satisfied the criteria, so we'll return -1 
    # return -1 
###############################################################################
    # get the sum of all elements in the list 
    total = sum(nums)
    # keep track of left sum, which starts off at 0 
    left = 0

    # iterate over the length of our nums
    for i, num in enumerate(nums):
        # our right sum is the total | left sum - our current num 
        right = total - left - num
        print(f'total {total}, right {right}, left {left}, i {i}, num {num}')     # visualize under the hood

        if left == right:
            return i

        # add the previous element to our left sum
        left += num

    return -1
    
nums = [1,7,3,6,5,6]
# nums = [10, 0]
# nums = [1, 2, 3]
print(pivot_index(nums))
"""
The pivot function takes an array of values and returns the pivot point of the
array if the the sum of the values left of the pivot equal to the sum of the 
values to the right of the pivot, then the function will return the index of 
that pivot point (NOT the actual number of the pivoted index). 

If you look at the print statement to see what is happening under the hood, 
you will notice that the right variable decreases the left increases. When the
left and right side converge, the function will stop and return the idx of that
converging idx. Since we know that when you are iterating one by one and within 
that iteration you know that one side is decreasing while the other is increasing,
the point were the two sides OUGHT to converge would be at a mid-like point. If 
there is no converging point, the default action is to return a -1.
"""