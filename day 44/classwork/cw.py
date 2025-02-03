#1
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)  
    return result


#2
def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planets.get(id)


#3
def human_years_cat_years_dog_years(human_years):

    dog = 15
    cat = 15
    if (human_years == 1):
        return [ human_years , dog, cat]
    elif (human_years == 2):
        return [  human_years , dog + 9, cat + 9]
    
    return [human_years, (dog + 9) + ((human_years-2) * 4), (cat + 9) + ((human_years - 2) *5)]

#4
def twice_as_old(dad_years_old, son_years_old):
    if dad_years_old >= 2 * son_years_old:
        return dad_years_old - 2 * son_years_old
    else:
        return 2 * son_years_old - dad_years_old
