name = input("What is your name")
print (name)
age = int(input("What is your age"))
print (age)
color = input("What is your favorite color")
print (color)
if age < 13:
	age_comment = "You are a child."
elif age < 20:
	age_comment = "You are a teenager."
elif age < 65:
	age_comment = "You are an adult."
else:
	age_comment = "You are a senior."

print("Hello " + name + ", you are " + str(age) + " years old. " + age_comment)
print("Your favorite color is " + color + ".")