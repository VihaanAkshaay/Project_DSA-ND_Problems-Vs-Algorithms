# Project Problems-Vs-Algorithms
## Data Structures and Algorithms - Udacity Nanodegree

This project expected me to answer seven questions that covered a variety of topics related to the basic algorithms I had learned in this course. This repository has clean and efficient answers in Python, as well as a text explanation of the efficiency and design choices of the code.

## problem_1.py
To match the expected **time complexity of O(log(n))**, a binary search style approach was used to tackle the problem. The middle element of the array was squared and compared with the target to find out the half of the array that the square root of the target belonged to, and the other half was eliminated. Since we did not explicitly create any data structure to store data in the program, the **space complexity is O(1)**.

## problem_2.py
Again, to match the expected **time complexity of O(log(n))**, a binary search had to be used to find the element, but since the array was rotated, an initial binary search approach had to be employed to find the pivot, then based on the pivot, the half containing the target is identified, and then binary search is applied on the desired half. Again, similar to the previous problem, as we did not explicitly create any data structure to store data in the program, the **space complexity is O(1)**.

## problem_3.py
In this problem, the goal is to maximize the sum of the two formed number. So, to begin with, the array was iterated, to find the frequency of each digits, and the frequencies are stored in an array. Now the original array is iterated through from last and the numbers are appended to form two numbers which are finnaly joined to create the required list. Since the array was iterated once the **time complexity is O(n)** and as we are creating another array of the same size finally, the **space complexity is O(n)**.

## problem_4.py
To sort the arrays with 0s, 1s and 2s, I moved all the 0s to the beginning, and 2s to the end which by default leaves the 1s in the middle. Since this was done in a single traversal, the **time complexity is O(n)** and as no extra memory was used to store data in the problem, the **space complexity is O(1)**.

## problem_5.py

