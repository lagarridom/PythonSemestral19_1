#import mod1 # Con expresiones

''' 1
import mod1

mod1.funcion(4)
print(mod1.a)
'''

''' 2
from mod1 import funcion

funcion(3)
'''

''' 3
from mod1 import funcion,Perro

funcion(4)
perro1 = Perro()
perro1.ladrar()
'''

''' 4
from mod1 import funcion as f
f(9)
'''

import mod1

# Que pasaría si - import mod2?

# Se importaría a si mismo y como tal no haría nada
# Error muy común al usar módulos