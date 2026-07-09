# Solve the following programming tasks:

# Lists*

#Find the largest number in a list.
#Find the second largest number.
#Remove duplicate values from a list.
#Reverse a list without using built-in reverse().
#Find common elements between two lists.
print( "===========Lists============")
l1= [3, 5, 7, 2, 88, 5, 3, 9]
l2= [1, 2, 3, 4, 5, 6, 7, 8, 9]    
print(max(l1))  # Find the largest number in a list.
l1.sort(reverse=False)
print(l1[-2])  # Find the second largest number in a list.
unique_list = list(set(l1))  # Remove duplicate values from a list.
print(unique_list)
print(l1[::-1])  # Reverse a list without using built-in reverse().
u_set1 = set(l1)
u_set2 = set(l2)
common_elements = list(u_set1 & u_set2)  # Find common elements between two lists.
print(common_elements)



#Tuples

# Count occurrences of an element.
# Convert a tuple into a list and vice versa.
print("============Tuples=============")
t1 = (1, 2, 3, 4, 5,4, 3, 2, 1)
print(t1.count(3))  # Count occurrences of an element.
l1 = list(t1)  # Convert a tuple into a list.
print(l1)
print(type(l1))
t2 = tuple(l1)  # Convert a list into a tuple.
print(t2)
print(type(t2))



#Sets

#Find unique values from a list.
#Perform union and intersection operations.

print("============Sets=============")
l1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
unique_values = list(set(l1))  # Find unique values from a list.
print(unique_values)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
union_result = s1 | s2  # Perform union operation.
intersection_result = s1 & s2  # Perform intersection operation.
print(union_result)
print(intersection_result)



#Dictionaries

#Create a student record dictionary.
#Calculate average marks of students.
#Count frequency of words in a sentence.

print("============Dictionaries=============")
student_record = {                # Student Records
    "name": "John Doe",
    "age": 20,
    "marks": [85, 90, 78, 92]
}
print(student_record)
print("Average marks:", sum(student_record["marks"]) / len(student_record["marks"]))  #Find average marks of students.
sentence = "This is a sample sentence. This sentence contains some repeated words."   # Count frequency of words in a sentence.
word_frequency = {}
for word in sentence.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("Word frequency:", word_frequency)