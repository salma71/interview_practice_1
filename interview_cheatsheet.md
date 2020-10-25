# Interview intermediate cheat sheet
#### Use `enumerate()` to iterate over both indices and values instead of `range()`
```
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
    print(i, num)
52 45
53 22
54 14
55 65
56 97
57 72
```
#### Use `list comprehension` instead of `map()` and `filter()`
```
[(lambda x: x * x )(x) for x in [1, 2, -5, 4]]
[1, 4, 25, 16]
```
#### Use `breakpoint()` instead of `print()`
you need to import `pdb` explicitlly for python < 3 ```import pdb; pdb.set_trace()``` 

#### Use `f` from string module to print strings
```
def get_name_and_decades(name, age):
    return f"My name is {name} and I'm {age / 10:.5f} decades old."
get_name_and_decades("Maria", 31)
My name is Maria and I'm 3.10000 decades old.
```
#### Use `sorted()` to sort complex lists
```
sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
['rhino', 'dog', 'cheetah', 'cat', 'bear]
```
or in dictionary
```
sorted(animals, key=lambda animal: animal['age'])
[
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
    {'type': 'penguin', 'name': 'Stephanie, 'age': 8},
]
```
#### Store unique values in a `set()` , `O(1)` time complexity
```
def get_unique_words():
...     words = set()
...     for _ in range(1000):
...         words.add(get_random_word())
...     return words
>>> get_unique_words()
{'world', 'all', 'the', 'words'}
```
#### Save memory with generators
```
sum((i * i for i in range(1, 1001)))
333833500
```
#### Define Default Values in Dictionaries With `.get()` and `.setdefault()`


MIT
