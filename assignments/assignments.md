# Python Fundamentals Assignment: Data Manipulation Masters 🧙‍♂️

These exercises are designed to challenge you with real-world data manipulation scenarios, enhancing your problem-solving skills and proficiency in Python! Let's dive into the magical world of Python data structures. 🐍✨

## Exercise Difficulty Legend

- ⭐ - Beginner
- ⭐⭐ - Elementary
- ⭐⭐⭐ - Intermediate
- ⭐⭐⭐⭐ - Advanced
- ⭐⭐⭐⭐⭐ - Expert

## Data Manipulation Challenges 📊

<details>
<summary>Exercise 1: Data Sorting and Ranking (⭐⭐)</summary>

### 🏆 Objective

Sort a complex data structure and add a ranking key based on a specific criterion.

```python
# Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93}
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.

# Your solution here:
# sorted_students = ...

def sorted_students(students):
    sorted_students =  sorted(students, key=lambda x:x["grade"], reverse=True)

    for i, student in enumerate(sorted_students):
        student["rank"] = i + 1

    return sorted_students

print(sorted_students(students))

# Expected Output
# print(sorted_students)
```

### Expected Output

```
[
    {"name": "Charlie", "grade": 93, "rank": 1},
    {"name": "Alice", "grade": 88, "rank": 2},
    {"name": "Bob", "grade": 75, "rank": 3}
]
```

</details>

<details>
<summary>Exercise 2: Merging Data from Two Lists (⭐⭐)</summary>

### 🔄 Objective

Merge data from two lists of dictionaries based on a common key.

```python
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.

# Your solution here:
# merged_data = ...

def merge_data(employees, salaries):
    merge = []
    for employee in employees:
        employee_id = employee["id"]
        for salary in salaries:
            if salary["id"] == employee_id:
                merge_entry = employee.copy()
                merge_entry.update(salary)
                merge.append(merge_entry)
                break
    return merge

print(merged_data(employees, salaries))

# Expected Output
# print(merged_data)
```

### Expected Output

```
[
    {"id": 1, "name": "Alice", "salary": 50000},
    {"id": 2, "name": "Bob", "salary": 60000}
]
```

</details>

<details>
<summary>Exercise 3: Advanced Filtering with Multiple Conditions (⭐⭐)</summary>

### 🔍 Objective

Apply multiple filtering criteria to a list of dictionaries.

```python
# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400}
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.

# Your solution here:
# filtered_products = ...

def filtered_products(products):
    filtered_list = []
    for item in products:
        if (item["category"] == "Electronics" and item["price"] < 500):
            filtered_list.append(item)
    return filtered_list

print(filtered_products(products))

# Expected Output
# print(filtered_products)
```

### Expected Output

```
[
    {"id": 3, "category": "Electronics", "price": 400}
]
```

</details>

<details>
<summary>Exercise 4: Complex Data Transformation (⭐⭐⭐)</summary>

### 🔄 Objective

Transform a list of dictionaries into a new structure.

```python
# Setup Code
orders = [
    {"order_id": 1, "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}]},
    {"order_id": 2, "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}]}
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

# Your solution here:
# product_quantities = ...

def product_quantities(orders):
    product_quantities = {}
    for order in orders:
        for item in order["items"]:
            #if order in list update

            if(item["product"] in product_quantities):
                product_quantities[item["product"]] += item["quantity"]
            else:
                product_quantities[item["product"]] = item["quantity"]
    return product_quantities

print(product_quantities(orders))

# Expected Output
# print(product_quantities)
```

### Expected Output

```
{
    "A": 3,
    "B": 3,
    "C": 1
}
```

</details>

<details>
<summary>Exercise 5: Data Consolidation and Summarization (⭐⭐⭐)</summary>

### 📊 Objective

Consolidate and summarize data from a list of dictionaries.

```python
# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"}
]
# Expected Task: Summarize the total amount spent per category.

# Your solution here:
# category_totals = ...
def category_totals(transactions):
    totals = {}

    for item in transactions:
        category = item["category"]
        amount = item["amount"]

        if(category in totals):
            totals[category] += amount
        else:
            totals[category] = amount
    return totals

print(category_totals(transactions))

# Expected Output
# print(category_totals)
```

### Expected Output

```
{
    "Food": 250,
    "Transport": 200
}
```

</details>

<details>
<summary>Exercise 6: Grouping and Aggregating Data (⭐⭐⭐)</summary>

### 📈 Objective

Group data by a specific key and perform aggregation.

