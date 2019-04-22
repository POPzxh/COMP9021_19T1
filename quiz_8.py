# A polynomial object can be created from a string that represents a polynomial
# as sums or differences of monomials.
# - Monomials are ordered from highest to lowest powers.
# - All factors are strictly positive, except possibly for the leading factor
# - For nonzero powers, factors of 1 are only implicit.
# A single space surrounds + and - signs between monomials.

# Written by *** and Eric Martin for COMP9021

# 惭愧惭愧，代码写的一点都不优雅。为了保持可读性，不少地方的判断语句会重复
# 不要只看答案哦，测试脚本放在quiz_8_test里了
from collections import defaultdict
from copy import deepcopy

class Polynomial:
    def __init__(self, polynomial=None):
        self.datagram = defaultdict(int)

        if not polynomial:
            self.datagram[0] = 0
        else:
            symbol = 1
            polynomial_splited = polynomial.split()
            leading_ele = polynomial_splited[0]

            if leading_ele[0] == '-':
                leading_ele = leading_ele[1:]
                symbol = -1

            analysed = self.__analyse_splited_polynomial(leading_ele)
            self.datagram[analysed[0]] = symbol*analysed[1]

            for i in range(0, len(polynomial_splited), 2)[1:]:
                # 正负号的index: i-1
                if polynomial_splited[i-1] == '-':
                    symbol = -1
                else:
                    symbol = 1
                analysed = self.__analyse_splited_polynomial(polynomial_splited[i])
                self.datagram[analysed[0]] = analysed[1] * symbol

    def __str__(self):
        datagram_sorted = sorted((i for i in self.datagram.items() if i[1] != 0), reverse=True, key=lambda x: x[0])
        if len(datagram_sorted) == 0:
            return '0'
        polynomial_string = self.__get_element(datagram_sorted[0][0], datagram_sorted[0][1])
        for i in datagram_sorted[1:]:
            tmp = self.__get_element(i[0], i[1])
            if tmp[0] == '-':
                tmp = ' - '+tmp[1:]
            else:
                tmp = ' + '+tmp
            polynomial_string += tmp
        return polynomial_string

    def __add__(self, other):
        c = deepcopy(self)
        for i in other.datagram.items():
            c.datagram[i[0]] += i[1]
        return c

    def __iadd__(self, other):
        for i in other.datagram.items():
            self.datagram[i[0]] += i[1]
        return self

    def __mul__(self, other):
        p = Polynomial()
        for i in self.datagram.items():
            for j in other.datagram.items():
                p.datagram[i[0]+j[0]] += i[1]*j[1]
        return p

    def __imul__(self, other):
        c = defaultdict(int)
        for i in self.datagram.items():
            for j in other.datagram.items():
                c[i[0]+j[0]] += i[1]*j[1]
        self.datagram = c
        return self

    def __get_element(self, p, f):
        # Inverse function of __analyse_splited_polynomial(self, ele)
        if p == 0:
            return str(f)
        elif p == 1:
            tail = 'x'
        else:
            tail = 'x^'+str(p)

        if f == 1:
            return tail
        elif f == -1:
            return '-'+tail
        else:
            return str(f)+tail

    def __analyse_splited_polynomial(self, ele):
        # 返回一个元组，第一位是幂，第二位是系数
        index = ele.find('x')

        if index == -1:
            # 如果不存在x，就认为可以直接转换成整数
            return 0, int(ele)

        if index == 0:
            # 系数为1
            f = 1
        else:
            # 系数不为1
            f = int(ele[0:index])

        if index == len(ele)-1:
            # 如果'x'位于最后一位，就认为幂是1
            p = 1
        else:
            # 幂大于1的情况
            p = int(ele[index+2:])

        return p, f

