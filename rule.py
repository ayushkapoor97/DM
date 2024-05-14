def violate_rule1(data):
    valid_statuses = {'setosa', 'versicolor', 'virginica'}
    counter = 0
    for status in data['species']:
        if status not in valid_statuses:
            counter += 1
    return counter


def violate_rule2(data):
    counter = 0
    for sl, sw, pl, pw in zip(data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']):
        if sl < 0 or sw < 0 or pl < 0 or pw < 0:
            counter += 1
    return counter


def violate_rule3(data):
    counter = 0
    for pl, pw in zip(data['petal_length'], data['petal_width']):
        if pl < 2 * pw:
            counter += 1
    return counter


def violate_rule4(data):
    counter = 0
    for sl in data['sepal_length']:
        if sl > 30:
            counter += 1
    return counter


def violate_rule5(data):
    counter = 0
    for pl, sl in zip(data['petal_length'], data['sepal_length']):
        if sl <= pl:
            counter += 1
    return counter


def count_violations(data):
    violations_count = {
        'Rule 1': violate_rule1(data),
        'Rule 2': violate_rule2(data),
        'Rule 3': violate_rule3(data),
        'Rule 4': violate_rule4(data),
        'Rule 5': violate_rule5(data)
    }
    return violations_count
