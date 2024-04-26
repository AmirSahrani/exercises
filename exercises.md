# implement functional programming concpets

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



# Caclulus

## Derivatives (SP1)

A derivative of a function give the slope of a function at a certain point, let's say you have a function with the distance traveled by a car, if you want to know exactly how fast that car is traveling at a certain point, you would want the slope of the function and that point. 
![Derivative animation](figures/derivative_animation.gif)

This derivate can be estimated with the following equation (note $$f'(x)$$ is the
derivative of $$f(x)$$:

$$ f'(x) \approx \frac{f(x + h) - f(x)}{h} $$

Your goal is to implement a function that takes in a function, and a value, and
returns the derivative of the function at that value. use `h=0.0001` as the
default value for h. Note that rounding might be different on your system.

```python
>>> def f(x):
...     return x ** 2

>>> derivative(f, 2)
3.999900000000167

>>> derivative(f, 2, h=1e-7)
4.000000091153311
```

# List usage

## Stride

When indexing a list, we can specify a step size we want, we call this step size
the stride. For example:

```python
>>> x = [1,2,3,4]
>>> x[::2]
[1,3]
```

Your job is to implement a function that can do the exact same as the stride
parameter, without using the parameter. Note that you should therefore also be able to take
in negative values.

```python
>>> x = [1,2,3,4] 
>>> stride(x, -2)
[4,2]
```

## Range

You have used the range function frequently during the course, now you are going
to implement it yourself. Your job is to implement a function that takes in a
start, stop and step value, and returns a list of numbers from start to stop,
with the given step size. If the step size is negative, the list should be in
descending order, but only if the start value is larger than the stop value.

```python
>>> range(1, 5, 1)
[1, 2, 3, 4]
>>> range(1, 5, 2)
[1, 3]
```

Now that you have implemented the range function, you have essentially all the
code you need index a list like you would using `x[start:stop:step]`. If you
want do have a more

## Your first DataBase

In this exercise you are going to implement a function that takes in a list of 4
lists, each containg some data, the first element in each list contains the name
of the person, the second element contains their hair color, and the last
contains a list of their favorite numbers.

| users \ data | Name | Hair Color | Favorite numbers |
| ------------ | ---- | ---------- | ---------------- |
| **1**        | Paul | 'black'    | [0,3,4]          |
| **2**        | Anna | 'gray'     | [9,7,1]          |
| **2**        | Tom  | 'red'      | [0,3,5]          |
| **2**        | Mary | 'blonde'   | [5,4]            |

Write a function that can take this data and an ID, and returns their hair color
and the favorite number (the first element in the list) of the person with that
ID. If the ID is not found, return None.

```python
>>> data = [
...     ['Paul', 'black', [0,3,4]],
...     ['Anna', 'gray', [9,7,1]],
...     ['Tom', 'red', [0,3,5]],
...     ['Mary', 'blonde', [5,4]]
... ]
>>> get_user_data(data, 1)
('black', 0)
>>> get_user_data(data, 2)
('gray', 9)
>>> get_user_data(data, 9)
None
```

