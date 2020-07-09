# No python podemos alterar o comportamento dos operadores através da
# sobreescrita de métodos específicos. Ao fazer isso dentro e uma
# classe, as operações realizadas diretamente nas instâncias delas serão
# processadas de acordo com o comportamento que você escreveu e não com o
# comportamento padrão que estava definido pelo Python.

# Por exemplo, podemos sobreescrever o comportamento do + com o método __add__
# Ele vai receber dois argumentos, o self e o other


class Incrivel:
    def __init__(self, nome):
        self.nome = nome

    def __add__(self, other):
        return f'{self.nome} + {other.nome} = Melhor casal do mundo! ❤'


class Homem(Incrivel):
    # Alteramos o comportamento do print pela função __repr__
    def __repr__(self):
        return f'{self.nome} é um cara incrível.'


class Mulher(Incrivel):
    def __repr__(self):
        return f'{self.nome} é a mulher mais fofa do mundo.'


eu = Homem('<Oi>')
voce = Mulher('<Manda isso pra morena programadora>')

print(eu)
print(voce)
print(eu + voce)

"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""
