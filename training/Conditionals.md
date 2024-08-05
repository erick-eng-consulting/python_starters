[índice](../README.md)

# Conditionals

## Testing truth value

### `bool`


```python
print('type of True and False: {}'.format(type(True)))
```

    type of True and False: <class 'bool'>
    


```python
print('0: {}, 1: {}'.format(bool(0), bool(1)))
print('empty list: {}, list with values: {}'.format(bool([]), bool(['woop'])))
print('empty dict: {}, dict with values: {}'.format(bool({}), bool({'Python': 'cool'})))
```

    0: False, 1: True
    empty list: False, list with values: True
    empty dict: False, dict with values: True
    

### `==, !=, >, <, >=, <=`


```python
print('1 == 0: {}'.format(1 == 0))
print('1 != 0: {}'.format(1 != 0))
print('1 > 0: {}'.format(1 > 0))
print('1 > 1: {}'.format(1 > 1))
print('1 < 0: {}'.format(1 < 0))
print('1 < 1: {}'.format(1 < 1))
print('1 >= 0: {}'.format(1 >= 0))
print('1 >= 1: {}'.format(1 >= 1))
print('1 <= 0: {}'.format(1 <= 0))
print('1 <= 1: {}'.format(1 <= 1))
```

    1 == 0: False
    1 != 0: True
    1 > 0: True
    1 > 1: False
    1 < 0: False
    1 < 1: False
    1 >= 0: True
    1 >= 1: True
    1 <= 0: False
    1 <= 1: True
    

You can combine these:


```python
print('1 <= 2 <= 3: {}'.format(1 <= 2 <= 3))
```

    1 <= 2 <= 3: True
    

### `and, or, not`


```python
python_is_cool = True
java_is_cool = False
empty_list = []
secret_value = 3.14
```


```python
print('Python and java are both cool: {}'.format(python_is_cool and java_is_cool))
print('secret_value and python_is_cool: {}'.format(secret_value and python_is_cool))
```

    Python and java are both cool: False
    secret_value and python_is_cool: True
    


```python
print('Python or java is cool: {}'.format(python_is_cool or java_is_cool))
print('1 >= 1.1 or 2 < float("1.4"): {}'.format(1 >= 1.1 or 2 < float('1.4')))
```

    Python or java is cool: True
    1 >= 1.1 or 2 < float("1.4"): False
    


```python
print('Java is not cool: {}'.format(not java_is_cool))
```

    Java is not cool: True
    

You can combine multiple statements, execution order is from left to right. You can control the execution order by using brackets.


```python
print(bool(not java_is_cool or secret_value and  python_is_cool or empty_list))
print(bool(not (java_is_cool or secret_value and  python_is_cool or empty_list)))
```

    True
    False
    

## `if`


```python
statement = True
if statement:
    print('statement is True')
    
if not statement:
    print('statement is not True')
```

    statement is True
    


```python
empty_list = []
# With if and elif, conversion to `bool` is implicit
if empty_list:
    print('empty list will not evaluate to True')  # this won't be executed
```


```python
val = 3
if 0 <= val < 1 or val == 3:
    print('Value is positive and less than one or value is three')
```

    Value is positive and less than one or value is three
    

## `if-else`


```python
my_dict = {}
if my_dict:
    print('there is something in my dict')
else:
    print('my dict is empty :(')
```

    my dict is empty :(
    

## `if-elif-else`


```python
val = 88
if val >= 100:
    print('value is equal or greater than 100')
elif val > 10:
    print('value is greater than 10 but less than 100')
else:
    print('value is equal or less than 10')
```

    value is greater than 10 but less than 100
    

You can have as many `elif` statements as you need. In addition, `else` at the end is not mandatory.


```python
greeting = 'Hello fellow Pythonista!'
language = 'Italian'

if language == 'Swedish':
    greeting = 'Hejsan!'
elif language == 'Finnish':
    greeting = 'Latua perkele!'
elif language == 'Spanish':
    greeting = 'Hola!'
elif language == 'German':
    greeting = 'Guten Tag!'
    
print(greeting)
```

    Hello fellow Pythonista!

[índice](README.md)