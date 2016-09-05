# hb_assessment6-CS2

##Recursion

####In your own words, what is Recursion?
A function that keeps calling itself until a predefined condition is met.

####Why is it necessary to have a Base Case?
With no base case, a recursive function would keep calling itself and end in the recursion depth exceeded error.

##Graphs

####What is a Graph?
A graph is a data structure that has nodes connected by directed or undirected arcs.

####How is a Graph different from a Tree?
Trees have a hierarchy and graphs do not.

####Give an example of somthing that would be good to model with a Graph.
A model for computer networks and the internet.

##Performance of Different Data Structures

####Fill in the missing spots in the chart with the correct runtimes. Do this by reasoning through how the data structures work, NOT by looking up the solution. Add-R means add to the right/end/top and Add-L means add to the left/beginning. There are Xs in the spots where that operation doesn’t make sense for that data structure (for instance, you can’t index a Stack, or pop from the end of a Queue). We’ve provided the first few answers for you.

| Data Structure               | Index | Search | Add-R | Add-L | Pop-L | Pop-R |
|------------------------------|-------|--------|-------|-------|-------|-------|
| Python List (Array)          | O(1)  | O(n)   | O(1)  | O(n)  | O(n)  | O(1)  |
| Linked List                  | O(n)  | O(n)   | O(1)  |  O(1) | O(1)  | O(n)  |
| Doubly-Linked List           | O(n)  | O(n)   | O(1)  | O(1)  | O(1)  | O(1)  |
| Queue (as Array)             | X     | X      | O(1)  | X     | O(n)  | X     |
| Queue (as LL or DLL)         | X     | X      | O(1)  | X     | O(1)  | X     |
| Stack (as Array, LL, or DLL) | X     | X      | O(1)  | X     | X     | O(1)  |
| Deque (as DLL)               | X     | X      | O(1)  | O(1)  | O(1)  | O(1)  |

* Index: Find an item in the structure when you know its position
* Search: Find an item in the structure when you know its data
* Add(R/L): Set a key in set/dictionary or add node to tree
* Pop(R/L): Remove a key or node

####Fill in Runtime and Memory: 

| Data Structure        | Get   | Add  | Delete | Iterate | Memory |
|-----------------------|-------|------|--------|---------|--------|
| Dictionary (Hash Map) | O(1)  | O(1) | O(1)   | O(n)    | medium |
| Set (Hash Map)        | O(1)  | O(1) |  O(1)  | O(n)    | medium |
| Binary Search Tree    |O(logn)| O(n) |  O(n)  |  O(1)   | low    |
| Tree                  | O(n)  | O(1) |  O(1)  |  O(1)   | low    |

* Get: Find an item in the structure
* Add: Set a key in set/dictionary or add node to tree
* Delete: Remove a key or node
* Iterate: Find next item in data structure
* Memory: Relative to data, how much memory is used? (Choices: a little, medium, or a lot)

##Sorting

####Describe in words how the Bubble Sort algorithm works.
Bubble sort takes the current value and one immediately following it and compares them to each other. For example, if current item is greater than the item after the current one, the two items will swap, or stay the same otherwise. After every iteration the largest item "bubbles" to the end of the list until the list is sorted.

####Describe in words how the Merge Sort algorithm works.
A merge algorithm recursively splits an array in half until there's only one item per array left and then merges them back together in the right order.

####Describe in words how the Quick Sort algorithm works.
A quick sort divides numbers in an array based on a specified number, called pivot. All the numbers smaller than the pivot go on one side, and all the bigger ones go on the other side. Using this system, the array keep getting split until all the numbers are sorted.

##Git Branching

####Give an instance when you would use git branching.
Starting a new feature. This way the project will remain stable on the master branch and once the feature works and has been tested, it can be merged with master.

####What is a pull request?
A request that another developer pulls a branch from your repository into their repository. 
