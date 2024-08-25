import numpy as np

# a = np.array(45)
# b = np.array([1,2,3,4,5])
# c = np.array([[1,2,3],[4,5,6]])
# d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[3,6,9],[3,6,9],[3,6,9]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)

# print(a)
# print(b)
# print(c)
# print(d)

# print(np.arange(120))
# print(np.zeros((3,4)))
# print(np.ones((3,4)))
# print(np.eye(2))
# print(np.random.rand(2,1))
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix[:2, :])        # Get the first two rows and all columns
# print(matrix[:, -2:])       # Get the first two rows and all columns

# arr1 = np.array([10,20,30,40,50,60])
# print(arr1[arr1>30])
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr[:,1])
# print(arr[2,:])

# arr = np.array([True,False,True],dtype = np.bool_)
# print(arr)

# arr = np.array(['apple',2,3.7],dtype=np.object_)
# print(arr)

# arr = np.array(['apple','world'],dtype=np.string_)
# print(arr)

# arr1 = np.array((4,5,6))
# print(arr1)
# arr2 = np.array([4,5,6])
# print(arr2)

# NOTE :  COPY AND VIEW

# creating VIEW 
# arr = np.array([10,20,30,40,50])
# arr2 = arr[1:4]

# print(arr)
# print(arr2)

# arr2[1] = 100
# print(arr)
# print(arr2)

# reverse the array using slicing
# arr = np.array([10,20,30,40,50])
# arr2 = arr[::-1]
# print(arr2)

# arr2 = arr[1:4].view()

# print(type(arr))
# print(type(arr2))
# arr2[:] = 0
# print(arr2)
# print(arr)

# arr[2] = 100
# print(arr)
# print(arr2)



#Creating COPY()
# arr = np.array([10,20,30,40,50])
# arr2 = arr[1:4].copy()

# print(arr)
# print(arr2)

# arr2[1] = 100
# print(arr)
# print(arr2)


# arr = np.zeros(5)
# print(arr)

# arr = np.zeros((5,3),dtype=int)
# print(arr)

# arr = np.zeros((5,3),dtype=int)
# arr = arr+10
# print(arr)

# arr = np.full((5,3),10,dtype=int)
# print(arr)

# arr = np.ones((5,3),dtype=int)+9
# print(arr)

# matrix = np.array([[3, 5, 2],
# [6, 1, 4]])
# # Sort along rows (axis=1) in ascending order
# sorted_matrix = np.sort(matrix, axis=1)
# print(sorted_matrix)
# arr1 = np.array([[1, 2], [3, 4]])
# print(arr1.shape)

# Synthetic dataset
# data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# # Split the data into training (70%) and testing (30%) sets
# train_data, test_data = np.split(data, [int(0.9 * len(data))])
# print("Training Data:")
# print(train_data)
# print("\nTesting Data:")
# print(test_data)

# Sales data: [Product ID, Sales Amount]
# sales_data = np.array([[101, 500], [102, 750], [103, 350], [104, 900], [105, 600]])
# # Sort the sales data by sales amount in descending order
# sorted_sales_data = sales_data[sales_data[:, 1].argsort()[::-1]]
# print("Top-selling products:")
# print(sorted_sales_data)

# Customer names and email addresses
# names = np.array(['Alice', 'Bob', 'Charlie', 'David'])
# emails = np.array(['alice@example.com', 'bob@example.com', 'charlie@example.com',
# 'david@example.com'])
# # Join names and email addresses horizontally
# customer_data = np.vstack((names, emails)).T
# print("Customer Data:")
# print(customer_data)

# arr = np.array([30, 25, 50, 45 , 60])
# print(np.std(arr))
# print(np.std(arr))]
# con = arr>30
# print(con)
# print(arr[con])
# arr[1:4] = 10
# print(arr)

#EYE METHOD
# arr = np.eye(3)
# print(arr)

# arr = np.eye(3,4)
# print(arr)

# arr = np.diag((3,4,7,6))
# print(arr)

# print(np.random.randint(4,10,5))
# print(np.random.rand(4))
# print(np.random.rand(4,3))


# arr = np.random.randint(0,100,12)
# print(arr)
# arr = arr.reshape(4,-1)                      # put -1 if you don't know row or column
# print(arr)
# arr = arr.reshape(6,2)
# print(arr)

# arr1 = np.array([1, 2])
# arr2 = np.array([3, 4])
# arr3 = np.array([3])
# # Stack arr1 and arr2 horizontally
# result = np.hstack((arr1, arr2,arr3))
# # Print the horizontally stacked array
# print(result)

arr = np.array([30, 25, 50, 45, 60])
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))

# np.random.seed(10)
# arr = np.random.randint(1,100,30).reshape(6,5)
# print(arr)
# print(arr[2:,2:])
# print(arr[3:5,2:4])

# list = [1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33,]
# arr = np.array(list)
# slicing = arr[4:9]
# print(slicing)
# print(arr)
# print(type(slicing))
# print(type(arr))
# slicing[:] = 0
# print(slicing)
# print(arr)


# hii i am new to python numpy . Can you generate some real world situations where i can use a numpy array with some source code

# Sample dataset with 3 features
# data = np.array([
#     [1.0, 200.0, 3.0],
#     [2.0, 220.0, 1.0],
#     [0.5, 180.0, 2.0]
# ])

# # Normalize the data (feature scaling)
# mean = np.mean(data, axis=0)
# std = np.std(data, axis=0)
# normalized_data = (data - mean) / std
# print("Normalized data:\n", normalized_data)



# hii let's create a real life example of weather data . use numpy to analyse temperature data for a week , perform slicing , indexing, shaping and reshaping operations and calculate various statistics

# Simulate temperature data for a week (7 days, 4 times a day)
# temperature_data = np.array([
#     [15, 22, 18, 12],  # Day 1
#     [16, 24, 19, 14],  # Day 2
#     [15, 23, 20, 13],  # Day 3
#     [17, 25, 21, 16],  # Day 4
#     [16, 26, 22, 15],  # Day 5
#     [18, 27, 23, 17],  # Day 6
#     [19, 28, 24, 18]   # Day 7
# ])

# print("Original Temperature Data:\n", temperature_data)

# # Slicing and Indexing
# first_three_days = temperature_data[:3, :]
# print("\nTemperatures for the first three days:\n", first_three_days)

# afternoon_temperatures = temperature_data[:, 1]
# print("\nAfternoon temperatures for the entire week:\n", afternoon_temperatures)

# # Reshape and Shape Operations
# reshaped_data = temperature_data.reshape(-1)
# print("\nReshaped data into a single array:\n", reshaped_data)

# original_shape_data = reshaped_data.reshape(7, 4)
# print("\nData reshaped back to its original shape:\n", original_shape_data)

# # Calculate Various Statistics
# mean_temperature_per_day = np.mean(temperature_data, axis=1)
# print("\nMean temperature for each day:\n", mean_temperature_per_day)

# mean_temperature_per_time = np.mean(temperature_data, axis=0)
# print("\nMean temperature for each time of the day:\n", mean_temperature_per_time)

# max_temperature = np.max(temperature_data)
# min_temperature = np.min(temperature_data)
# print("\nMaximum temperature for the week:", max_temperature)
# print("Minimum temperature for the week:", min_temperature)

# overall_average_temperature = np.mean(temperature_data)
# print("\nOverall average temperature for the week:", overall_average_temperature)


# arr = np.arange(1,15)                 # arrange numbers in given range in an array
# print(arr)
# print(arr[arr%2==0])
# print(arr[arr%2!=0])
# print(arr[arr > 8])
# arr[arr%2 == 0] = 0
# print(arr)
# print(arr+2)
# print(arr*2)
# print(arr**2)


# arr = np.array([10,20,25,35,6,2])
# print(np.min(arr))
# print(np.max(arr))
# print(np.argmin(arr))
# print(np.argmax(arr))
# print(np.sqrt(arr))
# print(np.sin(arr))
# print(np.cos(arr))

# np.random.seed(122)
# mat = np.random.randint(1,21,12).reshape(4,3)
# print(mat)
# print(np.sum(mat))
# print(np.cumsum(mat))
# print(np.min(mat))
# print(np.max(mat))
# print(np.sum(mat,axis=1))
# print(np.min(mat, axis=1))
# print(np.max(mat, axis=1))
# print(np.cumsum(mat, axis=1))
# print(np.sum(mat,axis=0))
# print(np.min(mat, axis=0))
# print(np.max(mat, axis=0))
# print(np.cumsum(mat, axis=0))


#NOTE : INCOMPLETE TASK
# np.random.seed(122)
# mat = np.random.randint(1,21,12).reshape(4,3)
# print(mat)
# def cumsum(arr):
#     li = []
#     sum = 0
#     for row in arr:
#         for ele in row:
#             sum += ele
#             li.append(sum)
#     return li
# print(cumsum(mat))

# when axis = 1
# np.random.seed(122)
# mat = np.random.randint(1,21,12).reshape(4,3)
# print(mat)
# def cumsum(arr):
#     li1=[]
#     for row in arr:
#         sum = 0
#         li2 = []
#         for ele in row:
#             sum += ele
#             li2.append(sum)
#         li1.append(li2)
#     return np.array(li1).reshape(4,3)
# print(cumsum(mat))


# when axis = 0
# np.random.seed(122)
# mat = np.random.randint(1,21,12).reshape(4,3)
# print(mat)
# def cumsum(arr):
#     li1=[]
#     for row in arr:
#         sum = 0
#         li2 = []
#         for ele in row:
#             sum += ele
#             li2.append(sum)
#         li1.append(li2)
#     return np.array(li1).reshape(4,3)
# print(cumsum(mat))

# np.random.seed(122)
# mat = np.random.randint(1,21,10)
# print(mat)
# np.random.shuffle(mat)
# print(mat)
# print(np.unique(mat,return_index=True,return_counts=True))
# print(np.unique(mat).size)


# arr1 = np.array([10,20,30,40])
# arr2 = np.array([50,60,70,80])
# print(arr1)
# print(arr2)
# print(np.vstack((arr1,arr2)))
# print(np.hstack((arr1,arr2)))

# np.random.seed(122)
# mat1 = np.random.randint(1,21,12).reshape(4,3)
# mat2 = np.random.randint(5,30,12).reshape(4,3)
# print(mat1)
# print(mat2)
# print(np.vstack((mat1,mat2)))
# print(np.hstack((mat1,mat2)))

# arr = np.array([10,25,65,85,25,63,95,65])
# w = np.where(arr==60)
# print(w)

# arr = np.array([10,25,36,78,89,96])
# ss = np.searchsorted(arr,90)
# print(ss)

# arr = np.array([3,1,2,4,5])
# sorted_arr = np.sort(arr)

# print("Sorted array : ascending ",sorted_arr)

# sorted_arr_desc = np.sort(arr)[::-1]
# print("Sorted array : ascending ",sorted_arr_desc)

# arr = np.array([3,1,2,4,5,6])

# sub_arr = np.split(arr,3)
# print(sub_arr)
# sub_arr2 = np.split(arr,[1,4])

# print(sub_arr2)


# Score of Class A students
# classA= np.array([85, 88, 90, 92, 95])
# # Score of Class A students
# classB= np.array([70, 80, 85, 95, 100])
# classA_mean=np.var(classA)
# classB_mean=np.mean(classB)
# print('Class A Score Average',classA_mean )
# print('Class B Score Average',classB_mean )

# scores = np.array([85,92,78,88,95,72,89])
# np.save('student_scores.npy',scores)

# loaded_scores = np.load('student_scores.npy')
# print("Original scores",scores)
# print("loaded scores ",loaded_scores)