
# [`for` loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

## Looping lists


```python
my_list = [1, 2, 3, 4, 'Python', 'is', 'neat']
for item in my_list:
    print(item)
```

    1
    2
    3
    4
    Python
    is
    neat
    

### `break`
Stop the execution of the loop.


```python
for item in my_list:
    if item == 'Python':
        break
    print(item)
```

    1
    2
    3
    4
    

### `continue`
Continue to the next item without executing the lines occuring after `continue` inside the loop.


```python
for item in my_list:
    if item == 1:
        continue
    print(item)
```

    2
    3
    4
    Python
    is
    neat
    

### `enumerate()`
In case you need to also know the index:


```python
for idx, val in enumerate(my_list):
    print('idx: {}, value: {}'.format(idx, val))
```

    idx: 0, value: 1
    idx: 1, value: 2
    idx: 2, value: 3
    idx: 3, value: 4
    idx: 4, value: Python
    idx: 5, value: is
    idx: 6, value: neat
    

## Looping dictionaries


```python
my_dict = {'hacker': True, 'age': 72, 'name': 'John Doe'}
for val in my_dict:
    print(val)
```

    hacker
    age
    name
    


```python
for key, val in my_dict.items():
    print('{}={}'.format(key, val))
```

    hacker=True
    age=72
    name=John Doe
    

## `range()`


```python
for number in range(5):
    print(number)
```

    0
    1
    2
    3
    4
    


```python
for number in range(2, 5):
    print(number)
```

    2
    3
    4
    


```python
for number in range(0, 10, 2):  # last one is step
    print(number)
```

    0
    2
    4
    6
    8
    
