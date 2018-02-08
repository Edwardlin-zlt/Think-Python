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
## 13.8 Markov analysis 
=======
## 14.3 Format operator
The argument of `write` has to be a string, so if we want to put other values in a file, we have to convert them to strings.

    >>> x = 52
    >>> f.write(str(x))

The alternative is to use **format operator**, `%`. When applied to integers, `%` is the modulus operator.
But when the first operand is a string, `%` is the format operator.

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

There is another `join`:

Syntax:  'sep'.join(seq)

sep：separator
seq：the sequence that need to be connected. The sequence could be a list, dictionary or tuple

Return：A string that was constructed by the elements in the sequence and separator between each elements.

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

## 14.6 Databases

The module `anydbm` provides an interface for creating and updating database files.

    >>> import anydbm
    >>> db = anydbm.open('captions.db', 'c')
   
The mode 'c' means that the database should be created if it doesn't already exist.
The result is a database object that can be used (for most operations) like a dictionary. 
If you create a new item, `anydbm` updates the database file.

    >>> db['cleese.png'] = 'Photo of John Cleese.'
    
When you access one of the items, `anydbm` reads the file.

If you make another assignment to an existing key, `anydbm` replaces the old value\

    >>> db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
    >>> print db['cleese.png']
    Photo of John Cleese doing a silly walk.
    
Many dictionary methods, like keys and items, also work with database objects.
So does iteration with a `for` statwment.
    
    >>> for key in db:
    >>>     print key
    
As with other files, you should close the database when you are done
    
    >>> db.close()
    
## Pickling

A limitation of `anydbm` is that the keys and values have to be strings. If you try to use any other type, you get an error.

`pickle.dumps` takes an object as a parameter and returns a string representation (dumps is short for 'dump string')

    >>> import pickle
    >>> t = [1, 2, 3]
    >>> pickle.dumps(t)
    '(lp0\nI1\naI2\naI3\na.'
    
`pickle.loads("load string")` reconstitutes the object
    
    >>> t1 = [1, 2, 3]
    >>> s = pickle.dumps(t1)
    >>> t2 = pickle.load(s)
    >>> print t2
    [1, 2, 3]
 
 Although the new object has the same value as the old, it is not (in general) the same object:
 
    >>> t1 = t2
    True
    >>> t1 is t2
    False
    
 In fact, this combination is so common that it has been encapsulated in a module called `shelve`
 
 ## 14.8 Pipes
 
 ## 14.9 Writing modules
 
 Programs that will be imported as a module often use the following idiom:
    
    If __name__ == '__main__':
        print 'something'
  
 `__name__` is a built-in variable that is set when the program starts.
 If the program is running as a script, `__name__` have the value `__main__`; in that case, the test code is executed.
 Otherwise, if the module is imported, the test code is skipped.
 
 ## 14.10 Debugging
 
 Escape Character 
 > \t tab
 
 > \n newline
 
 When you are reading and writing files, you might run into problems with whitespace. 
 These errors can be hard to debug because spaces, tabs and newlines are normally invisible.
 The built-in function `repr` can help.it takes any object as an argument and returns a string representation of the object.
 
 ## 14.11 Glossary
 
 - **persistent:** Pertaining to a program that runs indefinitely and keeps at least some of its data in permanent storage.
 - **format operator:** An operator, `%`, that takes a format string and a tuple and generates a string that includes the elements of the tuple formatted as specified by the format string.
 - **format string:** A string, used with the format operator, that contains format sequences.
 - **format sequence:** A sequence of characters in a format string, like %d, that specifies how a value should be formatted.
 - **text file:** A sequence of characters stored in permanent storage like a hard drive.
 - **directory:** A named collection of files, also called a folder.
 - **path:** A string that identifies a file.
 - **relative path:** A path that starts from the current directory.
 - **absolute path:** A path that starts from the topmost directory in the file system.
 - **catch:** To prevent an exception from terminating a program using the `try` and `except` statements.
 - **database:** A file whose contents are organized like a dictionary with keys that correspond to values.
 
 # 15 Classes and objects
 
## 15.1 User defined types

A class definition looks like this:

    Class Point(object):
        """Represents a point in 2-D space"""
        
## 15.2 Attribution

You can assign to an instance using dot notation
    
    >>> blank,x = 3
    >>> blank.y = 4

You can use dot notation as part of any expression:

    >>> print '(%g, %g)' % (blank.x, blank.y)
    (3.0, 4.0)

You can pass an instance as an argument in the usual way.

    >>> def print_point(p):
    >>>     print '(%g, %g) % p.x, p.y
    
## 15.3 Rectangles

    class Rectangle(object):
        """
        Represents a rectangle.
        
        attributes: width, height, corner.
        """
        
To represent a rectangle, you have to instantiate a Rectangle object and assign values to the attributes:

    box = Rectangle()
    box.with = 100.0
    box.height = 200.0
    box.cornor = Point()
    box.cornor.x = 0.0
    box.cornor.y = 0.0
    
An object that is an attribute of another object is **embedded**.

