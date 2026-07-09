# 🌐 First Lab Online

## 📝 Problem Statements

### Room Allocation (`room.cpp`)
**Question:** You are given `n` rooms, each with a specific capacity, and `m` groups of people, each requiring a certain capacity.
Write a program to assign each group to the smallest possible room that can accommodate them (i.e., room capacity ≥ group size).
Output the 1-based index of the allocated room after sorting the rooms in ascending order of their capacities. If no such room is available for a group, output `-1`.

---

### Even Number Selective Sort (`OnlineB2_2.cpp`)
**Question:** Given an array of `n` integers, sort only the **even numbers** among themselves using **Selection Sort**, while keeping the **odd numbers in their original positions**.
Output the modified array after sorting.

**Approach:**
- Implement a custom `sorted()` function that applies selection sort only when both the current minimum and the candidate element are even numbers.
- Odd numbers remain untouched in their original indices.
