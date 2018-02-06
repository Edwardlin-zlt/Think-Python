## 10.12 List arguments  ##
`append` method modifies a list, but the `+`operator creates a new list.

	>>> t1 = [1, 2]
	>>> t2 = t1.append(3)
	>>> print t1
	[1,2,3]
	>>> print t2
	None
	
	>>> t3 = t1 + [4]
	>>> print t3
	[1,2,3,4]

Watch out, when you want modify a list don't use operators,it won't achieve what your expected.

## 10.13 Debugging ##

- Don't ofrget that most list methods modify the argument and return None.
- Pick an idiom and stick to it
- Make copies to avoid aliasing

## 10.14 Glossary ##
- list: Asequence of values.
- element: One of the values in a list (or other sequence), also called items.
- index: an integer value that indicates an element in a list
- nested list: A list that is an element of another list.
- mapping: A relationship in which each element of one set corresponds to an element of another set. For example, a list is a mapping from indices to elements.
- accumulator: A variable used in a loop to add up or accumulate a result.
- augmented assignment: A statement that updates the value of a variale using an operator like +=
- reduce: A processing pattern that traverses a sequence and accumulates the element into a single result.
- map: A processing pattern that traverses a sequence and performs an operation on each element
- filter: A processing pattern that traverses a list and selects the elements that satisfy some criterion.
- object: Something a variable can refer to. An object has a type and a value.
- equivalent: Having the same value.
- identical: Being the same object (which implies equivalence).
- reference: The association between a variable and its value.
- aliasing: A circumstance where two or more variable refer to the same object.
- delimiter: A character or string used to indicate where a string should be split.

# 11 Dictionaries #
You can think of a dictionary as a mapping between a set of indices (which are called keys) and a set of value. Each key maos to a value. The association of a key and a balue is called key-value pair or sometimes an item.
The function `dict()` creates a new dictionary with on items.

	>>> eng2sp = dict()
	>>> print eng2sp
	{}

The squiggly-brackets,`{}`,represent an empty dictionary.To add items to the dictionary, you can use square brackets:

	>>> eng2sp['one'] = 'uno'

This line creates an item that maps from the key 'one' to the value 'uno'.

	>>>eng2sp = {'one':'uno','two':'dos','three':'tres'}  # dict format

In general, the order of items in a dictionary is unpredictable, but it doesn't matter because in a dictionary, a key always maps to its value.

The `len` function returns the number of key-value pairs:

	>>> len(eng2sp)
	3

The `in` operator tells you weather something appears as a key (NOT value) in the dictionary.

	>>>'one' in eng2sp
	True
	>>>'uno' in eng2sp
	False

To see whether something appears as a value in a dictionary, you can use the method `values`, which returns the values as a list, and then use the `in` operator.

	>>>vals = eng2sp.values()
	>>>'uno' in vals
	True

## Dictionary as a set of counters ##

	>>>def histogram(s):
	>>>    d = dict()
	>>>    for c in s:
	>>>        if c not in d:
	>>>            d[c] = 1
	>>>        else:
	>>>            d[c] += 1
	>>>    return d

Dictionary have amethod called `get` that takes a key and a default value. If the key appears in the dictionary, `get` returns the corresponding value, otherwise it returns the default value.

	>>> h = histogram('a')
	>>> print h
	{'a':1}
	>>> h.get('a',0)
	1
	>>> h.get('b',0)
	0

## 11.2 Looping and dictionaries ##

If you use a dictionary in a `for` statement, it traverses the keys of the dictionary.

	>>> def print_hist(h):
	>>>     for c in h:
	>>>         print c,h[c]

## 11.3 Reverse lookup ##

Here is a function that takes a value and returns the first key maps to that value.

	>>>def reverse_lookup(d,v):
	>>>    for k in d:
	>>>        if d[k] == v:
	>>>           return k
	>>>    raise ValueError

The `raise` statement causes an exception; in this case it cause an ValueError, which generally indicate that there is something worry with the value of parameter.

The result when you raise an exception is the same as when Python raise one it prints a traceback and an error message.

