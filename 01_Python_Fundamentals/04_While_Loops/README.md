# While Loops

## Purpose

A `while` loop is used to repeatedly execute a block of code as long as a given condition is `True`.

---

## Syntax

```python
while condition:
    # code
```

---

## Rules

- The condition is checked before every iteration.
- The loop continues while the condition is `True`.
- Update the loop variable to avoid an infinite loop.
- Indentation is mandatory.

---

## Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
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

- Forgetting to update the loop variable.
- Creating an infinite loop.
- Incorrect indentation.
- Using the wrong loop condition.

---

## Interview Tip

Use a `while` loop when the number of iterations is **not known in advance**.

Use a `for` loop when the number of iterations **is known**.

---

## Practice Programs

- Print Numbers
- Even Numbers
- Odd Numbers
- Multiples
- Sum of Numbers
- Build a List
- Pattern Printing

---

## Progress

- [x] Concept Learned
- [x] Practice Completed
- [x] Beginner Interview Ready

---

## Advanced Topics (Coming Later)

The following topics are important for interviews but will be covered after completing the Python fundamentals roadmap:

- `break`
- `continue`
- `pass`
- Nested While Loops
- Sentinel-Controlled Loops
- Input Validation Loops
- Infinite Loop Applications
- `while...else`
- Loop Optimization


## Frequently Asked Interview Questions

- Difference between while and for?
- What is an infinite loop?
- How do you stop an infinite loop?
- What is while...else?