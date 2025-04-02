# Question 3 – Egalitarian Division

This project implements an **egalitarian resource allocation algorithm** using the `cvxpy` library.

The input is a value matrix where:
- Each **row** represents an agent.
- Each **column** represents a resource.
- The value at position `(i, j)` represents how much **Agent i** values **Resource j**.

The goal is to **maximize the minimum value** any agent receives from the allocation — ensuring a fair (egalitarian) division.

---

## 📥 Input (value_matrix) and 🖥️ Console Output:

---

### 🔹 Example 1: Based on lecture slides (Avi and Batia)

```python
value_matrix = [[80, 1, 79], [20, 1, 1]]
