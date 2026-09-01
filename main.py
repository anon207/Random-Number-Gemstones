import random
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# My first game (made by THE Mark Samuel)

# Spin a random number and get one of the following:

#    |       range       ||        Gemstone       ||    value    |   decimal  | probabilty
#-----------------------------------------------------------------------------------------
# 1  | 1                 -> Blue Diamond          -> $50,000,000 | 0.00000002 | 0.000002%
# 2  | 2-10              -> Imperial Jadeite      -> $25,000,000 | 0.00000018 | 0.000018%
# 3  | 11-50             -> Pink Diamond          -> $12,500,000 | 0.0000008  | 0.00008%
# 4  | 51-500            -> Red Diamond           -> $6,250,000  | 0.000009   | 0.0009%
# 5  | 501-1500          -> Burmese Ruby          -> $3,125,000  | 0.00002    | 0.002%
# 6  | 1501-3000         -> Alexandrite           -> $1,562,500  | 0.00003    | 0.003%
# 7  | 3001-6000         -> Musgravite            -> $781,250    | 0.00006    | 0.006%
# 8  | 6001-12000        -> Columbian Emerald     -> $390,625    | 0.00012    | 0.012%
# 9  | 12001-24000       -> Kashmir Sapphire      -> $195,312    | 0.00024    | 0.024%
# 10 | 24001-48000       -> Red Beryl             -> $97,656     | 0.00048    | 0.048%
# 11 | 48001-96000       -> Grandidierite         -> $48,828     | 0.00096    | 0.096%
# 12 | 96001-192000      -> Padparadscha Sapphire -> $24,414     | 0.00192    | 0.192%
# 13 | 192001-384000     -> Black Opal            -> $12,207     | 0.00384    | 0.384%
# 14 | 384001-768000     -> Benitoite             -> $6,103      | 0.00768    | 0.768%
# 15 | 768001-1536000    -> Tanzanite             -> $3,051      | 0.01536    | 1.536%
# 16 | 1536001-3072000   -> Aquamarine            -> $1,525      | 0.03072    | 3.072%
# 17 | 3072001-6144000   -> Topaz                 -> $762        | 0.06144    | 6.144%
# 18 | 6144001-12288000  -> Amethyst              -> $381        | 0.12288    | 12.288%
# 19 | 12288001-24576000 -> Natural Citrine       -> $190        | 0.24576    | 24.576%
# 20 | 24576001-50000000 -> Clear Quartz          -> $95         | 0.50848    | 50.848%

# Additionally have a 1 in 500 chance to roll a multiplier with one of the following probabilities: 

#    |    range    ||   modifier   || mult. | decimal | probability
#-------------------------------------------------------------------------------------------
# 1  | 1           -> Transcendent -> x1000 | 0.00002 | 0.002%
# 2  | 2-5         -> Eternal      -> x400  | 0.00008 | 0.008%
# 3  | 6-15        -> Mythic       -> x300  | 0.0002  | 0.02%
# 4  | 16-30       -> Celestial    -> x200  | 0.0003  | 0.03%
# 5  | 31-60       -> Divine       -> x100  | 0.0006  | 0.06%
# 6  | 61-110      -> Immortal     -> x90   | 0.001   | 0.1%
# 7  | 111-180     -> Anomalous    -> x80   | 0.0014  | 0.14%
# 8  | 181-330     -> Radiant      -> x70   | 0.003   | 0.3%
# 9  | 331-630     -> Gilded       -> x60   | 0.006   | 0.6%
# 10 | 631-1200    -> Tempest      -> x50   | 0.0114  | 1.14%
# 11 | 1201-2000   -> Glitched     -> x30   | 0.016   | 1.6%
# 12 | 2001-3000   -> Corrupted    -> x25   | 0.02    | 2%
# 13 | 3001-4500   -> Astral       -> x20   | 0.03    | 3%
# 14 | 4501-6500   -> Cataclysmic  -> x15   | 0.04    | 4%
# 15 | 6501-10500  -> Phantom      -> x10   | 0.08    | 8%
# 16 | 10501-16000 -> Quantum      -> x6    | 0.11    | 11%
# 17 | 16001-24000 -> Volcanic     -> x5    | 0.16    | 16%
# 18 | 24001-34000 -> Overclocked  -> x4    | 0.2     | 20%
# 19 | 34001-50000 -> Luminous     -> x3    | 0.32    | 32%

