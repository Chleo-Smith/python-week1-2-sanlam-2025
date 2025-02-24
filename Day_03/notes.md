# Python - Day 03

- Operators 2
- string methods
  - `index() `
  - `count()`
  - `find()`
- List
- List methods

## Shortcuts

- `alt ➕ ⬆️` ➡️ to move lines
- `!<tab>` ➡️ boiler plate code
- `win ➕ .` ➡️ emojis
- `Ctrl ➕ /` ➡️ comment
- `Ctrl ➕ <space>` ➡️ auto complete
- `ctrl ➕ d` ➡️ multi cursor (similar items)
- `hold Alt` ➡️ Multi cursor (different items)

## QUESTION 4

```Python
load = input("Please enter your number: ")
loader = int(load) // 10
output = loader * "="
blank = (10 - loader) * " "
print(f"[{output}{blank}] {load}%")
```

```js
Console.log(5);
```

## Operators

1. Floor divison
   ```Python
   7 // 2 = 3
   ```
2. Exponentiontion
   ```Python
   2 ** 2 = 4
   ```
3. Modulus
   ```Python
   7 % 3 = 1
   ```

> concatenate - **cannot** mix data _types_
>
> `str + int` -> no

## references

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Tables](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet#tables)

| Operator |             function             |      example |
| -------- | :------------------------------: | -----------: |
| `//`     | Floor divison / integer division | `7 // 2 = 3` |
| `**`     |          exponentiation          | `2 ** 2 = 4` |
| `%`      |             modulus              |  `7 % 3 = 1` |
| `+`      |             addition             |  `1 + 1 = 2` |

## Notes

- -----: right aligned
- :-------------: center aligned
- `CONST_CASE` all capitals
- `python` in terminal to access REPL
- `print(...,...)` print multiple values
- `20 * "*"` print things out 20 times
- if any value `false` output false
- `Ctrl ➕ ~` pen and close terminal
- all comparison and logical operators return boolean
- Evaluate expression from L -> R
- `word[start:end]` end index not included
- `word[:]` can be used to copy string
- `word[start index:end index:step]` step dictates how many letters we move
- if step value negative we move backwards through string
- `print(movie[-4:-1:-1])` if no way to get there its blank
- strings are immutable and changed when manipulated
- `strip()` removes leading and trailing items
- dot chaining: `variable.function().function()`. only works when chaining on the same data type.
- Lexical order when comparing values number values that are strings `"180" > "20"` it only considers the first letter. so `20 will be considered greater than 180`

```Python
comparison operators
# Equal
print(5 == 5)
# Not Equal
print(5 != 3)
# Greater Than
print(5 > 3)
# Less Than
print(3 < 5)
# Greater Than or Equal to
print(5 >= 5)
# Less Than or Equal to
print(3 <= 5)

logical operators
#and
print(True and True)
#or
print(True or False)
#not
print(not True)
```

## `and`

- If any is `False` then `False`
- Only both `True` then `True`

| Operator          |  Output |
| ----------------- | ------: |
| `True and True`   |  `True` |
| ` True and False` | `False` |
| `False and True`  | `False` |
| `False and False` | `False` |

## `or`

- If any is `True` then `True`
- Only both `False` then `False`

| Operator         |  Output |
| ---------------- | ------: |
| `True or True`   |  `True` |
| ` True or False` |  `True` |
| `False or True`  |  `True` |
| `False or False` | `False` |

```
>>> (3 < 4) and (10 >= 5)
True
>>> (5 != 10) or (800 < 5)
True
>>> ( (80 % 5) == 0) and ( (3 * 6) == 35)
False
>>> ( 7 > 5 ) and (4 != 4 ) or (3 <= 10)
True
>>>

```

## String opertors

- index always starts with 0 `print(word[index])`
-

## control flow

1. decision tree
   - `if...else`
   - `if...elif...else`
2. loops
   - `while`
   - `for`
