
import random
array = [1,2,3,4,5,6,7,8,9]
random.shuffle(array)
result = array[1] 
valor =int(input("Descreva o número que acha que é:"))
i =1
if valor == result:
    print("parabéns acertou o número")
else:
    while valor != result and i < 10:
        valor = int(input("tente denovo e vamos ver se tu acerta"))
        i = i +1