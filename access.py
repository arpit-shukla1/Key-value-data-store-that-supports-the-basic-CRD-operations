#!/usr/bin/env python
# coding: utf-8

# In[1]:


import code_for_CRM_operation as z


# In[2]:


z.create("arpit",30)


# In[3]:


z.create("abc",60,3600) 


# In[4]:


z.read("arpit")


# In[5]:


z.read("abc")


# In[6]:


z.create("arpit",50)

#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


# In[7]:


z.modify("arpit",45)
#it replaces the initial value of the respective key with new value 


# In[8]:


z.delete("arpit")
#it deletes the respective key and its value from the database


# In[ ]:


#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

