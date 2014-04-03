# Exercises for chapter 2:

# Name: Caitlin Riggs


# Exercise 2.1
'''
zipcode = 02492 
zipcode should be saved as a string, otherwise Python will
read the zip as a base 8 number. 
'''

# Exercise 2.2
'''
The Python interpreter in the command line outputs each line individually
as the line is typed and returned. Typing in these 3 lines and running a 
script does not output anything because the answer has neither been saved
in a variable nor printed to the screen.
'''

# Exercise 2.3
'''
width = 17
height = 12.0
delimiter = '.'

1. width/2 >>		8
2. width/2.0 >>		8.5
3. height/3 >>		4.0
4. 1 + 2 * 5 >>		11
5. delimeter * 5 >>	'.....'
'''

# Exercise 2.4
print "Exercise 2.4.1"
'''
1. The volume of a sphere with radius r is (4/3)pir^3. What is the volume of a 
sphere with radius 5? Hint: 392.7 is wrong!
'''
import math
r = 5
volume = (4.0 / 3.0) * math.pi * (r ** 3)
print "The volume of the sphere in Exercise 2.4 is: %s" %volume
print '' #break between exercises

print "Exercise 2.4.2"
'''
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% 'discount. 
Shipping costs $3 for the first copy and 75 cents for each additional copy. What is 
the total wholesale cost for 60 copies?
'''
pricePerBook = 24.95
discount = 0.40
copies = 60

def bookPrice(pricePerBook, discount, copies):
	costAfterDiscount = pricePerBook - (pricePerBook * discount)
	return costAfterDiscount * copies

def shippingCost (copies):
	firstBook = 3.0
	remainingBooks = (copies - 1) * 0.75
	return firstBook + remainingBooks

def totalPrice ():
	return bookPrice(pricePerBook, discount, copies) + shippingCost(copies)

print "The cost of %s books with shipping is $%s." %(copies, totalPrice())
print '' #break between exercises

print "Exercise 2.4.3"
'''
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do 
I get home for breakfast?
'''
import datetime #Not sure how to add non-base 10 numbers with python. Import datetime?
				#Or compute numbers out of 60?


