[índice](README.md)

## Estructuras de datos

### sets o conjuntos

Python incluye un tipo de datos para conjuntos o sets. Un set es una colección no ordenada que contiene elementos no repetidos. Es empleado para comprobación de duplicados o operaciones matemáticas de conjuntos como: union, intersección y diferencia.

Las llaves o la operación set() puede ser utlizada para crear conjuntos.


```python
# Conjunto vacio
conjunto_vacio = set()
conjunto_vacio
```




    set()




```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket
```




    {'apple', 'banana', 'orange', 'pear'}




```python
# Comprobación de membresia
'orange' in basket 
```




    True




```python
'crabgrass' in basket
```




    False




```python
# Obtención de conjuntos de letras basado en palabras
a = set('abracadabra')
b = set('alacazam')
a
```




    {'a', 'b', 'c', 'd', 'r'}




```python
# Letras en a pero no en b
a - b
```




    {'b', 'd', 'r'}




```python
# letras en a o en b o en ambos
a | b
```




    {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}




```python
# letras en a y en b
a & b
```




    {'a', 'c'}




```python
# Letras en a o en b pero no en ambos
a ^ b
```




    {'b', 'd', 'l', 'm', 'r', 'z'}




```python
# Se puede hacer set comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
a
```




    {'d', 'r'}



## Diccionarios

Otro tipo de dato muy útil en el diccionario. Comúnmente llamado memoria asociativa. A diferencia de las secuencias que son accesadas por índices en el rango de números. Los diccionarios son accesados por llaves o keys. Las llaves puede ser de cualquier inmutable tipo. La mejor forma de tratar un diccionario como un conjunto de pares: llave : valor.


```python
# un diccionario vacio
a = {}
a
```




    {}




```python
# Creación de un diccionario
tel = {'jack': 4098, 'sape': 4139}
tel
```




    {'jack': 4098, 'sape': 4139}




```python
# Modificación de un valor
tel['guido'] = 4127
tel
```




    {'jack': 4098, 'sape': 4139, 'guido': 4127}




```python
# Acceso de un elemento por medio de una llave
tel['jack']
```




    4098




```python
# Borrado de un par llave: valor
del tel['sape']
tel
```




    {'jack': 4098, 'guido': 4127}




```python
# Creación de un nuevo par llave: valor
tel['irv'] = 4127
tel
```




    {'jack': 4098, 'guido': 4127, 'irv': 4127}




```python
# listar las llaves de un diccionario
list(tel)
```




    ['jack', 'guido', 'irv']




```python
sorted(tel)
```




    ['guido', 'irv', 'jack']




```python
# Consulta de una llave en específico
'guido' in tel
```




    True




```python
'jack' not in tel
```




    False




```python
# Otra forma de crear un diccionario
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
```




    {'sape': 4139, 'guido': 4127, 'jack': 4098}




```python
# Por medio de dict comprehension
{x: x**2 for x in (2, 4, 6)}
```




    {2: 4, 4: 16, 6: 36}




```python
# POr medio de argumento de la función dict
dict(sape=4139, guido=4127, jack=4098)
```




    {'sape': 4139, 'guido': 4127, 'jack': 4098}




```python
# Borrar todos los elementos del diccionario
a = {'sape': 4139, 'guido': 4127, 'jack': 4098}
a.clear()
a
```




    {}




```python
# Obtiene una copia del diccionario
a = {'sape': 4139, 'guido': 4127, 'jack': 4098}
id(a)
```




    132333312




```python
b = a.copy()
id(b)
```




    7578608




```python
# crea un diccionario dado una secuencia de llaves
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
vowels
```




    {'i': None, 'a': None, 'o': None, 'u': None, 'e': None}




```python
# utilizando valores
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
vowels
```




    {'i': 'vowel', 'a': 'vowel', 'o': 'vowel', 'u': 'vowel', 'e': 'vowel'}




```python
# Crear un diccionario basado un objeto mutable
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)
```

    {'i': [1], 'a': [1], 'o': [1], 'u': [1], 'e': [1]}
    {'i': [1, 2], 'a': [1, 2], 'o': [1, 2], 'u': [1, 2], 'e': [1, 2]}
    


# [Dictionaries retake](https://docs.python.org/3/library/stdtypes.html#dict) 
Collections of `key`-`value` pairs. 


```python
my_empty_dict = {}  # alternative: my_empty_dict = dict()
print('dict: {}, type: {}'.format(my_empty_dict, type(my_empty_dict)))
```

    dict: {}, type: <class 'dict'>
    

## Initialization


```python
dict1 = {'value1': 1.6, 'value2': 10, 'name': 'John Doe'}
dict2 = dict(value1=1.6, value2=10, name='John Doe')

print(dict1)
print(dict2)

print('equal: {}'.format(dict1 == dict2))
print('length: {}'.format(len(dict1)))
```

    {'value1': 1.6, 'value2': 10, 'name': 'John Doe'}
    {'value1': 1.6, 'value2': 10, 'name': 'John Doe'}
    equal: True
    length: 3
    

## `dict.keys(), dict.values(), dict.items()`


```python
print('keys: {}'.format(dict1.keys()))
print('values: {}'.format(dict1.values()))
print('items: {}'.format(dict1.items()))
```

    keys: dict_keys(['value1', 'value2', 'name'])
    values: dict_values([1.6, 10, 'John Doe'])
    items: dict_items([('value1', 1.6), ('value2', 10), ('name', 'John Doe')])
    

## Accessing and setting values


```python
my_dict = {}
my_dict['key1'] = 'value1'
my_dict['key2'] = 99
my_dict['key1'] = 'new value'  # overriding existing value
print(my_dict)
print('value of key1: {}'.format(my_dict['key1']))
```

    {'key1': 'new value', 'key2': 99}
    value of key1: new value
    

Accessing a nonexistent key will raise `KeyError` (see [`dict.get()`](#dict_get) for workaround):


```python
# print(my_dict['nope'])
```

## Deleting


```python
my_dict = {'key1': 'value1', 'key2': 99, 'keyX': 'valueX'}
del my_dict['keyX']
print(my_dict)

# Usually better to make sure that the key exists (see also pop() and popitem())
key_to_delete = 'my_key'
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
else:
    print('{key} is not in {dictionary}'.format(key=key_to_delete, dictionary=my_dict))
```

    {'key1': 'value1', 'key2': 99}
    my_key is not in {'key1': 'value1', 'key2': 99}
    

## Dictionaries are mutable


```python
my_dict = {'ham': 'good', 'carrot': 'semi good'}
my_other_dict = my_dict
my_other_dict['carrot'] = 'super tasty'
my_other_dict['sausage'] = 'best ever'
print('my_dict: {}\nother: {}'.format(my_dict, my_other_dict))
print('equal: {}'.format(my_dict == my_other_dict))
```

    my_dict: {'ham': 'good', 'carrot': 'super tasty', 'sausage': 'best ever'}
    other: {'ham': 'good', 'carrot': 'super tasty', 'sausage': 'best ever'}
    equal: True
    

Create a new `dict` if you want to have a copy:


```python
my_dict = {'ham': 'good', 'carrot': 'semi good'}
my_other_dict = dict(my_dict)
my_other_dict['beer'] = 'decent'
print('my_dict: {}\nother: {}'.format(my_dict, my_other_dict))
print('equal: {}'.format(my_dict == my_other_dict))
```

    my_dict: {'ham': 'good', 'carrot': 'semi good'}
    other: {'ham': 'good', 'carrot': 'semi good', 'beer': 'decent'}
    equal: False
    

<a id='dict_get'></a>
## `dict.get()`
Returns `None` if `key` is not in `dict`. However, you can also specify `default` return value which will be returned if `key` is not present in the `dict`. 


```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
d = my_dict.get('d')
print('d: {}'.format(d))

d = my_dict.get('d', 'my default value')
print('d: {}'.format(d))
```

    d: None
    d: my default value
    

## `dict.pop()`


```python
my_dict = dict(food='ham', drink='beer', sport='football')
print('dict before pops: {}'.format(my_dict))

food = my_dict.pop('food')
print('food: {}'.format(food))
print('dict after popping food: {}'.format(my_dict))

food_again = my_dict.pop('food', 'default value for food')
print('food again: {}'.format(food_again))
print('dict after popping food again: {}'.format(my_dict))

```

    dict before pops: {'food': 'ham', 'drink': 'beer', 'sport': 'football'}
    food: ham
    dict after popping food: {'drink': 'beer', 'sport': 'football'}
    food again: default value for food
    dict after popping food again: {'drink': 'beer', 'sport': 'football'}
    

## `dict.setdefault()`
Returns the `value` of `key` defined as first parameter. If the `key` is not present in the dict, adds `key` with default value (second parameter).


```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
a = my_dict.setdefault('a', 'my default value')
d = my_dict.setdefault('d', 'my default value')
print('a: {}\nd: {}\nmy_dict: {}'.format(a, d, my_dict))
```

    a: 1
    d: my default value
    my_dict: {'a': 1, 'b': 2, 'c': 3, 'd': 'my default value'}
    

## `dict.update()`
Merge two `dict`s


```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
dict1.update(dict2)
print(dict1)

# If they have same keys:
dict1.update({'c': 4})
print(dict1)
```

    {'a': 1, 'b': 2, 'c': 3}
    {'a': 1, 'b': 2, 'c': 4}
    

## The keys of a `dict` have to be immutable

Thus you can not use e.g. a `list` or a `dict` as key because they are mutable types
:


```python
# bad_dict = {['my_list'], 'value'}  # Raises TypeError
```

Values can be mutable


```python
good_dict = {'my key': ['Python', 'is', 'still', 'cool']}
print(good_dict)
```

    {'my key': ['Python', 'is', 'still', 'cool']}
    


### Técnica de ciclos


```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
```

    gallahad the pure
    robin the brave
    


```python
# se puede obtener la secuencia con el índice de posición
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```

    0 tic
    1 tac
    2 toe
    


```python
# Para iterar por 2 secuencias al mismo tiempo
# se pueden hacer parejas con la función zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```

    What is your name?  It is lancelot.
    What is your quest?  It is the holy grail.
    What is your favorite color?  It is blue.

[índice](README.md)