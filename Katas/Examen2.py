# PREGUNTA 1
def h(x):
    if x % 2 == 0:
        return x*2
    else:
        return x

x1 = 3
#print(h(x1))


# PREGUNTA 2/3
def mystery(elements, max_value):
    accum = []
    for elt in elements:
        if elt < max_value:
            accum.append(elt)
    return accum

elements2 = [1, 2, 3, 4, 5]
max_value2 = 3
#print(mystery(elements2, max_value2))
#print(mystery([],5))


# PREGUNTA 4/5
def f(string):
    vowels = set('aeiou')
    normalized = string.lower()
    return normalized[0] in vowels

string4 = "Hola amigos"
#print(f(string4))

# PREGUNTA 6
def frob(elements, predicate):
    accum = []
    for element in elements:
        if predicate(element):
            accum.append(element)
    return accum

elements6 = [1, 2, 3, 4, 5]
#print(frob(elements6, lambda x: x % 2))


# PREGUNTA 7/8
def candida(elements, combiner, initial_value):
    accum = initial_value
    for elt in elements:
        accum = combiner(accum, elt)
    return accum

elements7 = [1, 2, 3, 4, 5]
initial_value7 = 0
#print(candida(elements7, lambda a, b: a + b, initial_value7))
#print(candida([1, 2, 34, 56], lambda a, b: a +b, 0))


# PREGUNTA 9/10
def g(elements, transformer):
    accum = []
    for elt in elements:
        accum.append(transformer(elt))
    return accum

elements9 = [1, 2, 3, 4, 5]
#print(g(elements9, lambda x: 2*x))

def lens(list_of_lists):
    return g(list_of_lists, len)

list_of_lists10 = [[1, 2], [3, 4, 5]]
#print(lens(list_of_lists10))


# PREGUNTA 11
def epl(elements, predicate, new_value):
    new_list = []
    for element in elements:
        if predicate(element):
            new_list.append(new_value)
        else:
            new_list.append(element)
    return new_list

elements11 = [1, 2, 3, 4, 5]
new_value11 = 0
#print(epl(elements11, lambda x: x%2, new_value11))


# PREGUNTA 12
# while True:
#     name = input('Type your name:')
#     if name == 'Anakin':
#         break


# PREGUNTA 13
# name == 'Anakin'

# PREGUNTA 14
def sum_all(numbers):
    index = 0
    sum = 0
    while index < len(numbers):
        sum = sum + numbers(index)
        index = index + 1
    return sum

numbers14 = [1, 2, 3, 4, 5]
#print(sum_all(numbers14))