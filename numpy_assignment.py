import numpy as np

# Question One
print(f"Question One (numpy version): {np.__version__}")

# Question Two
question_two = np.array(range(0,9,1))
print(question_two)

# Question Three
question_three = np.genfromtxt("Iris_Data.csv", 
                            delimiter = ",", 
                            dtype = [float, float, float, float, "U25"],
                            names = ["Sepal Length", "Sepal Width",
                                     "Petal Length", "Petal Width",
                                     "Species"])

# Question Four
for position, value in enumerate(question_three):
    if value[3] > 1.0:
        print(f"Petal Width is greater than 1.0 at position {position}")
        break

# Question Five
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
for position, value in enumerate(a):
    if(value) > 30:
        a[position] = 30
    if(value) < 10:
        a[position] = 10
print(f"Question Five: \n{a}")
