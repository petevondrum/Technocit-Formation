# def check_alive(health):
#     if():
#        health < 0:
#         return false
#     else:
#         return true    

# debug: 
# def check_alive(health):
#     if health < 0:
#         return False
#     else:
#         return True
# print(check_alive(10))



def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"

# debug:

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)       
print(greet('Johnny'))


