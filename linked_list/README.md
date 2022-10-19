## Data Structure (Practice)

### Linked List
* import
```python
from linked_list import LinkedList, Node
```
---
* init linked list
```python
linked_list_1 = LinkedList()  # Empty linked list
linked_list_2 = LinkedList(1, 2, 3)  # Linked list with values
```
---
* Add items to linked list
```python
linked_list = LinkedList()
linked_list.add(1, 2, 3)
```
---
* `__repr__`
```python
print(LinkedList(1, 2, 3))  # LL[1 > 2 > 3]
```
---
* Apply `len()`
```python
linked_list = LinkedList(1, 2, 3)
len(linked_list)  # 3
```
---
* Equation with linked list
```python
LinkedList(1, 2, 3) == LinkedList(1, 2, 3)  # True
LinkedList(1, 2, 3) == LinkedList(3, 2, 1)  # False
```
---
* Iteration
```python
for i in LinkedList(1, 2, 3):
    ...
```
* Indexing
```python
linked_list = LinkedList(1, 2, 3)
isinstance(linked_list[1], Node)  # True
linked_list[1]  # 2
del linked_list[1]  # linked_list -> LL[1 > 2]
linked_list[0] = 2  # linked_list -> LL[2 > 2]
```
---
* Reversed
```python
linked_list = LinkedList(1, 2, 3)
print(reversed(linked_list))  # LL[3 > 2 > 1]
```