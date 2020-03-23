#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread( './stereo-imgs/r-1316653677.431323-2838369375.ppm', cv2.IMREAD_UNCHANGED )
depth = cv2.imread( './stereo-imgs/d-1316653648.611579-1109571627.pgm', cv2.IMREAD_UNCHANGED )


# In[3]:


plt.imshow( img )
plt.show()


# In[4]:


plt.imshow( depth )
plt.show()
print( depth )


# In[5]:


from matplotlib import cm
import numpy as np


# In[7]:


xs, ys = np.mgrid[ 0:depth.shape[0], 0:depth.shape[1] ]

fig = plt.figure()
ax = fig.gca( projection='3d' )
ax.plot_surface( xs, ys, depth, rstride=1, cstride=1, cmap=cm.gray, linewidth=0 )
ax.view_init( elev = 10, azim = 30 )
plt.show()


# In[ ]:




