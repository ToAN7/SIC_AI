# ax + b = 0
while True:
    try: # try code if it may have errors
        a = float(input('a =  '))
        b = float(input('b =  '))
    except ValueError as ex: # run the follow-up code when try got errors
        temp = str(ex)
        while temp[0] != "\'":
            if temp != "\'":
                temp = temp.replace(temp[0],"",1) 
        print(f"Day la loi do ban da nhap: {temp}")
    else: # run when code are not throw any exceptions
    # improving code by not using ()
        if a == 0: 
            if b == 0:
                print("PT vo so nghiem")
            else:
                print("PT vo nghiem")
        else:
            print('x = ', -b/a)
        break
    finally: # run when try end smoothly
        print("Done!!!")

# List - mutable
e = [1, True, 'a', "b", """d""", '''c''']
print(len(e))

# Tuple - immutable/Read-only
f = (0, 786, 34.432432, "12", "hELLA")
print(f[:-1])

# Set
g = {a,b,"greeting"}
print(g)

# Dictionary
dict = {
    "name": 'Chau Duc Toan',
    "year": 2002
}
print(dict)
print(dict["year"])