#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Imports the python script
import Filippone_Exam4


# In[44]:


#Checks to see if function runs with a string
def check_Possible():
    string = "ATTTGGATT"
    k = 3
    output = Filippone_Exam4.possible_kmers(string,k)
    print(output)


# In[46]:


#Checks to see if function runs with an integer
#The function should throw off an error
def check_Possible_int():
    string = 3
    k = 3
    output = Filippone_Exam4.possible_kmers(string,k)
    print(output)


# In[47]:


#Checks to see if function runs with string
def check_obs():
    string = "ATTTGGATT"
    k = 3
    output = Filippone_Exam4.observed_kmers(string,k)
    print(output)


# In[48]:


#Checks to see if function runs with an integer
#The function should throw off an error
def check_obs_int():
    string = 3
    k = 3
    output = Filippone_Exam4.observed_kmers(string,k)
    print(output)


# In[49]:


#Checks to see if function runs with a string
def check_kmer():
    string = "ATTTGGATT"
    output = Filippone_Exam4.kmer_df(string)
    print(output)


# In[34]:


#Checks to see if function runs with an integer
#The function should throw off an error
def check_kmer_int():
    string = 456
    output = Filippone_Exam4.kmer_df(string)
    print(output)


# In[32]:


#Checks to see if function runs with a string
def check_comp():
    string = "ATTTGGATT"
    output = Filippone_Exam4.comp(string)
    print(output)


# In[30]:


#Checks to see if function runs with an integer
#The function should throw off an error
def check_comp_int():
    string = 100
    output = Filippone_Exam4.comp(string)
    print(output)


# In[51]:


# main function that just runs all of the testing functions
def main():
    check_Possible()
    check_obs()
    check_obs_int()
    check_kmer()
    check_kmer_int()
    check_comp()
    check_obs_int()
main()


# In[ ]:




