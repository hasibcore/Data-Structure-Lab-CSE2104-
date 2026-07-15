<div align="center">

# 📚 CSE2104 — Data Structure Lab
### Ahsanullah University of Science and Technology
**Student:** Hasibul Hasan &nbsp;|&nbsp; **ID:** 00724205101098 &nbsp;|&nbsp; **Section:** B2 &nbsp;|&nbsp; **Semester:** Fall 2025

</div>

---

## 📂 Assignment Index

| # | Type | Topic | Folder |
|---|------|--------|--------|
| 1 | 🟦 Offline | Binary Search, Lower Bound & Upper Bound | [`Offline_assignment_1/`](./Offline_assignment_1/) |
| 2 | 🟦 Offline | Selection Sort (Multi-key) | [`Offline_assignment_2/`](./Offline_assignment_2/) |
| 3 | 🟦 Offline | Quick Sort & Merge Sort (10 Tasks) | [`Offline_assignment_3/`](./Offline_assignment_3/) |
| 4 | 🟩 Online | Product Inventory Search | [`Online_assignment_1/`](./Online_assignment_1/) |

---

<br>

## 🟦 Offline Assignment 1 — Binary Search, Lower Bound & Upper Bound

> 📁 **Files:** [`Offline_assignment_1/00724205101098_Offline1.cpp`](./Offline_assignment_1/00724205101098_Offline1.cpp) &nbsp;|&nbsp; [`Offline_assignment_1/00724205101098_Offline1.pdf`](./Offline_assignment_1/00724205101098_Offline1.pdf)

### 🎯 Problem Statement

A bookstore maintains a **sorted list of unique book IDs** to quickly identify whether a book is available in stock. Write a C++ program that uses **Binary Search** to determine if a specific book ID is present in the list. Additionally, the store often needs to find:
- The **first book ID ≥ a given value** (lower bound) for restocking
- The **first book ID > a given value** (upper bound) for categorization

Given a sorted array of book IDs and a query book ID, output:
1. Whether the book **exists** in the list
2. The **lower bound** position
3. The **upper bound** position

#### ✅ Tasks
1. Read the number of book IDs and the sorted list.
2. Read the query book ID to be searched.
3. Implement **Binary Search** to check existence.
4. Implement logic to find the **lower bound**.
5. Implement logic to find the **upper bound**.
6. Display search result along with lower and upper bound indices.

> You should write user defined functions for Binary Search, Lower Bound and Upper Bound. Input should be taken inside `main`. All user defined functions must be called from `main`.

---

### 🧠 Algorithm

```
1. Read N (number of book IDs)
2. Read all book IDs into a vector
3. Sort the vector in ascending order
4. Read the query book ID (key)
5. Binary Search:
      low = 0, high = N-1
      while low <= high:
          mid = (low + high) / 2
          if key == arr[mid] → Found, break
          if key > arr[mid]  → low = mid + 1
          else               → high = mid - 1
6. Lower Bound:
      Find first index where arr[index] >= key
7. Upper Bound:
      Find first index where arr[index] > key
8. Print result
```

---

### 💻 Source Code

