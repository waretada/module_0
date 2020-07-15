#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np                     
number = np.random.randint(1,101)

        
def score_game(game_core):
    """Running game 1000 times to know how many attempts on average about 
    are needed for prediction
    """
    
    count_ls = []
    np.random.seed(1945)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101,size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def get_mid(a,b):
    """Getting 'a middle': the left nearest integer to the arithmetic mean 
    of two integers numbers
    """
        
    mid = (a+b) // 2 
    return mid


def game_core_v3a(number):
    """Improved predicting number algorithm based on approximately  
    twice reducing the search interval with every next attempt
    """
    
    count = 1                          
    predict = 100 
    
    if number == predict:             
        pass    
    else:                          
        left_p = 1        
        right_p = 100     
        while number != predict:    
            count+=1 
            if number < predict:  
                right_p = predict
                predict = get_mid(left_p,right_p)  
            elif number > predict:
                left_p = predict
                predict = get_mid(left_p,right_p)      
    return(count)                        


# In[11]:


score_game(game_core_v3a)


# In[ ]:




