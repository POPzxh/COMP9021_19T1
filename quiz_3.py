# Written by Eric Martin for COMP9021

import sys
from random import seed, randint, randrange


# try:
#     arg_for_seed, upper_bound, length =\
#             (int(x) for x in input('Enter three integers: ').split())
# except ValueError:
#     print('Incorrect input, giving up.')
#     sys.exit()


def length_of_longest_increasing_sequence(L):
    """
    >>> L_1 = [3]
    >>> length_of_longest_increasing_sequence(L_1)
    1
    >>> L_1 = [3, 3, 3, 3, 3]
    >>> length_of_longest_increasing_sequence(L_1)
    5
    >>> L_1 = [3, 3, 0, 2]
    >>> length_of_longest_increasing_sequence(L_1)
    4
    >>> L_1 = [6, 6, 0, 4, 8]
    >>> length_of_longest_increasing_sequence(L_1)
    3
    >>> L_1 = [2, 1, 4, 1, 7, 7, 7]
    >>> length_of_longest_increasing_sequence(L_1)
    4
    >>> L_1 = [2, 9, 1, 4, 1, 7]
    >>> length_of_longest_increasing_sequence(L_1)
    2
    >>> L_1 = [6, 3, 6, 3, 0, 2, 4, 3, 3, 6]
    >>> length_of_longest_increasing_sequence(L_1)
    4
    >>> L_1 = [0, 0, 0, 2, 1, 2, 2, 4, 1, 4]
    >>> length_of_longest_increasing_sequence(L_1)
    4
    >>> L_1 = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5, 3, 8, 2, 4, 2, 1, 4, 8, 2, 4]
    >>> length_of_longest_increasing_sequence(L_1)
    4
    >>> L_1 = [1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 0, 2, 0, 1, 0, 0, 2, 1, 2, 2, 2, 0, 1, 0]
    >>> length_of_longest_increasing_sequence(L_1)
    6
    """
    longest = 1
    i = 0
    while i < len(L):

        tmp = 1

        for j in range(i, i+len(L)):
            i = j + 1
            if L[j % len(L)] > L[(j+1) % len(L)]:
                break
            if tmp < len(L):
                tmp += 1

        if tmp > longest:
            longest = tmp

    return longest


def built_int(start, l):
    cur = start
    int_str = ''
    visited = set()
    while cur not in visited:
        int_str += str(l[cur])
        visited.add(cur)
        cur = l[cur]
    return int(int_str)


def max_int_jumping_in(L):
    """
    >>> L_2 = [3, 3, 2, 3]
    >>> max_int_jumping_in(L_2)
    33
    >>> L_2 = [3, 3, 2, 3, 2]
    >>> max_int_jumping_in(L_2)
    33
    >>> L_2 = [3, 3, 5, 3, 1, 0]
    >>> max_int_jumping_in(L_2)
    5033
    >>> L_2 = [5, 3, 6, 1, 0, 3, 0]
    >>> max_int_jumping_in(L_2)
    605313
    >>> L_2 = [4, 7, 5, 9, 3, 8, 2, 4, 2, 1]
    >>> max_int_jumping_in(L_2)
    439174
    >>> L_2 = [0, 9, 2, 6, 6, 8, 5, 8, 7, 8]
    >>> max_int_jumping_in(L_2)
    65878
    >>> L_2 = [3, 2, 10, 15, 17, 3, 11, 13, 10, 19, 6, 17, 15, 14, 16, 8, 1, 17, 0, 2]
    >>> max_int_jumping_in(L_2)
    13141612106111717
    >>> L_2 = [23, 2, 21, 10, 15, 17, 3, 11, 13, 10, 19, 20, 6, 17, 15, 14, 16, 8, 1, 17, 0, 2, 23, 12, 22]
    >>> max_int_jumping_in(L_2)
    1120023126310191781317
    """
    return max(built_int(i, L) for i in range(len(L)))
    # REPLACE pass ABOVE WITH  YOUR CODE

# seed(arg_for_seed)
# L_1 = [randint(0, upper_bound) for _ in range(length)]
# print('L_1 is:', L_1)
# print('The length of the longest increasing sequence\n'
#       '  of members of L_1, possibly wrapping around, is:',
#       length_of_longest_increasing_sequence(L_1), end = '.\n\n'
#      )
# L_2 = [randrange(length) for _ in range(length)]
# print('L_2 is:', L_2)
# print('The maximum integer built from L_2 by jumping\n'
#       '  as directed by its members, from some starting member\n'
#       '  and not using any member more than once, is:',
#       max_int_jumping_in(L_2)
#      )
