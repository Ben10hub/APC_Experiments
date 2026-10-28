import numpy as np
import pandas as pd

# NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)

# Pandas Series
marks = pd.Series([80, 75, 90, 85])

print("\nPandas Series:")
print(marks)

print("Average Marks:", marks.mean())

# Pandas DataFrame
data = {
    "Name": ["Rahul", "Amit", "Priya"],
    "Marks": [80, 75, 90]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])