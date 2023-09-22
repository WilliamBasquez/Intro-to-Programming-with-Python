# Variables, and the flexibility of them (Python)
In python, variables (or placeholders) do not have a default type (number, text, other). Therefore, using them is pretty straightforward. 
For example, if we wanted to store the value `5` in a variable called `age`, we would do that as such:
>`age = 5`

Simple, same applies if we want to store a string (word or phrase), for example:
> `name = "John"`

In python, if we want to see what's inside a variable we can print it (display it on the terminal [more of this later])
```
print(age)
5

print(name)
John
```

The tricky part, comes when we do something like this:

```
age = "Connor"
name = 123
```

and if we print the variables, we get...

```
print(age)
Connor
```

```
print(name)
123
```

Decimal numbers are also something that does not need special treatment, look at this:

`height = 163.4`

This creates a variable that holds the value 163.4 inside, this can be inch, cm, m, km, mm, whatever you want.

Something to keep in mind the name of variables, since we don't know the type of a variable, it's easy to get them confused as time goes on, so we
can use 'camelCase' or using underscore in between words (_) to help us; like this:

Yes )
```
firstName = "John"
tv_height_inches = 40.5
```

No)
```
word = "1234 Street Ave."
temp = 123.4
Something = "1234" 			# avoid using uppercase letter in the first letter
my weight in lbs = 145.5	# white spaces is not allowed
```

'#' in python means comment, something that does not execute.

### Make sure a variable name is meaningful!

Remember how Python has no default variable type? This is called DYNAMIC TYPING, because a variable adjusts its type to whatever you pass it; It can be of type 'number' or 'string' (To see this, we can print the type of a variable by typing: `print(type(age))`)

Other programs, like Java or C/C++/C# are called STATIC TYPED, because in those you do have to specify what type of information you'll be storing in a variable

JAVA
```
int age = 5;			# Notice how 'int' means integer or a whole number
String name = "John";	# Notice how 'String' means a word or phrase
```
One thing that all (of not most) programming languages share, is that strings, for example, are inside the ("/') symbol, single or double quotation marks.

### WORK
1. Assign variables for the following, with appropriate names
	a) The name of an animal
	b) The age of your country
	c) The size of your house (in feet, meters, etc)

# Logic (If, Elif, Else)
Sometimes when we want to make decisions, we ask ourselves: "If it rains today. then I will stay inside and read a book, if it's not, then I will go outside `How can we put this into code?`

Python uses the keywords: if, elif, else to denote this. So, going back to the previous example, we can do this:
```
raining_outside = True
if raining_outside == True:
	print("Stay Inside")
else:
	print("Go Outside")
```

- True means... well true, or yes
- Notice the difference between '=' and '==':
	- `=` assigns things
	- `==` compares things
- Also, notice how the conditional expression (conditional because it's a condition that needs to be met) ends with a `:`

What do you think will be displayed in the screen?
	a) "Stay Inside"
	b) "Go Outside"

The answer is a). If we were to change the line where we set 'raining_outside' and set it to False, then we would get the message "Go Outside".

Sometimes we have more than 2 options, based on different criteria, this is where ELIF comes in.

Let's say that: "If today rains, I will stay inside; If today is sunny, I will play outside; else I will watch TV"

We can transform that sentence into code by doing something like this:
```
weather_today = "cloudy"
if weather_today == "rainy":
	print("Stay Inside")
elif weather_today == "sunny":
	print("Play Outside")
else:
	print("Watch TV")
```

What will be the output when we run the code?
a) "Stay Inside"
b) "Play Outside"
c) "Watch TV"

The answer is c). Because the variable 'weather_today' was not set to either "rainy" or "sunny", the execution of the code falls on the ELSE part.

Combining conditions

At this point we can create some sort of thinking and decision-making in our code, now what happens when there are more than one condition to do something?
For example: "If today rains, and it is after 5pm, I will stay inside". How can we implement this in code? Something like this:

