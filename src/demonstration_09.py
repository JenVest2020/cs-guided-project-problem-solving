"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"

    -to find out if string length is even we could decompose the logic into its own function
    
    -we will need to find out the length of the string and set it to str_len
    -to get the middle/mean index of the string length we can divide the str_len by 2 and set it to #middle_index
    -make sure the number is usable as an index we want to floor it
    -in python we have a floor divide //  in JS/TS 'Math.floor' method to do a similar thing
   
    
    -in the case of even length: return a slice of [middle_index - 1: middle_index + 1]
    
    -in the case of odd: return a slice of [middle_index: middle_index +1]
"""
def get_middle(input_str):
    # to find out if string length is even we could decompose the logic into its own function
    str_len = len(input_str)
    #we will need to find out the length of the string and set it to str_len
    #to get the middle/mean index of the string length we can divide the str_len by 2 and set it to #middle_index
    #make sure the number is usable as an index we want to floor it
    # in python we have a floor divide //  in JS/TS 'Math.floor' method to do a similar thing
    middle_index = str_len // 2
    
    #in the case of even length: return a slice of [middle_index - 1: middle_index + 1]
    if str_len % 2 == 0:
        return input_str[middle_index - 1: middle_index + 1]
    #in the case of odd: return a slice of [middle_index: middle_index +1]
    else:
        return input_str[middle_index: middle_index + 1]


#some tests
print(get_middle("test")) # -> "es"
print(get_middle("testing")) # -> "t"
print(get_middle("middle")) # -> "dd"
print(get_middle("A")) # -> "A"