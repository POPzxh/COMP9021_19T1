# Written by YZCJ and Eric Martin for COMP9021

# 仅供学习交流，不得作为作业提交，被查重本人概不负责
# 代码千万条，自律第一条，借鉴不规范，亲人两行泪

def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}


def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    >>> describe_rule(4)
    The rule encoded by 4 is:  {(0, 0): 0, (0, 1): 1, (1, 0): 0, (1, 1): 0}
    <BLANKLINE>
    After 0 followed by 0, we draw 0
    After 0 followed by 1, we draw 1
    After 1 followed by 0, we draw 0
    After 1 followed by 1, we draw 0
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for i in rule.items():
        print(f'After {i[0][0]} followed by {i[0][1]}, we draw {i[1]}')


def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".

    >>> draw_line(3, 0, 0, 0)
    <BLANKLINE>
    >>> draw_line(3, 0, 0, 1)
    0
    >>> draw_line(3, 0, 0, 2)
    00
    >>> draw_line(3, 1, 0, 5)
    10101
    >>> draw_line(4, 1, 0, 9)
    100000000
    >>> draw_line(4, 1, 0, 0)
    <BLANKLINE>
    >>> draw_line(4, 0, 1, 13)
    0110000000000
    >>> draw_line(11, 1, 0, 16)
    1010101010101010
    >>> draw_line(11, 1, 1, 19)
    1111111111111111111
    >>> draw_line(14, 0, 0, 21)
    001101101101101101101
    >>> draw_line(14, 1, 0, 22)
    1011011011011011011011
    '''
    rule = rule_encoded_by(rule_nb)
    line = f'{first}{second}'
    if length >= 3:
        for _ in range(length - 2):
            line += str(rule[(int(line[-2]), int(line[-1]))])
        print(line)
    else:
        print(line[0:length])


def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    >>> uniquely_produced_by_rule('1100110011')
    12
    >>> uniquely_produced_by_rule('01100001')
    -1
    >>> uniquely_produced_by_rule('001100101')
    -1
    >>> uniquely_produced_by_rule('01100000')
    4
    >>> uniquely_produced_by_rule('001101101')
    14
    >>> uniquely_produced_by_rule('11111111')
    -1
    >>> uniquely_produced_by_rule('00011')
    -1
    >>> uniquely_produced_by_rule('11001')
    -1
    >>> uniquely_produced_by_rule('0010001')
    -1
    >>> uniquely_produced_by_rule('0010001')
    -1
    '''
    rule = [(1, 1), (1, 0), (0, 1), (0, 0)]
    t = 0
    try:
        for i in range(len(rule)):
            index = line.index(f'{rule[i][0]}{rule[i][1]}', 0, len(line) - 1)
            value = int(line[index + 2])
            for j in range(index + 1, len(line) - 2):
                if line[j:j + 2] == f'{rule[i][0]}{rule[i][1]}' and line[j + 2] != f'{value}':
                    return -1
            t += value * 2 ** i
    except ValueError:
        return -1
    return t
    # REPLACE pass ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
