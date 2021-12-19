from math import ceil, log
import argparse

msg_err = "Incorrect parameters"

parser = argparse.ArgumentParser()
parser.add_argument("--type", default="empty")
parser.add_argument("--principal", default="empty")
parser.add_argument("--interest", default="empty")
parser.add_argument("--periods", default="empty")
parser.add_argument("--payment", default="empty")

args = parser.parse_args()

loan_type = args.type
principal = args.principal
interest = args.interest
periods = args.periods
payment = args.payment


def plural(number):
    if number > 1:
        return 's'
    return ''


mis = "empty"

if loan_type == 'diff' and principal != mis and periods != mis and interest != mis:
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    summa = 0.0
    i = interest / 1200
    for m in range(1, periods + 1):
        payment = ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
        summa += payment
        print("Month {}: payment is {}".format(m, payment))
    print()
    print("Overpayment = {}".format(int(summa - principal)))
elif loan_type == 'annuity' and interest != mis:
    interest = float(interest)
    if principal != mis and periods != mis:
        principal = float(principal)
        periods = float(periods)
        i = interest / 1200
        payment = ceil(principal * i * pow(1 + i, periods) / (pow(1 + i, periods) - 1))
        print("Your annuity payment = {}!".format(payment))
        print("Overpayment = ".format(payment * periods - principal))
    elif payment != mis and periods != mis:
        payment = float(payment)
        periods = float(periods)
        i = float(interest) / 1200
        principal = ceil(payment * (pow(1 + i, periods) - 1) / (i * pow(1 + i, periods)))
        print("Your loan principal = {}!".format(principal))
        print("Overpayment = ".format(payment * periods - principal))
    elif principal != mis and payment != mis:
        principal = float(principal)
        payment = float(payment)
        i = interest / 1200
        n = ceil(log(payment / (payment - principal * i), 1 + i))
        years, months = n // 12, n % 12
        if years == 0:
            print("It will take {} month{} to repay this loan!".format(months, plural(months)))
        elif months == 0:
            print("It will take {} year{} to repay this loan!".format(years, plural(years)))
        else:
            print("It will take {} year{} and {} month{} to repay this loan!".format(years, plural(years), months, plural(months)))
        overpayment = int(payment * n - principal)
        print("Overpayment = ".format(overpayment))
else:
    print(msg_err)
