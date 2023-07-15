'''
Question:
William Macfarlane wants to look at an array.

You are given a list of N numbers and Q queries. Each query is specified by two numbers i and j; the answer to each query is the sum of every number between the range [i, j] (inclusive).

Note: the query ranges are specified using 0-based indexing.

Input
The first line contains N, the number of integers in our list (N <= 100,000). The next line holds N numbers that are guaranteed to fit inside an integer. Following the list is a number Q (Q <= 10,000). The next Q lines each contain two numbers i and j which specify a query you must answer (0 <= i, j <= N-1).

Output
For each query, output the answer to that query on its own line in the order the queries were made.

Example
Input:
3
1 4 1
3
1 1
1 2
0 2

Output:
4
5
6
'''

#Solution - Use prefix 

def cummulative_sum(nums, queries):
    prefix_dict = {}
    prefix_sum = 0
    for index,num in enumerate(nums):
        prefix_sum += num
        prefix_dict[index] = prefix_sum
    
    returnlist = []
    for query in queries:
        i = query[0]
        j = query[1]
        returnlist.append(prefix_dict[j] - prefix_dict.get(i-1,0))
    return returnlist
    
print(cummulative_sum([1,4,1], [[1,1],[1,2],[0,2]]))

# Answer is [4,5,6]