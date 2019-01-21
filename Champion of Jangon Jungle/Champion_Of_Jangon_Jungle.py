# This is a Python Based Text Game called, "The Champion of Jangon Jungle". 
# A Player starts playing the game by entering his name credentials and consent to play.
# The game takes the player through a series of text based quests and the performance of the player is determined based on his choices.
# There are 5 playing arenas in this game Meadow, Muck, Mines, Falls and Mangroves.
# There is a dimension called Crossroads that is the key arena choosing point.
# Wrong Choices, Losing Combats, Energy Deprecation all lead to Death of the player and results in Game Over.
# Trailing Program Code
import time
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

energy = 50             # variable that computes and stores player energy
moves = 0               # variable that counts nover of times the player moves
EnergyStats = []        # A list with energy status with every move(numeric)
Moves_Record=[]         # A list with description of every move
Items = ["Lighter"]     # A list of objects player has with him for survival needs
arena = []              # A list with arena status change with every move


def game():  # Enter game and setup with player credentials and feel of scenario of game
    global moves
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" THE JANGON CHAMPION")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(3)
    player_name = input("What is your name survivor?")
    print("Hello Doctor {}. Welcome to Jangon Jungle- The pride of Amazonians.".format(player_name))
    ch1 = str(input("Do you wish to continue playing this game?(Y/N)"))
    if ch1.lower() == "y" or ch1.lower() == "yes":  #Play game
        jangon(arena, Moves_Record)
    else:   #Quit game
        arena.append('Home')
        moves = moves + 1
        Moves_Record.append('Quit game')
        EnergyStats.append(energy)
        print("Thanks for embarking on this journey, Not all humans are brave! Happy cake-baking!!!")
        game_over(EnergyStats, Items, arena)


def jangon(arena, Moves_Record):    #Fuction for entering Jangon Jungle arena
    global moves
    arena.append('Jangon Jungle')
    moves = moves+1
    Moves_Record.append('Entered Jangon Jungle')
    EnergyStats.append(energy)

    print("The world faced a massive peril. \nJakaall Industries had experimented with deadliest chemicals ")
    time.sleep(4)
    print(" Creatures that created havoc with a cloned ferocious beasts.\n These beasts were set to get unleashed onto the world destroying Everything")
    time.sleep(4)
    print("Your work has ensured that Jakall shuts down.\n But this One beast that can kill a thousand people every hour, got released into Jangon")
    time.sleep(4)
    print("You have volunteered to tranquilize this beast and bring it for lab trials .")
    time.sleep(4)
    print("\nYou set out to Jangon jungle, on your helicopter with your close friend and comrade Captain Timothy Sparks")
    time.sleep(5)
    print("The view of Amazon forests is breathtaking at 36000 ft when suddenly the engines of your helicopter fails.")
    time.sleep(5)
    print("\nWHAM!")
    print("GRRRR!")
    print("GRRRRRR!!!")
    print("TIMMMMMMMM!!!")
    time.sleep(5)
    Items.append('Girl')
    print("\nHello! Are you alright?")
    print("Hello! Sir! Are you fine")
    moves = moves+1
    EnergyStats.append(energy)
    Moves_Record.append('In Crash Site')
    arena.append(' Crash site')
    time.sleep(4)
    print("\nBlink! Your eyes open, there is fumes and smoke and the pilot moans... \nYou have a pretty woman standing next to you tending your wounds")
    print("You get up with difficulty and reach out to your pilot who takes his beloved's name and gasps his last breath.")
    time.sleep(4)
    print("\nSuddenly you realise that Tim is not around!!!")
    time.sleep(4)
    print("Pretty girl says,..  Please rest for a while , There is a meadow nearby, We can get you something to eat and tend to your wounds better")
    time.sleep(4)
    print("The village doctor can see you.")

    ch2 = " "   #Choose Falls or meadow
    while ch2 != "1" and ch2 != "2":
        time.sleep(4)
        print("Your Energy now=" + str(energy))
        time.sleep(2)
        ch2 = input('What do you do? \nGo to find Tim Energy(-20x) \n    or\nGo with the girl to the nearby meadow(+100x). (1/2)')


    if ch2 == "1":
      falls(Moves_Record,EnergyStats, Items, arena)

    else:
      meadow(Moves_Record,EnergyStats, Items, arena)


