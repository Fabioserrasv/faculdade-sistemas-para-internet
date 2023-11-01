revert = lambda x: lambda y, z: x(y, z) * -1

def compare(i1, i2):
    if i1.get_solution_rating() == i2.get_solution_rating():
        return 0   
    return 1 if i1.get_solution_rating() > i2.get_solution_rating() else -1
