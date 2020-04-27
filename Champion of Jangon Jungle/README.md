## CREATING A TEXT BASED GAME IN PYTHON:

Champion to Jangon Jungle is an adventurous game and its starts with a premise built on the theme of a flight crash in the Jangon Jungle.  The plot starts with the Player who was traveling in a plane with his friend to Jangon Jungle in search of an antidote to the tame the deadly beast that was accidentally developed by the Jakall Industries during its cloning experiment. After the crash, the player wakes up to find a girl next to him who saved his life. The player is weak and is losing his health and has lost his friend after the plane crash. He must regain and maintain his health and must also search for his friend along with the antidote in the Jangon Jungle. The girl in the game later needs you to save her father who is trapped in the muck of the Jangon Jungle and needs rescuing. It is her father who is clue on solving this game and you need to save him to win the game. 
The Jangon Jungle game is set up in five arenas namely the Mangroves, Falls, Mines, Meadow and Muck. All these arenas are both positively and negatively marked in terms of energy requirement. While some levels require you to spend energy, the others will help you in gaining energy to maintain health which is essential for being alive in the game. The energy, arenas, items collected by the player and moves followed are all separately monitored in the game in variables:


    Energy_Stats: A list
    Moves_Record: A list
    Arena: A list
    moves: an integer
    energy: an integer

Functions used:


    game() #For beginning game
    jangon(arena, Moves_Record) # For entering the game arena
    falls(Moves_Record,EnergyStats, Items, arena) # At Falls
    meadow(Moves_Record,EnergyStats, Items, arena) #At Meadows
    crossroads(Moves_Record) #At crossroads
    mines(Moves_Record, EnergyStats, Items , arena) #At mines
    mangrove(Moves_Record, EnergyStats, Items, arena) #At mangroves
    muck(Moves_Record, EnergyStats, Items, arena) #At muck
    scorpion_attack(Moves_Record, EnergyStats,Items,arena) # Encounter Scorpion
    energy_check(energy) #Check energy level and check if player’s energy is 0 or below 
    game_over(EnergyStats, Items, arena) # Game over shows stats and graphs


 All the five arenas of the game further have some challenges, characters and items that will help the player in winning the game eventually.
 The characters, challenges, items and health points in the arenas are as follows:
1)	Mangroves:  It has a scorpion encounter and a deadly beast encounter in it. (Health points: -10xp) 
2)	Falls: The friend and a rope are in this arena. (Health Points: -20xp)
3)	Mines: Mines have the antidote, treasure. (Health Points: -20xp)
4)	Meadow: The meadow leads to house of chieftain, scorpion encounter and muck as well. (Health Points: +100xp)
5)	Muck: The muck has the girl’s father drowning in quagmire and rewards sword and clue in it. (Health Points: +50xp)

The easiest way to win the game is 
1)	 go to the falls first, find the friend, save him and take the rope.
2)	 Then, the Meadows should be chosen to maintain the health.
3)	enter the Muck and save the girl’s father and get the sword from there.
4)	 Enter Mines and don’t choose both the antidote and treasure
5)	enter the Mangroves defeat scorpion with sword and tame beast with the antidote