```python
# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100}
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.

# Your solution here:
# sales_by_person = ...
def sales_by_person(sales):
    sales_filtered = {}
    for person in sales:
        name = person["salesperson"]
        amount = person["amount"]

        if(name in sales_filtered):
            sales_filtered[name] += amount
        else:
            sales_filtered[name] = amount
    return sales_filtered

print(sales_by_person(sales))

# Expected Output
# print(sales_by_person)
```

### Expected Output

```
{
    "Alice": 300,
    "Bob": 150
}
```

</details>

## Magical Function Manipulation 🧙‍♂️

<details>
<summary>Exercise 7: Lambda Functions for Spell Power (⭐⭐)</summary>

### ✨ Objective

Use a lambda function to sort a list of spells by their power level.

```python
# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.

# Your solution here:
# sorted_spells = ...
def sorted_spells(spells):

    return sorted(spells, key = lambda x: x[1], reverse=True)

print(sorted_spells(spells))

# Expected Output
# print(sorted_spells)
```

### Expected Output

```
[('Obliviate', 10), ('Expelliarmus', 7), ('Lumos', 5)]
```

</details>

<details>
<summary>Exercise 8: Map Transformation for Potion Ingredients (⭐⭐)</summary>

### 🧪 Objective

Transform a list of potion ingredients to their required quantities using `map`.

```python
# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.

# Your solution here:
# formatted_ingredients = ...
def formatted_ingredients(ingredients):
    return list(map(lambda ingredient: ingredient + ": 3 grams", ingredients))
print(formatted_ingredients(ingredients))
# Expected Output
# print(formatted_ingredients)
```

### Expected Output

```
['Wolfsbane: 3 grams', 'Eye of Newt: 3 grams', 'Dragon Scale: 3 grams']
```

</details>

<details>
<summary>Exercise 9: Magical Book Filter and Formatter (⭐⭐⭐)</summary>

### 📚 Objective

Combine `filter`, `map`, and lambda functions to process a list of books and format their titles.

```python
# Setup Code
books = [{"title": "A History of Magic", "pages": 100}, {"title": "Magical Drafts and Potions", "pages": 150}]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.

# Your solution here:
# formatted_titles = ...
def formatted_titles(books):

    filtered_books = filter(lambda book: book["pages"] > 120, books)
    uppercase_books = map(lambda book: book["title"].upper(), filtered_books)
    return list(uppercase_books)

print(formatted_titles(books))
# Expected Output
# print(formatted_titles)
```

### Expected Output

```
['MAGICAL DRAFTS AND POTIONS']
```

</details>

## Classes and Advanced Error Handling 🧩

<details>
<summary>Exercise 10: Wizard Duel Game Class (⭐⭐⭐⭐)</summary>

### ⚔️ Objective

Create a `WizardDuel` class where wizards can cast spells at each other until one wins.

```python
# Setup Code
class WizardDuel:
    # Your implementation here
    pass

# Example usage:
# duel = WizardDuel("Harry", "Draco", 50, 40)
# duel.cast_spell("Harry", 10)
# duel.cast_spell("Draco", 5)
# winner = duel.get_winner()
```

### Expected Output

```
After a duel between Harry and Draco, Harry wins with 10 health points left.
```

</details>

<details>
<summary>Exercise 11: Custom Error Handling in Potion Making (⭐⭐⭐)</summary>

### 🧪 Objective

Create a custom exception to handle errors in potion making, such as using the wrong ingredient.

```python
# Setup Code
class PotionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'

def brew_potion(potion_name, ingredients):
    valid_ingredients = {
        "Love Potion": ["Rose Petal", "Unicorn Hair"]
    }

    if potion_name not in valid_ingredients:
        raise PotionError(
            f"'{potion_name}' is not a valid potion."
        )

    for ingredient in ingredients:
        if ingredient not in valid_ingredients[potion_name]:
            raise PotionError(f"'{ingredient}' is not a valid ingredient for the {potion_name}.")

# Example usage:
# try:
#     brew_potion("Love Potion", ["Rose Petal", "Unicorn Hair"])
# except PotionError as e:
#     print(f"Caught PotionError: {e}")
```

### Expected Output

```
Caught PotionError: 'Eye of Newt' is not a valid ingredient for the Love Potion.
```

</details>

## Magical Data Processing 🔮

<details>
<summary>Exercise 12: Hogwarts Library Database Query (⭐⭐)</summary>

### 📚 Objective

Simulate a database query to find books by a specific author using list comprehensions.

```python
# Setup Code
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"}
]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.

# Your solution here:
# bagshot_books = ...
def bagshot_books(library):
    return [book for book in library if book["author"] == "Bathilda Bagshot"]
print(bagshot_books(library))
# Expected Output
# print(bagshot_books)
```

### Expected Output

```
[{'title': 'Magical Hieroglyphs and Logograms', 'author': 'Bathilda Bagshot'}]
```

