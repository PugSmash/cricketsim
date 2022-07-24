from classes import Game, Team, Player

Roy = Player("Jason", "Roy", 1, 0, 3, 78, 20)
Bairstow = Player("Johnny", "Bairstow", 1, 0, 1, 83, 34)
Salt = Player("Phil", "Salt", 1, 0, 3, 76, 45)
Root = Player("Joe", "Root", 1, 0, 3, 90, 67)
Butler = Player("Jos", "Butler", 1, 0, 1, 81, 9)
Livingstone = Player("Liam", "Livingstone", 1, 0, 4, 78, 56)
Ali = Player("Moeen", "Ali", 3, 0, 3, 74, 77)
Curran = Player("Sam", "Curran", 2, 0, 1, 57, 78)
Willey = Player("David", "Willey", 2, 0, 2, 45, 81)
Rashid = Player("Adil", "Rashid", 2, 0, 4, 30, 84)
Topley = Player("Reece", "Topley", 2, 0, 1, 43, 81)

Malan = Player("Janneman", "Malan", 1, 0, 1, 79, 34)
DeCock = Player("Quinton", "De Cock", 1, 0, 1, 86, 42)
VanDerDussen = Player("Rassie", "Van Der Dussen", 1, 0, 1, 84, 23)
Markram = Player("Aiden", "Markram", 1, 0, 3, 78, 68)
Klassen = Player("Heinrick", "Klassen", 3, 0, 3, 74, 43)
Miller = Player("David", "Miller", 1, 0, 1, 77, 34)
Pretorius = Player("Dwaine", "Pretorius", 1, 0, 1, 76, 43)
Maharaj = Player("Keshav", "Maharaj", 2, 0, 3, 53, 83)
Nortje = Player("Anrich", "Nortje", 2 ,0, 1, 34, 79)
Ngidi = Player("Lungi", 'Ndidi', 2, 0, 1, 54, 87)
Shamsi = Player("Tabraiz", "Shamsi", 2, 0, 4, 32, 81)

eng_players = [Roy, Bairstow, Salt, Root, Butler, Livingstone, Ali, Curran, Willey, Rashid, Topley]
sa_players = [Malan, DeCock, VanDerDussen, Markram, Klassen, Miller, Pretorius, Maharaj, Nortje, Ngidi, Shamsi]

ENG = Team("England", 0, eng_players)
SA = Team("South Africa", 0, sa_players)

match = Game(50, ENG, SA)

print(ENG)
print(SA)

match.toss()

for i in range(match.total_overs):
    match.bowl_over()