# maybe will work on adding modifiers to gemstones at some point?

def general_command_logic(gamemode, query):
    if query == "spin":
        gamemode = "spin"
    elif query == "upgrade":
        gamemode == "upgrade"
    elif query == "bag":
        gamemode == "bag"
    elif query == "stats":
        gamemode = "stats"
    elif query == "save":
        pass # print user stats
    elif query == "exit":
            gamemode == "exit"
    elif query == '?' and gamemode == "spin":
        print("Valid commands are:")
        print("s -> spins a gemstone")
        print("a -> automates the process of spinning gemstones (must be bought from upgrades first)")
    else:
        print("Valid commands are:")
        print("spin    -> brings user to the spin menu.")
        print("upgrade -> brings user to the upgrade menu.")
        print("bag     -> displays the users bag (or inventory), this is where gemstones can be sold or simply marveled at.") 
        print("stats   -> prints user stats.")
        print("save    -> creates a save file that saves the state of the users game.")
        print("exit    -> exits the game, will ask user if they are sure they want to quit first.")
    return(gamemode)

def mult_spin(mult_chance, mult_luck):
    num = random.randint(1,500) * mult_chance
    mult = None

    if num == 1:

        mult_num = random.randint(1,50000) * mult_luck

        if 0 < mult_num <= 1:
            # TRANSCENDENT
            mult = "transcendent"
        elif mult_num <= 5:
            # ETERNAL
            mult = "eternal"
        elif mult_num <= 15:
            # MYTHIC
            mult = "mythic"
        elif mult_num <= 30:
            # CELESTIAL
            mult = "celestial"
        elif mult_num <= 60:
            # DIVINE
            mult = "divine"
        elif mult_num <= 110:
            # IMMORTAL
            mult = "immortal"
        elif mult_num <= 180:
            # ANOMALOUS
            mult = "anomalous"
        elif mult_num <= 330:
            # RADIANT
            mult = "radiant"
        elif mult_num <= 630:
            # GILDED
            mult = "gilded"
        elif mult_num <= 1200:
            # TEMPEST
            mult = "tempest"
        elif mult_num <= 2000:
            # GLITCHED
            mult = "glitched"
        elif mult_num <= 3000:
            # CORRUPTED
            mult = "corrupted"
        elif mult_num <= 4500:
            # ASTRAL
            mult = "astral"
        elif mult_num <= 6500:
            # CATACLYSMIC
            mult = "cataclysmic"
        elif mult_num <= 10500:
            # PHANTOM
            mult = "phantom"
        elif mult_num <= 16000:
            # QUANTUM
            mult = "quantum"
        elif mult_num <= 24000:
            # VOLCANIC
            mult = "volcanic"
        elif mult_num <= 34000:
            # OVERCLOCKED
            mult = "overclocked"
        elif mult_num <= 50000:
            # LUMINOUS
            mult = "luminous"

    return (mult)

