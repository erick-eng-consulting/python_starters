[índice](../README.md)

## Operaciones a los strings

Aplicar mayúscula a la primera letra


```python
'hola'.capitalize()
```




    'Hola'



Número de veces que un caracter, un un pequeño string está contenida


```python
'hooola'.count('o')
```




    3



Replaca las tabulaciones por espacios


```python
'\thola\t'.expandtabs(4)
```




    '    hola    '



Verifica que una subcadena está al final de la cadena


```python
'hasta luego'.endswith('ego')
```




    True




```python
'hasta luego'.endswith('lu')
```




    False



Busca un substring y devuelve el índice del lugar donde comienza


```python
'hasta luego. adios'.find('luego')
```




    6



Verifica si la cadena es alfa numérica


```python
'hasta luego. adios'.isalpha()
```




    False




```python
'hastaluegoadios'.isalpha()
```




    True



Verifica si el dato es un números


```python
'10'.isdigit()
```




    True




```python
'10a'.isdigit()
```




    False



Parte una cadena por un token específico y devuelve una lista


```python
'hola a todos'.split(' ')
```




    ['hola', 'a', 'todos']



Une con caracter específico todos los elementos de una lista 


```python
"-".join(['hola', 'a', 'todos'])
```




    'hola-a-todos'



Cambia todas las letras a minúsculas


```python
'Adios a todos. Gracias'.lower()
```




    'adios a todos. gracias'



Reemplaza una cadena por otra


```python
'Adios a todos. Gracias'.replace('Adios', 'Hola')
```




    'Hola a todos. Gracias'



Verifica si un string comienza con un substring específico


```python
'hasta luego'.startswith('hasta')
```




    True




```python
'hola, hasta luego'.startswith('hasta')
```




    False



Intercambia todas las mayúsculas por minúsculas y viceversa


```python
'Adios a todos. Gracias'.swapcase()
```




    'aDIOS A TODOS. gRACIAS'

[índice](README.md)
