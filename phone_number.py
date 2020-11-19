'''
Anas Albedaiwi
albedaiwi1994@gmail.com
'''

def _check_first_format(phone_number):
    if len(phone_number) < 14:
        return False
    if phone_number[0] == '(' and phone_number[4] == ')' and phone_number[5] == ' ' and phone_number[9] == '-':
        digits= [1, 2, 3, 6, 7, 8, 10, 11, 12, 13]
        for d in digits:
            if not phone_number[d].isdigit():
                return False
            return True
        else:
            return False
        def _check_second_format(phone_number):
            if len(phone_number) < 12:
                return False
            if phone_number[3] == '-' and phone_number[7] =='-':
                digits = [0, 1, 2, 4, 5,6, 8, 9, 10, 11]
                for d in digits:
                    if not phone_number[d].isdigit():
                        return False
                    return True
                else:
                    return False
                def _convert_first_to_second(phone_number):
                    digits = [1, 2, 3, 6, 7, 8, 10, 11, 12, 13]
                    new_number = ''
                    dash = [3, 7]
                    counter = 0
                    for d in digits:
                        new_number+=phone_number[d]
                        counter+=1
                        if counter in dash:
                            new_number += '-'
                            return new_number
                        def standardize_phone_number(phone_number):
                            if _check_second_format(phone_number):
                                return phone_number
                            if _check_first_format(phone_number):
                                return _convert_first_to_second(phone_number)
                            return None
                        print(standardize_phone_number('(123) 456-7890'))
                        print(standardize_phone_number('123-456-7890'))
