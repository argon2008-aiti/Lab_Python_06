"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure

# I use a dictionary with player names as keys and dates and scores as values
import datetime

player_stats ={ 'rooney' : ([ datetime.date( 2012, 6, 23) , 2 ] , [ datetime.date( 2012, 6, 25), 2 ]) ,
                'ronaldo': ([ datetime.date( 2012, 6, 19 ) , 0 ] , [ datetime.date( 2012, 6, 20 ) , 3 ]),
                'torres' : ([ datetime.date( 2012, 6, 21 ) , 0 ] , [ datetime.datetime( 2012, 6, 21 ) , 1 ]) }

# I chose list in dictinaries because dictionaries have key, value pairs which can help me store and access the data
# easily

## implement highest_score

def highest_score( player_stats ):     # function definition with statics of players as parameter
    result_tup = ('')           # an empty tuple to store the final result
    max_score = 0               # variable to store the highest score
    score = 0                    # the score so far after an iteration
    who_is = ''                 # empty string to store name of player with highest score
    match_date = 0               # variable to get the match date on which the highest score occurs
    
    for player in player_stats:    # iterate over all players in 'player_stats'
        
        for i in range( 0 , 2 ):           # check on which date a player occurs the highest
            score = player_stats[player][i][1]
            
            if score > max_score:          # if a players score is higher than any previous one, assign to
                max_score = score          # 'max_score'
                who_is = player            # also record the player with the highest so far as well as the            
                match_date = player_stats[player][i][0]   #match date for which the highest occurs

    result_tup = ( who_is,) + ( match_date.__format__(''),) + (max_score,)  #save the result in a tuple
    return result_tup
            
    

                
            
        



## implement highest_score_for_player

def highest_score_for_player( player_stats, player ): #function definition takes a player as parameter
    if player in player_stats:                       # if the player exist our statistics,
        return max( player_stats[player][0][1], player_stats[player][1][1] )  # cal the highest goal scored by that
    return None                                 # player



## implement highest_scorer

def highest_scorer(player_stats):    # function definition takes no argument
    total_goals = 0       # variable to store the total for a particular player
    
    player_with_highest = '' # name of player with the highest sum of goals so far

    for player in player_stats:   # loop through players available in our dictionary

        # find the sum of all the goals scored by that player
        
        player_max_score = sum( [player_stats[player][0][1],player_stats[player][1][1]] )
        # assign 'player_max_score' to total goals if its higher
        if player_max_score > total_goals:
            
            total_goals = player_max_score
            player_with_highest = player

    return player
