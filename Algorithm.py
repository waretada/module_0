#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 

def get_mid(a,b):
    """Getting 'a middle': the left nearest integer to the arithmetic mean 
    of two integers numbers

    :param a: an integer number
    :param b: an integer number
  
    """
        
    mid = (a+b) // 2 
    return mid


def game_core_v3a(number):
    """Improved predicting number algorithm based on approximately  
    twice reducing the search interval with every next attempt
    
    :param number: an integer number between 1 and 100, to be predicted
    
    """
    
    count = 1                          # The attempt's counter.The 1-st attempt.
    predict = 100                      # Setting predictable value for the 1-st attempt.
    if number == predict:              # Is the right end of interval (1;100) the desired number? 
        pass
    
    else:                               # If the 1-st attempt is not successful...
        # At every next attempt: count it, take the next search interval 
        # and check whether its 'middle' what is needed or not.
        left_p = 1        # The left point of the previous,i.e.the 1-st, search interval.
        right_p = 100     # The right point of the search interval mentioned above.    
    
        while number != predict:    # Repeat procedure below until find the desired number 
            count+=1 
            if number < predict:  
                # If the desired number is less than the 'middle' of the previous search interval, 
                # take the left half of the previous one as the next interval.
                right_p = predict
                predict = get_mid(left_p,right_p)  
                
            elif number > predict:
                # If the desired number is more than the 'middle' of the previous search interval,
                # take the right half of the previous one as the next interval.
                left_p = predict
                predict = get_mid(left_p,right_p)       
                       
    return(count)                        # Return how many attempts did it take