def falls(Moves_Record,EnergyStats, Items , arena): #Function to enter Falls Arena
    global moves
    global energy
    moves=moves+1
    energy = energy-20
    EnergyStats.append(energy)
    Moves_Record.append('Saved Tim at Falls')
    Items.remove('Girl')
    arena.append('Falls')
    energy_check(energy)
    time.sleep(4)
    print( "\nYou look around. You hear gushing water noise from a direction, \nYou can see fumes arising from that site...")
    time.sleep(4)
    print(" We don't leave buddies and bodies behind- You say to yourself and rush in a hope to find Tim")
    time.sleep(4)
    print(" It would be good if you can come too, You ask the girl, turning around")
    time.sleep(4)
    print("She's gone already! You sigh for a moment but now your friend needs you more than your heart. You run in the direction of Falls")
    time.sleep(4)
    print("\nYou find Tim there... Lying with his abdomen bleeding. You rush in... Look around")
    time.sleep(4)
    print("You use your lighter an pull out the metal shard, using herbs nearby you \ntend to his wounds, get him water and ask him to rest while you  ")
    print(" decide to continue.")
    time.sleep(4)
    print("\nBefore you go Tim says -Mate! Take this rope it might help you! Thanks for showing up")
    time.sleep(4)
    print("Get better Tim- You say!")
    time.sleep(2)
    print("Your Energy now= "+str(energy))
    time.sleep(2)
    ch3 = str(input("Take the rope? energy cost -20x (Y/N)"))
    if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        moves = moves+1
        energy = energy-20
        arena.append('Falls')
        Moves_Record.append('Take Rope')
        EnergyStats.append(energy)
        Items.append('Rope')
        energy_check(energy)

    else:
        moves=moves+1
        EnergyStats.append(energy)
        arena.append('Falls')
        Moves_Record.append('Didnt Take Rope')


    crossroads(Moves_Record)    #Return to make more choices, wander between arenas


def crossroads(Moves_Record):   #Function to enter Crossroads
    global moves
    moves = moves+1
    arena.append("Crossroads")
    Moves_Record.append('At crossroads')
    EnergyStats.append(energy)
    print("\nAs you walk you find yourself on a crossroads ")
    print("on north there are mangroves(-10x energy) ")
    print("on south you have a meadow(+100x energy) ")
    print("on your east mines(-20x energy) and ")
    print("on west juniper shrubs that lead to muck(+50x energy) where a girl is crying for help")
    print("Your Energy now= "+str(energy))

    flag = 0
    while flag != 1:
      time.sleep(9)
      ch4 = str(input("Which path do you choose(E/W/N/S)"))
      if ch4.lower() == "e" or ch4.lower() == "east":
        mines(Moves_Record, EnergyStats, Items , arena)
        flag = 1
      elif ch4.lower() == "w" or ch4.lower() == "west":
        muck(Moves_Record, EnergyStats, Items, arena)
        flag = 1
      elif ch4.lower() == "n" or ch4.lower() == "north":
        mangrove(Moves_Record, EnergyStats, Items, arena)
        flag = 1
      elif ch4.lower() == "s" or ch4.lower() == "south":
        meadow(Moves_Record, EnergyStats, Items, arena)
        flag = 1