## 15.4 Instances as return values

    def find_center(rect):
        p = Point()
        p.x =rect.cornor.x +rect.width/2.0
        p.y = rect.cornor.y + rect.height/2.0
    return p
    
## 15.5 Objects are mutable

## 15.6 Copying

Copying an object is often an alternative to aliasing.
The `copy` module contains a function called `copy` that can duplicate any object

    >>> p1 = Point()
    >>> p1.x = 3.0
    >>> p1.y = 4.0
    
    >>> import copy
    >>> p2 = copy.copy(p1)

`p1` and `p2` contain the same data, but they are not the same point.

    >>> p1 is p2
    >>> False
    >>> p1 == p2
    >>> False

The `is` operator indicates that `p1` and `p2` are not the same object, which is what we expect.
But you might have expected `==` to yield `True` because these points have the same data.
In that case, you will be disappointed to learn that for instances, the default behavior of the `==` operator is the same as the `is` operator.
It checks objects identity, not object equivalence.

IF you use `copy.copy` to duplicate a Rectangle,you will find that it copies the Rectangle but not the embedded Point.

    >>> box2 = copy.copy(box)
    >>> box2 is box
    False
    >>> box2.corner is box.corner
    True

This operation is called **shallow copy** because it copy the object and any references it contains, but not the embedded objects.

Fortunately, the `copy` module contains a method named `deepcopy` that copies not only the object but also the object it refer to.

## 15.7 Debugging

If you try to access an attribute that doesn't exist, you get an `AttributeError`

If you are not sure whether an object has a particular attribute, you can use the built-in function `hasattr`:

    >>> hasattr(p, 'x')
    True
    >>> hasattr(p, 'z')
    False

The first argument can be any object; the second argument is a `string` that contains the name of a attribute.

## 15.8 Glossary

- **class:** A user-defined type. A class definition create a new class object.
- **class object:** An object that contains information about a user defined type. The class object can be used to create the instances of this type.
- **instance:** An object that belongs to a class.
- **attribution:** One of the named values associated with an object.
- **embedded (object):** An object that is stored as a attribute of another object.
- **shallow copy:** To copy the contents of an object, including any references to embedded objects;implemented by the copy function in the `copy` module.
- **deep copy:** To copy the contents of an object as well as any embedded objects, and any objects embeded in them, and so on.implemented by the `deepcopy` function in the copy module.
- **object diagram:** A diagram that shows objects, their attributes, and the value of the attributes. 

# 16 Classes and functions

## 16.1 Time

`%`, string formatting:

syntax: %[(name)][flag][width].[precision]typecode

## 16.2 Pure functions

A development plan called prototype and patch. > pure function > improved version

## 16.3 Modifiers

Sometimes it is useful for a function to modify the object it get as a parameters. In that case, the changes are visible to the caller. Functions that works in this way are called modifier.

## 16.4 Prototyping versus planning

## Debugging

Using an `assert` statement, which checks a given invariant and raises an exception if it fails.
    
    def add_time(t1, t2):
        assert valid_time(t1) and valid_time(t2)
        second = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

## 16.6 Glossary

- **prototype and patch:** A development plan that involves writing a rough draft of a program, testing, and correcting errors as they are found.
- **planned development:** A development plan that involves high-level insight into the problem and more planning than incremental development or prototype development.
- **pure function:** A function that does not modify any of the objects that it receives as arguments. Most modifiers are fruitless.
- **functional programming style:** A style of program design in which the majority of functions are pure.
_ **invariant:** A condition that should always be true during the execution of a program.

# 17 Classes and methods

## 17.1 Object-oriented features

In the `Time` program, there is no obvious connection between the class definition and the function definitions that follow.
With some examination, It is apparent that every functions takes at least one `time` object as an argument.
This observation is the motivation for `methods`.
A `method` is a function that is associated with a particular class.

Methods are semantically the same as functions; but there are two syntactic differences:

- Methods are defined inside a class definition in order to make the relationship between the class and the method explicit.
- The syntax for invoking a method is different from the syntax for calling a function.

## 17.2 Print object

    Class Time(object):
        
        def print_time(time):
            print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
Now there are two ways to call print_time.

The First (and less common) way is to use function syntax:

    >>> Time.print_time(start)
    09:45:00

In this use of dot notation, Time is the name of the class, and print_time is the name of the method. `start` is passed as a parameter.

THe second (and more concise) way is to use method syntax:

    >>>start.print_time()
    09:45:00
    
In this use of dot notation, print_time is the name of the method (again), and start is the object the method is invoked on, which is called the subject.

Inside the method, the subject is assigned to the first parameter, so in this case `start` is assigned to `time`.

By convention, the first parameter of a method is called `self`, so it would be more common to write `print_time` like this:
    
    class Time(object):
        def print_time(self):
            print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
            
The reason for this convention is an implicit metaphor:

- The syntax for a function call, `print_time(start)`, suggests that the function is the active agent. It says something like, "Hey print_time! Here's an object for you to print."
- In object-oriented programming, the objects are the active agents. A method invocation like `start.print_time()` says, "Hey start! Please print yourself"

## 17.3 Another example

