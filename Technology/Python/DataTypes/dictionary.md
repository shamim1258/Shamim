# Dictionary

-  It represents data in key, value pair where key can any immutible data-type example integer or string.
-  Methods - clear(), copy(), formkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()
-  Few most common methods :
   -  items
      -  Syntax : `dict.items()`
      -  Return object type is dict_item which is view of key,value pair
      -  Example :
^
   d = {1: 300, 2:500, 3:100, 4: 200, 5:400}
   i = d.items()
   print(i)
   Output :: [(1,300), (2,500), (3,100), (4,200), (5,400)]
^
-  Advance Dictionay concepts :
  -  Python dictionaries are implemented as hash tables.
  -  Hash tables must allow for hash collisions i.e. even if two distinct keys have the same hash value, the table's implementation must have a strategy to insert and retrieve the key and value pairs unambiguously.
  -  Each entry in the table is actually a combination of the three values `< hash, key, value >`.
  -  The keys of the dictionary are hashable i.e. the are generated by hashing function which generates unique result for each unique value supplied to the hash function.
-  Write A Program :
  -  To merge 2 dict.
^
This is the best solution where ** represents unpacking
{**d1, **d2}
^