```cpp
#include <bits/stdc++.h>
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
        if(key == v[mid])      { flag = 1; break; }
        else if(key > v[mid])  { low = mid + 1; }
        else                   { high = mid - 1; }
    }
    if(flag == 1) cout << "Book Found";
    else          cout << "Book Not Found";
}

int lowerBound(vector<int> a, int key)
{
    int low = 0, high = a.size() - 1;
    int ans = a.size();
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (a[mid] >= key) { ans = mid; high = mid - 1; }
        else               { low = mid + 1; }
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
        else              { low = mid + 1; }
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

### 📊 Sample I/O

| Sample Input | Sample Output |
|---|---|
| `7` | `Book Found` |
| `10 20 30 40 50 60 70` | `Lower Bound Index: 3` |
| `40` | `Upper Bound Index: 4` |

---

<br>

## 🟦 Offline Assignment 2 — Selection Sort (Multi-key)

> 📁 **Files:** [`Offline_assignment_2/00724205101098_Offline2.cpp`](./Offline_assignment_2/00724205101098_Offline2.cpp) &nbsp;|&nbsp; [`Offline_assignment_2/00724205101098_Offline2.pdf`](./Offline_assignment_2/00724205101098_Offline2.pdf)

### 🎯 Problem Statement

You are given a list of books, each with a **title**, **author**, and **publication year**. Sort the books using the **Selection Sort** algorithm with the following multi-key criteria:

| Priority | Key | Order |
|----------|-----|-------|
| 1st | Publication Year | Descending (newest first) |
| 2nd | Author Name | Ascending (A → Z) |
| 3rd | Book Title | Ascending (A → Z) |

**Input Format:**
- Line 1: Integer `N` — number of books (`1 ≤ N ≤ 1000`)
- Next `N` lines: `Title, Author, Publication Year`
  - Title length: `1 ≤ len ≤ 100`
  - Author length: `1 ≤ len ≤ 100`
  - Year: `1900 ≤ year ≤ 2025`

**Output Format:** Print each book as `Title, Author, Publication Year`

---

### 🧠 Algorithm

```
1. Read N books → store in struct { bName, author, y }
2. Selection Sort (find "maximum" per criteria each pass):
      for i = 0 to N-2:
          max = i
          for j = i+1 to N-1:
              if b[j].year  > b[max].year          → max = j   (descending year)
              if b[j].year == b[max].year:
                  if b[j].author < b[max].author   → max = j   (ascending author)
                  if authors equal:
                      if b[j].name < b[max].name   → max = j   (ascending title)
          swap(b[i], b[max])
3. Print sorted books
```

**Time Complexity:** `O(N²)`

---

### 💻 Source Code

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
                if(b[j].author < b[max].author)          { max = j; }
                else if(b[j].author == b[max].author)
                {
                    if(b[j].bName < b[max].bName)        { max = j; }
                }
            }
            else if(b[j].y > b[max].y)                  { max = j; }
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
        if (b[i].author[0] == ' ') b[i].author.erase(0, 1);
        ss >> b[i].y;
    }
    selectionSort(b, n);
    for(int i = 0; i < n; i++)
        cout << b[i].bName << ", " << b[i].author << ", " << b[i].y << endl;
}
```

### 📊 Sample I/O

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

<br>

## 🟦 Offline Assignment 3 — Quick Sort & Merge Sort (10 Tasks)

> 📁 **Folder:** [`Offline_assignment_3/`](./Offline_assignment_3/) &nbsp;|&nbsp; 📋 **Report:** [`00724205101098_Offline3.pdf`](./Offline_assignment_3/00724205101098_Offline3.pdf) &nbsp;|&nbsp; 📝 **Questions:** [`Offline-3.pdf`](./Offline_assignment_3/Offline-3.pdf)

This assignment contains 10 tasks exploring the behavior, comparison/swap counts, and modifications of Quick Sort and Merge Sort.

### 🎯 Task Overview & Files