The `raise` statement takes a detailed error message as an optional argument.

	>>> raise ValueError, 'value does not appear in the dictionary'

## 11.4 Dictionary and lists##

Here is a function that inverts a dictionary.

	>>> def inver_dict(d):
	>>>     inverse = dict()
	>>>     for key in d:
	>>>         val = d[key]
	>>>         if val not in inverse:
	>>>             inverse[val] = [key]  # attention: assignment is a list
	>>>         else:
	>>>             inverse[val].append(key)
	>>>     return inverse

In dictionary, a key must be **hashable**. The system works well when key are unmutable, but if the keys are mutable, like lists, bad things happen. The simplest way to get around this limitation is to use **tuples**. Since dictionary are mutable, they can't be used as keys, but they can be used as values.

## 11.5 Memos ##

A **call graph** shows a set of function frames, with lines connecting to the frame of the function it called.

A previously computed value that is stored for later use is called a **memo**. Here is an implementation of *fibonacci* using memos:

	>>> known = {0:0,1:1}
	>>> def fibonacci(n):
	>>>     if n in known:
	>>>         return known[n]
	>>>     res = fibonacci(n-1) +fibonacci(n-2)
	>>>     known[n] = res
	>>>     return res

## 11.6 Global variables ##

To reassign a global variable inside a function you have to **declare** the global variabel before you use it.

	>>> been_called =False
	>>> def example2():
	>>>     global been_called
	>>>     been_called = True

The `global` statement tells the interpreter something like, "In this function, when I say been_called, I mean the global variable; don't create a local one."

If the global value is mutable, you can modify it without declare it.

	>>> known = {0:0,1:1}
	>>> def example4():
	>>>     known[2] = 1

So you can add, remove and replace elements of global list or dictionary, but if you want to reassign the variable, you have to declare it:

	>>> def example5():
	>>>     global known
	>>>     known = dict()

## 11.7 Long integer ##

In python 3, `long` is gone; all integer, even really big ones, are type `int`.

## 11.8 Debugging ##

## 11.9 Glossary ##

- **dictionary:** A mapping from a set of keys to their corresponding values.
- **Key-value pair:** The representation of the mapping from a key to a value.
- **item:** Another name for key-value pair.
- **key:** An object that appears in a dictionary as the first part of a key-value pair.
- **Value:** An objuect that appears in a dictionary as the second part of a key-value pair.
- **Implementation:** A way of performing a computation.
- **Hashtable:** The algorithm used to implement Python dictionaries.
- **Hash function:** A function used by a hashable to compute the location for a key.
- **Hashable:** A type that has a hash function. Immutable types like integers, floats and strings are hashable; mutable types like lists and dictionaries are not.
- **Lookup:** A dictionary operation that takes a key and finds the corresponding value.
- **reverse lookup:** A dictionary operation that takes a value and finds one or more keys that map to it.
- **singleton:** Alist (or other sequence) with a single element.
- **call graph:** A diagram that shows every frame created during the execution of a program, with an arrow form each caller to each callee.
- **histofram:** A set of counters.
- **Memos:** A computed value stored to avoid unnecessary future computation.
- **Global variable:** A variable defined outside a function. Global variable can be accessed from any function.
- **Flag:** A boolean variable used to indicate whether a condition is true.
- **Declaration:** A statement like `globle` that tells the interpreter some thing about a variable.

# 12 Tuples #

## 12.1 Tuples are inmutable ##

You can't modify a tuple, but you can replace one tuple with another one.

	>>> t = ('A',) + t[1:]
	>>> print t
	('A','b','c','d','e')

## 12.2 Tuple assignment ##

The left side is a tuple of variable; the right side is a tuple of expressions.Each value is assigned to its respective variable.

	>>> a,b = b,a

The number of value on the left side and the number of value on the right side have to be the same.

More generally, the right side can be any kind of sequence (string, list or tuple). For example, to split an email address into a user name and a domain, you could write:

	>>>addr = 'monty@python.com'
	>>>uname,domain = addr.split('@')

