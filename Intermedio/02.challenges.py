
print("************************************************************")
print("Challenges")
print("************************************************************")


print("")
print("************************************************************")
print("Fizz Buzz")
print("************************************************************")

def fizzbuzz():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
            print("FIZZBUZZ")
        elif index % 3 == 0:
            print("FIZZ")
        elif index % 5 == 0:
            print("BUZZ")
        else:
            print(index)

fizzbuzz()


print("")
print("************************************************************")
print("Anagrama")
print("************************************************************")

def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False

    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagram("amor", "roma"))


print("")
print("************************************************************")
print("Fibonacci")
print("************************************************************")


def fibonacci(num = 50):

    prev = 0
    next = 1

    for index in range(0,num):
        print(index, prev)

        fib = prev + next
        prev = next
        next = fib



fibonacci(7)

print("")
print("************************************************************")
print("Es un numero primo? hay 168 menos de 1000")
print("************************************************************")

max = 1000
contador = 0

def es_primo(num):
    num_primo = True
    
    if num < 2:
        num_primo = False
    else:
        for index in range(2, num):
            if num % index == 0:
                num_primo = False
                break 

    return num_primo

for i in range(2,max+1):
    if es_primo(i):
        contador += 1
        print(i)

print(f"hay {contador} de números primos hasta el {max}")



print("")
print("************************************************************")
print("invertir el orden en una cadena")
print("************************************************************")
texto ="Iba caperucita cantando"

def reverse(text):
    text_len = len(text)
    reverse_text = ""

    for i in range(0, text_len):
        reverse_text += text[text_len - i - 1]

    return reverse_text


print(texto)
print(reverse(texto))