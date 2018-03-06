# -*- coding: utf-8 -*-

def fizzbuzz(num):
    result = []
    for a in range(0, num+1):
        if a == 0:
            result.append('ValueError')
        else:
            if a % 3 == 0:
                if a % 5 == 0:
                    result.append('fizzbuzz')
                else:
                    result.append('fizz')
            elif a % 5 == 0:
                result.append('buzz')
            else:
                result.append(a)
    return result

if __name__ == "__main__":
    print fizzbuzz(5)