```
weather_today = "rainy"
time_of_day = 17			# 17 in a 24hr clock is the same as 5pm

if weather_today == "rainy" and time_of_day > 17:
	print("Stay Inside")
else:
	print("Go Outside")
```

Here the important part is the connector (and). Python also has the connector 'or'.
```
if weather_today == "rainy" or time_of_day > 17:
	print("Stay Inside")
else:
	print("Go Outside")
```

### WORK
1. Transform the following sentences to code:
	a) If I am tired today, I will stay inside
	b) If it's after 3pm and it is sunny outside, I will visit my friend
	c) If today is Monday or Wednesday, I will do homework, otherwise I will watch TV
	d) If tomorrow is Saturday and Sunday, I will call my grandma, otherwise if tomorrow is Monday, I will can the doctor, Other than that, I will call my parents

# Loops
Remember when we had to write a sentence multiple times in a sheet of paper when we didn't do our homework? It looked something like this:

"I will do my homework everyday and I will not forget it at home"
"I will do my homework everyday and I will not forget it at home"
"I will do my homework everyday and I will not forget it at home"
"I will do my homework everyday and I will not forget it at home"
								...

It was exhausting! But what if I tell you there is a faster way to do this?

If we think about it, this is nothing more than a loop, something that repeats until a condition is met (in this case, writing this phrase 100 times).

There are 3 main types of loops, although Python only uses 2
1. WHILE loop
2. FOR loop
*DO-WHILE loop

In a while loop, we are performing an action WHILE a condition is True. For example, we can wash the dishes until they're all clean, how would this look in code?...
```
unwashed_dished = 10
while unwashed_dished != 0:					# '!=' means 'does not equal'
	print("Washing the dishes")
	unwashed_dishes = unwashed_dishes - 1	# After we wash a dish, the number of unwashed dishes goes down by one
```

This code will repeat until the number of unwashed dishes reaches 0, in which case the condition "unwashed_dishes != 0" becomes False, therefore the loop exits (stops).

We need to be careful when using while loops, because if we do not update the checked variable, we can run into an infinite loop (a loop that does not stop, it will stop eventually because nothing is truly infinite)
and you will get an error or get stuck in execution.

We could write the phrase manually 100 times, or we can use a loop to write it for us...

In a for loop, we are performing an action FOR as long as we set. For example, going back to the dishes example, we can also write the loop like this:
```
for i in range(10):
	print("Washing the dishes")
```

Something to notice is that *for* loops start at 0 and not at 1, this is why the number inside RANGE is exclusive, because it goes from 0, 1, 2, ..., 9 which is 10 numbers (including 0)!

You'll notice that this is more compact, and that is uses things like "i", "in", "range". I will explain this quickly:

* i :    This is the name of a variable that exists inside the loop, think of it as our checked variable, we can name it whatever we want, so let's do that to avoid confusion and allow further comparison.
* in:    This could also be interpreted as "is in", or "belongs to", "is inside".
* range: Length of units (could be numbers or objects [more of this later]).

To avoid confusion and see comparison between a for and while loop...

#### WHILE
```
unwashed_dished = 10
while unwashed_dished != 0:
	print("Washing the dishes")
	unwashed_dishes = unwashed_dishes - 1
```

