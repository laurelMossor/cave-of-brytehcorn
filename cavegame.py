import time
import random

INTRO_SCROLL = """
                                             _______________________
   _______________________-------------------                       `\

 /:--__                                                              |
||< > |                                   ___________________________/
| \__/_________________-------------------                         |
|                                                                  |
 |                    THE CAVE OF BRY'TEH CORHN                     |
 |                                                                  |
 |          It's a misty morning at dawn.                            |
  |        You've traveled all night to reach your destination.      |
  |            Before you,                                           |
  |             wide and dark as the gaping maw of a giant,           |
  |                lies the Cave of Bry'teh Corhn.                    |
   |           Inside,                                                |
   |             you hope to find the fabled treasure.               |
   |                                                                 |
   |     It's the last glimmer of purpose left in your life...       |
   |                                                                 |
  |                                              ____________________|_
  |  ___________________-------------------------                      `\

  |/`--_                                                                 |
  ||[ ]||                                            ___________________/
   \===/___________________--------------------------
        """
CYCLOPS = """
           _......._
       .-'.'.'.'.'.'.`-.
     .'.'.'.'.'.'.'.'.'.`.
    /.'.'               '.\

    |.'    _.--...--._     |
    \    `._.-.....-._.'   /
    |     _..- .-. -.._   |
 .-.'    `.   ((@))  .'   '.-.
( ^ \      `--.   .-'     / ^ )
 \  /         .   .       \  /
 /          .'     '.  .-    \

( _.\    \ (_`-._.-'_)    /._\)
 `-' \   ' .--.          / `-'
     |  / /|_| `-._.'\   |
     |   |       |_| |   /-.._
 _..-\   `.--.______.'  |
      \       .....     |
       `.  .'      `.  /
         \           .'
          `-..___..-`
"""

##### Bad Guys #####
##BADDY 1
bad1_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 4
bad1_ac = 14

def bad1_damage_calc():
    bad1_damage = random.randint(1,4) + 2
    return bad1_damage

##BADDY 2
bad2_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 2
bad2_ac = 13

def bad2_damage_calc():
    bad2_damage = random.randint(1,4) + 2
    return bad2_damage

##BADDY 3
bad3_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 4
bad3_ac = 12

def bad3_damage_calc():
    bad3_damage = random.randint(1,4) + random.randint(1,4) + 1
    return bad3_damage

##BADDY4
bad4_hp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + 3
bad4_ac = 17

def bad4_damage_calc():
    bad4_damage = random.randint(1,10) + 4
    return bad4_damage

##### Static play function #####
def enemy_hit_chance():
    enemy_hit = random.randint(1,20) + 4
    return enemy_hit
    
def player_hit_chance():
    player_hit = random.randint(1,20) + 5
    return player_hit

#### Narrative Functions ####
def enter_cave_intro():
    """Validate that player wants to move forward with game.
    If player wants to move forward, return True,
    Else, return False"""
    while True:
        print("Do you walk into the cave? (Type Y or N)") 
    
        enter_cave = input("> ")
        enter_cave = enter_cave.upper()
    
        if enter_cave == "Y":
            print()
            print("Onward... to destiny!")
            return True
    
        elif enter_cave == "N":
            print()
            print("Coward. Enjoy a life of meaningless mediocrity")
            print()
            return False
    
        else:
            print()
            print("""Please type Y or N.
            > """)
            print()

#######################################################################
def player_name_animal_class():
    print("Before you go much further... what is your name, brave adventurer?")
    player_name = input("> ")
    player_name = player_name.title()
    print()
    print(f"Ah. What a name. Welcome, {player_name}.")
    print()
    
    print(f"What kind of animal are you {player_name}?")
    player_animal = input("> I am a... ")
    print()
    time.sleep(1)
    print(f"A {player_animal}? I could tell just by the smell.")
    print()
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    print("""
Next up, what kind of hero are you?
Wizards use magic to defeat their foes. They are "glass cannons": which mean they blast hard, but are easier to damage.
Fighters carry a sword and shield. They are easier to hit but have a lot of life.
Rogues have two small daggers and are very hard to hit.""")
    print()
    
    ### This choice also assigns the player their AC and weapon. ###
    player_class = None 
    
    while player_class == None:
        print(f"""Tell me, {player_name}, are you...
A. A Wizard
B. A Fighter
C. A Rogue""")
        player_class_choice = input("> ")
        player_class_choice = player_class_choice.upper()
    
        if player_class_choice == "A":
            player_class = "wizard"
            player_ac = 15
            player_weapon = "spells"
    
        elif player_class_choice == "B":
            player_class = "fighter" 
            player_ac = 12
            player_weapon = "sword"
        
        elif player_class_choice == "C":
            player_class = "rogue"
            player_ac = 18
            player_weapon = "daggers"
        
        else:
            print() 
            print("Please choose A, B, or C.")
            print() 
    
    print()
    print(f"{player_name}, the {player_animal} {player_class}. Nice to meet you.")
    print()
    
    print(f"""Your AC is {player_ac}, that number represents how hard it is to hit you. 
Don't worry about it though. I'm sure you'll be just fine: your {player_weapon} will protect you!""")
    print()
    
    return player_name, player_animal, player_class, player_ac, player_weapon
    