def mines(Moves_Record,EnergyStats, Items , arena): #Function to enter Mines Arena
    global moves
    global energy
    moves = moves+1
    Moves_Record.append('Into the Mines')
    energy = energy - 20
    arena.append('Mines')
    EnergyStats.append(energy)
    energy_check(energy)
    print("You decide to enter the mines")
    time.sleep(2)
    print("With happenings of the day still in your mind, You search for the antidote")
    time.sleep(2)
    print("In the dark, dingy mine you see a lantern nearby and light it with your lighter.")
    time.sleep(2)
    print("There you find it , Gleaming in the dark flourescent box that contains your antidote")
    time.sleep(2)
    print("Your heart pounds and you rush to grab it")
    time.sleep(2)
    print("But nearby you hear a screech")
    time.sleep(2)
    print("That was a coin under your feet, A golden coin! As you turn your lantern you see a treasure-chest")
    time.sleep(2)
    print("What do you do?")
    print("Energy="+str(energy))

    ch5 = input(str("1) Take the treasure chest and antidote(+100x energy).\n 2) Take the antidote only(-20x energy)"))
    time.sleep(4)
    if ch5 == 1:
        energy=energy+100
        time.sleep(3)
        print("As you pick the treasure chest. A pop is heard. There was a landmine underneath.Money killed you!!!")
        Items.append('Antidote', 'Treasure Chest')
        moves = moves + 1
        arena.append('Mines')
        Moves_Record.append('Take antidote and Treasure')
        EnergyStats.append(energy)
        energy_check(energy)

        print("You lost!!!")
        game_over(EnergyStats, Items , arena)
    else:
        Items.append('Antidote')
        energy = energy-20
        EnergyStats.append(energy)
        moves = moves + 1
        arena.append('Mines')
        Moves_Record.append('Take only Antidote')
        energy_check(energy)

        print("Where do you want to head next?")
        crossroads(Moves_Record)


def meadow(Moves_Record,EnergyStats, Items , arena):    #Function to enter Meadow Arena
  global moves
  global energy
  moves= moves+1
  arena.append('Meadow')
  Moves_Record.append('In Meadows')
  print("You go to village chieftains house nearby meadow eat some food rest for a few hours and return back on your way")
  energy = energy + 100
  EnergyStats.append(energy)

  energy_check(energy)

  if 'Rope' not in Items:
    print("As you return")
    time.sleep(2)
    scorpion_attack(Moves_Record,EnergyStats, Items , arena)
  else:
    print( "As you hurry in your way... The Damsel calls out for help. You see her standing in front of a quagmire while the chieftain drowns.")
    print("Your Energy now= "+str(energy))
    ch6 = input("\nDamsel: Please Help my father!!\n Do you help her father drowning in a muck near the juniper shrubs(+50x energy)?[Y/N]")
    if ch6 in ['y', 'Y', 'Yes', 'YES', 'yes']:
       muck(Moves_Record,EnergyStats, Items, arena)
    else:
       crossroads(Moves_Record)


def muck(Moves_Record,EnergyStats, Items, arena):   #Function to enter Muck Arena
  global moves
  global energy
  moves=moves+1
  Moves_Record.append('Into Muck')
  energy = energy + 50
  arena.append('Muck')
  EnergyStats.append(energy)

  energy_check(energy)

  print("You see the local chieftain drowning and rush to help him to pull him out of quagmire")
  if 'Rope' in Items:
     print('Just then you realise the rope that Tim gave you')
     time.sleep(2)
     print('You swing into action and save the chieftain')
     time.sleep(2)
     print("Chieftain: Thankyou for saving my life. As a token of gratitude please accept my daughter's hand in marriage and this Sword.")
     time.sleep(2)
     print("On your route if ever you encounter a Treasure-chest, Remember to not take it. ")
     time.sleep(2)
     print("That wealth belongs to our deities. There is a landmine underneath.")
     moves=moves+1
     arena.append('Muck')
     Moves_Record.append('Save chieftain-Take Sword and Girl')
     EnergyStats.append(energy)
     Items.extend(['Sword', 'Girl'])
     time.sleep(4)
     print("\nYou are so happy to get the love of your life. Now you leave for taming the beast")
     crossroads(Moves_Record)

  else:
       print("As you reach out to help the chieftain  ")
       scorpion_attack(Moves_Record,EnergyStats, Items , arena)


def mangrove(Moves_Record,EnergyStats, Items , arena):  #Function to enter Mangrove Arena
  global moves
  global energy
  moves=moves+1
  Moves_Record.append('Into Mangroves')
  energy = energy - 10
  EnergyStats.append(energy)
  arena.append('Mangroves')
  energy_check(energy)
  scorpion_attack(Moves_Record, EnergyStats,Items,arena)

  if 'Antidote' in Items:
     print("As you walk inside the labyrinthine mangroves, You encounter the beast enjoying its last meal")
     time.sleep(4)
     print("You slyly walk towards it, Aim for it and fire your antidote in its direction")
     time.sleep(4)
     print("It falls asleep and as you wonder how you will commute with the beast to labs...")
     time.sleep(4)
     print("Tim arrives on the spot with rescue team and the team evacuates you, your friend and the beast.")
     time.sleep(4)
     print("You win the game, Champion!!!")
     game_over(EnergyStats, Items, arena)

  else:
      time.sleep(4)
      print( "As you walk inside the labyrinthine mangroves, You encounter the beast enjoying its last meal")
      time.sleep(4)
      print("The beast senses your presence and before you can do anything, it Eats you alive")
      time.sleep(4)
      print("You lost!!!")
      game_over(EnergyStats, Items, arena)