#### FOR
```
for unwashed_dish in range(10):
	print("Washing the dishes")
```
We can write pretty much any WHILE loop as a FOR loop, and we can write pretty much any FOR loop as a WHILE loop
(behind the scenes, a for loop is actually a while loop; a while loop is the second-most basic form of a loop [we'll touch on recursion later])

We can do some pretty cool things with loops and conditional statements, for example:

* "If a number from 0 to 100 [inclusive] is divisible by 5, print the number and the word "Five"

WHILE
```
while result <= 100:
	if (result % 5) == 0:		# If the remainder of a division is 0, then we can say a number is divisible by another (% means remainder)
		print(result)
		print("Five")
	result = result + 1
```
FOR
```
for result in range(101):		# in for loops, the number inside 'range' is exclusive, so we add 1 to this number to make it 100 inclusive
	if (result % 5) == 0:
		print(result)
		print("Five")
```

After running the code, we can see that only multiple of 5 are printed along with the word "Five".

### WORK 
1. Do the following in both a while and a for loop:
	a) If a number from 0 to 100[exclusive] is divisible by 3 and 5, print that number.
	b) If a number from 0 to 10[inclusive] is bigger than 50 when you multiply it times itself, print "Big", else, print "Small"
	c) ONLY WHILE LOOP: if a number (i) is less than 3, multiply it times 2, else if it's bigger than 3 but smaller than 7, multiply it times 3, else subtract 1 from it

# Functions
Now, what if we could have several lines of code and we need to repeat some actions, but you don't want to write the same code several times, this is where functions come in handy.

Funtions are reusable pieces of code that execute actions and return some result. For example, if we want to repeat a text multiple times but we do not repeat the same text, instead of writing the same loop with different texts, like this:
```
literature_text = "I will do my homework always, and don't forget it at home

# Write this 100 times
for i in range(100):
	print(literature_text)

history_text = "I will do my assigned project and work with my teammates"

# Write this 50 times
for i in range(50):
	print(history_text)

science_text = "I will not fight with my teammates for project credit"

# Write this 80 times
for i in range(80):
	print(science_text)
```

Instead of doing this, we can write a function to do this for us!

Functions have this syntax:
```
def 'function name' ('arguments'):
```

So in our example, we would write the function as such:
```
def repeat_text(text, times):
	for i in range(times):
		print(text)
```

Then, we just call the function and we "pass" the right arguments to the function!

```
literature_text = "I will do my homework always, and don't forget it at home
repeat_text(literature_text, 100)

history_text = "I will do my assigned project and work with my teammates"
repeat_text(history_text, 50)

science_text = "I will not fight with my teammates for project credit"
repeat_text(science_text, 80)
```

We can also use functions to return values when needed. For example,

```
def return_multiplication(a, b):
	return a * b

def return_summation(a, b):
	return a + b
```

One thing that is pretty neat, is that you can ask for user input, which is how we interact with the code.

If we want to write a simple greeter, we can write something like this:
```
def salutation(name, text="Welcome, "):
	print(text, name)
```

You may be wondering why one argument has a '=' symbol, this just means that we assign a default value to a variable; and we can call this function like this:

```
salutation("John")						# "Welcome, John"
salutation("John", "Hello There")		# "Hello There, John"
```

But we cannot call it like this:
```
salutation()
```

This will result in a problem, because the variable `name` does not have a default value!!

We can then take user input like this:
```
name = input("What is your name: ")

salutation(name)

# Or something like this

name = input("What is your name: ")
text = input("What would you like to say: ")

salutation(name, text)
```
You can notice that `input` is a function, but we don't know how it works behind the scenes, and that's ok. Another example of a function (As you can remember) is `range` for loops.

### Work (Taken from Harvard's 'Intro to Programming with Python' course)
1. Write a function that computes the result of Einstein's energy equation:
	- E = mc^2^ 
		- (c^2^ is the same as c * c)
2. Complete the code provided to create a simple tip calculator
	```
	def main():
	    dollars = dollars_to_float(input("How much was the meal? "))
	    percent = percent_to_float(input("What percentage would you like to tip? "))
	    tip = dollars * percent
	    print(f"Leave ${tip:.2f}")


	def dollars_to_float(d):
    # TODO


	def percent_to_float(p):
    # TODO


	main()
	```

# Project
- Write a code that converts a number in lbs to kg
	- Use functions!
- Write a code that converts a number in Celsius to Fahrenheit
	- Use functions!
- Complete the code that tries to guess a number
	- You should not change the code provided, but you can add as much code as you want
