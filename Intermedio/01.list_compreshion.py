print("************************************************************")
print("Lista de compresion")
print("************************************************************")

my_original_list = [35, 24, 62, 52, 30, 30, 17]
my_list = [i for i in my_original_list]
print(my_list)

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
my_list = [i for i in range(8)]
print(my_original_list)
print(my_list)

my_range = range(8)
print(my_range)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list)

my_list = [i+1 for i in range(8)]
print(my_list)

def sum_five(num):
    return num + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)
