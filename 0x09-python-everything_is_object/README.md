<h1>0x09. Python - Everything is object</h1>

<h4>ALX SE project to test understanding of objects in Python. Below are reasons for responses to some of the queries:</h4>

**Task 0** - `type()` can be used to check the data type of an object.

**Task 1** - `id()` can be used to retrieve the memory address where a passed variable arg is stored.

**Task 2** - No. The two variables have been assigned references to 2 different int objects.

**Task 3** - Yes. The two variables have been assigned references to an int object of the same value.

**Task 4** - Yes. Since variables in Python do not hold the values, but hold references to the values; thus *a* is a ref to 89 while *b* is a ref to *a* and thus pointing to the same thing.

**Task 5** - No. Flowing from reasoning in task 4; since ints are immutable, a new object is created to store the value, and it's reference is then assigned to *b*.

**Task 6** - True. The `==` operator is used to check whether two variables reference objects with equal value.

**Task 7** - True. The `is` operator is used to check whether two variables point to the same object in memory.

**Task 8** - True. Same reasoning on task 6 applies.

**Task 9** - True. Same reasoning on task 7 applies.

**Task 10** - True. Same reasoning on task 6 applies.

**Task 11** - False. Since lists are mutable and can be arbitrarily changed, Python resource optimization will not assign the variables to the same object.

**Task 12** - True. Same reasoning on task 6 applies.

**Task 13** - True. Although the object (list) is mutable, var *b* points to the same value as var *b*.

**Task 14** - An in-place modification of a mutable object that is referenced by multiple variables will impact the other co-referencing variables.

**Task 15** - Same reasoning on tast 14 applies.

**Task 16** - The `+=` operand revalues an assigned element by adding the value of an input to it.

**Task 17** - `.append()` adds an item to the end of a list.

**Task 18** - Assignment gives an item a reference to an object in memory.

**Task 19** - `.copy()` performs a simple shallow copy of an object.

**Task 20** - Yes, because an empty tuple can be formed by an empty pair of parentheses.

**Task 21** - Yes, because a tuple is a collection of objects enclosed in a parentheses and separated by commas.

**Task 22** - No, because a comma must follow an expression when creating a tuple 'singleton'.

**Task 23** - Yes, becuase of the same reason that applies to task 22.

**Task 24** - True. Because the `is` operator compares the identity of two objects and returns a Boolean depending on whether they're similar or not.

**Task 25** - False.

**Task 26** - True.

**Task 27** - No.

**Task 28** - Yes. 
