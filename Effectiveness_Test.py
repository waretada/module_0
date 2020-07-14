#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np                     
number = np.random.randint(1,101)

        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1945)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101,size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

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


# In[6]:


score_game(game_core_v3)


# In[ ]:




