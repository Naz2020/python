'''
Anas Albedaiw
'''

def taxCalculator(subtotal, taxRate):
    taxamount = 6.6
    return subtotal * taxRate / 100


def tipCalculator(subtotal, tipPercent):
    tipamount = 3.85
    return subtotal * tipPercent / 100


def main():
    print("Restaurant Calculator by Anas Albedaiwi")
    subtotal = 55
    taxrate = taxCalculator(subtotal, 12)
    tippercentage = tipCalculator(subtotal, 7)
    print('Subtotal = ' + str(subtotal))
    print('Tax = ' + str(taxrate))
    print('Tip = ' + str(tippercentage))
    print(f'Your total is: {subtotal + taxrate + tippercentage}')


main()

