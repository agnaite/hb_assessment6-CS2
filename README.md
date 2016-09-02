# hb_assessment6-CS2

##Recursion

####In your own words, what is Recursion?

####Why is it necessary to have a Base Case?

##Graphs

####What is a Graph?
####How is a Graph different from a Tree?
####Give an example of somthing that would be good to model with a Graph.


##Performance of Different Data Structures

####Fill in the missing spots in the chart with the correct runtimes. Do this by reasoning through how the data structures work, NOT by looking up the solution. Add-R means add to the right/end/top and Add-L means add to the left/beginning. There are Xs in the spots where that operation doesn’t make sense for that data structure (for instance, you can’t index a Stack, or pop from the end of a Queue). We’ve provided the first few answers for you.

| Data Structure               | Index | Search | Add-R | Add-L | Pop-L | Pop-R |
|------------------------------|-------|--------|-------|-------|-------|-------|
| Python List (Array)          | O(1)  | O(n)   | O(1)  |       |       |       |
| Linked List                  |       |        |       |       |       |       |
| Doubly-Linked List           |       |        |       |       |       |       |
| Queue (as Array)             | X     | X      |       | X     |       | X     |
| Queue (as LL or DLL)         | X     | X      |       | X     |       | X     |
| Stack (as Array, LL, or DLL) | X     | X      |       | X     | X     |       |
| Deque (as DLL)               | X     | X      |       |       |       |       |

* Index: Find an item in the structure when you know its position
* Search: Find an item in the structure when you know its data
* Add(R/L): Set a key in set/dictionary or add node to tree
* Pop(R/L): Remove a key or node

####Fill in Runtime and Memory: 

| Data Structure        | Get  | Add  | Delete | Iterate | Memory |
|-----------------------|------|------|--------|---------|--------|
| Dictionary (Hash Map) | O(1) | O(1) | O(1)   | O(n)    | medium |
| Set (Hash Map)        |      |      |        |         |        |
| Binary Search Tree    |      |      |        |         |        |
| Tree                  |      |      |        |         |        |

* Get: Find an item in the structure
* Add: Set a key in set/dictionary or add node to tree
* Delete: Remove a key or node
* Iterate: Find next item in data structure
* Memory: Relative to data, how much memory is used? (Choices: a little, medium, or a lot)

##Sorting

####Describe in words how the Bubble Sort algorithm works.
####Describe in words how the Merge Sort algorithm works.
####Describe in words how the Quick Sort algorithm works.

##Git Branching

####Give an instance when you would use git branching.
####What is a pull request?
