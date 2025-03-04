def greet(name):
    return f"HI, {name}"


# can do this if function body one line
# lambda expression/ lambda function
greet1 = lambda name: f"HI, {name}"

# print(greet1("Jevan"))


def add(n1, n2):
    return n1 + n2


# 1. anonymous - nameless functions
# 2. one liner
# 3. implicit return (automatically)
add = lambda n1, n2: n1 + n2
# print(add(1, 2))


# map and fliter

player_stats = [10, 30, 60]

# take in mat and iterable
boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))

# higher order functions take function as argument
# function is called with elements behind the scenes
# map calls: lambda(element)
boosted_stats = map(lambda x: x * 2, [10, 30, 60])

# 1. def - reuse else where
# 2. lambda - one time use, concise


# filter --> higher order function
# HOF --> filter and map
gt1 = lambda x: x > 10  # predicate returns boolean values
# filter always expects predicate
result = filter(gt1, [10, 30, 60])
print(result, list(result))


# -------------------------------------------------------------------------------
#                   WHEN TO USE MAP AND WHEN TO USE FILTER
# -------------------------------------------------------------------------------

#                                  MAP
#               1. len(input_list) = len (output_list)
#               2. Transform data type
#               3. copy the list. original list not affected

#                                 FILTER
#               1. len(input_list) >= len (output_list)
#               2. Input data_type = output data_type. doesnt change data type
#               3. copy the list. original list not affected
