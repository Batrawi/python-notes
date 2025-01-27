# Inverting List Values in Python

This file documents a Python function that takes a list of integers and returns a new list where each integer is replaced with its additive inverse (positives become negatives and vice versa). The input list remains unmodified.

---

## **Problem: Invert List Values**

Given a list of integers:

1. Replace each positive number with its negative counterpart.
2. Replace each negative number with its positive counterpart.
3. For an empty list, return an empty list.
4. Do not mutate the input list.

### **Examples**

| Input               | Output                 |
| ------------------- | ---------------------- |
| `[1, 2, 3, 4, 5]`   | `[-1, -2, -3, -4, -5]` |
| `[1, -2, 3, -4, 5]` | `[-1, 2, -3, 4, -5]`   |
| `[]`                | `[]`                   |

---

## **Solution**

Here is the implementation of the function:

### **Optimized Function**

```python
def invert(lst):
    return [item * -1 for item in lst]
```

### **Explanation**

1. **List Comprehension:**

   - The expression `[item * -1 for item in lst]` iterates through each element in the input list `lst`.
   - For each `item`, it calculates the additive inverse by multiplying it by `-1`.
   - If `lst` is empty, the list comprehension returns another empty list (`[]`).

2. **No Mutation:**

   - The function creates a new list rather than modifying the input list.

3. **Graceful Handling of Empty Lists:**
   - Since list comprehensions naturally handle empty inputs, there is no need for an explicit `if not lst` check.

---

## **Test Cases**

```python
# Test cases
print(invert([1, 2, 3, 4, 5]))  # Expected: [-1, -2, -3, -4, -5]
print(invert([1, -2, 3, -4, 5]))  # Expected: [-1, 2, -3, 4, -5]
print(invert([]))  # Expected: []
print(invert([0, -1, 1]))  # Expected: [0, 1, -1]
```

---

## **Reflection and Learning**

- **Simplifying Conditions:** Avoid redundant checks like `if not lst` when they are unnecessary. List comprehensions naturally handle edge cases like empty lists.
- **Pythonic Style:** Using a list comprehension makes the function concise and easy to read.
- **Avoiding Mutation:** The function respects the principle of immutability by creating a new list.

---

## **Future Improvements**

- Consider extending the function to handle other types of iterable inputs (e.g., tuples).
- Explore performance implications of the solution with larger datasets.
