a = int(input())  #Задание №1
b = int(input())
if a==0 or b==0:
    print("На ноль делить нельзя!")
elif (-100<=a<=100) and (-100<=b<=100):
    print(a+b, a*b, ("{:f}".format(a/b)), a-b, max(a, b), min(a, b), sep='\n')
else:
    print("Ограничение!")


a, b, c = int(input()), int(input()), int(input()) #Задание №2
if ((-100<=a<=100) and (-100<=b<=100) and (-100<=c<=100)) and ((a and b and c)!=0):
    print(a+b+c, a*b*c, ("{:f}".format(a/b)), a-b-c, max(a,b,c), min(a,b,c), sep='\n')
else:
    print("Ограничение!")

#эту часть можно проверить