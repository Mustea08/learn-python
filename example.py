# print('hello')
# celi_degree = 21
# fer_degree = (celi_degree * 9/5) + 32
# print(fer_degree)

# def say_hello():
#     hello = 'hey'
#     name = 'mustafa'
#     print(hello + " " + name)

# say_hello()

# ======================
# def hello(name):
#     print("hello " + name)

# hello("Eku")
# hello("se")


# def add(number_one, number_two):
#     result = number_one + number_two
#     return result

# total = add(3,7)
# print(total)


#==============
# def converter(celsius):
#     fahrenheit = (celsius * 9 / 5) + 32
#     return fahrenheit
# temp = converter(21.5)
# print(temp)
# #================
# def addition(a,b):
#     message = "the answer is "
#     sum = a+b
#     return message + str(sum)
# result = addition(4,6)
# print(result)

# #===============
# # def convert_temp(celsius):
# #     temp = input("Enter a temperature in degrees Celsius:")
# #     return str(celsius) + " degree is " + str(float(celsius) * 9/5) + str(32) + " Farenheit"
# # weather = convert_temp(0)
# # print(weather)
# #=================
# def convert_temp(celsius):
#     result = celsius * 9/5 + 32
#     return str(celsius) + " degree is " + str(result) + " Farenheit"

# temp = input("Enter a temperature in degrees Celsius:")
# weather = convert_temp(float(temp))
# print(weather)


# #================================
# print("Please enter your name:")

# name = input()

# print("Your name is " + name)

# # name = input("Please enter your name: ")
# # print("Your name is " + name)

# #=====================
# secret_number = 5
# guess = input("Enter a number between 1 and 10: ")
# print(secret_number == int(guess))

#==================================
# secret_word = "Kiwi"
# guess = input('what is the secret word: ')
# print(secret_word == guess)

# #==========================
# guess_num = input('what is the result of 5 + 2? ')
# if guess_num == '7':
#     print('Correct!')

#========================
# secret_number2 = 8
# guess= input('guess a number between 1 to 10: ')

# if secret_number2 == int(guess):
#     print("You got it!")
# else:
#     print("try again")

# print("the program is working")

#==========================
# a = input("Enter a number: ")
# b = input("Enter another number: ")

# if int(a) > 10 and int(b) > 10:
#     print("Both numbers are greater than 10")
# else:
#     print("At least one of the numbers you entered is not greater than 10")

#==========================
d = input("Enter a number between 1 and 20: ")
f = input("Enter a color: ")
number = 8
color = "black"
if int(d) == number and f > color:
    print("Both guesses are correct :)")
elif int(d) == number or f > color:
    print("At least one of the secret you guess")
else:
    print("None of the guesses were correct :(")

print("test done")