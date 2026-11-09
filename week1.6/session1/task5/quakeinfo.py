# Week 1.6, Session 1: Task 5

from dataset import QuakeDataset
from feed import QuakeFeed

level = input("Significance level: ")
period = input("Time period: ")

feed = QuakeFeed(level, period)
dataset = QuakeDataset(feed)
dataset.read_feed()

print(dataset)
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")
print()

quake = dataset.strongest_quake()
print(f"Strongest quake occurred at {quake.when.strftime('%H:%M:%S')} on {quake.when.date()}")
print(f"at {quake.longitude}° longitude, {quake.latitude}° latitude")
print(f"The depth was {quake.depth} km")
print(f"The magnitude was {quake.magnitude}")
