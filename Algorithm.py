#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 

def get_mid(a,b):
    mid = (a+b) // 2 
    return mid

def game_core_v3(number):
    '''Реализация принципа вложенных отрезков 
    (последовательное сужение интервала поиска с учетом опыта предыдущих попыток)'''
    count = 1                          # счетчик попыток
    predict = 100
    if number == predict:
        return(count)  
    else:
        predict = get_mid(1,100)
        count+=1
        left = 1
        right = 100
        while number != predict:
            count+=1
            if number > predict: 
                left = predict
                predict = get_mid(left,right)
            elif number < predict: 
                right = predict
                predict = get_mid(left,right)
            #print(left, right)
    return(count) # выход из цикла, если угадали


# In[ ]:




