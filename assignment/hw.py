import numpy as np 
import matplotlib.pyplot as plt

# part 1 to 7
x = np.linspace(0,1,50)
y = np.log(x)
z = np.exp(x)
plt.scatter(x,y, label ='Natural Log')
plt.scatter(x,z, label='Exponential')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='lower right')
plt.title('Natural Log and Exponential Functions')
plt.show()

# part 8 - 12
x = np.linspace(-6.5,6.5,100)
y = np.sin(x)
z = np.cos(x)
# plt.scatter(x,y)
# plt.scatter(x,z)
plt.plot(x,y, label ='Sine')
plt.plot(x,z, label='Cosine')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='lower left')
plt.title('Sine and Cosine')
plt.show()