def spin(gemstone_values, mult_chance, mult_luck, spin_luck, modifier_values):
    num = random.randint(1,50000000) * spin_luck
    mult = mult_spin(mult_chance, mult_luck)
    gem = None

    if 0 < num <= 1:
        # BLUE DIAMOND
        gem = "blue_diamond"
    elif num <= 10:
        # IMPERIAL JADEITE
        gem = "imperial_jadeite"
    elif num <= 50:
        # PINK DIAMOND
        gem = "pink_diamond"
    elif num <= 500:
        # RED DIAMOND
        gem = "red_diamond"
    elif num <= 1500:
        # BURMESE RUBY
        gem = "burmese_ruby"
    elif num <= 3000:
        # ALEXANDRITE
        gem = "alexandrite"
    elif num <= 6000:
        # MUSGRAVITE
        gem = "musgravite"
    elif num <= 12000:
        # COLUMBIAN EMERALD
        gem = "columbian_emerald"
    elif num <= 24000:
        # KASHMIR SAPPHIRE
        gem = "kashmir_sapphire"
    elif num <= 48000:
        # RED BERYL
        gem = "red_beryl"
    elif num <= 96000:
        # GRANDIDIERITE
        gem = "grandidierite"
    elif num <= 192000:
        # PADPARADSCHA SAPPHIRE
        gem = "padparadscha_sapphire"
    elif num <= 384000:
        # BLACK OPAL
        gem = "black_opal"
    elif num <= 768000:
        # BENITOITE
        gem = "benitoite"
    elif num <= 1536000:
        # TANZANITE
        gem = "tanzanite"
    elif num <= 3072000:
        # AQUAMARINE
        gem = "aquamarine"
    elif num <= 6144000:
        # TOPAZ
        gem = "topaz"
    elif num <= 12288000:
        # AMETHYST
        gem = "amethyst"
    elif num <= 24576000:
        # NATURAL CITRINE
        gem = "natural_citrine"
    else:
        # CLEAR QUARTZ
        gem = "clear_quartz"

    if mult is None:
        print(
            f"You spun a(n) {gemstone_values[gem]['col']}{gemstone_values[gem]['name']}{Style.RESET_ALL} "
            f"worth {Fore.GREEN}${gemstone_values[gem]['val']:,}"
        )
    else:
        print("You spun a(n)", modifier_values[mult]["name"], gemstone_values[gem]["name"], "worth", gemstone_values[gem]["val"] * modifier_values[mult]["val"])
    #money += gemstone_values[gem]["val"]


def spin_logic(gamemode, automate, gemstone_values, mult_chance, mult_luck, spin_luck, modifier_values): # will eventually need to pass stats tuple, bag tuple, etc.
    while gamemode == "spin":

        query = input()
        if query == 's':
            spin(gemstone_values, mult_chance, mult_luck, spin_luck, modifier_values)
        elif query == 'a' and automate:
            print("Automation!")
            pass #automate()
        elif query == 'a' and not(automate):
            print("Automation not unlocked yet!")
        else:
            general_command_logic(gamemode, query)

def exit_logic(gamemode):
    print("Are you sure you want to quit? Y/N?")
    while gamemode == "exit":
        query = input()
        if query == 'Y':
            gamemode = "quit"
        elif query == 'N':
            gamemode = "spin"
        else:
            print("Please answer either Y or N.")
    return gamemode

