import matplotlib.pyplot as plt

#place values on scatter chart
xValues = list(range(1,1001))
yValues = [x**2 for x in xValues]

#size of dot 200
plt.scatter(xValues,yValues,c=yValues,cmap=plt.cm.YlGnBu,edgecolor='none' ,s=40)

#set chart title and label axes
plt.title("square numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0,1100,0,1100000])

#set the size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
