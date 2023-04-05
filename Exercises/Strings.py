# 1. Create a variable that contains a message and print it out to the screen.
message = "Let's get started"
# print(message)
# 2. Create a variable that can contain a customer's name and print a message to that customer.
first_name = "Robert"
last_name = "Young"
full_name = first_name + " " + last_name
# print(full_name)
# 3. With the customer name variable created above apply the case methods that we used in this lesson, title(), upper(), lower()
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
# 4. Print to the screen a string that contains single and double quotes.
print("Yo, what's going on?")
print('Nothing I can tell')
# 5. Create a variable with additional whitespace and using Python's lstrip(), rstrip(), and strip() methods to remove it.
var1 = "      Can you tell"
print(var1)
print(var1.lstrip())

var2 = "What about now?      "
print(var2)
print(var2.rstrip())

var3 = "     finally, here       "
print(var3)
print(var3.strip())