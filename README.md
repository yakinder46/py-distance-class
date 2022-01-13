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
distance = Distance(20)  # distance.km == 20

__str__
distance = Distance(20)
print(distance)  # "Distance: 20 kilometers."

__repr__
distance = Distance(20)
repr(distance)  # "Distance(km=20)"

__add__
distance1 = Distance(20)
distance2 = Distance(30)
distance3 = distance1 + distance2  
# isinstance(distance3, Distance) == True
# distance3.km == 50

__iadd__
distance = Distance(20)
distance += 30  # distance.km == 50

__mul__
distance = Distance(20)
distance2 = distance * 5  
# isinstance(distance2, Distance) == True
# distance2.km == 100

__truediv__
distance = Distance(20)
distance2 = distance / 7  
# isinstance(distance2, Distance) == True
# distance2.km == 2.85
# Note: rounded to 2 decimals

__mod__
distance = Distance(20)
distance2 = distance % 15
# isinstance(distance2, Distance) == True
# distance2.km == 5

__lt__, __gt__, __eq__, __le__, __ge__
distance >= 50  # True
distance == 100  # False
distance < 60  # True
distance <= 49  # False
distance < 120  # True

__len__
distance = Distance(20)
len(distance) == 20
```
