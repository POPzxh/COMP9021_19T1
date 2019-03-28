# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by Eric Martin for COMP9021


import sys


try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
    encoded_set = bin(encoded_set)[2 :][: : -1]
    decoded_set = []
    for i in range(len(encoded_set) // 2 * 2 - 1, -1, -2):
        if encoded_set[i] == '1':
            decoded_set.append(-(i + 1) // 2)
    for i in range(0, len(encoded_set), 2):
        if encoded_set[i] == '1':
            decoded_set.append(i // 2)
    return decoded_set
    
def code_derived_set(encoded_set):
    running_sums = []
    running_sum = 0
    encoded_set = bin(encoded_set)[2 :][: : -1]
    for i in range(len(encoded_set) // 2 * 2 - 1, -1, -2):
        if encoded_set[i] == '1':
            running_sum += -(i + 1) // 2
            running_sums.append(running_sum)
    for i in range(0, len(encoded_set), 2):
        if encoded_set[i] == '1':
            running_sum += i // 2
            running_sums.append(running_sum)
    encoded_running_sum = 0
    for value in running_sums:
        if value < 0:
            encoded_running_sum |= 1 << (-value * 2 - 1)
        else:
            encoded_running_sum |= 1 << (value * 2)
    return encoded_running_sum

print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))

    
