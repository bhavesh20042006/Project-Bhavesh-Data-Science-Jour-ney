programming_dictionary ={
    "Bug": "An error in a program that prevents the program from running as expected.",
     "Function": "A piece of code that you can easily call over and over again." }
print(programming_dictionary["Bug"])



programming_dictionary["loop"] = "the action of doing something again and again"
print(programming_dictionary)
#this shows that dictionaries in python are mutable and can be changed.



programming_dictionary["bug"] = "i changed the definition."
print(programming_dictionary)
#and dictionaries can be edited.



for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])