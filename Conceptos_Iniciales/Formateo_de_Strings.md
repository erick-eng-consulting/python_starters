[índice](../README.md)

## Formateo de strings por medio del operador %

Todos los datos puedes ser mostrados mediante conversión o formato

Por ejemplo, los números enteros pueden ser convertidos a formato decimal o hexadecimal


```python
# Formateo de enteros
integerValue = 4237 
print("Integer ", integerValue )
print("Decimal integer %d" % integerValue)
print("Hexadecimal integer %x\n" % integerValue)
```

    Integer  4237
    Decimal integer 4237
    Hexadecimal integer 108d
    
    

De la misma manera, la conversión de un número decimal o flotante y controlarle la expresión, por ejemplo la forma exponencial


```python
floatValue = 123456.789 
print("Float", floatValue)
print("Default float %f" % floatValue)
print("Default exponential %e\n" % floatValue)
print("Right justify integer (%8d)" % integerValue)
print("Left justify integer  (%-8d)\n" % integerValue)
```

    Float 123456.789
    Default float 123456.789000
    Default exponential 1.234568e+05
    
    Right justify integer (    4237)
    Left justify integer  (4237    )
    
    

Del mismo modo, puede controlarse la cantidad de dígitos por mostrar.


```python
stringValue = "String formatting"
print("Force eight digits in integer %.8d" % integerValue)
print("Five digits after decimal in float %.5f" % floatValue)
print("Fifteen and five characters allowed in string:")
print("(%.15s) (%.5s)" % ( stringValue, stringValue ))
```

    Force eight digits in integer 00004237
    Five digits after decimal in float 123456.78900
    Fifteen and five characters allowed in string:
    (String formatti) (Strin)

[índice](README.md)