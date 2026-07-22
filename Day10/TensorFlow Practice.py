#practice problems 
import tensorflow as tf
int=tf.constant(12)  # do not changed value afetr assign it
Flo=tf.constant(3.12)
stri=tf.constant("Hello")
li=tf.constant([2,3,4,5])    #1D list but in tensor calls vector
#print(tf.rank(li))         # tell number of D
#print(tf.size(li))        # tell size of tensor
va=tf.Variable(10)      # changed value afetr assign it
va.assign(50)
va.assign_add(10)   # add value
va.assign_sub(10)   # subtract values value
#print(va)

# Tensor Operation
a = tf.constant([1,2,3])
b = tf.constant([4,5,6])
#print(a+b)
#print(a-b)
#print(a*b)
#print(b/a)
#print(tf.square(a))
A=tf.constant([[1,2],[3,4]])           # for matrix calcualtion 2D and vice versa
B=tf.constant([[5,6],[7,8]])
#print(tf.matmul(A,B))

x=tf.random.uniform((3,3))
x1=tf.random.normal((2,4))
#print(x)
#print(x1)
y=tf.reshape(li,(2,2))    # convert 1D to 2 D and vice versa
#print(y)
#print(len(tf.config.list_physical_devices("GPU"))>0)
#print(tf.config.list_physical_devices("GPU"))
 

''' Complete  Tensorflow Structure 

TensorFlow
│
├── tf.constant()
├── tf.Variable()
├── tf.random
├── tf.math
├── tf.linalg
├── tf.data
├── tf.image
│
└── tf.keras
      │
      ├── models
      │      ├── Sequential
      │      └── Model
      │
      ├── layers
      │      ├── Input
      │      ├── Dense
      │      ├── Conv2D
      │      ├── Flatten
      │      ├── Dropout
      │      └── LSTM
      │
      ├── activations
      ├── optimizers
      ├── losses
      ├── metrics
      ├── callbacks
      └── datasets      '''