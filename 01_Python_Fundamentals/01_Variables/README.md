# Variables

## Purpose

Variables are used to store data in memory so that it can be used later in a program.

---

## Syntax

```python
name = "Rakesh"
age = 21
cgpa = 6.14
```

---

## Rules

- Variable names should be meaningful.
- Variable names are case-sensitive.
- Variable names cannot start with a number.
- Do not use Python keywords (`if`, `for`, `class`, etc.) as variable names.
- Use `snake_case` for better readability.

---

## Common Data Types

| Data Type | Example |
|-----------|---------|
| int       |   `10`  |
| float     | `6.14`  |
| str       |`"Rakesh"`|
| bool      | `True`  |

---

## Example

```python
name = "Rakesh"
age = 21

print(name)
print(age)
```

---

## Common Mistakes

- Starting a variable name with a number.
- Using reserved keywords as variable names.
- Giving unclear names like `a`, `x`, or `temp`.
- Forgetting to convert user input using `int()` or `float()` when needed.

---

## Interview Tip

A variable is a name that refers to a value stored in memory. It allows us to store and reuse data throughout a program.

---

## Practice Programs

- Creating variables
- Printing variables
- Taking user input
- Type conversion using `int()`
- Simple calculator

---

## Progress

- [x] Concept Learned
- [x] Practice Completed
- [x] Beginner Interview Ready


---

## Advanced Topics (Coming Later)

The following topics are important for interviews but will be covered after completing the Python fundamentals roadmap:

- Variable Scope (Local & Global Variables)
- Global Keyword
- Multiple Variable Assignment
- Variable Swapping Techniques
- Type Casting (`int()`, `float()`, `str()`, `bool()`) in Detail
- Dynamic Typing
- Mutable vs Immutable Objects
- Memory Management (`id()` function)
- Constants (Python Naming Convention)
- Variable Annotations (Type Hints)