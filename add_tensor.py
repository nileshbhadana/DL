#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:40:05 2019

@author: nilesh
"""

import tensorflow as tf

#creating constant(variable)
x=tf.constant([15])
y=tf.constant([20])


#graph add perform
z=x+y

print(z)
z1=tf.add(x,y)


#resource allocation
resource_provider=tf.Session()

#using resource provider to run your graph --cpu --gpu

output=resource_provider.run(z1)
print(output)


#after use close your resource tool
resource_provider.close()

#without closing session

with tf.Session() as r_session:
    print(r_session.run(z1))