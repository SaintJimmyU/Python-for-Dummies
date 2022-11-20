''' Otra Forma de Llamar una funcion con args y kwargs '''

def func(*args, **kwargs):
    print(f"{args=},{kwargs=}")

func()
func(*[10,20,30])
func(**{'x':1,'y':2,'z':3})
func(*[10,20,30],**{'x':1,'y':2,'z':3})

# -----------------------------------------------------------------

''' AHORA APLICANDOLO CON DESEMPAQUETADO E ITERANDOLO (--> esto se corrio en REPL <--)

Python provides an awesome variety of sequential data structures. The most common of them are list and tuple. These sequences are sometimes used to store records, which later needs to be unpacked.

When unpacking the values from a sequence you may encounter error like- ValueError: too many values to unpack. In this short post I will share a short PyTip to avoid this error.
Problem

Create a file or run the below code in the Python REPL.

primes = [2, 3, 5, 7, 11]
first, second, third = primes

The above code will produce the following error.

Traceback (most recent call last):
 File “<stdin>”, line 1, in <module>
ValueError: too many values to unpack (expected 3)

The above error states that to unpack your iterable, your iterable size must be three.
Solution

To solve this problem PEP 3132 was proposed. Now, write the following code in Python REPL to see Extended Iterable Unpacking in action.

>>> primes = [2, 3, 5, 7, 11]
>>> first, second, third, *_ = primes
>>> print(first, second, third, _)
2 3 5 [7, 11]

In the above output you can see that `*_` syntax caught all the excess values from the iterable. The `_` variable could be anything of your choice, it doesn’t have to be an underscore. Additionally, “*_” may be used anywhere in the statement. Consider the example below to get the idea.

>>> primes = [2, 3, 5, 7, 11]
>>> first, *_ , last = primes
>>> print(first, last, _)
2 11 [3, 5, 7]

I find this feature extreamly useful and hope you find it useful too. Thanks for the reading today’s PyTip.
'''