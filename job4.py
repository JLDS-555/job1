for n in range(1,101):
    if n% 3 ==0 and n% 5==0:
        print("FizzBuzz")

        # les FizzBuzz qui apparaîssent sont divisible par 3 et par 5.


    elif n % 5 ==0:
        print("Buzz")

     # Ici les Buzz sontn les multiples de 5 qui sont divisibles par 5 et que le résultat est 0

    elif n % 3 ==0:
        print("Fizz")

    #Ici les Fizz sont des multiples de 3 c'est le même principe que les multiples de 5.


    else: 
        print(n)

        # le else c'est pour apparaitre le reste des numéros normaux qui ne sont pas des multiples de 3 et de 5.

print("----------------------------------------------")