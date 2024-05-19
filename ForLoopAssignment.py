#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1.  Explain with an example each when to use a for loop and a while loop. 


# In[ ]:


'''FOR LOOP:
In Python, a ‘for loop‘ is used to iterate over a sequence of items, such as a Python tuple, list, string, or range. The loop will execute a block of statements for each item in the sequence.
Syntax:
for var in iterable:
    #statements
Example of for loop:Print numbers from 1 to 10:
for i in range(10):
      print(i)
      
WHILE LOOP:
In Python, a while loop is used to repeatedly execute a block of statements while a condition is true. The loop will continue to run as long as the condition remains true.
Syntax:
while condition:

    # Set of statements
    
Example of while loop:Print numbers from 1 to 10:
i=1
while i<=10:
     print(i)
     i=i+1
'''


# In[2]:


#Q2.  Write a python program to print the sum and product of the first 10 natural numbers using for  and while loop. 


# In[4]:


#sum and product of first 10 natural numbers using for loop
sum=0
product=1
for i in range(1,11):
    sum=sum+i
    product=product*i
print('Sum of 10 natural numbers:',sum)
print('Product of 10 natural numbers:',product)


# In[5]:


#sum and product of first 10 natural numbers using while loop
i=1
sum=0
product=1
while i<=10:
    sum=sum+i
    product=product*i
    i=i+1
print('Sum of 10 natural numbers:',sum)
print('Product of 10 natural numbers:',product)
    


# In[ ]:


'''Q3. Create a python program to compute the electricity bill for a household. 
The per-unit charges in rupees are as follows:
    For the first 100 units, the user will be charged Rs. 4.5 per  unit, for the next 100 units,
    the user will be charged Rs. 6 per unit, and for the next 100 units, the user will  be charged Rs. 10 per unit,
    After 300 units and above the user will be charged Rs. 20 per unit. '''


# In[9]:


units=int(input('Enter units of electricity'))
if units<=100:
    bill=4.5*units
    print("Your electricity bill is:",bill)
elif units>100 and units<=200:
    bill=(100*4.5)+6*(units-100)
    print("Your electricity bill is:",bill)
elif units>200 and units<=300:
    bill=10*(units-200)+(100*4.5)+(100*6)
    print("Your electricity bill is:",bill)
else:
    bill=20*(units-300)+(100*4.5)+(100*6)+(100*10)
    print("Your electricity bill is:",bill)


# In[ ]:


'''Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each  number
and if the cube of that number is divisible by 4 or 5 then append that number in a list and print  that list. 
'''


# In[11]:


#For loop
l=[]
for i in range(1,101):
    cube=i**3
    if cube%4==0 or cube%5==0:
         l.append(cube)
l


# In[13]:


#while loop
i=1
l=[]
while i<=100:
    cube=i**3
    if cube%4==0 or cube%5==0:
        l.append(cube)
    i=i+1
l
    


# In[ ]:


'''Q5.  Write a program to filter count vowels in the below-given string. 
string = "I want to become a data scientist" '''


# In[21]:


s="I want to become a data scientist"
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count=count+1
print('Number of vowels:',count)


# In[ ]:




