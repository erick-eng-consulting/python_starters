[índice](README.md)

# Tuplas

Una tupla es una colección de elementos de cualquier tipo de dato. Una característica de las tuplas que sus elementos no se pueden modificar.


```python
# Crear una tupla, la sintaxis requiere que se usen los parentesis.
T = (1,2,3,4)
```


```python
# Se obtiene la longitud de una tupla.
len(T)
```




    4



Es posible ejecutar operaciones como la concatenación.


```python
T + (5,6)
```




    (1, 2, 3, 4, 5, 6)



Consultar por el elemento en una posición en especifico:


```python
T[0]
```




    1



Adicionalmente, cuál es la posición de un elemento en particular.


```python
T.index(4)
```




    3



Contar por el número veces que la tupla contiene un determinado elemento


```python
T.count(4)
```




    1



No es posible modificar algún elemento


```python
T[0]=2
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-35-044687bb86e2> in <module>()
    ----> 1 T[0]=2
    

    TypeError: 'tuple' object does not support item assignment


Es posible crear o reconstruir la tupla uniendo tuplas


```python
T = (2,) + T[1:]
T
```




    (2, 2, 3, 4)



Otra forma de componer tuplas


```python
T = 'spam' , 3.0 , [11,22,33]
T
```




    ('spam', 3.0, [11, 22, 33])



Consultando un elemento en particular


```python
T[1]
```




    3.0



Y sus subelementos:


```python
T[2][1]
```




    22


