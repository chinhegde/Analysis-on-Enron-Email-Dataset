# Analysis-on-Enron-Email-Dataset
Frequent Itemsets on Enron email dataset using Hadoop MapReduce:

Firstly, download the dataset: Enron Email Dataset

This exercise is implemented in the following way:
1. Get all email data from the given directories into 1 file -> emails.txt
2. Create datasets for mappers & reduces for each part of the exercise:
  a. Line as unit -> 3a.txt
  b. Sentence as unit -> 3b.txt
  c. Paragraph as unit -> 3c.txt
3. Execute MapReduce for all the text files on Hadoop 
4. Execute FPG using MAHOUT for all text files

### Data pre-processing:
● Remove lines that start with “To:”, “From:”, “Subject:”, etc.
● Due to the presence of threads, forwards, and replies, we will still have such data.
● Remove digits and replace with space “ “.
● Remove all special characters (except full stop/period for Exercise 3B - Sentence)
● Remove ‘\t’ tabs.
● Convert all words to lowercase

### Steps to execute on Mahout: 

1. Copy input file 3a.txt to HDFS
  a. hdfs dfs -put 3a.txt /hegde/q3/
2. Run Mahout command:
  a. mahout fpg -i /hegde/q3/3a.txt -o /hegde/q3/output -method mapreduce
3. Sequence Dumper command to see frequent patterns:
  a. mahout seqdumper -i /hegde/q3/output_3b/frequentpatterns/part-r-00000
