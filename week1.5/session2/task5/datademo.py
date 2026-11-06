# Week 1.5, Session 2: Task 5

from data import Dataset

filename = input("Name of the data file: ")

dataset = Dataset(filename)

print(f"size of the dataset: {len(dataset)}")
print(f"mean: {dataset.mean()}")
print(f"median: {dataset.median()}")

print("the values are:")
for value in dataset:
    print(value)