</details>

<details>
<summary>Exercise 13: Hogwarts House Points Calculator (⭐⭐⭐)</summary>

### 🏆 Objective

Calculate the total points for each house using nested loops and a list of dictionaries.

```python
# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40}
]
# Expected Task: Aggregate points for each house and print the total.

# Your solution here:
# house_totals = ...
def house_totals(house_points):
    aggregate_points = {}
    for points in house_points:
        name = points["house"]
        amount = points["points"]

        if name in aggregate_points:
            aggregate_points[name] += amount
        else:
            aggregate_points[name] = amount
    return aggregate_points


print(house_totals(house_points))
# Expected Output
# print(house_totals)
```

### Expected Output

```
{
    "Gryffindor": 95,
    "Slytherin": 90
}
```

</details>

<details>
<summary>Exercise 14: Class Inheritance for Magical Creatures (⭐⭐⭐⭐)</summary>

### 🐉 Objective

Implement a class hierarchy for magical creatures where each subclass overrides a common method.

```python
# Setup Code
class MagicalCreature:
    # Your implementation here
    pass

class Dragon(MagicalCreature):
    # Your implementation here
    pass

class Unicorn(MagicalCreature):
    # Your implementation here
    pass

# Example usage:
# dragon = Dragon("Norwegian Ridgeback")
# unicorn = Unicorn("Silver-maned")
# dragon.sound()  # Should print "Roar"
# unicorn.sound()  # Should print "Neigh"
```

### Expected Output

```
Norwegian Ridgeback the Dragon says: Roar!
Silver-maned the Unicorn says: Neigh!
```

</details>

## Advanced Sorting and Manipulation 🔀

<details>
<summary>Exercise 15: Custom Sorting with Lambda for Magical Artifacts (⭐⭐⭐)</summary>

### 🔍 Objective

Sort a list of magical artifacts by their age and power level using a custom lambda function.

```python
# Setup Code
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7}
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.

# Your solution here:
# sorted_artifacts = ...

# Expected Output
# print(sorted_artifacts)
```

### Expected Output

```
[
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
    {"name": "Elder Wand", "age": 1000, "power": 10}
]
```

</details>

<details>
<summary>Exercise 16: Wizard Profile Generator with f-strings (⭐)</summary>

### 🧙‍♂️ Objective

Dynamically generate wizard profiles using f-strings and dictionary unpacking.

```python
# Setup Code
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.

# Your solution here:
# profile = ...

# Expected Output
# print(profile)
```

### Expected Output

```
Albus Dumbledore, the Headmaster of Gryffindor.
```

</details>

<details>
<summary>Exercise 17: Magical Creature Adoption Matching (⭐⭐⭐)</summary>

### 🦄 Objective

Match potential magical creature adopters with creatures based on preferences using `filter` and `map`.

```python
# Setup Code
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.

# Your solution here:
# matches = ...

# Expected Output
# print(matches)
```

### Expected Output

```
[('Harry', 'Fawkes'), ('Hermione', 'Dobby')]
```

</details>

<details>
<summary>Exercise 18: Advanced Potion Making with Nested Loops (⭐⭐⭐)</summary>

### 🧪 Objective

Simulate potion making where each combination of ingredients produces a unique result using nested loops.

```python
# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

# Your solution here:
# potential_potions = ...

# Expected Output
```

### Expected Output

```
Combining Moonstone and Silver Dust produces a unique potion.
Combining Moonstone and Dragon Blood produces a unique potion.
Combining Silver Dust and Dragon Blood produces a unique potion.
```

</details>

## Expert Data Challenges 🏆

<details>
<summary>Exercise 19: Nested Data Manipulation (⭐⭐⭐⭐)</summary>

### 🧩 Objective

Navigate and manipulate a nested data structure.

```python
# Setup Code
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]}
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.

# Your solution here:
# modified_data = ...

# Expected Output
# print(modified_data)
```

### Expected Output

```
[
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2", "tag4"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3", "tag4"]}
]
```

</details>

<details>
<summary>Exercise 20: Implementing a Custom Sort Function (⭐⭐⭐⭐⭐)</summary>

### 🔄 Objective

Implement a custom sort function for a list of dictionaries based on multiple criteria.

```python
# Setup Code
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False}
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").

# Your solution here:
# sorted_tasks = ...

# Expected Output
# print(sorted_tasks)
```

### Expected Output

```
[
    {"id": 1, "priority": "High", "completed": False},
    {"id": 3, "priority": "Medium", "completed": False},
    {"id": 2, "priority": "Low", "completed": True}
]
```

</details>

Good luck, Python wizards! 🧙‍♂️✨
