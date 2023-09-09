
import random

vidas= 5

puntos= 0

#si sale 0 pierde una vida
#si se genera cualquier otro numero dentro un rango establecido,gana puntos

while vidas !=0:

    num=random.randint(0,9)

    if num !=0:
        puntos+=1 #que se incremente 
        print("tienes",puntos,"puntos")
    else:
        vidas-=1
        print("te quedan",vidas,"vidas")