#######################################################################
def player_damage_calc(player_class):
    if player_class == "wizard":
        player_damage = random.randint(1,10) + 2
    if player_class == "fighter":
        player_damage = random.randint(1,8) 
    if player_class == "rogue":
        player_damage = random.randint(1,4) + random.randint(1,4) + 1
    return player_damage

#######################################################################
def discover_hp(player_name, player_animal, player_class):
    print()
    print("Now...")
    time.sleep(1)
    print()
    print(f"Come closer, {player_name}...")
    time.sleep(2)
    print(f"Closer, {player_name}.")
    time.sleep(1)
    print(f"Good {player_animal}.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print()

    print("Press enter to continue")
    input("> ")
     
    if player_class == "wizard":
        player_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 12
        player_hp_range = "17 - 32"
    
    if player_class == "fighter":
        player_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 20
        player_hp_range = "28 - 44"
    
    if player_class == "rogue":
        player_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 15
        player_hp_range = "21 - 39"
    
    print(f"""
Ahhh, yes.
I can see that you have {player_hp} HP: that's the amount of life you have. 
You should know that {player_class.title()}s usually have {player_hp_range}.
    """)
    time.sleep(2)
    
    ### A KEY DECISION to keep HP or roll again ### 
    while True:
        
        print("""
Should I take a closer look to see if I am mistaken?
...I can only look once more, and then I'm sure.""")
        print("""
Do you want me to take another look? 
(Type 'keep' to save your HP, or 'look again' to get new stats.)
        """) 
    
        reroll_hp = input("> ")
        reroll_hp = reroll_hp.lower()
    
        if reroll_hp == "keep":
            print(f"You kept your HP as {player_hp}... Good luck.")
            break
    
        elif reroll_hp == "look again":
            if player_class == "wizard":
                player_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 12
    
            if player_class == "fighter":
                random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 20
    
            if player_class == "rogue":
                player_hp = random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + random.randint(1,4) + 15
            print()
            print(f"Your new HP is {player_hp}. I hope you're happy.")
            break
            
        else:
            print()
            print("""Please enter 'keep' or 'look again'.
            > """)
    print()
    return player_hp
    
#######################################################################
def battle_sequence(enemy_hp, enemy_damage_calc, enemy_ac, player_hp, player_class, player_ac):
    while player_hp > 0 and enemy_hp > 0:
        input("Press ENTER to hit: ")

        if player_hit_chance() < enemy_ac:
            print()
            time.sleep(1)
            print("You missed...")
            print("Enemy HP = ", enemy_hp)
                    
        else:
            enemy_hp = enemy_hp - player_damage_calc(player_class)
            print()
            time.sleep(1)
            print("You hit the enemy!")
            print("Enemy HP = ", enemy_hp)

        if enemy_hp <= 0:
            time.sleep(1)
            print("You win!")
            break

        if enemy_hit_chance() < player_ac:
            print()
            time.sleep(1)
            print("The enemy missed!")
            print("Player HP = ", player_hp)
            print()

        else: 
            player_hp = player_hp - enemy_damage_calc()
            print()
            time.sleep(1)
            print("The enemy hit you!")
            print("Player HP = ", player_hp)
            print()

        if player_hp <=0:
            time.sleep(2)
            print("YOU DIED!")
            break

    return player_hp

#######################################################################
def player_motivation_narrative():
    print("You step into the mouth of the cave and gather your thoughts.")
    print()
    time.sleep(1)
    
    print("The sound around you diminishes to a deafening quiet.")
    print()
    time.sleep(1)
    
    print("You take a torch from your pack and light it, dimly illuminating the rough walls surrounding you.")
    print()
    time.sleep(1)
    
    print("Your eyes adjust to the darkness.")
    print()
    time.sleep(1)
    
    print("Press enter to continue")
    input("> ")
    
    print("...")
    print()
    time.sleep(1)

    print("Tiny specks of crystal shine back at you in the dim light of the cave.")
    print()
    time.sleep(2)

    print("Your footsteps echo endlessly down and back the winding tunnel stretching before you, and you think to yourself...")
    print()
    time.sleep(3)
    
    print("...Why am I here?")
    print()
    time.sleep(2)
    
    print("""
A. I've never been recognized for anything in my entire life. I just want someone to see me for what I am: Great.
B. The fated treasure of Bry'teh Corhn. It's everything I ever wanted, and more. 
C. The spirit of adventure calls to me! Experiencing whatever lies ahead is what I was born for. 
    """)
    
    player_motivation = None
    
    while player_motivation == None:
        print("I'm here for...")
        player_motivation_choice = input("> ").upper()
        player_motivation_choice = player_motivation_choice
        
        if player_motivation_choice == "A":
            player_motivation = "Fame and Glory"
        
        elif player_motivation_choice == "B":
            player_motivation = "B"
        
        elif player_motivation_choice == "C":
            player_motivation = "The Spirit of Adventure"
        
        else:
            print("Please choose A, B, or C.")
            print()
        
        if player_motivation == "B":
            print("What did you hear was in the cave? For what do you seek?")
            player_motivation = input("> ").title()

    print()
    time.sleep(1)
    print(f"You step deeper into the cave, emboldened by your desire for {player_motivation}.") 
    return player_motivation

#######################################################################


    
# # # # # # # # # # # # # MAIN # # # # # # # # # # # # # 
def main():

    print(INTRO_SCROLL)
    print()
    print()
    time.sleep(1)
    
    while True:
           
        if enter_cave_intro() == False:
            return
        print()
        time.sleep(1)
        
        player_name, player_animal, player_class, player_ac, player_weapon = player_name_animal_class()
        player_damage_calc(player_class)
        
        
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print()
        time.sleep(1)
        print("Press enter to continue")
        input("> ")
        
        player_hp = discover_hp(player_name, player_animal, player_class)
        
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print()
        time.sleep(1)
        print("Press enter to continue")
        input("> ")
        print()
        
        player_motivation = player_motivation_narrative()
        time.sleep(1)

        print()
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print()
        time.sleep(1)
        print("Press enter to continue")
        input("> ")
        print()

        print("Continuing on, you approach a dark corner.")
        print()
        time.sleep(2)

        print("You pause to take in your surroundings, hoping to maintain the sense of direction you had upon entering the mouth of the cave.")
        print()
        time.sleep(2)

        print("As you slow your pace, the echoing of your footsteps grows louder, disorienting you briefly.")
        print()
        time.sleep(2)

        print("Press enter to continue")
        input("> ")
        time.sleep(1)

        print("What you thought was the sound of your own footsteps echoing in the darkness...")
        print()
        time.sleep(2)

        print("...is actually that of a beast approaching!")
        print()
        print("Press enter to continue")
        input("> ")
        time.sleep(1)

        print(CYCLOPS)
        print()
        print("Press enter to continue")
        input("> ")
        time.sleep(1)

        print(f"You spin around just in time to ready your {player_weapon}.")
        print()
        time.sleep(1)
        
## Battle sequence              
# battle_sequence(bad1_hp, bad1_damage_calc, bad1_ac, player_hp) 
        
        player_hp = battle_sequence(bad1_hp, bad1_damage_calc, bad1_ac, player_hp, player_class, player_ac)
        
        
        print()
        print("Drawn by the sound of the conflict, another beast jumps out from behind the next corner!")
        print()
        time.sleep(2)

        player_hp = battle_sequence(bad2_hp, bad2_damage_calc, bad2_ac, player_hp, player_class, player_ac)
        
        
        print()
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print()
        time.sleep(1)
        print("Press enter to continue")
        input("> ")
        time.sleep(1)
        print()
        
        print("Breathing deeply, you check for cuts.")
        print()
        time.sleep(1)

        print(f"Your HP is {player_hp}")
        print()
        time.sleep(1)

        print("You're alive.")
        print()
        time.sleep(1)

        print("You continue on, taking care to listen for other footsteps.")
        print()
        time.sleep(1)

        print("Due to your increased vigilance, you hear ahead of you a familiar sound.")
        print()
        time.sleep(1)

        print("Thankfully, this time you can prepare yourself.")
        print()
        time.sleep(1)
        
        print("Press enter to continue")
        input("> ")
        time.sleep(1)
        print()

        print("The beast blocks the way forward, but you must persist... CHARGE!")
        print()
        time.sleep(1)

        player_hp = battle_sequence(bad4_hp, bad4_damage_calc, bad4_ac, player_hp, player_class, player_ac)
        
        print()
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print()
        time.sleep(1)

        print("You made it out alive.")
        print()
        time.sleep(1)
        
        print("You must have some reason to be alive.")
        print()
        time.sleep(1)
        
        
        ## FINAL MESSAGES
        print("Thank you for playing The Cave of Bry'teh Corhn. People will sing songs of your glory for many years to come.")
        break

main()