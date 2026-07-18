# append()

## Purpose
`append()` adds an element to the **end** of a list.

## Syntax

```python
list_name.append(value)
```

## Example

```python
numbers = [10, 20]
numbers.append(30)

print(numbers)
```

Output:

```python
[10, 20, 30]
```

## Key Points

- Adds one element at the end.
- Changes the original list.
- Very commonly used in loops to build a list.

## Common Pattern

```python
numbers = []

i = 1

while i <= 5:
    numbers.append(i)
    i = i + 1

print(numbers)
```

## Interview Tip

Use `append()` whenever you need to collect or store values while processing data.