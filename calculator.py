# There are functions for each operation that takes in a list as an argument
def add(nums):
	return nums[0] + nums[1]

def sub(nums):
	return nums[0] - nums[1]

def multi(nums):
	return nums[0] * nums[1]

def divi(nums):
	return nums[0]/nums[1]

def mod(nums):
	return nums[0] % nums[1]

def tip(nums):
	return nums[0] * (float(nums[1])/100)

# I took the long way to getting the two values from the user input there are better, more efficient ways to do this. 
def getUserValues(prompt):
  user_values = input(prompt)
  index = user_values.find(" ")
  value_1 = int(user_values[:index].strip())
  value_2 = int(user_values[index:].strip())
  values = [value_1,value_2]
  return values

# Using a flag to break the while loop
active = True
while active:
  prompt = "Welcome to 'My First Calculator', Choose you function by selecting a number:"
  prompt += "\n1:Add\n2:Subtract\n3:Multiply\n4:Divide\n5:Modulus\n6:Tip\n7:Quit\n"
  prompt += "What operation would you like to perform? "
  operation = int(input(prompt))
  results_message = "Your result is: "
  # If use is doing addition or multiplication, the order of the numbers doesn't matter
  if operation == 1 or operation == 3:
	  prompt = "Please input two values seperated by a space. The order does not matter.\n"
	  vals = getUserValues(prompt)
	  if operation == 1:
	    print(results_message + str(add(vals)))
	  else:
	   print(results_message + str(multi(vals)))
  elif operation == 2:
    prompt = "Please input two values seperated by a space, where the first value is the number you're subtracting from\n"
    print(results_message + str(sub(getUserValues(prompt))))
  elif operation == 4 or operation == 5:
    prompt = "Please input two values seperated by a space, where the first value is the dividend and the second value is the divisor\n"
    vals = getUserValues(prompt)
    if operation == 4:
	    print(results_message + str(divi(vals)))
    else:
	    print(results_message + str(mod(vals)))
  elif operation == 6:
    prompt = "Please input two values seperated by a space, where the first value is the amount and the second value is the percentage.\n"
    print(results_message + str(tip(getUserValues(prompt))))
  elif operation == 7:
    active = False
    print("Goodbye!")
  else:
    print("Error")
  print("\n")
