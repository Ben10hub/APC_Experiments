import matplotlib.pyplot as plt

# Sample data
subjects = ["Python", "Java", "DBMS", "Maths"]
marks = [85, 75, 90, 80]

# Line graph
plt.figure()
plt.plot(subjects, marks, marker="o")
plt.title("Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Bar graph
plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie chart
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# Histogram
plt.figure()
plt.hist(marks, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(subjects, marks)
plt.title("Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()