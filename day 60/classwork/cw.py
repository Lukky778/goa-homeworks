#1
def count_arara(n):
    result = []
    while n >= 2:
        result.append("adak")
        n -= 2
    if n == 1:
        result.append("anane")
    return " ".join(result)

#2
def is_planet_mnemonic_correct(solar_system, mnemonic):
    planets = [planet for planet in solar_system if planet != "Asteroid"]

    words = mnemonic.split()
    
    if len(planets) != len(words):
        return False
    
    for planet, word in zip(planets, words):
        if planet[0].lower() != word[0].lower():
            return False
    
    return True


#3
def max_possible_score(points, seen):
    total = 0
    for question, score in points.items():
        if question in seen:
            total += score * 2
        else:
            total += score
    return total
