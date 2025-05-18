def madlib():

    name = input("enter your name:")
    father_name = input("enter your father name:")
    mother_name = input("enter your mother name:")
    age = input("enter your age:")

    gender = input("ender your gender MALE/FEMALE:")
    to_get_siblingsinfo = input("do you have siblings yes/no:")

    if to_get_siblingsinfo=="yes":
        sister_name = (input("enter your sister name:"))
        brother_name = input("enter your brother name:")
        madlib = f"hey hi i am {name} , and my father name is {father_name} and my mother name is {mother_name} and i my age is {age} years old and i have a sister her name is {sister_name} and i have a brother his name is {brother_name}"
        print(madlib)
    else:
        madlib= f"hey hi i am {name} , and my father name is {father_name} and my mother name is {mother_name} and i am {age} years old"
        print(madlib)
    
