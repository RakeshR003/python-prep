# For Loops

## Purpose

A `for` loop is used to execute a block of code repeatedly by iterating over a sequence or a range of values.

---

## Syntax

```python
for variable in sequence:
    # code
```

Using `range()`:

```python
for i in range(5):
    print(i)
```

---

## range() Variations

| Syntax | Example | Output |
|---------|---------|--------|
| `range(stop)` | `range(5)` | 0 1 2 3 4 |
| `range(start, stop)` | `range(2, 6)` | 2 3 4 5 |
| `range(start, stop, step)` | `range(2, 11, 2)` | 2 4 6 8 10 |

---

## Rules

- A `for` loop repeats code for each value in a sequence.
- `range()` does **not** include the stop value.
- The loop variable updates automatically.
- Indentation is mandatory.

---

## Example

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

## Common Mistakes

- Forgetting that `range()` excludes the stop value.
- Incorrect indentation.
- Modifying the loop variable expecting it to affect the next iteration.
- Using the wrong step value.

---

## Interview Tip

A `for` loop is preferred when the number of iterations is known in advance.

---

## Practice Programs

- Print 1 to 10
- Print Even Numbers
- Print Odd Numbers
- Sum of Numbers
- Multiplication Table
- FizzBuzz
- Basic Pattern Printing
- Nested Loops

---

## Progress

- [x] Concept Learned
- [x] Practice Completed
- [x] Beginner Interview Ready

---

## Advanced Topics (Coming Later)

The following topics are important for interviews but will be covered after completing the Python fundamentals roadmap:

- Iterating through Strings
- Iterating through Lists
- `break`
- `continue`
- `pass`
- `enumerate()`
- `zip()`
- Nested Loop Optimization
- Looping through Dictionaries
- Iterables and Iterators
- Comprehensions (List, Set, Dictionary)


## Frequently Asked Interview Questions

- Difference between for and while?
- Explain range().
- Why doesn't range() include the stop value?
- When should you use a for loop?