| Task | Title | Problem Statement | Source Code |
|---|---|---|---|
| 1 | Quick Sort Comparison Count | Count comparisons during Quick Sort (last element as pivot). | [Task 1](./Offline_assignment_3/00724205101098_Offline3_Task1.cpp) |
| 2 | Partitioning Array around Pivot | Rearrange array elements around a pivot. | [Task 2](./Offline_assignment_3/00724205101098_Offline3_Task2.cpp) |
| 3 | Quick Sort Swap Count | Count total swaps during Quick Sort. | [Task 3](./Offline_assignment_3/00724205101098_Offline3_Task3.cpp) |
| 4 | Output Chosen Pivot at Each Recursion | Print selected pivot at each recursion step. | [Task 4](./Offline_assignment_3/00724205101098_Offline3_Task4.cpp) |
| 5 | Output Pivot Placement Index | Print final placement index of pivot in array. | [Task 5](./Offline_assignment_3/00724205101098_Offline3_Task5.cpp) |
| 6 | Count Elements Less Than Pivot | Count elements smaller than pivot at each step. | [Task 6](./Offline_assignment_3/00724205101098_Offline3_Task6.cpp) |
| 7 | Merge Sort Combined Median | Merge two sorted arrays and find the median. | [Task 7](./Offline_assignment_3/00724205101098_Offline3_Task7.cpp) |
| 8 | Merge Sort Comparison Count | Count comparisons made during Merge Sort. | [Task 8](./Offline_assignment_3/00724205101098_Offline3_Task8.cpp) |
| 9 | Count Merge Operations | Count total merge operations executed. | [Task 9](./Offline_assignment_3/00724205101098_Offline3_Task9.cpp) |
| 10 | Determine Recursive Calls | Count total recursive calls in Merge Sort. | [Task 10](./Offline_assignment_3/00724205101098_Offline3_Task10.cpp) |

---

<br>

## 🟩 Online Assignment 1 — Product Inventory Search

> 📁 **File:** [`Online_assignment_1/Product_Inventory_Search.cpp`](./Online_assignment_1/Product_Inventory_Search.cpp)

### 🎯 Problem Statement

A warehouse maintains an **unsorted list of product IDs**. Write a C++ program to:
1. **Sort** the given array of product IDs.
2. Use **Binary Search** to check if a requested product ID exists → print `Found` or `Not found`.
3. Find and print the **Upper Bound Index** (first product ID `>` query).
4. Find and print the **Lower Bound Index** (first product ID `≥` query).

---

### 🧠 Algorithm

```
1. Read N product IDs into a vector
2. Read query key
3. Sort the vector in ascending order
4. Binary Search:
      if key found → print "Found"
      else         → print "Not found"
5. Upper Bound:
      Find first index where product_id > key
6. Lower Bound:
      Find first index where product_id >= key
7. Print Upper Bound Index and Lower Bound Index
```

---

### 💻 Source Code

```cpp
#include<bits/stdc++.h>
using namespace std;

int binarySearch(vector<int> v, int key)
{
    int low = 0;
    int high = v.size() - 1;
    while(low <= high)
    {
        int mid = (low + high) / 2;
        if(key == v[mid])     { return 1; }
        else if(key > v[mid]) { low = mid + 1; }
        else                  { high = mid - 1; }
    }
    return -1;
}

int upperBound(vector<int> v, int key)
{
    int high = v.size() - 1, low = 0;
    while(high >= low)
    {
        int mid = (high + low) / 2;
        if(key >= v[mid]) { low = mid + 1; }
        else              { high = mid - 1; }
    }
    return low;
}

int lowerBound(vector<int> v, int key)
{
    int high = v.size() - 1, low = 0;
    while(high >= low)
    {
        int mid = (high + low) / 2;
        if(key > v[mid]) { low = mid + 1; }
        else             { high = mid - 1; }
    }
    return low;
}

int main()
{
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++) { int x; cin >> x; v.push_back(x); }
    int key;
    cin >> key;
    sort(v.begin(), v.end());
    int q = binarySearch(v, key);
    if(q == 1) cout << "Found" << endl;
    else       cout << "Not found" << endl;
    cout << "Upper Bound Index : " << upperBound(v, key) << endl;
    cout << "Lower Bound Index : " << lowerBound(v, key) << endl;
}
```

### 📊 Sample I/O

| Sample Input | Sample Output |
|---|---|
| `5` | `Found` |
| `30 10 50 20 40` | `Upper Bound Index : 3` |
| `30` | `Lower Bound Index : 2` |

---

<br>

<div align="center">

*Made with ❤️ for CSE2104 Data Structure Lab — AUST*

</div>
