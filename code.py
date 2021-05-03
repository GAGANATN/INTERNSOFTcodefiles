#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Integers
x=1
type(x)


# In[ ]:


#float
x=0.1
type(x)


# In[ ]:


#boolean 
b1= True
b2= False


# In[ ]:


#string
name= 'your name'
type(name)


# In[ ]:


#complex num
x=1.0-2.0j
type(x)
print(x)
print(x.real,x.imag)


# In[ ]:


#defining assignments
tenth=10
two=2
print(tenth)
print(two)


# In[ ]:


#dynamic typing
ten=10
ten
ten="ten"
ten


# In[ ]:


#string typing
"day"+ "1"


# In[ ]:


'day' + str(1)


# In[ ]:


#boolean evaluation
'a' is 'a'


# In[ ]:


i=3
if i<3:
    print('less than 3')
elif i<5:
    print('less than 5')
else:
    print('5 or more')


# In[ ]:


#lists
l=[]
l


# In[ ]:


l= list()
l


# In[ ]:


l=['a','b','c']
print(l)
type(l)


# In[ ]:


l=['a',6]
l


# In[ ]:


l2= list(l)
l2


# In[ ]:


list('abcdef')


# In[ ]:


l=[1,2]
print(l)
l.append ('b')
print (l)
l.append ('c')
print(l)
l.insert(1,56)
l


# In[ ]:


for i in l:
    print(i)


# In[ ]:


#program to find sum of all num
num=[6,5,3,8,4,2,5,4,9]
sum=0
for i in num:
    sum=sum+i
print('the sum is',sum)
sum


# In[ ]:


digits=[0,1,5]
for i in digits:
    print(i)
else:
    print("no items left.")


# In[2]:


#while loop to add n num
n= int(input("Enter n:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum is",sum)


# In[4]:


#range()
print (range(10))


# In[5]:


print (list(range(10)))


# In[7]:


print (list(range(2,8)))


# In[8]:


print (list(range(2,20,5)))


# In[9]:


genre=['pop','rock','jazz','sapna']
for i in range(len(genre)):
    print("i like",genre[i])


# In[18]:


#break
for val in "HARSHITHA":
    if val=="I":
        break
    print (val)
print('The end')


# In[21]:


#continue
for val in "HARSHITHA":
    if val== "I":
        continue
        print (val)
print("the end")


# In[27]:


#to take i/p string from user
name=input("what is your name?\n")
type(name)


# In[28]:


#to read int from user
age=int(input("what is your age?\n"))
print("your age is",age)
type(age)


# In[30]:


#example
name= input("what is your name?")
print("it was nice talking to you"+name+"!")
age=input("enter your age?")
print("hey,you are already" + age + "years old," + name +"!")


# In[ ]:




