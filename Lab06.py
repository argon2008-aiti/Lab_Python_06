# Part II

import datetime

# class definition
class Player:
    #__init__() method initializes the object with the parameters provided
    def __init__(self,firstname,lastname,team=None):

        self.first_name = firstname  # assign any instance of the class' first_name to firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,date,score):  # this function adds scores to a player's tally
        for a_score in score:
            self.scores.append(a_score)

    def total_score(self):    # this function returns the sum of a player's scores
        return sum(self.scores)

    def average_score(self):   # this function returns the average score by  a player
        return self.total_score()/len(self.scores)

torres = Player( 'Fernando' , 'Torres' , 'Spain' ) #initialize torres as an instance of Player class

#use the add_score method to add scores to torres' tally

torres.add_score( [''], [ 0, 0, 1, 0, 1 ]) 


#find torres' average
torres.average_score()




# Part III

class Team:     # class definition

    # initialize any instance of the class with the provided parameters
    def __init__(self, name, league, manager_name, points=0 ):
        self.name = name
        self.league = league
        self.manager = manager_name
        self.points = points
        self.players = []

    def __str__(self):
        print 'league:', self.league, 'points:', self.points

    def add_player( self, player ):
        self.players.append(player)
        return None


portugal = Team( 'Portugal', 'euro cup 2012' , 'Jose Murinho', 14 )

spain    = Team( 'Spain', 'euro cup 2012', 'Raphael Benitez', 17 )

torres = Player( "Fernando", "Torres", spain.name )

ronaldo = Player( "Cristiano", "Ronaldo", portugal.name )

portugal.add_player( "C. Ronaldo" )

spain.add_player( "F. Torres" )




class Match:
    def __init__( self,home_team, away_team, date ):
        self.home_team = home_team
        self.away_team = away_team
        self.home_scores = {}
        self.away_scores = {}

    def home_score(self):
        return sum(self.home_scores.values())

    def away_score(self):
        return sum(self.away_scores.values())

    def winner(self):
        if self.home_score() > self.away_score():

            return self.home_team
 
        return self.away_team
    
    def add_score( self, player, score ):
        player_team = player.team
        if player_team == self.home_team:
            if player.last_name not in self.home_scores:
                self.home_scores[player.last_name] = score
            else:
                self.home_scores[player.last_name] += score
        else:
            if player.last_name not in self.away_scores:
                self.away_scores[player.last_name] = score
            else:
                self.away_scores[player.last_name] += score

        return None

euro_semi_final = Match( 'Spain', 'Portugal', datetime.date(2012,6,27).__format__('') )
    
    
euro_semi_final.add_score( torres, 1 )

euro_semi_final.add_score( ronaldo, 1 )

euro_semi_final.add_score( torres, 1 )

print 'winner of the game is', euro_semi_final.winner()

        

