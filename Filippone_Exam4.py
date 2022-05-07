#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[15]:


#Function that finds all possible kmers given a string and k
def possible_kmers(string, k):
    #Checks to see if the string is actually an integer
    #If it is an integer then it throws off an error
    if isinstance(string, int):
        print("The sequence is not valid")
    #If the string is not an integer, then the function runs
    else:
 # Declares an empty list called counts
        counts = []
  # Loop over the length of the string - k + 1
        for i in range(len(string) - k + 1):
      # Slice the string to get the kmer
            kmer = string[i:i+k]
            counts.append(kmer)
      # Add the kmer to the list if it's not there
            if kmer not in counts:
              counts.append(kmer)
        # Increment i
            i += 1
# Return the length final counts
    return int(len(counts))


# In[10]:


#Function that finds all observed kmers given a string and k
def observed_kmers(string, k):
    #Checks to see if the string is actually an integer
    #If it is an integer then it throws off an error
    if isinstance(string, int):
        print("The sequence is not valid")
    #If the string is not an integer, then the function runs
    else:
 # Declares an empty list called counts
        counts = []
  # Loop over the length of the string - k + 1
        for i in range(len(string) - k + 1):
      # Slice the string to get the kmer
            kmer = string[i:i+k]
      # Add the kmer to the list if it's not there
            if kmer not in counts:
              counts.append(kmer)
        # Increment i
            i += 1
# Return the length final counts
        return len(counts)


# In[11]:


#Function that creates a dataframe based off the number of k, observed kmers, and possible kmers
def kmer_df(word):
    #Checks to see if the string is actually an integer
    #If it is an integer then it throws off an error
    if isinstance(word, int):
        print("The sequence is not valid")
    else:
        #Declares three empty lists for the data frame
        out = []
        count_obs = []
        count_pos = []
        #Declare a counter
        kmer = 0
        
        #Finds all values of k given the string
        for i in range(len(word)):
            kmer = kmer + 1
            #Appends the k to the list
            out.append(kmer)
        #Adds the k to the data frame
        df = pd.DataFrame (out, columns = ['k'])

        #Finds all observed kmers in the word
        for i in range(len(word)):
            #Adds the observed kmers to a list 
            count_obs.append(observed_kmers(word, out[i]))
        #Finds all observed kmers in the word
        for i in range(len(word)):
            #Adds the observed kmers to a list
            count_pos.append(possible_kmers(word, out[i]))
        #Adds the lists to the data frame
        df["Observed Kmer"] = count_obs
        df["Possible Kmer"] = count_pos
        #Returns the data frame
        return df


# In[12]:



def comp(seq):
    #Checks to see if the string is actually an integer
    #If it is an integer then it throws off an error
    if isinstance(seq, int):
        print("The sequence is not valid")
    else:
        #Declares three empty lists that will be added to the data frame
        out = []
        count_obs = []
        count_pos = []
        
        #Declares three counter variables that will be used for the math calculations
        total_obs = 0
        total_pos = 0
        total = 0
        
        #The three below for loops all calculate things that are needed for linguistic complexity
        for i in range(len(seq)):
            out.append(i+1)
        
        for i in range(len(seq)):
            count_obs.append(observed_kmers(seq, out[i]))
        
        for i in range(len(seq)):
            count_pos.append(possible_kmers(seq, out[i]))
        
        #Below calculates linguistic complexity
        total_obs = sum(count_obs)
        total_pos = sum(count_pos)
        total = total_obs / total_pos
        
        return total


# In[6]:


if __name__ == "__main__":
    #Reads in the data file
    file = open("sampledna.txt.txt", "r")
    #Assigns the sequences to a list
    lines = file.readlines()
    #Removes the semicolon from the third sequence
    lines[2] = lines[2]. replace(";", "")
    
    #Makes an output file with the data frame for the first sequence
    seq1 = kmer_df(lines[0])
    seq1.to_csv(r'sequence1.txt', header=None, index=None, sep='\t', mode='a')   
    #Finds the linguistic complexity of the first sequence
    output1 = comp(lines[0])
    print("The linguistic complexity for the first sequence is: ", output1)

    #Makes an output file with the data frame for the second sequence
    seq2 = kmer_df(lines[1])
    seq2.to_csv(r'sequence2.txt', header=None, index=None, sep='\t', mode='a')   
    #Finds the linguistic complexity of the first sequence
    output2 = comp(lines[1])
    print("The linguistic complexity for the second sequence is: ", output2)
    
    #Makes an output file with the data frame for the third sequence
    seq3 = kmer_df(lines[2])
    seq3.to_csv(r'sequence3.txt', header=None, index=None, sep='\t', mode='a')   
    #Finds the linguistic complexity of the first sequence
    output3 = comp(lines[2])
    print("The linguistic complexity for the third sequence is: ", output3)


# In[ ]:




