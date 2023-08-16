#!/usr/bin/env python3
#eturns a list of all of the even elements of a sequence of integers between 0 and 9
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0 in range(0,10)]
    

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]