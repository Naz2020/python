'''
Anas Albedaiwi
'''

def displayProgramTitle(firstName, lastName):
    print(f' Display Month Program by {firstName} {lastName}')
    
    
def displayList(ListName, List):
    print(ListName)
    
    for element in List:
        print(format(element))
        
        
def main():
    monthsOfYear = [' January',
                    ' February',
                    ' March',
                    ' April',
                    ' May',
                    ' June',
                    ' July',
                    ' August',
                    ' September',
                    ' October',
                    ' November',
                    ' December']
    displayProgramTitle('Anas','Albedaiwi')
    displayList('Months of Year:',monthsOfYear)
    print(' Display Months program completed')
    
if __name__ == '__main__': main()
