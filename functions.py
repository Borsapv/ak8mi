import random


repetitions = 30
dimensions_5 = 5
dimensions_10 = 10
dimensions_10 = 20
iterations = 10000
iterations_local = 1000

range_min = -5
range_max = 5

#creates random n-dimensional array / vector)

def new_random_item(r_min, r_max, dim):
    items = []

    for x in range(dim):
        random_num = round(random.uniform(r_min, r_max), 5)
        items.append(random_num)

    return items

# counts f(x)
def fcost_first_de_jong(items):
    current_value = 0
    for x in range(len(items)):
        current_value += items[x] ** 2

    return current_value

# RANDOM SEARCH #
def apply_first_de_jong_random_search():
    best_random_values = []
    random_starting_point = new_random_item(range_min, range_max, dimensions_5)
    best_value = fcost_first_de_jong(random_starting_point)
    best_random_values.append(best_value)

    for x in range(iterations):
        random_items = new_random_item(range_min, range_max, dimensions_5)
        current_value = fcost_first_de_jong(random_items)

        if current_value < best_value:
            best_value = current_value
            best_random_values.append(best_value)

    return best_random_values




# HILL CLIMBING
def apply_first_de_jong_hill_climbing_v2():
    random_starting_point = new_random_item(range_min, range_max, dimensions_5)

    local_vector = random_starting_point
    local_current_vector = random_starting_point

    best_local_value = fcost_first_de_jong(random_starting_point)
    original = fcost_first_de_jong(random_starting_point)

    # generate sigma for local_iteratons times
    for i in range(iterations_local):
        generate_sigma = round(random.uniform(-0.5, 0.5), 5)

        for k in range(len(random_starting_point)):
            local_current_vector[k] = local_current_vector[k]+generate_sigma
            local_current_value = fcost_first_de_jong(local_current_vector)

            if local_current_value < best_local_value:
                local_vector = local_current_vector
                best_local_value = local_current_value
                print(best_local_value)

        local_current_vector = local_vector


print(apply_first_de_jong_random_search())
apply_first_de_jong_hill_climbing_v2()