The return value from `split` is a list with two elements, the first element is assigned to uname, the second to domain.

## Tuple as return value ##

Strictly speaking, a function can only return one value, but the value is a tuple, the effect is the same as returning multiple values.

The build-in function `divmod` takes two arguments and returns a tuple of two values, the quotient and remainder. You can store the result as a tuple.

	>>>t = divmod(7,3)
	>>>print t
	(2,1)

Or use tuple assignment to store the two value separately.

	>>> quot,rem = divmod(7,3)
	>>> print quot
	2
	>>> print rem
	1

Here is an example of a function that returns a tuple:
	
	>>> def min_max(t)
	>>>     return min(t),max(t)

`max` and `min` are built-in function that find the largest and smallest element of a sequence.

## 12.4 Variable-length argument tuple ##

functions can take a variable number of arguments. A parameter name that begins with * gathers arguments into a tuple.

The complement of gather is scatter. If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the * operator.

## 12.5 Lists and tuples ##

`zip` is a built-in function that takes two or more sequences and "zips" them into a list of tuples where each tuple contains one element from each sequence. In Python 3, `zip` returns an iterator of tuples, but for most purpose, an iterator behaves like a list.

	>>> s = 'abc'
	>>> t = [0,1,2]
	>>> zip(s,t)
	[('a',0),('b',1),('c',2)]

If the sequences are not the same length, the result has the length of the shorter one.

	>>> zip('Anne','Elk')
	[('A','E'),('n','l'),('n','k')]

You can use tuple assignment in a `for` loop to traverse a list of tuples:

	>>> t = [('a',0),('b',1),('c',2)]
	>>> for letter, number in t:
	>>>     print number,letter

IF you combine `zip`, `for` and tuple assignment, you get a useful idiom for traversing two (or more) sequences at the same time.

	>>> def has_match(t1,t2):
	>>>     for x,y in zip(t1,t2):
	>>>         if x == y:
	>>>             return True
	>>>     return False

If you need to traverse the elements of a sequence and their indices, you can use the build-in function `enumerate`

	>>> for index, element in enumerate('abc')
	>>>     print index, element

The output of this loop is:

	0 a
	1 b 
	2 c

## 12.6 Dictionaries and tuples ##

Dictionaries has a method called `items` that returns a list of tuples, where each tuple is a key-value pair .

You can use a list of tuple to initialize a new dictionary.

	>>> t = [('a',0),('c',2),('b',1)]
	>>> d = dict(t)
	>>> print d
	{'a':0,'c':2,'b':1}

Combine `dict` with `zip` yields a concise way to create a dictionary.

	>>>d = dict(zip('abc',range(1,3)))
	>>>print d
	{'a':1,'b':2,'c':3}

