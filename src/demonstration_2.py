"""
You are given a non-empty array that represents the digits of a non-negative integer.
​
Write a function that increments the number by 1.
​
The digits are stored so that the digit representing the most significant place value is at the beginning of the array.
Each element in the array only contains a single digit.
​
You will not receive a leading 0 in your input array (except for the number 0 itself).
​
Example 1:
​
Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.
​
Example 2:
​
Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.
​
Example 3:
​
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here
    # turning the list of digits into a string 
    # turning the string into an int 
    # add one to the int 
    # transform the new number back into an array of digits 

    # traverse through a digits in reverse 
    for i in range(len(digits) - 1, -1, -1):
        # if our right-most digit is a 9 
        if digits[i] == 9:
            # change that to a 0 
            digits[i] = 0
            # we need to carray a 1 over to the next digit 
        # our digit is not a 9 
        else:
            # add 1 to our digit 
            digits[i] += 1
            # return 
            return digits

    # if we get to the end our loop, we had to carry all the way 
    # through every digit 
    # we need to insert a 1 at the beginning of the digits list 
    return [1] + digits
    
print(plus_one([8,9,9]))
"""
The plus_one function takes and array of non-negative ints and adds one. It 
is very similar to joining all of the numbers to add one more and parsing again. 
However, the function only is worried about the ints 9 and 0. If a value contains 
a 9, then replace with a zero and carry the one or add the one to the reversed idx.
If the ending value a 9 then traverse through normally but start the arrary with
the number 1. 

For instance, 999 because 1000 and 899 becomes 900.
"""