data = ["value", 50, 91.1, (2001, 11, 21)]
#un_texto, un_valor, un_decimal, una_fecha = data

# _, un_valor, un_decimal, _ = data

un_texto, *_, (un_año, *_) = data
pass