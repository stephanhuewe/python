# Creating a List 
List = [1, 2, 3, 4, 5, 6,  
        7, 8, 9, 10, 11, 12, 'hallo'] 
print("Intial List: ") 
print(List) 

# Single elements
print(List[0]) 
print(List[-1]) 

print("Adding a new one at the beginning")
List.insert(0,"Foo")
print(List) 
 
# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 
  
# Removing elements from List 
# using iterator method 
for i in range(1, 5): 
    List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 

#Multi Lists
# Creating a Multi-Dimensional List 
List = [['Student', 'Studentin'] , ['Studenten']] 
  
# accessing an element from the  
# Multi-Dimensional List using 
# index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1]) 
print(List[1][0]) 
# print(List[1][1]) # Peng 


# Python program to illustrate 
# enumerate function in loops 
l1 = ["eat","sleep","repeat"] 
  
# printing the tuples in object directly 
for ele in enumerate(l1): 
    print(ele) 
print 

# changing index and printing separately 
for count,ele in enumerate(l1,100): 
    print (count,ele)
    
    
# dictionary
woerter = {"house" : "Haus", "cat":"Katze", "black":"schwarz"}
print (woerter["house"])
print (woerter["cat"])

# add
woerter["Farbe"] = "color"

#print key
for key in woerter:
	print(key)

#print value
for value in woerter:
    print(value)
	
#print all
for item in woerter.items():
    print(item)
