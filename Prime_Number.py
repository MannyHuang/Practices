
# coding: utf-8

# In[1]:


y = [2]
for x in range(2,10):
    for i in range(2,x):
        if x%i == 0:
            break
        else:
            y.append(x)
print(list(set(y)))


# 9不是质数，错误原因：没有实践循环中的算法
# 

# In[ ]:


p = [i for i in range(2, 10000) ]
for i in range(3, 10000):
    for j in range(2, i):
        if i % j == 0:
            p.remove(i)
            break
print(p)
print('\n10000以内的质数有' + str(len(p)) + '个')


# 优化方法：p排除偶数
