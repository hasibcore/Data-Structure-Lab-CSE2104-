# 📚 Data Structure Lab: Offline Assignment 1

Welcome to **Offline Assignment 1** for the CSE2104 Data Structure Lab! This assignment focuses on implementing searching algorithms and understanding their variations. 

This directory contains the C++ implementation for **Binary Search**, **Lower Bound**, and **Upper Bound** algorithms applied to a bookstore inventory system.

---

## 🎯 Problem Statement

A bookstore maintains a sorted list of unique book IDs to quickly identify whether a book is available in stock. The task is to write a C++ program that uses **Binary Search** to determine if a specific book ID is present in the list. Additionally, the store often needs to find the first book ID that is not smaller than a given value (**lower bound**) and the first book ID that is greater than a given value (**upper bound**) in order to manage restocking and categorization. 

Given a sorted array of book IDs and a query book ID, the program outputs:
1. Whether the book exists in the list.
2. The lower bound position.
3. The upper bound position corresponding to the query.

---

## 💡 Concepts Explained

### 1. 🔍 Binary Search
Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

**How it works in our code:**
- **Initial State:** We have pointers `low = 0` and `high = n - 1`.
- **Process:** We calculate the middle index `mid`.
  - If the target matches the middle element (`key == arr[mid]`), we found it!
  - If the target is greater, it must be in the right half (`low = mid + 1`).
  - If the target is smaller, it must be in the left half (`high = mid - 1`).
- **Time Complexity:** `O(log N)`

### 2. 📉 Lower Bound
The Lower Bound of a target value is the **first element in a sorted array that is greater than or equal to (`>=`) the target**. It essentially finds the earliest valid insertion point for the target value without disrupting the sorted order.

**How it works in our code:**
- **Initial State:** `low = 0`, `high = n - 1`, and we assume the answer might be out of bounds initially (`ans = n`).
- **Process:**
  - Calculate `mid`.
  - If `arr[mid] >= key`: This could be our answer, so we record it (`ans = mid`). But wait, there might be a smaller index to the left that also satisfies the condition! So we continue searching the left half (`high = mid - 1`).
  - If `arr[mid] < key`: The target must be to the right, so we discard the left half (`low = mid + 1`).

### 3. 📈 Upper Bound
The Upper Bound of a target value is the **first element in a sorted array that is strictly greater than (`>`) the target**.

**How it works in our code:**
- **Initial State:** `low = 0`, `high = n - 1`, `ans = n`.
- **Process:**
  - Calculate `mid`.
  - If `arr[mid] > key`: This element is strictly greater, so it could be our answer (`ans = mid`). To find the *first* such element, we keep searching the left half (`high = mid - 1`).
  - If `arr[mid] <= key`: The element is less than or equal to the target, so the upper bound must be further to the right (`low = mid + 1`).

---

## 🚀 How to Run

1. **Compile the code:**
   ```bash
   g++ 00724205101098_Offline1.cpp -o offline1
   ```

2. **Run the executable:**
   ```bash
   ./offline1
   ```

3. **Provide Input:**
   ```text
   7
   10 20 30 40 50 60 70
   40
   ```

4. **Expected Output:**
   ```text
   Book Found
   Lower Bound Index: 3
   Upper Bound Index: 4
   ```

---
*Generated with ❤️ for CSE2104 Data Structure Lab*
