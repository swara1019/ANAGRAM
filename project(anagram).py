#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 'boat'
y = list(x)
print(y)


# In[2]:


def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap(y,0,2)


# In[3]:


str = ''
d=str.join(y)
print(d)


# In[3]:


a = input("enter any word=")
b = list(a)
print(b)
def swap_words(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap_words(b,1,4)
str1 = ''
z=str1.join(b)
print(z)


# In[2]:


#Project 1 (Anagram):-
A = input("enter any word=")
B = list(A)
print(B)
def swap_words(list,pos1,pos2,pos3):
    list[pos1],list[pos2],list[pos3]=list[pos3],list[pos1],list[pos2]
    return list
swap_words(B,1,3,5)
str2 = ''
Z=str1.join(B)
print(Z)


# In[11]:


#write a program to check weather the two given words are anagram or not. ensure that the words are 
#prompt
word1 = input("Enter word one: ")
word2 = input("Enter word two: ")

clean_word1 = word1.replace(" ", "").lower()
clean_word2 = word2.replace(" ", "").lower()

if sorted(clean_word1) == sorted(clean_word2):
    print(word1, "and", word2, "are anagrams.")
else:
    print(word1, "and", word2, "are not anagrams.")


# In[ ]:





# In[ ]:





# In[ ]:




