#!/usr/bin/env python
# coding: utf-8

# In[ ]:


19520417 - Võ Quốc Bình


# In[ ]:


1. a)


# In[1]:


1 + 1


# In[2]:


1 * 3


# In[3]:


1 / 2 


# In[4]:


2 ** 4


# In[5]:


4 % 2


# In[6]:


5 % 2


# In[7]:


(2 + 3) * (5 + 5)


# In[ ]:


1.b)


# In[10]:


name_of_var=2


# In[16]:


x = 2
y = 3


# In[17]:


z = x + y


# In[18]:


z


# In[ ]:


1.c)


# In[19]:


'single quotes'


# In[20]:


"double quotes"


# In[22]:


" wrap lot's of other quotes"


# In[ ]:


1.d)


# In[23]:


x = 'hello'


# In[24]:


x


# In[25]:


print(x)


# In[27]:


num = 12
name = 'Sam'


# In[28]:


print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))


# In[30]:


print('My number is: {}, and my name is: {}'.format(num,name))


# In[ ]:


1.e)


# In[31]:


[1,2,3]


# In[32]:


['hi',1,[1,2]]


# In[33]:


my_list = ['a','b','c']


# In[34]:


my_list.append('d')


# In[35]:


my_list


# In[36]:


my_list[0]


# In[37]:


my_list[1]


# In[38]:


my_list[1:]


# In[39]:


my_list[:1]


# In[41]:


my_list[0] = 'NEW'


# In[43]:


my_list


# In[44]:


nest = [1,2,3,[4,5,['target']]]


# In[45]:


nest[3]


# In[46]:


nest[3][2]


# In[47]:


nest[3][2][0]


# In[ ]:


1.f)


# In[48]:


d = {'key1':'item1','key2':'item2'}


# In[49]:


d


# In[50]:


d['key1']


# In[ ]:


1.g)


# In[51]:


True


# In[52]:


False


# In[ ]:


1.h)


# In[53]:


t = (1,2,3)


# In[54]:


t = (1,2,3)


# In[55]:


t[0]


# In[57]:


t[0] = 'New'


# In[ ]:


1.i)


# In[58]:


{1,2,3}


# In[59]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# In[ ]:


1.j)


# In[61]:


1 > 2


# In[62]:


1 < 2


# In[63]:


1>=1


# In[64]:


1<=4


# In[65]:


1==1


# In[66]:


'hi' == 'bye'


# In[ ]:


1.k)


# In[67]:


(1 > 2) and (2<3)


# In[68]:


(1>2) or (2<3)


# In[69]:


(1==2) or (2==3) or (4==4)


# In[ ]:


1.l)


# In[71]:


if 1<2: print('Yep!')


# In[74]:


if 1 < 2: print ('first')
else: print('last')


# In[75]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[76]:


if 1 == 2:
    print('first')
elif 3 ==3:
    print('middle')
else:
    print('last')
    


# In[ ]:


1.m)


# In[77]:


seq = [1,2,3,4,5]


# In[78]:


for item in seq:
    print(item)


# In[79]:


for item in seq:
    print('Yep')


# In[80]:


for jelly in seq:
    print (jelly+jelly)


# In[ ]:


1.n)


# In[81]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i + 1


# In[ ]:


1.o)


# In[82]:


range(5)


# In[83]:


for i in range(5):
    print(i)


# In[84]:


list(range(5))


# In[ ]:


1.p)


# In[85]:


x = [1,2,3,4]


# In[86]:


out = []
for item in x:
    out.append(item **2)
print (out)


# In[87]:


[item ** 2 for item in x]


# In[ ]:


1.q)


# In[88]:


def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print (param1)


# In[89]:


my_func


# In[90]:


my_func()


# In[91]:


my_func('new param')


# In[92]:


my_func(param1='new param')


# In[93]:


def square(x):
    return x **2


# In[94]:


out = square(2)


# In[95]:


print(out)


# In[ ]:


1.r)


# In[96]:


def times2(var):
    return var*2


# In[97]:


times2(2)


# In[98]:


lambda var: var * 2


# In[ ]:


1.s)


# In[99]:


seq = [1,2,3,4,5]


# In[100]:


map(times2, seq)


# In[101]:


list(map(times2,seq))


# In[102]:


list(map(lambda var: var * 2, seq))


# In[103]:


filter(lambda item: item%2 == 0, seq)


# In[104]:


list(filter(lambda item: item% 2 == 0, seq))


# In[ ]:


1.t)


# In[105]:


st = 'hello my name is Sam'


# In[106]:


st.lower()


# In[107]:


st.upper()


# In[108]:


st.split()


# In[109]:


tweet = 'Go Sports! #Sports'


# In[110]:


tweet.split('#')


# In[111]:


tweet.split('#')[1]


# In[112]:


d


# In[113]:


d.keys()


# In[114]:


d.items()


# In[115]:


lst = [1,2,3]


# In[116]:


lst.pop()


# In[118]:


lst


# In[119]:


'x' in [1,2,3]


# In[120]:


'x' in ['x', 'y','z']


# In[ ]:




