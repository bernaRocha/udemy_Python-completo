"""
Tipos de dados
str - string "Texto" 'Texto'
int - inteiro 12344 67905 0
float - real/ ponto flutuante 3.141592
bool - booleano/ lógico True/ False
"""

print(type('Texto'))
print(type(123))
print(type(3.141592))
print(type(True))
print(bool([])) # lista vazia

#  Type casting
print('Nome', type('Nome'), bool('Nome')) #  Nome <class 'str'> True
print(10.5, type(int(10.5))) # 10.5 <class 'int'>

# Nome: string
print('Bernardo', type('Bernardo'))

# Idade: int
print(34, type(34))

# Altura: float
print(1.68, type(1.68))

# Maior de idade: bool
print(34 > 18, type(34 > 18))

"""
Bernardo <class 'str'>
34 <class 'int'>
1.68 <class 'float'>
True <class 'bool'>
"""