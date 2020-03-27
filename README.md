# Project Problems-Vs-Algorithms
## Data Structures and Algorithms - Udacity Nanodegree

This project expected me to answer seven questions that covered a variety of topics related to the basic algorithms I had learned in this course. This repository has clean and efficient answers in Python, as well as a text explanation of the efficiency and design choices of the code.

## problem_1.py
To match the expected **time complexity of O(log(n))**, a binary search style approach was used to tackle the problem. The middle element of the array was squared and compared with the target to find out the half of the array that the square root of the target belonged to, and the other half was eliminated. Since we did not explicitly create any data structure to store data in the program, the **space complexity is O(1)**.

## problem_2.py
Again, to match the expected **time complexity of O(log(n))**, a binary search had to be used to find the element, but since the array was rotated, an initial binary search approach had to be employed to find the pivot, then based on the pivot, the half containing the target is identified, and then binary search is applied on the desired half. Again, similar to the previous problem, as we did not explicitly create any data structure to store data in the program, the **space complexity is O(1)**.

## problem_3.py
In this problem, the goal is to maximize the sum of the two formed number. So, to begin with, the array was iterated, to find the frequency of each digits, and the frequencies are stored in an array. Now the original array is iterated through from last and the numbers are appended to form two numbers which are finnaly joined to create the required list. Since the array was iterated once the **time complexity is O(n)** and as we are creating another array of constant size, the **space complexity is O(1)**.

## problem_4.py
To sort the arrays with 0s, 1s and 2s, I moved all the 0s to the beginning, and 2s to the end which by default leaves the 1s in the middle. Since this was done in a single traversal, the **time complexity is O(n)** and as no extra memory was used to store data in the problem, the **space complexity is O(1)**.

## problem_5.ipynb
This jupyter notebook contains code for building a **trie** for searching and inserting words and we attempt to autocomplete words with the trie defined. The time complexity depends on the length of the word (*a*) that is being searched for, inserted and the total number of words (*t*) making the **time complexity as O(n)**. Since we have not created any data structure that is of the size of the variable, and only have a set of fixed size pointers, the **space complexity is O(1)**.

## problem_6.py
Here, we are required to find the smallest and largest in an unsorted array in one traversal and so the **time complexity is O(n)**. For this, we create two variables to hold the smallest and largest value of the array, and as we traverse through the array, we keep comparing with all the elements in the array and update them if necessary. Again, since we only have two variables of fixed length to store the maximum and mimimum length, the **space complexity is O(1)**.

## problem_7.py
It is similar to problem 5, except for the edge cases, like "root handler", and working with a hierarchy of web pages instead of strings and we use a tries to accomplish the same. For the trie,searching and inserting from a trie depends on the length of the path (**n**) that’s being searched for, inserted, making the **time complexity as O(n)**. Looking into the space complexity of a trie, the worst case, would be when we have a path (or paths), with no common folders between them, hence having, a node for each path block (path between forward slashes). Resulting in a **space complexity of O(n)**.
