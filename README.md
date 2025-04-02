# 🧮 Question 3 – Egalitarian Division

This project implements an **egalitarian resource allocation algorithm** using the `cvxpy` library.

Given a **value matrix**, where:

- Each **row** represents an agent.
- Each **column** represents a resource.
- The value at position `(i, j)` represents how much **Agent *i*** values **Resource *j***,

the algorithm finds an allocation that **maximizes the minimum total value** received by any agent — promoting a **fair (egalitarian)** division of resources.

---

## 📥 Input & 🖥️ Output

### Input:
A 2D list (`value_matrix`) where `value_matrix[i][j]` indicates the value Agent *i* assigns to Resource *j*.

### Output:
For each agent, the fraction of each resource allocated to them, displayed with two decimal precision.

---

### 🔹 Example 1: Based on lecture slides (Avi and Batia)
```python
value_matrix = [[80, 1, 79], [20, 1, 1]]
```
**Output:**
```
Agent #1 gets 0.00 of resource #1, 0.00 of resource #2, 0.28 of resource #3.
Agent #2 gets 1.00 of resource #1, 1.00 of resource #2, 0.72 of resource #3.
```

### 🔹 Example 2: Mixed preferences
```python
value_matrix = [[81, 19, 1], [70, 1, 29]]
```
**Output:**
```
Agent #1 gets 0.53 of resource #1, 1.00 of resource #2, 0.00 of resource #3.
Agent #2 gets 0.47 of resource #1, 0.00 of resource #2, 1.00 of resource #3.
```

### 🔹 Example 3: Agent 1 dominates most resources
```python
value_matrix = [[90, 90, 90], [1, 1, 1]]
```
**Output:**
```
Agent #1 gets 0.01 of resource #1, 0.01 of resource #2, 0.01 of resource #3.
Agent #2 gets 0.99 of resource #1, 0.99 of resource #2, 0.99 of resource #3.
```

### 🔹 Example 4: Agent 2 dominates one important resource
```python
value_matrix = [[10, 5, 2], [2, 3, 100]]
```
**Output:**
```
Agent #1 gets 1.00 of resource #1, 1.00 of resource #2, 0.83 of resource #3.
Agent #2 gets 0.00 of resource #1, 0.00 of resource #2, 0.17 of resource #3.
```

### 🔹 Example 5: Inverse valuations
```python
value_matrix = [[100, 0, 50], [0, 100, 50]]
```
**Output:**
```
Agent #1 gets 1.00 of resource #1, 0.00 of resource #2, 0.50 of resource #3.
Agent #2 gets 0.00 of resource #1, 1.00 of resource #2, 0.50 of resource #3.
```

### 🔹 Example 6: Sparse interests
```python
value_matrix = [[1, 0, 0], [0, 1, 1]]
```
**Output:**
```
Agent #1 gets 1.00 of resource #1, 0.21 of resource #2, 0.21 of resource #3.
Agent #2 gets 0.00 of resource #1, 0.59 of resource #2, 0.59 of resource #3.
```

---

## 🛠 Requirements

- Python 3.7+
- [`cvxpy`](https://www.cvxpy.org/)
- [`numpy`](https://numpy.org/)

Install dependencies with:

```bash
pip install cvxpy numpy
```

---

## 📁 Project Files

- `assignment2_q3.py` – Python script implementing the egalitarian allocation algorithm and running test cases.
- `README.md` – Project documentation with description, examples, and setup instructions.