def main():

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME VARIABLES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    gamemode = "start"
    automate = False

    money = 0
    total_spins = 0

    mult_chance = 1
    mult_luck = 1

    spin_luck = 1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GEMSTONE VALUES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    gemstone_values = {
    "blue_diamond": {"name": "Blue Diamond", "val": 50000000, "col": Fore.BLUE + Style.BRIGHT},
    "imperial_jadeite": {"name": "Imperial Jadeite", "val": 25000000, "col": Fore.GREEN + Style.BRIGHT},
    "pink_diamond": {"name": "Pink Diamond", "val": 12500000, "col": Fore.MAGENTA + Style.BRIGHT},
    "red_diamond": {"name": "Red Diamond", "val": 6250000, "col": Fore.RED + Style.BRIGHT},
    "burmese_ruby": {"name": "Burmese Ruby", "val": 3125000, "col": Fore.RED + Style.BRIGHT},
    "alexandrite": {"name": "Alexandrite", "val": 1562500, "col": Fore.MAGENTA},
    "musgravite": {"name": "Musgravite", "val": 781250, "col": Fore.BLACK + Style.BRIGHT},
    "columbian_emerald": {"name": "Columbian Emerald", "val": 390625, "col": Fore.GREEN + Style.BRIGHT},
    "kashmir_sapphire": {"name": "Kashmir Sapphire", "val": 195312, "col": Fore.BLUE + Style.BRIGHT},
    "red_beryl": {"name": "Red Beryl", "val": 97656, "col": Fore.RED},
    "grandidierite": {"name": "Grandidierite", "val": 48828, "col": Fore.CYAN},
    "padparadscha_sapphire": {"name": "Padparadscha Sapphire", "val": 24414, "col": Fore.RED + Style.BRIGHT},
    "black_opal": {"name": "Black Opal", "val": 12207, "col": Fore.BLACK + Style.BRIGHT},
    "benitoite": {"name": "Benitoite", "val": 6103, "col": Fore.BLUE},
    "tanzanite": {"name": "Tanzanite", "val": 3051, "col": Fore.BLUE},
    "aquamarine": {"name": "Aquamarine", "val": 1525, "col": Fore.CYAN + Style.BRIGHT},
    "topaz": {"name": "Topaz", "val": 762, "col": Fore.YELLOW},
    "amethyst": {"name": "Amethyst", "val": 381, "col": Fore.MAGENTA},
    "natural_citrine": {"name": "Natural Citrine", "val": 190, "col": Fore.YELLOW + Style.BRIGHT},
    "clear_quartz": {"name": "Clear Quartz", "val": 95, "col": Fore.WHITE + Style.BRIGHT}
    }
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODIFIER VALUES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    modifier_values = {
        "transcendent": {"name": "Transcendent", "val": 1000},
        "eternal": {"name": "Eternal", "val": 400},
        "mythic": {"name": "Mythic", "val": 300},
        "celestial": {"name": "Celestial", "val": 200},
        "divine": {"name": "Divine", "val": 100},
        "immortal": {"name": "Immortal", "val": 90},
        "anomalous": {"name": "Anomalous", "val": 80},
        "radiant": {"name": "Radiant", "val": 70},
        "gilded": {"name": "Gilded", "val": 60},
        "tempest": {"name": "Tempest", "val": 50},
        "glitched": {"name": "Glitched", "val": 30},
        "corrupted": {"name": "Corrupted", "val": 25},
        "astral": {"name": "Astral", "val": 20},
        "cataclysmic": {"name": "Cataclysmic", "val": 15},
        "phantom": {"name": "Phantom", "val": 10},
        "quantum": {"name": "Quantum", "val": 6},
        "volcanic": {"name": "Volcanic", "val": 5},
        "overclocked": {"name": "Overclocked", "val": 4},
        "luminous": {"name": "Luminous", "val": 3}
    }

    while True:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME MODE LOGIC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        if gamemode == "start":
            print("Welcome to Random Number Gemstones!")
            print("This is a probability based game where you will improve incrementally.")
            print("You will start by 'spinning' for gemstones, upon recieving them you will be able to sell them for cash.")
            print("Using the cash gained by selling gemstones, you can purchase upgrades that will allow you to not only spin")
            print("better gemstones but spin more efficiently and even automate the process.")
            print("Here is a list of all the commands you can use within the game and what they do:")
            print("spin    -> brings user to the spin menu.")
            print("upgrade -> brings user to the upgrade menu.")
            print("bag     -> displays the users bag (or inventory), this is where gemstones can be sold or simply marveled at.") 
            print("stats   -> prints user stats.")
            print("save    -> creates a save file that saves the state of the users game.")
            print("exit    -> exits the game, will ask user if they are sure they want to quit first.")
            print("Your 'gamemode' will now be set to 'spin', type s and then click enter to spin for your very first gemstone!")
            print("P.S if you ever get stuck simply type ? and hit enter and you should be pointed in the right direction.")
            gamemode = "spin"
            
        if gamemode == "spin":
            spin_logic(gamemode, automate, gemstone_values, mult_chance, mult_luck, spin_luck, modifier_values)

        if gamemode == "upgrade":
            pass

        if gamemode == "bag":
            pass

        if gamemode == "stats":
            pass

        if gamemode == "save":
            pass

        if gamemode == "exit":
            print("Are you sure you want to quit? Y/N?")
            exit_logic(gamemode)

        if gamemode == "quit":
            sys.exit()
            
main()