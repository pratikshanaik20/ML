age_input=input("Enter your age:")
age=int(age_input)
if age<0:
    print("Please enter a valid age")
elif age<18:
    print("you are minor")
elif age>=18 and age<65:
    print("you are an adult")
elif age>65 and age<=120:
    print("you are senior citizen")
else:
    print("invalid")



#     #import keywoed
# import keyword
# print("The list of keyword are:")
# print(keyword.kwlist)
