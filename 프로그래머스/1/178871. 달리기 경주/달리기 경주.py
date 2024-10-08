def solution(players, callings):
    players_dict = {}
    
    for i in range(len(players)):
        players_dict[i+1] = players[i]
        players_dict[players[i]] = i+1
        
    for i in callings:
        rank = players_dict[i]
        front_player = players_dict[rank - 1]
        
        players_dict[rank - 1], players_dict[rank] = players_dict[rank], players_dict[rank - 1]
        players_dict[i], players_dict[front_player] = players_dict[front_player], players_dict[i]
        
    return [players_dict[i+1] for i in range(len(players))]