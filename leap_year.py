# -*- coding: utf-8 -*-

def leap_year(age):
    result = ""
    if age%400 == 0:
        result = "윤년"
    elif age%100 == 0:
        result = "평년"
    elif age%4 == 0:
        result = "윤년"
    else:
        result = "평년"
    return result

if __name__ == "__main__":
    print leap_year(1500)
    pass
