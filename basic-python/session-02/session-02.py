# This is the first program we are learning from ...
# print("Hello, World!")
# todo : global and local variables


n1 = 56
n1 = "John"

name = "Ali"


x = [1, 2, 4]

y = range(1, 10)

n = True

y = 4+2j

a = "   jjdgjasdgjasdh   "


name = "Shyda"
family = "Ahmadi"
# print ("Please write the name: ", name, " and write the family: ", family)

# print("Please write the name: {} and write the family: {}".format(name,family))

x = {"Name": "Shiva", "Family": "Ahmadi"}

x["Name"] = "Shyda"
# print(x.get("Name"))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
# print(thisdict)


# function

def add_numbers(n1, n2, n3):
    '''
    This is a function that gets 3 numbers and give you the sum of them as a result
    '''
    result = n1+n2+n3
    print(result)


def print_fullname(name, family):
    '''
    This function print your full name.
    '''
    # print("My fullname is {} {}".foramt(name , family) )
    print("My fullname is ", name, family)

# print_fullname("Shiva", "Ahmadi")


command = "no"
while command == "no":
    n = input("Please enter your name: ")
    f = input("Please enter family name: ")

    print_fullname(n, f)

    command = input("Do you want to stop the function: (no/yes)")