It is common to use tuples as keys in dictionaries (primarily because you can't use lists)

	>>> directory[last,first] = number # A telephone directory

## 12.7 Comparing tuples ##

The relational operator works with tuples and other sequences. Python starts ny comparing the first element from each sequence. If they are equal, it goes on to the next elements, and so on, until it finds elementa that differ.
	
	>>> (0,1,2) < (0,3,4)
	True
	>>> (0,1,200000) < (0,3,4)
	True

The `sort` function works the same way. It sorts primarily be first element, but in the case of a tie, it sorts by second element, and so on.

This feature lends itself to a pattern called **DSU** for

**Decorate** a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,

**Sort** the list of tuples, and

**Undecorate** by extracting the sorted elements of the sequence

	>>> def sort_by_length(words):
	>>>     t = []                            # Decorate
	>>>     for word in words:
	>>>         t.append((len(word),word))
	
	>>>     t.sort(reverse = True)            # Sort

	>>>     res = []                          # Undecorate
	>>>     for length, word in t:
	>>>         res.append(word)
	>>>     return res                        

## 12.8 Sequences of sequences ##

In many contexts, the different kinds of sequences(string, lists and tuples) can be used interchangeably. So how and why do you choose one over the others?

- strings are more limited than other sequences because the elements have to be characters, and they are immutable.
- In some contexts, like a `return` statement, it is syntactically simpler to create a tuple than a list. In other contexts, you might prefer a list.
- If you want a sequence as a dictionary key, you have to use an immutable type like a tuple or a string.
- If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

Because tuples are immutable, they don't provide methods like `sort` and `reverse`, which modify existing lists. But Python provides the built-in functions `sorted` and `reversed`, which take any sequence as parameter and return a new list with the same elements in a different order.

## 12.9 Debugging ##

List, dictionaries and tuples aare known generically as **data structure**

If you are having trouble keeping track of your data structures, [structshape](http://www.greenteapress.com/thinkpython/code/structshape.py) can help

## 12.10 Glossary ##

**Tuple:** An immutable sequence of elements.

**Tuple assignment:** An assignment with a sequence on the right side and a tuple of variables on the left. The right side is evaluated and then its elements are assigned to the variables on the left.

**Gather:** The operation of assembling a variable-length argument tuple.

**Scatter:** The operation of treating a sequence as a list of atguments.

**DSU:** Abbreviation of "decorate-sort-undecorate" pattern that involves building a list of tuples, sorting, and extracting part of the result.

**Data structure:** Acollection of related values, often organized in list,dictionaries, tuples, etc.

**shape (of a data structure):** A summary of the type, size and composition of a data structure.

# Case study： data structure selection #

## 13.1 Word frequency analysis ##

## 13.2 Random numbers ##

The `random` module provides functions that generate pseudorandom numbers. 
>The function `random` returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0)
>
>The function `randint` takes parameters *low* and *high* and returns an integer between *low* and *high*. (including both)
>
>To choose an element from a sequence at random, you can use `chioce`.
>
	>>> t = [1,2,3]
	>>> random.choice(t)
	2
	>>> random.choice(t)
	3

## 13.3 Word histogram ##

str.replace(old, new[, count])
>Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

get(key[, default])
>Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

Question:
`word = word.strip(string.punctuation + string.whitespace)`

## 13.4 Most common words ##

## 13.5 Optional parameters ##

## 13.6 Dictionary subtraction ##
`subtract` takes dictionaries `d1` and `d2` and returns a new dictionary that contains alla the keys form `d1` that are not in `d2`.

	>>> def subtract(d1,d2):
	>>>     res = dict()
	>>>     for key in d1:
	>>>         if key not in d2:
	>>>             res[key] = None
	>>>     return res

<<<<<<< HEAD
## 13.7 Random words ##

The expression `[word] * freq` creates a list with freq copies of string word. The `extend` method is similar to `append` except that the argument is a sequence.

## 13.8 Markov analysis 
=======
## 14.4 Filenames and paths

The `os` module provides functions for working with files and directories ('os' stands for 'operating system')
`os.getcwd` returns the name of the current directory ('cwd' stands for 'current working directory).

A relative path starts from the current directory, and an absolute path starts from the topmost directory in the file system

To find the absolute path to a file, you can use `os.path.abspath('filename')`

`os.path.exists` checks whether a file or directory exists.

`os.path.isdir` checks whether it's a directory.

`os.path.isfile` checks whether it's a file.

`os.listdir` returns a list of files (and other directories) in the given directory.

`os.chdir` changes the working directory to the path you named it.

`os.path.join` takes a directory and a file name and join them into a complete path. 

## 14.5 Catching exceptions

If you try to open a file that doesn't exist, you get an IOError.

If you don't have permission to access a file, you get a IOError.

IF you try to open a directory for reading, IOError.

The `try` statement's syntax is similar to an `if` statement.

    try:
        fin = open('bad_file')
        for line in fin:
            print line
        fin.close()
    except:
        print 'Something went wrong'
       
Python starts by executing the `try` clause. If all goes well, it skips the `except` clause and proceeds.
If an exception occurs, it jumps out the `try` clause and executes the `except` clause.

Handling an exception with a try statement is called **catching** a exception.
>>>>>>> parent of 0106e4b... till Chapter 15
