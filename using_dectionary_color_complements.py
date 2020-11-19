color_complements = {
     'red' : 'green',
     'green' : 'red',
     'blue' : 'orange',
     'orange' : 'blue',
     'yellow' : 'purple',
     'purple' : 'yellow'
}
user_color = input("plesae inter a color: ")
if user_color not in color_complements:
    print("sorry ..")
else:
    print(f" the complement of {user_color} is {color_complements[user_color]}")
    
