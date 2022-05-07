Jason Filippone
Exam 4 Directions for Running in Command Line and 


Filippone_Exam4 Python Script:
The python script contains four functions and a main function. Below will explain each function of the Python script:

1. Possible Kmers
  a. This function finds all possible kmers of a sequence given k
  b. The functions takes a string and k as parameters 
  
2. Obeservd Kmers
  a. This function finds all observed kmers of a sequence given k
  b. The functions takes a string and k as parameters 

3. Kmer Df
  a. Function that creates a dataframe based off the number of k, observed kmers,          and possible kmers
  b. The data frame has three columns, k, observed kmers, and possible kmers
  
4. Comp
  a. Finds the linguistic complexity given a sequence
  b. Uses both the possible kmers and observed kmers function
  c. Divides total observed kmers by total possible kmers
  
5. Main
  a. The main function opens the data file, reads the three sequences, and stores the      sequences in a list
  b. The function removes a ; from the end of the tird sequence
  c. It also makes three output files for each sequence
  d. The output files include the data frame from the third function
  e. The function finally calculates the linguistic complexity for each sequence
  
Test Script:

The test script is ran to check if the functions from the previous scripts are running properly. The script checks that the functions only run with strings and not integers.

Files in the Repo:
There are seven files in the Repo which include:
1. README
2. Filippone_Exam4 Python Script
3. Test Script
4. Data File
5. Sequence 1 output file containing a data frame
6. Sequence 2 output file containing a data frame
7. Sequence 3 output file containing a data frame

How to Run the Files:
1. Download the python script, test script, and data file to your desktop
2. Open your terminal or command line on your computer
3. To run the python script to receive the output files, run python3 Filippone_Exam4.py in the command line
4. To test the script, run python3 test_exam.py in the command line


