# # Write a program in Codeboard that uses a function to reverse a string (this function needs to use a return)
# # and then a function that prints the output of the first function.
# #Use split, reverse, and join properties to reverse the string)
string = "This is the song the song that never ends and it goes on and on my friends!"


def reverse():
    global string
    user = string[::-1]
    print(user)


reverse()
