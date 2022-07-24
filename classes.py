import random


class Player():
    def __init__(self, firstName, surname, role, highscore, bowl_type, bat_rating, bowl_rating) -> None:
        '''
        Bowl Type : 1 = Fast, 3 = Off spin, 4 = Leg spin
        Role Type : 1 = Batter, 2 = Bowler, 3 = Allrounder
        '''
        self.firstName = firstName
        self.surname = surname
        self.role = role
        self.highscore = highscore
        self.bowl_type = bowl_type
        self.bat_rating = bat_rating
        self.bowl_rating = bowl_rating
        self.ovr = (self.bat_rating + self.bowl_rating) / 2
        self.batted = False
        self.score = 0

    def bowl_ball(self, game, batsman):
        chance_of_wide = 90 - self.bowl_rating
        randomChance = random.randint(1, 100)
        if randomChance <= chance_of_wide:
            game.balls_in_over -= 1
            print("Wide")
            return 1
        else:
            if randomChance <= int(0.05*(100 - batsman.bat_rating)):
                print(f"{game.on_strike.surname} Makes a big misske and is out lbw!")
                return "W"
            elif randomChance <= 100 - int(self.bowl_rating):
                print(f"Absolute Jaffa from {game.current_bowler.surname}")
                print(f"{game.on_strike.surname} is gone!")
                return "W"
            elif randomChance <= batsman.bat_rating - 50:
                return 6
            elif randomChance <= batsman.bat_rating - 40:
                return 4
            elif randomChance <= batsman.bat_rating - 30:
                return 3
            elif randomChance <= batsman.bat_rating - 20:
                return 2
            elif randomChance <= batsman.bat_rating - 10:
                return 1
            else:
                return 0
            
            
            
            
            
            

class Team():
    def __init__(self, name, wins, players) -> None:
        self.name = name
        self.wins = wins
        self.players = players
        self.total = 0
        self.wickets = 0
        self.index = None

        for player in players:
            total =+ player.ovr
        self.ovr = total / len(self.players)
    
    def __repr__(self) -> str:
        output = "Name : role : bowl : bat : index \n"
        index = 0
        for i in self.players:
            i.index = index
            output += f"{i.firstName} {i.surname} : {i.role} : {i.bowl_rating} : {i.bat_rating} : {index} \n"
            index += 1
        return output
    

class Game():

    def __init__(self, total_overs, team_1, team_2) -> None:
        self.total_overs = total_overs
        self.team_1 = team_1
        self.team_2 = team_2

        self.batting_side = None
        self.bowling_side = None

        self.on_strike = None
        self.off_strike = None

        self.current_bowler = None
        self.balls_in_over = 1

    
    def toss(self):
        toss = random.randint(1, 2)
        if toss == 1:
            self.batting_side = self.team_1
            self.bowling_side = self.team_2
        else:
            self.batting_side = self.team_2
            self.bowling_side = self.team_1
        self.on_strike = self.batting_side.players[0]
        self.off_strike = self.batting_side.players[1]
        print(f"Welcome to this One day between {self.team_1.name} and {self.team_2.name}")
        print(f"{self.batting_side.name} will bat first")
        print(f"{self.on_strike.surname} and {self.off_strike.surname} will open")

    def bowl_over(self):
        self.current_bowler = self.bowling_side.players[int(input("What number bowler do you want? "))]
        while (self.balls_in_over <= 6) and (self.batting_side.wickets < 10):
           outcome = self.current_bowler.bowl_ball(game=self, batsman=self.on_strike)
           if outcome == "W":
            self.batting_side.wickets += 1
            ok = True
            while ok:
                player_choice = self.batting_side.players[int(input("What number batter do you want? "))]
                if player_choice.batted == True:
                    pass
                else:
                    self.on_strike = player_choice
                    print(f"{self.on_strike.surname} is on strike")
                    ok = False
            self.balls_in_over += 1
           else:
            self.batting_side.total += outcome
            self.on_strike.score += outcome
            self.balls_in_over += 1
            if outcome % 2 == 0:
                pass
            else:
                self.on_strike, self.off_strike = self.off_strike, self.on_strike
           print(f"{self.batting_side.name}: {self.batting_side.total}-{self.batting_side.wickets}")
        self.balls_in_over = 0

    def summary(self):
        print("\n")
        print(f"{self.on_strike.surname} : {self.on_strike.score}")
        print(f"{self.off_strike.surname} : {self.off_strike.score}")
        print(f"{self.batting_side.name}: {self.batting_side.total}-{self.batting_side.wickets}")
        print("\n")