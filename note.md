## Control Flow

1. decision tree
   - `if...else`
   - `if...elif...else`
2. loops
   - `while`
   - `for`

## Loops

- simple repeating executions

### While

Execute statements while the condition true

```py
while(condition)
```

```py
i = 1

while i <= 3:
    print("vote for Jevan")
    i = i + 1
```

### For

- `range()` always starts at 0
- `range()` excludes the end value
- `for` and `range()` takes care of incrementing variable
- step default value is 1

```py
for variable in range(end_value)
```

```py
for j in range(3):
    print(j)
```

## GIT

Git is a version control system

### What letters mean

- `U` means untracked file
- `A` means files added

### Steps to Push to Git

1. `git init`
2. Stage All
3. Provide Message - Why? > What?
4. When to Commit?
   1. _Commit at least 3 times in an hour_
   2. _Logical commit - Complete commit (No bugs)_
   3. _Small Commit_
5. Commit (Save Point)
6. Sync to Github (online)

- _`Blue(master)`_ offline
- _`Purple(origin/master)`_ online
