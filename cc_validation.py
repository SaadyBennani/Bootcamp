# ccvalidation.py


def cc_validation(cc):
    """
    returns wether  a string containing a credit card number is valid as a boolean
    """
    check_digit = cc[-1]
    cc_list = list(cc)[0:-1]
    rev = cc_list[::-1]
    rev = [int(i) for i in rev]
    rev[::2] = [int(i) * 2 for i in rev[::2]]
    min_9 = []
    for i in rev:
        if i <= 9:
            min_9.append(i)
        else:
            min_9.append(i-9)
    sum_m9 = sum(min_9)
    if check_digit == str(sum_m9)[-1]:
        return 'Valid'
    else:
        return 'Invalid'


print(cc_validation('4556737586899855'))