def scorpion_attack(Moves_Record,EnergyStats, Items , arena):   #Function to encounter scorpion
    global moves
    global energy
    moves=moves+1
    a=arena[-1]
    arena.append(a)
    EnergyStats.append(energy)
    Moves_Record.append('Encounter Scorpion')
    time.sleep(4)
    print("A giant scorpion draws closer ")
    time.sleep(4)
    print("As you draw closer, you begin to muster courage!")
    time.sleep(1)
    print("Its a scorpion")
    time.sleep(4)
    print("Your Energy= "+str(energy))
    time.sleep(4)
    ch7 = str(input("Do you try to fight it? Energy -50x [Y/N]"))

    if ch7 in ['y', 'Y', 'Yes', 'YES', 'yes']:
        moves = moves + 1
        arena.append(a)
        Moves_Record.append('Fight Scorpion')
        energy = energy - 50
        EnergyStats.append(energy)
        energy_check(energy)
        if 'Sword' in Items:
         print("Luckily you have a sword")
         time.sleep(3)
         print("You kill the scorpion")
         time.sleep(3)
        else:
          print("You dont have a sword, The scorpion kills you!")
          time.sleep(4)
          print("You lost!!!")
          game_over(EnergyStats, Items, arena)



    else:
        moves = moves + 1
        arena.append(a)
        Moves_Record.append('Dont Fight Scorpion')
        EnergyStats.append(energy)
        print("You turn away from the Scorpion letting it be")
        time.sleep(4)
        print("But it attacks you with deadliest poison bite")
        time.sleep(4)
        print("You lost!!!")
        game_over(EnergyStats, Items, arena)



def game_over(EnergyStats, Items , arena):  #Function to project game over and show statistics
    time.sleep(4)
    print("Game Over")
    time.sleep(4)
    print("Thanks for playing!!!")
    time.sleep(4)
    print("In the end you had {}x energy".format(energy))
    time.sleep(4)
    print("The arena your game led you through are as follows")
    print(*arena, sep=", ")
    time.sleep(4)
    print("Items collected in this journey are")
    print(*Items, sep=", ")
    time.sleep(4)
    print("The energy counts in each move are as follows")
    print(*EnergyStats, sep=", ")
    print("Each move description is as follows")
    print(*Moves_Record, sep=", ")

    x=np.arange(0, moves, 1)
    plt.subplot(221)    #Energy Stats plot
    plt.bar(x,EnergyStats, color='m')
    plt.title('Energy Record per move')
    plt.xlabel('Move Number')
    plt.ylabel('Energy level(xp)')
    plt.subplot(222)    #Arena traversed Plot
    star = mpath.Path.unit_regular_star(6)
    circle = mpath.Path.unit_circle()
    verts = np.concatenate([circle.vertices, star.vertices[::-1, ...]])
    codes = np.concatenate([circle.codes, star.codes])
    cut_star = mpath.Path(verts, codes)
    plt.plot(x, arena,'--b', marker=cut_star, markersize=15)
    plt.title('Arena location per move')
    plt.xlabel('Move Number')
    plt.ylabel('Arena Location)')
    plt.subplot(223)    #Moves taken record plot
    plt.plot(x, Moves_Record, '-g', marker=cut_star, markersize=15)
    plt.title('Move Record')
    plt.xlabel('Move Number')
    plt.ylabel('Move in Game)')

    plt.show()
    time.sleep(4)
    print('The number of moves counts in this game= '+ str(moves)+" with move records as:")
    print(*Moves_Record, sep="\n ")

    exit()

def energy_check(energy):   #Check if energy drops below or equal to zero. Game over if true.
    if energy <= 0:
        print("Zero Energy!!You lost!!!")
        game_over(EnergyStats, Items, arena)


game()  #Function call to begin game
