# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-5
# Topic  :-
# Take input from the user of 5 numbers and store it in a list.
# Perform below operations:
# 1) Calculate the sum of all the elements in the list
# 2) Find the smallest number
# 3) Find the largest number
# 4) Display list in ascending order
# 5) Display list in descending order
# 6) Convert list into tuple
# 7) Delete the list
# Date   : 19-06-2023

# Program:-
List=[];
print("Enter 5 numbers:-");
for i in range(5):
    n=int(input("Enter no. {} : ".format(i+1)))
    List.append(n);
print();

print("List =",List);
print();

print("Sum of all the elements in the 'List' :",sum(List));
print();

print("The smallest number in 'List' :",min(List));
print();

print("The largest number in 'List'  :",min(List));
print();

List.sort();
print("Displaying 'List' in ascending order  := List =",List);
print();

List.sort(reverse=True);
print("Displaying 'List' in descending order := List =",List);
print();

# OR [After 'List.sort()']:-
# print("Displaying 'List' in descending order := ",List.reverse());
# print();

print("After convertion of 'List' into tuple :=",tuple(List));
print();

del List;
# print(List); #-> NameError: name 'List' is not defined.
# print();

# Output:-
# Enter 5 numbers:-
# Enter no. 1 : 9
# Enter no. 2 : 6
# Enter no. 3 : 7
# Enter no. 4 : -4
# Enter no. 5 : 0

# List = [9, 6, 7, -4, 0]

# Sum of all the elements in the 'List' : 18

# The smallest number in 'List' : -4

# The largest number in 'List'  : -4

# Displaying 'List' in ascending order  := List = [-4, 0, 6, 7, 9]

# Displaying 'List' in descending order := List = [9, 7, 6, 0, -4]

# After convertion of 'List' into tuple := (9, 7, 6, 0, -4)