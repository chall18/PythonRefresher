course = "Python for Beginners"
print(len(course)) #num of chars in string
print(course.find('n')) #returns first instance of char in the string
print(course.find("Beginners")) #returns index where the substring begins in the parent string
print(course.replace("Beginners", "Blah")) #replace one substring with another

print("Python" in course) #Returns boolean value based on whether string contains given substring
print("Foo" in course)