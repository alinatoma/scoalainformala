#Exercitiul 1: Să se scrie o funcție care primește un număr nedefinit de parametrii si face suma numerelor
def number_sum(*args, **kwargs):
    result = 0
    for i in args:
        if type(i) == int or type(i) == float:
            result += i
    return result

print(number_sum(2, 4, 'abc', param_1=2))

#Exercitiul 2: Functie recursiva

def recursive_sum(n):
    if n == 0:
        return n
    return n + recursive_sum(n-1)
print(recursive_sum(5))

def recursive_sum_par(n):
    if n == 0:
        return 0
    sum_par = recursive_sum_par(n-1)
    if n % 2 == 0:
        sum_par += n
    return sum_par
print(recursive_sum_par(7))

def recursive_sum_impar(n):
    if n == 0:
        return 0
    sum_impar = recursive_sum_impar(n-1)
    if n % 2 != 0:
        sum_impar += n
    return sum_impar
print(recursive_sum_impar(8))

#Exercitiul 3: Functie care citeste de la tastatura si returneaza valoarea sau 0

def check_input(input_verificat):
    if input_verificat.strip().isdigit():
        print(input_verificat)
    else:
        print("0")

numar=input("Introduceti un numar: ")
check_input(numar)

