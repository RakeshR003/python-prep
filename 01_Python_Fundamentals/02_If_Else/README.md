# If-Else

## Purpose

If-Else statements are used to make decisions in a program. They allow the program to execute different blocks of code based on whether a condition is True or False.

---

## Syntax

```python
if condition:
    # code

elif condition:
    # code

else:
    # code
```

---

## Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

---

## Rules

- Every `if` condition must evaluate to `True` or `False`.
- Indentation is mandatory.
- Only one `else` block is allowed.
- `elif` can be used multiple times.
- `else` is optional.

---

## Example

```python
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

## Common Mistakes

- Using `=` instead of `==`
- Incorrect indentation
- Forgetting to convert input using `int()`
- Writing multiple `else` blocks
- Forgetting the colon (`:`)

---

## Interview Tip

`if` checks a condition.

`elif` checks another condition only if the previous condition was False.

`else` runs when none of the conditions are True.

---

## Practice Programs

- Even or Odd
- Positive or Negative
- Largest of Two Numbers
- Fizz
- FizzBuzz
- Grade Calculator
- Voting Eligibility

---

## Progress

- [x] Concept Learned
- [x] Practice Completed
- [x] Beginner Interview Ready


---

## Advanced Topics (Coming Later)

The following topics are important for interviews but will be covered after completing the Python fundamentals roadmap:

- Logical Operators (`and`, `or`, `not`)
- Nested If-Else
- Conditional (Ternary) Operator
- Short-Circuit Evaluation
- Membership Operators (`in`, `not in`)
- Identity Operators (`is`, `is not`)
- Truthy and Falsy Values
- Complex Conditional Expressions
- Decision-Making Interview Problems