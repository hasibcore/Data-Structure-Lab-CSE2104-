# 📊 Sorting Algorithms — CSE2104 Data Structure Lab

এই ফোল্ডারে ৫টি গুরুত্বপূর্ণ Sorting Algorithm-এর implementation রয়েছে।  
নিচে প্রতিটির **theory**, **কাজের ধরন**, **complexity** এবং **Input/Output** উদাহরণ দেওয়া হলো।

---

## 📌 Table of Contents
1. [Bubble Sort](#1-bubble-sort)
2. [Selection Sort](#2-selection-sort)
3. [Insertion Sort](#3-insertion-sort)
4. [Merge Sort](#4-merge-sort)
5. [Quick Sort](#5-quick-sort)

---

## 1. Bubble Sort

### 🔍 Theory
Bubble Sort হলো সবচেয়ে সহজ sorting algorithm। এটি array-এর পাশাপাশি দুটো element তুলনা করে এবং যদি ভুল ক্রমে থাকে তাহলে swap করে। প্রতিটি **pass**-এ সবচেয়ে বড় element-টি শেষে চলে যায় — ঠিক যেভাবে পানিতে বুদবুদ (bubble) উপরে ওঠে।

### ⚙️ কাজের ধরন
```
Pass 1: [5, 3, 8, 1] → [3, 5, 1, 8]  ← 8 সবশেষে গেল
Pass 2: [3, 5, 1, 8] → [3, 1, 5, 8]  ← 5 জায়গায় গেল
Pass 3: [3, 1, 5, 8] → [1, 3, 5, 8]  ← sorted ✅
```

### 📈 Complexity
| Case | Time Complexity | Space |
|------|----------------|-------|
| Best | O(n) — already sorted | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

### 💻 Input / Output
```
Input:
5
64 34 25 12 22

Output:
Sorted array: 12 22 25 34 64
```

---

## 2. Selection Sort

### 🔍 Theory
Selection Sort প্রতিটি pass-এ unsorted অংশ থেকে **সবচেয়ে ছোট element** খুঁজে বের করে এবং সেটাকে সামনের (unsorted অংশের প্রথম) position-এ রাখে। এভাবে একটি একটি করে minimum select করে array sort হয়।

### ⚙️ কাজের ধরন
```
Array: [64, 25, 12, 22, 11]

Pass 1: min=11 → swap with 64 → [11, 25, 12, 22, 64]
Pass 2: min=12 → swap with 25 → [11, 12, 25, 22, 64]
Pass 3: min=22 → swap with 25 → [11, 12, 22, 25, 64]
Pass 4: min=25 → no swap    → [11, 12, 22, 25, 64] ✅
```

### 📈 Complexity
| Case | Time Complexity | Space |
|------|----------------|-------|
| Best | O(n²) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

> ⚠️ Selection Sort সব ক্ষেত্রেই O(n²) — এমনকি array আগে থেকে sorted থাকলেও।

### 💻 Input / Output
```
Input:
5
64 25 12 22 11

Output:
Sorted array: 11 12 22 25 64
```

---

## 3. Insertion Sort

### 🔍 Theory
Insertion Sort কার্ড সাজানোর মতো কাজ করে। প্রতিটি element-কে তার সঠিক position-এ **insert** করা হয়। Sorted অংশের সাথে তুলনা করে element-টিকে সঠিক জায়গায় ঢুকিয়ে দেওয়া হয়।

### ⚙️ কাজের ধরন
```
Array: [5, 2, 4, 6, 1]

i=1: key=2, [5]>2 → shift → [2, 5, 4, 6, 1]
i=2: key=4, [5]>4 → shift → [2, 4, 5, 6, 1]
i=3: key=6, [5]<6 → no shift → [2, 4, 5, 6, 1]
i=4: key=1, shift all → [1, 2, 4, 5, 6] ✅
```

### 📈 Complexity
| Case | Time Complexity | Space |
|------|----------------|-------|
| Best | O(n) — already sorted | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

### 💻 Input / Output
```
Input:
5
5 2 4 6 1

Output:
Sorted array: 1 2 4 5 6
```

---

## 4. Merge Sort

### 🔍 Theory
Merge Sort একটি **Divide and Conquer** algorithm। এটি array-কে দুই ভাগে ভাগ করে, প্রতিটি অর্ধেককে recursively sort করে, তারপর দুটো sorted অর্ধেককে **merge** করে একটি sorted array তৈরি করে।

### ⚙️ কাজের ধরন
```
Array: [38, 27, 43, 3, 9, 82, 10]

Divide:
[38, 27, 43, 3] | [9, 82, 10]
[38, 27] [43, 3] | [9, 82] [10]
[38][27] [43][3] | [9][82] [10]

Merge (conquer):
[27, 38] [3, 43] | [9, 82] [10]
[3, 27, 38, 43]  | [9, 10, 82]
[3, 9, 10, 27, 38, 43, 82] ✅
```

### 📈 Complexity
| Case | Time Complexity | Space |
|------|----------------|-------|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

> ✅ Merge Sort সবসময় **O(n log n)** — সবচেয়ে stable ও predictable।  
> ⚠️ Extra **O(n)** space লাগে।

### 💻 Input / Output
```
Input:
7
38 27 43 3 9 82 10

Output:
Sorted array: 3 9 10 27 38 43 82
```

### 📝 Code Snippet (Core Logic)
```cpp
void merge(vector<int>& v, int l, int m, int r) {
    vector<int> left(v.begin()+l, v.begin()+m+1);
    vector<int> right(v.begin()+m+1, v.begin()+r+1);
    int i=0, j=0, k=l;
    while (i<left.size() && j<right.size())
        v[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
    while (i<left.size())  v[k++] = left[i++];
    while (j<right.size()) v[k++] = right[j++];
}

void mergeSort(vector<int>& v, int l, int r) {
    if (l < r) {
        int m = l + (r-l)/2;
        mergeSort(v, l, m);
        mergeSort(v, m+1, r);
        merge(v, l, m, r);
    }
}
```

---

## 5. Quick Sort

### 🔍 Theory
Quick Sort একটি **Divide and Conquer** algorithm। এটি একটি **pivot** element বেছে নেয় এবং array-কে দুই ভাগে ভাগ করে — pivot-এর চেয়ে ছোট সব বাঁয়ে, বড় সব ডানে। এরপর প্রতিটি অর্ধেকে recursively এই process চলে।

### ⚙️ কাজের ধরন
```
Array: [10, 80, 30, 90, 40, 50, 70], pivot = 70 (last)

Partition:
→ 10<70 ✅, 80>70 skip, 30<70 ✅, 90>70 skip,
  40<70 ✅, 50<70 ✅, swap pivot
→ [10, 30, 40, 50, 70, 90, 80]
           ↑ pivot at correct position

Recurse on [10,30,40,50] and [90,80]
Final: [10, 30, 40, 50, 70, 80, 90] ✅
```

### 📈 Complexity
| Case | Time Complexity | Space |
|------|----------------|-------|
| Best | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst | O(n²) — sorted/reverse sorted input | O(n) |

> ✅ Average case-এ Quick Sort সবচেয়ে **fast** (Merge Sort-এর চেয়ে কম memory)।  
> ⚠️ Worst case তখন হয় যখন pivot সবসময় সবচেয়ে ছোট বা বড় হয়।

### 💻 Input / Output
```
Input:
7
10 80 30 90 40 50 70

Output:
Sorted array: 10 30 40 50 70 80 90
```

### 📝 Code Snippet (Core Logic)
```cpp
int partition(vector<int>& v, int low, int high) {
    int pivot = v[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (v[j] <= pivot) {
            i++;
            swap(v[i], v[j]);
        }
    }
    swap(v[i+1], v[high]);
    return i + 1;
}

void quickSort(vector<int>& v, int low, int high) {
    if (low < high) {
        int pi = partition(v, low, high);
        quickSort(v, low, pi - 1);
        quickSort(v, pi + 1, high);
    }
}
```

---

## 📊 সব Algorithm-এর তুলনা

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No |

> **Stable Sort** মানে — সমান মানের দুটি element-এর আপেক্ষিক ক্রম sorting-এর পরেও অপরিবর্তিত থাকে।

---

*CSE2104 — Data Structure Lab | Sorting Algorithms*
