# Implement functional programming concpets

## Map (SP1)

Your goal is to implment the map funtion, it should take in a function and a
list, and return a new list, each element of which is the result of applying the
function on the corresponding element of the original list.

```python
>>> map(math.sqrt, [1, 4, 9, 16, 25])
[1.0, 2.0, 3.0, 4.0, 5.0]
```

```python
>>> map(int, [1.0, 2.0, 3.0, 4.0, 5.0])
[1, 2, 3, 4, 5]
```

```python >>> map(lambda x: x * 2, [1, 2, 3, 4, 5])
[2, 4, 6, 8, 10]
```

## Filter (SP1)

Your goal is to implement the filter function, it should take in a function and
a list, and return a new list, each element of which is the result of applying
the function on the corresponding element of the original list.

```python
>>> filter(string.isdigit, ['a', '1', 'b', '2', 'c', '3'])
['1', '2', '3']
```

```python
>>> filter(lambda x: x > 2, [1, 2, 3, 4, 5])
[3, 4, 5]
```

## Partial (SP2)

> Probably really hard, not for exam in its current state Maybe this can be made
> easier by providing a template for the partial function

Your goal is to implement the partial function, it should take in a function and
a list of arguments, and return a new function that takes in the remaining
arguments.

```python
>>> def add(a, b):
...     return a
>>> add_5 = partial(add, 5)
>>> add_5(3)
8
```

```python
>>> def power(base, exponent):
...     return base ** exponent
>>> square = partial(power, 2)
>>> square(3)
9
```



