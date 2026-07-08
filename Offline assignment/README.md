# 📚 Data Structure Lab: Offline Assignments (CSE2104)

Welcome to the **Offline Assignments** for the CSE2104 Data Structure Lab! This repository contains C++ implementations covering searching and sorting algorithms.

---

## 📁 Assignments

---

## 🔎 Offline Assignment 1 — Binary Search, Lower Bound & Upper Bound

This assignment focuses on implementing searching algorithms applied to a bookstore inventory system.

### 🎯 Problem Statement

A bookstore maintains a sorted list of unique book IDs to quickly identify whether a book is available in stock. The task is to write a C++ program that uses **Binary Search** to determine if a specific book ID is present in the list. Additionally, the store often needs to find the first book ID that is not smaller than a given value (**lower bound**) and the first book ID that is greater than a given value (**upper bound**) in order to manage restocking and categorization.

Given a sorted array of book IDs and a query book ID, the program outputs:
1. Whether the book exists in the list.
2. The lower bound position.
3. The upper bound position corresponding to the query.

### 💡 Concepts

#### 🔍 Binary Search
Binary search works by repeatedly dividing in half the portion of a sorted list that could contain the target item.
- If `key == arr[mid]` → Found!
- If `key > arr[mid]` → Search right half (`low = mid + 1`)
- If `key < arr[mid]` → Search left half (`high = mid - 1`)
- **Time Complexity:** `O(log N)`

#### 📉 Lower Bound
The **first element ≥ target** in a sorted array.
- If `arr[mid] >= key` → record `ans = mid`, search left half
- If `arr[mid] < key` → search right half

#### 📈 Upper Bound
The **first element > target** in a sorted array.
- If `arr[mid] > key` → record `ans = mid`, search left half
- If `arr[mid] <= key` → search right half

### 📄 Source Code (`00724205101098_Offline1.cpp`)

```cpp
#include<bits/stdc++.h>
using namespace std;

void binarySearch(vector<int> v, int key)
{
    int flag = 0;
    int high = v.size() - 1;
    int low = 0;
    int mid;
    sort(v.begin(), v.end());
    while(low <= high)
    {
        mid = (low + high) / 2;
        if(key == v[mid]) { flag = 1; break; }
        else if(key > v[mid]) { low = mid + 1; }
        else { high = mid - 1; }
    }
    if(flag == 1) cout << "Book Found";
    else cout << "Book Not Found";
}

int lowerBound(vector<int> a, int key)
{
    int low = 0, high = a.size() - 1;
    int ans = a.size();
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (a[mid] >= key) { ans = mid; high = mid - 1; }
        else { low = mid + 1; }
    }
    return ans;
}

int upperBound(vector<int> a, int key)
{
    int low = 0, high = a.size() - 1;
    int ans = a.size();
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (a[mid] > key) { ans = mid; high = mid - 1; }
        else { low = mid + 1; }
    }
    return ans;
}

int main()
{
    int n, x, key;
    vector<int> vec;
    cin >> n;
    for(int i = 0; i < n; i++) { cin >> x; vec.push_back(x); }
    cin >> key;
    binarySearch(vec, key);
    cout << endl;
    cout << "Lower Bound Index: " << lowerBound(vec, key) << endl;
    cout << "Upper Bound Index: " << upperBound(vec, key) << endl;
    return 0;
}
```

### 🚀 Sample I/O

**Input:**
```
7
10 20 30 40 50 60 70
40
```
**Output:**
```
Book Found
Lower Bound Index: 3
Upper Bound Index: 4
```

---

## 📖 Offline Assignment 2 — Selection Sort (Multi-key)

This assignment focuses on implementing **Selection Sort** with multi-key comparison criteria on a list of books.

### 🎯 Problem Statement

You are given a list of books, each with a **title**, **author**, and **publication year**. Your task is to sort the books using the **Selection Sort** algorithm with the following criteria:

1. **Primary key:** Publication year in **descending order** (most recent first).
2. **Secondary key:** Author name in **ascending lexicographic order** (if years are equal).
3. **Tertiary key:** Book title in **ascending lexicographic order** (if year and author are both equal).

**Input Format:**
- First line: integer `N` — the number of books (`1 ≤ N ≤ 1000`)
- Next `N` lines: each line contains `Title, Author, Publication Year`
  - Title length: `1 ≤ length ≤ 100`
  - Author length: `1 ≤ length ≤ 100`
  - Year: `1900 ≤ year ≤ 2025`

**Output Format:**
- Print each book on a new line in the format: `Title, Author, Publication Year`

### 💡 Algorithm

**Selection Sort with multi-key comparison:**
1. Read `N` books, each with title, author, and year.
2. Store each book in a `struct` with fields `bName`, `author`, and `y`.
3. In each pass `i` (from `0` to `n-2`), find the "maximum" element from position `i` to `n-1` using:
   - Larger year → wins (descending year)
   - If years equal → smaller author name wins (ascending)
   - If year and author equal → smaller title wins (ascending)
4. Swap the found "maximum" element to position `i`.
5. After all passes, print the sorted books.

**Time Complexity:** `O(N²)`

### 📄 Source Code (`00724205101098_Offline2.cpp`)

```cpp
#include<bits/stdc++.h>
using namespace std;

struct Book
{
    string bName;
    string author;
    int y;
};

void selectionSort(vector<Book> &b, int n)
{
    for(int i = 0; i < n-1; i++)
    {
        int max = i;
        for(int j = i+1; j < n; j++)
        {
            if(b[j].y == b[max].y)
            {
                if(b[j].author < b[max].author)
                {
                    max = j;
                }
                else if(b[j].author == b[max].author)
                {
                    if(b[j].bName < b[max].bName)
                    {
                        max = j;
                    }
                }
            }
            else if(b[j].y > b[max].y)
            {
                max = j;
            }
        }
        swap(b[i], b[max]);
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore();
    vector<Book> b(n);
    for(int i = 0; i < n; i++)
    {
        string line;
        getline(cin, line);
        stringstream ss(line);
        getline(ss, b[i].bName, ',');
        getline(ss, b[i].author, ',');
        if (b[i].author[0] == ' ')
            b[i].author.erase(0, 1);
        ss >> b[i].y;
    }
    selectionSort(b, n);
    for(int i = 0; i < n; i++)
    {
        cout << b[i].bName << ", "
             << b[i].author << ", "
             << b[i].y << endl;
    }
}
```

### 🚀 Sample I/O

**Input:**
```
5
Sapiens, Yuval Noah Harari, 2011
21 Lessons for the 21st Century, Yuval Noah Harari, 2018
Educated, Tara Westover, 2018
Becoming, Michelle Obama, 2018
Money: Vintage Minis, Yuval Noah Harari, 2018
```

**Output:**
```
Becoming, Michelle Obama, 2018
Educated, Tara Westover, 2018
21 Lessons for the 21st Century, Yuval Noah Harari, 2018
Money: Vintage Minis, Yuval Noah Harari, 2018
Sapiens, Yuval Noah Harari, 2011
```

---

*Generated with ❤️ for CSE2104 Data Structure Lab*
