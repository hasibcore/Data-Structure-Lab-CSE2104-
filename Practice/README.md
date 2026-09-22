# 📚 Data Structure Practice Problems & Implementations

This directory contains categorized practice implementations for core **Data Structures & Algorithms (CSE2104)**, covering **Graph Algorithms**, **Stack Applications**, and **Linked List Sorting**.

---

## 📁 Directory Structure

```
Practice/
├── README.md
├── Graph/
│   ├── Biparthite.cpp
│   ├── cycleByHareAndToroise.cpp
│   ├── cycleDetection.cpp
│   ├── DFS_unconnected_withoutrecursion.cpp
│   ├── DFS_unconnectedGraph.cpp
│   ├── DFS_withoutRecursion.cpp
│   └── Topological_Sort.cpp
├── Stack/
│   ├── evaluate.cpp
│   └── infixToPostfix.cpp
└── Linked List/
    ├── singlyLinklistInsertionSort.cpp
    └── singlyLinklistSelectionSort.cpp
```

---

## 🌐 1. Graph Algorithms (`Practice/Graph/`)

| File | Algorithm / Topic | Description |
|---|---|---|
| [`Biparthite.cpp`](./Graph/Biparthite.cpp) | **Bipartite Graph 2-Coloring** | Checks whether a graph is 2-colorable (bipartite) using DFS and outputs the two independent vertex sets. |
| [`cycleDetection.cpp`](./Graph/cycleDetection.cpp) | **Cycle Detection (DFS)** | Detects cycles in an undirected graph using DFS back-edge detection and prints cycle nodes. |
| [`cycleByHareAndToroise.cpp`](./Graph/cycleByHareAndToroise.cpp) | **Floyd's Tortoise & Hare** | Cycle detection algorithm using two pointers moving at different speeds. |
| [`DFS_withoutRecursion.cpp`](./Graph/DFS_withoutRecursion.cpp) | **Iterative DFS** | Traverses a connected graph using an explicit `std::stack` instead of system recursion. |
| [`DFS_unconnectedGraph.cpp`](./Graph/DFS_unconnectedGraph.cpp) | **DFS on Disconnected Graphs** | Traverses all components of a disconnected graph using recursive DFS. |
| [`DFS_unconnected_withoutrecursion.cpp`](./Graph/DFS_unconnected_withoutrecursion.cpp) | **Iterative DFS (Disconnected)** | Iterative stack-based DFS traversal covering all disconnected components. |
| [`Topological_Sort.cpp`](./Graph/Topological_Sort.cpp) | **Topological Sort (DAG)** | Computes linear ordering of vertices in a Directed Acyclic Graph using DFS departure times and stack. |

---

## 🥞 2. Stack Applications (`Practice/Stack/`)

| File | Topic | Description |
|---|---|---|
| [`infixToPostfix.cpp`](./Stack/infixToPostfix.cpp) | **Infix to Postfix Conversion** | Converts standard arithmetic infix expressions containing operators (`+`, `-`, `*`, `/`, `^`) and parentheses into postfix notation (Reverse Polish Notation) using an operator stack. |
| [`evaluate.cpp`](./Stack/evaluate.cpp) | **Postfix Expression Evaluation** | Evaluates a postfix arithmetic expression using an operand stack to calculate final numerical results. |

---

## 🔗 3. Linked List Algorithms (`Practice/Linked List/`)

| File | Topic | Description |
|---|---|---|
| [`singlyLinklistSelectionSort.cpp`](./Linked%20List/singlyLinklistSelectionSort.cpp) | **Selection Sort on Singly Linked List** | Implements Selection Sort on a dynamic singly linked list by finding the minimum node and swapping data values. |
| [`singlyLinklistInsertionSort.cpp`](./Linked%20List/singlyLinklistInsertionSort.cpp) | **Insertion Sort on Singly Linked List** | Implements Insertion Sort by dynamically maintaining a sorted sublist and inserting nodes into their proper position. |

---

<div align="center">

*CSE2104 - Data Structures & Algorithms Practice | Department of Computer Science & Engineering*

</div>
