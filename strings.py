course = 'Python for Beginners'
print(course)
print(course[0]) #string is treated as array of char
print(course[-1]) #prints last char in string
print(course[-2]) #Now we're basically just counting chars to point to from the right instead of left
print(course[0:3]) #print 3 chars starting from index 0, so 0-2
print(course[0:]) #if no end index is given, print from 0 to end of string
print(course[2:]) #print starting from index 2 to end of string
print(course[:5]) #if no beginning index given, assume 0 and 5 chars, so 0-4

another = course[:] #creates a copy
print(another)

