import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [10,20,30,40,50]

# #create a line plot
# plt.plot(x,y)

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line plot")

# # simple line plot
# plt.show()


# x = list(range(1,31))
# y = [10,20,30,40,50,60,70,4,23,6,7,4,6,6,6,4,4,7,3,78,3,7,3,7,3,7,3,7,3,7]

# #create a line plot
# plt.plot(x,y,marker='o')

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line plot")

# # simple line plot
# plt.show()

                                                                # bar chart
                                    
# x = list(range(1,31))
# y = [10,20,30,40,50,60,70,4,23,6,7,4,6,6,6,4,4,7,3,78,3,7,3,7,3,7,3,7,3,7]

# #create a line plot
# plt.bar(x,y)

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line plot")

# # simple line plot
# plt.show()

# x = list(range(1,31))
# y = [10,20,30,40,50,60,70,4,23,6,7,4,6,6,6,4,4,7,3,78,3,7,3,7,3,7,3,7,3,7]

# #create a line plot
# plt.barh(x,y) 

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line plot")

# # simple line plot
# plt.show()

# categories = ['Category A','Category B','Category C','Category D']
# values = [25,40,30,35]

# plt.figure(figsize=(8,6))

# bars = plt.bar(categories,values, color=['blue','green','red','purple'], width=0.4, edgecolor='y', linewidth=5, linestyle=":",alpha=0.6, label="Utpal")

# plt.xlabel('Categories',fontsize=14)
# plt.ylabel('Values',fontsize=14)
# plt.title('Bar plot example', fontsize=16)
# plt.xticks(rotation = 45)

# plt.tight_layout()
# plt.legend()
# plt.show()


                                                            # Histogram 
# ages = [1, 1, 2, 3, 3, 5, 7, 8, 9, 10,
# 10, 11, 11, 13, 13, 15, 16, 17, 18, 18,
# 18, 19, 20, 21, 21, 23, 24, 24, 25, 25,
# 25, 25, 26, 26, 26, 27, 27, 27, 27, 27,
# 29, 30, 30, 31, 33, 34, 34, 34, 35, 36,
# 36, 37, 37, 38, 38, 39, 40, 41, 41, 42,
# 43, 44, 45, 45, 46, 47, 48, 48, 49, 50,
# 51, 52, 53, 54, 55, 55, 56, 57, 58, 60,
# 61, 63, 64, 65, 66, 68, 70, 71, 72, 74,
# 75, 77, 81, 83, 84, 87, 89, 90, 90, 91]
# b=[0,10,20,30,40,50,60,70,80,90,100]
# plt.hist(ages, bins=b, edgecolor='g',histtytpe="step")
# plt.xlabel('Age')
# plt.ylabel('Number of Respondents')
# plt.axvline(50,color='green',linestyle="-.",linewidth=4)
# plt.title('Age Distribution of Survey Respondents')
# plt.show()

                                                     #pie plot

# # Market share data
# manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Others']
# market_share = [30, 25, 18, 12, 15]
# # Colors for each slice
# colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']
# ex = [0.3,0.0,0.1,0.0,0.0]
# # Create a pie chart
# plt.pie(market_share, labels=manufacturers, colors=colors, autopct='%1.2f%%',explode=ex,radius=0.9,shadow=True,wedgeprops={"linewidth":7, "edgecolor":"r"},labeldistance=0.3,textprops={"fontsize":10,"color":"g"},counterclock=False)
# # Title
# plt.title('Smartphone Market Share')
# plt.legend()     #to add labels
# # Show the pie chart
# plt.show()

# x1= [10,20,30,40]
# x2 = [50,60,70,80]
# y = ["Samsung","Lava","MI","Iphone"]
# col = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink']
# plt.pie(x1,labels=y,radius=1.2)
# plt.pie([1],colors='w')
# plt.show()
  
                                                                   #scatter plot

# # Student data (study hours and exam scores)
# study_hours = [2, 3, 1, 4, 3, 5, 2, 6, 5, 7]
# exam_scores = [65, 75, 60, 80, 70, 85, 70, 90, 88, 92]
# # Create a scatter plot
# plt.scatter(study_hours, exam_scores, c='green', marker='o', label='Student Data',s=exam_scores)
# # Labeling and Title
# plt.xlabel('Study Hours')
# plt.ylabel('Exam Scores')
# plt.title('Study Hours vs. Exam Scores')
# # Show the scatter plot
# plt.legend(loc=11)
# plt.grid(True)
# plt.show()

                                                                          #Subplot
                    
# # Sample student data
# students = ['Jhon', 'Smith', 'Marry', 'Rose', 'Devid']
# math_scores = [85, 92, 78, 88, 90]
# science_scores = [76, 88, 92, 80, 78]
# # Create a subplot with two subplots (1 row, 2 columns)
# fig, axs = plt.subplots(1, 2, figsize=(4, 3))
# # Plot Math Scores
# axs[0].bar(students, math_scores, color='b')
# axs[0].set_title('Math Scores')
# axs[0].set_xlabel('Students')
# axs[0].set_ylabel('Score')
# # Plot Science Scores
# axs[1].bar(students, science_scores, color='g')
# axs[1].set_title('Science Scores')
# axs[1].set_xlabel('Students')
# axs[1].set_ylabel('Score')
# # Adjust spacing between subplots
# plt.tight_layout()
# # Show the subplot
# plt.show()

x = [10,20,30,40,50,60,70,80,90]
y = [1,2,3,4,5,6,7,8,9]
plt.subplot(2,2,1)
plt.plot(x,y,color='g')


plt.subplot(2,2,2)
plt.pie([1,3,6],colors='r')

plt.subplot(2,2,3)
a = [20,40,60]
plt.pie(a)

plt.subplot(2,2,4)
a1 = ["r",'a','h','u']
a2 = [20,40,60,80]
plt.bar(a1,a2)

plt.show()

x = [1,2,3,4,5]
y = [2,3,5,5,11]

plt.plot(x,y)

#Adding title and axis labels
plt.title('Plot with general text')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#Adding general text
plt.text(2,8,'General Text',fontsize=10)
incomplete

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y)

plt.xticks([1,2,3,4,5],['c','c++','java','python','Adv python'])
plt.yticks()

plt.title('Plot with general text')
plt.xlabel('X-axis')
plt.ylabel('Y-axis') 
plt.show()


x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y)
plt.xlim(0,10)
plt.ylim(0,12)


# plt.savefig("LineChart.png",facecolor='r',transparent=True, dpi = 500)
# plt.show()


                                                                       # Saving any chart

# x = [9,5,3,7,4,7]
# y = [2,3,5,7,89,6]

# plt.plot(x,y)

# plt.title('Sample Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.savefig("LineChart.png",facecolor='r',transparent=True, dpi = 500)
# plt.show()


