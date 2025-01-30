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
