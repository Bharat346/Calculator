import matplotlib.pyplot as plt 
import numpy as np 

#generate x 
x = np.linspace(-10,10,1000)
y1 = np.sqrt(100-(x**2))


#plot curves 
plt.plot(x,y1,label = 'x^2 + Y^2 =1',linestyle = '-',color='blue')
#plt.plot(x,y2,label = 'cos(x)',linestyle = ':',color='red')
#plt.plot(x, y3, label='x^2', linestyle='-.', color='green')

# Set y-axis limits
plt.ylim(-10, 10)
#plt.axis([2, 6, -1, 1])


#Add labels
plt.title('Curves with Different Styles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

#add legend
plt.legend()

#show the plot
plt.show()