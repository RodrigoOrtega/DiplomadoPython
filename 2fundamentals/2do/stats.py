#
# select and write 
# one of the following stat functions
#

# def sum(lst): pass

# def avg(l): pass

# def min(l): pass

# def max(l): pass

# def range(l): pass

# def std(l): pass

numbers = [82,15,16,11,15,19,30,18,50,75,19,48,79,19,30,19,33]
#El numero mas repetido es el 19

#funcion de moda
def mode(list):
    frequency = {}

    for value in list:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items()
                      if value == most_frequent]

    return modes[0]

print("La moda de la lista es: " + str(mode(numbers)))