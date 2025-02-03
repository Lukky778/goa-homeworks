#1
def points(games):
    total_points = 0

    for game in games:
        our_score = int(game[0])       
        opponent_score = int(game[2])

        if our_score > opponent_score:
            total_points += 3  
        elif our_score == opponent_score:
            total_points += 1  

    return total_points

#2
age = 15
binary_age = ""
while age > 0:
    binary_age = str(age % 2) + binary_age
    age = age // 2



#3
def fake_bin(x):
    result = []
    
   
    for digit in x:
       
        if int(digit) < 5:
            result.append('0')  #
        else:
            result.append('1') 
    
 
    return ''.join(result)


#4
def dna_to_rna(dna):
    return dna.replace('T', 'U')