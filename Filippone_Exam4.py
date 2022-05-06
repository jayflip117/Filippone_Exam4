#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[15]:


#Function for Possible Kmers
def possible_kmers(string, k):
    if isinstance(string, int):
        print("The sequence is not valid")
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
# Return the final counts
    return int(len(counts))


# In[10]:


#Function for Observed Kmers
def observed_kmers(string, k):
    if isinstance(string, int):
        print("The sequence is not valid")
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
        return len(counts)


# In[11]:


#Function that creates a dataframe based off the number of k, observed kmers, and possible kmers
def kmer_df(word):
    if isinstance(word, int):
        print("The sequence is not valid")
    else:

        out = []
        count_obs = []
        count_pos = []
        kmer = 0
        for i in range(len(word)):
            kmer = kmer + 1
            out.append(kmer)
        df = pd.DataFrame (out, columns = ['k'])

        for i in range(len(word)):
            count_obs.append(observed_kmers(word, out[i]))
  
        for i in range(len(word)):
            count_pos.append(possible_kmers(word, out[i]))
        df["Observed Kmer"] = count_obs
        df["Possible Kmer"] = count_pos
        return df


# In[12]:


def comp(seq):
    if isinstance(seq, int):
        print("The sequence is not valid")
    else:
        out = []
        count_obs = []
        count_pos = []
        total_obs = 0
        total_pos = 0
        total = 0
        for i in range(len(seq)):
            out.append(i+1)
        for i in range(len(seq)):
            count_obs.append(observed_kmers(seq, out[i]))
        for i in range(len(seq)):
            count_pos.append(possible_kmers(seq, out[i]))
        total_obs = sum(count_obs)
        total_pos = sum(count_pos)
        total = total_obs / total_pos
        return total


# In[6]:


if __name__ == "__main__":
    file = open("sampledna.txt.txt", "r")
    lines = file.readlines()
    lines[2] = lines[2]. replace(";", "")

    seq1 = kmer_df(lines[0])
    seq1.to_csv(r'sequence1.txt', header=None, index=None, sep='\t', mode='a')   
    output1 = comp(lines[0])
    print("The linguistic complexity for the first sequence is: ", output1)

    seq2 = kmer_df(lines[1])
    seq2.to_csv(r'sequence2.txt', header=None, index=None, sep='\t', mode='a')   
    output2 = comp(lines[1])
    print("The linguistic complexity for the second sequence is: ", output2)
    
    seq3 = kmer_df(lines[2])
    seq3.to_csv(r'sequence3.txt', header=None, index=None, sep='\t', mode='a')   
    output3 = comp(lines[2])
    print("The linguistic complexity for the third sequence is: ", output3)


# In[ ]:




