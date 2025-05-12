#1
double_char = lambda s: ''.join(c * 2 for c in s)


#2
get_average = lambda marks: sum(marks) // len(marks)


#3
def get_planet_name(id):
    if id == 1:
        return "Mercury"
    elif id == 2:
        return "Venus"
    elif id == 3:
        return "Earth"
    elif id == 4:
        return "Mars"
    elif id == 5:
        return "Jupiter"
    elif id == 6:
        return "Saturn"
    elif id == 7:
        return "Uranus"
    elif id == 8:
        return "Neptune"
    return ""  

#4
sum_str = lambda a, b: str(int(a or '0') + int(b or '0'))


#5
def merge_arrays(arr1, arr2):
    merged = arr1 + arr2
    merged = list(set(merged))
    merged.sort()
    return merged
