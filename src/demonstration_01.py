"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

(reverse)
write a function that retrieves the first n elements from a list
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

-[0 to n] python we hae a slice (takes a sub section of a list and returns tht dat as a list)
- [start inclusive : end exclusive]
-in JS/ TS '.slice()' method

# check if n is greater than the length of the list
    #then return 'invalid' to the caller
#otherwise if n is equal to zero
    #return an empty list

#otherwise
    # return the slice of [0: n]

    (forward)
write a function that retrieves the first n elements from a list
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

-[0 to n] python we hae a slice (takes a sub section of a list and returns tht dat as a list)
- [start inclusive : end exclusive]
-in JS/ TS '.slice()' method

# check if n is greater than the length of the list
    #then return 'invalid' to the caller
#otherwise if n is equal to zero
    #return an empty list

#otherwise
    # return the slice of [length of the list -(n - 1): length of list + 1]




"""


def last(a, n):
    if n > len(a):
        return 'invalid'
    elif n == 0:
        return []
    else:
        #return [len(a) - n : len(a)]
        #return a slice of list a[-n : ]
        return a[-n: ]

