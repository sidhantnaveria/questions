# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:34:31 2020

@author: sidhant
"""
#### Question 2
#### assumption: no duplicate numbers in the list
lst=[3,5,8,6,10,9,2,11]

k=3
lst.sort()
new_list=[]
for i in range(len(lst)):
#    x=i+1
    print("")
    for x in range(i+1,len(lst)):
        
        if lst[i]-lst[x]==k or lst[i]-lst[x]==-k:
           new_list.append((lst[i],lst[x]))
           break
print("Number of pairs: ",len(new_list))   
print("\n Pairs: ",new_list)   
###################################################################################################
           
###### question 3
import itertools
          
data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
("usernameA","phone_numberZ", "emailA"),
("usernameB","phone_numberB", "emailB"),
("usernamec","phone_number1", "emailc"),
]

#print(len(data))
main_list=[]

for i in range(len(data)):
    test_list=[]
    test_list.append(i)
    
    for j in range(i+1,len(data)):
        
        if data[i][0] in data[j] or data[i][1] in data[j] or data[i][2] in data[j]:
            test_list.append(j)
    
    main_list.append(test_list)        
            
            

L=main_list

LL = set(itertools.chain.from_iterable(L)) 

for each in LL:
  components = [x for x in L if each in x]
  for i in components:
    L.remove(i)
  L += [list(set(itertools.chain.from_iterable(components)))]
print(L)
