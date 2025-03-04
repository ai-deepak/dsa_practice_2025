**derivation** behind why `k + left (low)` works, not just an intuitive explanation. Let's break it down step by step.

---

### **Step 1: Understanding the Missing Count at `high`**

When we complete **binary search**, we have:

- `low = the index where the k-th missing number should be placed`
- `high = low - 1`, meaning `high` is the **last valid index before the k-th missing number**.

Now, let's calculate **how many numbers are missing before `arr[high]`**.

\[
\text{Missing before } arr[high] = arr[high] - (high + 1)
\]

- `arr[high]` tells us the **actual number at that index**.
- `(high + 1)` tells us **how many numbers should have existed** if nothing was missing.
- The difference gives us **how many numbers are missing before `arr[high]`**.

---

### **Step 2: How Many More Missing Numbers Do We Need?**

- We want the **k-th missing number**, but we only have `arr[high] - (high + 1)` missing numbers so far.
- So, we still need:

\[
\text{more missing numbers} = k - (\text{missing before } arr[high])
\]

Substituting:

\[
\text{more missing numbers} = k - (arr[high] - (high + 1))
\]

---

### **Step 3: Computing the k-th Missing Number**

- The next missing number starts **after** `arr[high]`.
- If we need `more` missing numbers, the **k-th missing number is:**

\[
\text{k-th missing} = arr[high] + \text{more}
\]

Substituting:

\[
\text{k-th missing} = arr[high] + k - (arr[high] - (high + 1))
\]

Simplifying:

\[
\text{k-th missing} = arr[high] + k - arr[high] + high + 1
\]

\[
\text{k-th missing} = k + high + 1
\]

Since after binary search, `low = high + 1`, we substitute `high + 1 = low`:

\[
\text{k-th missing} = k + low
\]

---

### **Step 4: Intuition Behind `k + low`**

- `low` tells us **how many elements from `arr` come before the k-th missing number**.
- `k` tells us **how many missing numbers we need**.
- **By adding `k + low`, we directly land on the k-th missing number.**

---

### **Example Walkthrough**

```python
arr = [2, 3, 4, 7, 11]
k = 5
```

#### **Missing numbers**:

`1, 5, 6, 8, 9, 10, ...`

- The **5th missing number is `9`**.

#### **Binary Search Result**:

After binary search,

- `low = 4`, `high = 3`
- `arr[high] = 7`
- **Missing before `7`**:  
  \[
  7 - (3 + 1) = 7 - 4 = 3
  \]
  (**Only 3 numbers are missing so far: `[1, 5, 6]`**).
- We need **2 more missing numbers**:  
  \[
  k - 3 = 5 - 3 = 2
  \]
- k-th missing number:
  \[
  \text{k-th missing} = arr[high] + 2 = 7 + 2 = 9
  \]
  ✅ **Correct!**  
  Alternatively, using the derived formula:  
  \[
  \text{k-th missing} = k + low = 5 + 4 = 9
  \]
  ✅ **Correct!**

---

### **Final Takeaway**

1. **Binary search tells us `low`, which is where the k-th missing number should be placed.**
2. **We calculate how many missing numbers exist before `arr[high]`.**
3. **If we need `more` missing numbers, we add that to `arr[high]`.**
4. **This simplifies to `k + low`, because `low` naturally accounts for the numbers before k-th missing.**

---

### **This is the intuition behind `k + low`** 🎯🚀
