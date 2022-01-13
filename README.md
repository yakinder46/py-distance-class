# Distance class

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Every day you have morning running. You want to store your result. 
To easy calculating, comparison and printing you result write class
`Distance`.

`Distance`'s constructor takes only
one argument `km` and saves it to `self.km`.

For `Distance` class you should implement such magic
methods:
```python
__init__
distance = Distance(20) # distance.km == 20
__str__
print(distance) # "Distance: 20 kilometers."
__add__
dist2 = distance + 10 # dist2 == 30
__iadd__
distance += 30 # distance.km == 50
__mul__
dist2 = distance * 5 # dist2 == 250
__truediv__
dist2 = distance / 7 # dist2 == 7.14
# Note: rounded to 2 decimals
__mod__
dist2 = distance % 20 # dist2 == 10
__lt__, __gt__, __eq__, __le__, __ge__
distance >= 50 # True
distance == 100 # False
distance < 60 # True
distance <= 49 # False
distance < 120 # True
__len__
len(distance) == 50
```