Here's a version of increment rewritten as a method:
    
    # inside class Time:
        def increment(self, seconds)
            seconds += self.time_to_int()
            return int_to_time(seconds)
            
Here's how you would invoke increment:
    
    >>> start.print_time()
    09:45:00
    >>> end = start.increment(1337)
    >>> end.print_time()
    10:07:17
    
The subject, `start`, gers assigned to the first parameter, `self`. The argument, `1337`, gets assigned to the second parameter, `seconds`.

This mechanism can be confusin, especially if you make an error. For example, if you invoke `increment` with two arguments, you get:

    >>> end = start.increment(117,249)
    TypeError: increment() takes exactly 2 arguments (3 given)
    
The error message is initially confusin, because there are only two arguments in parentheses. But the subject is also considered an argument, so all together that's three.

## 17.4 A more complicated example

## 17.5 The init method 

The `__init__` method (short for initalization) is a special method that gets invoked when an object is instantiated.

    #inside class Time
        
        def __init__(self, hour=0, minute=0, second=0):
            self.hour = hour
            self.mimute = minute
            self.second = second

It is common for the parameters of `__init__` to have the same names as the attributes.

The parameters are optional, so if you call Time with no arguments, you get the default values.

    >>> time = Time()
    >>> time.print_time()
    00:00:00

If you provide two argument, it overrides hour and minute:

    >>> time = Time(9, 45)
    >>> time.print_time()
    09:45:00
    
## 17.6 The `__str__` method

`__str__` is a special method, like `__init__` , that is supposed to return a string representation of an object.

For example, here is a `__str__` method for Time objects:
    
    inside class Time:
        def __str__(self):
            return '%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)

when you print an object, Python invokes the `str` method

    >>> time = Time(9, 45)
    >>> print time
    09:45:00
    
When you write a new class, you should always start by writing `__init__`, which makes it easier to instantiate objects, and `__str__`, which is useful for debugging.


## 17.7 Operator overloading

By defining other special methods, you can specify the behavior of operators on user-defined types.
For example, if you define a method named `__add__` for the Time class, you can use the + operator on Time objects.

    # inside class Time:
        def __add__(self, other):
            seconds = self.time_to_int() +other.time_to_int()
            return int_to_time(seconds)
            
Here is how you use it:
    >>> start = Time(9, 45)
    >>> duration = Time(1, 35)
    >>> print start + duration
    11;20:00
    
## 17.8 Type-based dispatch

In the previous section we added two Time objects, but you also might want to add an integer to a Time object.
The following is a version of `__add__` that checks the type of `other` and invokes either add_time or increment.
    
    # inside class Time:
    
        def __add__(self,other):
            if isinstance(other, Time):
                return self.add_time(other)
            else:
                return self.increment(other)

The built-in function `isinstance` takes a value and a class object, and returns True if the value is an instance of the class.

Unfortunately, this implementation of addition is not commutative. If the integer is the first operand, you get:
    
    >>> print 137 + start
    TypeError: unsupported operand type(s) for +: `int` and `instance`
    
But there is a clever solution for this problem: the special method `__radd__`, which stands for "right-side add." 
This method is invoked when a Time object appears on the right side of the + operator.

    # inside class Time:
        def __radd__(self, other):
            return self.__add__(other)
            
## 17.9 Polymorphism

Functions that can work with several types are called **polymorphic**. Polymorphism can facilitate code reuse.
For example, the built-in function `sum`, which adds the elements of a sequence, works as long as the elements of the sequence support addition.

Since Time objects provide an `add` method, they work with `sum`:
    
    >>> t1 = Time(7, 43)
    >>> t2 = Time(7, 41)
    >>> t3 = Time(7, 37)
    >>> total = sum([t1, t2, t3])
    >>> print total
    23:01:00

## 17.10 Debugging

If you are not sure whether an object has a particular attribute, you can use the built-in function `hasattr`.

Another way to access the attributes of an object is through the special attribute `__dict__`, which is a dictionary that maps attribute names (as strings) and values:
    
    >>> p = Point(3, 4)
    >>> print p.__dict__
    
For purpose of debugging, you might find it useful to keep this function handy.

    def print_attributes(obj):
        for attr in obj.__dict__:
            print attr, getattr(obj, attr)

The built-in function `getattr` takes an object and an attribute name (as string) and returns the attribute's value.

## Interface and implementation (Hard to understand)

A design principle that helps achieve that goal is to keep interfaces separate from implementations.
For objects, that means that the methods a class provides should not depend on how the attributes are represented.

## 17.12 Glossary

- **object-oriented language:** A language that provides features, such as user-defined classes and method syntax, that facilitate object-oriented programming.
- **object-oriented programming:** A style of programming in which data and the operations that manipulate it are organized into classes and methods.
- **subject:** The object a method is invoked on.
- **operator overloading:** Changing the behavior of an operator like + so it works with a user-defined type.
- **type-based dispatch:** A programming pattern that checks the type of an operand and invokes different functions for different types.
- **polymorphic:** Pertaining to a function that can work with more than one type.
_ **imformation hiding:** The principle that he interface provided by an object should not depend on its implementation, in particular the representation of its attributes..