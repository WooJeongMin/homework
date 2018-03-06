# -*- coding: utf-8 -*-


def tax(income, age, baby):
    result = ""
    tax = 0
    if age >= 16 and age <= 65:
        if income < 20000:
            tax += int(income*0.2)
            if baby == 1:
                tax = int(tax - (tax*0.1))
                result = "나이 : {}, 내야하는 세금 : {}".format(age, tax)
            else:
                result = "나이 : {}, 내야하는 세금 : {}".format(age, tax)
        else:
            tax += int(income*0.5)
            if baby == 1:
                tax = int(tax - (tax*0.1))
                result = "나이 : {}, 내야하는 세금 : {}".format(age, tax)
            else:
                result = "나이 : {}, 내야하는 세금 : {}".format(age, tax)
    else:
        result = "세금 안내도됌"
    return result


if __name__ == "__main__":
    print tax(30000, 20, 1)
    pass

