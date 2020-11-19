'''
Anas Albedaiwi

'''

def number_to_word(number):
    FD = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
          6:'six', 7:'seven', 8:'eight', 9:'nine'}
    SD = {10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
          60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    teens = {11:'eleven', 12: 'twelve', 13:'thirteen', 14:'fourteen',
             15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
             19:'nineteen'}
    if number in FD:
        return FD.get(number)
    elif number in SD:
        return SD.get(number)
    elif number in teens:
        return teens.get(number)
    else:
        return None
