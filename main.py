import random
import sys
from colorama import Fore, Style, init
from dataclasses import dataclass, field

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

def stripe_text(text, color1, color2):
    striped_result = ""
    
    for index, char in enumerate(text):
        if index % 2 == 0:
            striped_result += f"{color1}{char}"
        else:
            striped_result += f"{color2}{char}"
            
    return striped_result + Style.RESET_ALL

def print_inventory(player, gemstone_values, modifier_values):
    print(f"\n{Style.BRIGHT}=== YOUR GEM BAG ===")
    
    if not player.bag:
        print("Your bag is empty!")
        return
        
    for (gem_id, modifier_id), quantity in player.bag.items():

        # Get standard gemstone name and color
        gem_name = gemstone_values[gem_id]['name']
        gem_col = gemstone_values[gem_id]['col']
        
        # Check if there is a modifier to append
        if modifier_id is not None:
            mod_name = modifier_values[modifier_id]['name']
            full_display = f"{mod_name} {gem_col}{gem_name}{Style.RESET_ALL}"
        else:
            full_display = f"{gem_col}{gem_name}{Style.RESET_ALL}"
            
        print(f"• {full_display} x{quantity}")
    print("====================\n")

def general_command_logic(game_state, query, player):
    if query == "spin":
        game_state["gamemode"] = "spin"
    elif query == "upgrade":
        game_state["gamemode"] = "upgrade"
    elif query == "bag":
        game_state["gamemode"] = "bag"
    elif query == "stats":
        print("Money: ", player.money)
        print("Total spins: ", player.total_spins)
        print("Best spin: ", player.best_spin)
        print("Mult chance: ", player.mult_chance)
        print("Mult luck: ", player.mult_luck)
        print("Spin luck: ", player.spin_luck)
    elif query == "save":
        #game_state["gamemode"] = "save"
        pass
    elif query == "exit":
            game_state["gamemode"] = "exit"
    elif query == '?' and game_state["gamemode"] == "spin":
        # SPIN HELP
        print("Valid commands within the spin gamemode:")
        print("s       -> spins a gemstone")
        print("a       -> automates the process of spinning gemstones (must be bought from upgrades first)")
        print("spin    -> brings user to the spin menu.")
        print("upgrade -> brings user to the upgrade menu.")
        print("bag     -> brings user to their bag, this is where gemstones can be sold or simply marveled at.") 
        print("stats   -> prints user stats.")
        print("save    -> creates a save file that saves the state of the users game.")
        print("exit    -> exits the game, will ask user if they are sure they want to quit first.")
    elif query == '?' and game_state["gamemode"] == "bag":
        # BAG HELP
        print("Valid commands within the bag gamemode:")
        print("b       -> prints the contents of users bag")
        print("spin    -> brings user to the spin menu.")
        print("upgrade -> brings user to the upgrade menu.")
        print("bag     -> brings user to their bag, this is where gemstones can be sold or simply marveled at.") 
        print("stats   -> prints user stats.")
        print("save    -> creates a save file that saves the state of the users game.")
        print("exit    -> exits the game, will ask user if they are sure they want to quit first.")
    else:
        print("type ? for help")

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

def spin(gemstone_values, player, modifier_values):
    num = random.randint(1,50000000) * player.spin_luck
    mult = mult_spin(player.mult_chance, player.mult_luck)
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
        final_value = gemstone_values[gem]['val']
        display_name = f"{gemstone_values[gem]['col']}{gemstone_values[gem]['name']}{Style.RESET_ALL}"
    else:
        final_value = gemstone_values[gem]['val'] * modifier_values[mult]['val']
        display_name = f"{modifier_values[mult]['name']} {gemstone_values[gem]['col']}{gemstone_values[gem]['name']}{Style.RESET_ALL}"

    print(f"You spun a(n) {display_name} worth {Fore.GREEN}${final_value:,}")

    bag_key = (gem, mult)

    if bag_key in player.bag:
        player.bag[bag_key] += 1
    else:
        player.bag[bag_key] = 1 

    player.total_spins += 1

def spin_logic(game_state, automate, gemstone_values, player, modifier_values): # will eventually need to pass stats tuple, bag tuple, etc.
    while game_state["gamemode"] == "spin":

        query = input()
        if query == 's':
            spin(gemstone_values, player, modifier_values)
        elif query == 'a' and automate:
            print("Automation!")
            pass #automate()
        elif query == 'a' and not(automate):
            print("Automation not unlocked yet!")
        else:
            general_command_logic(game_state, query, player)

def exit_logic(game_state):
    print("Are you sure you want to quit? Y/N?")
    while game_state["gamemode"] == "exit":
        query = input()
        if query == 'Y':
            game_state["gamemode"] = "quit"
        elif query == 'N':
            print("Okay, setting your gamemode back to spin!")
            game_state["gamemode"] = "spin"
        else:
            print("Please answer either Y or N.")

def bag_logic(game_state, player, gemstone_values, modifier_values):
    while game_state["gamemode"] == "bag":
    
        query = input()
        if query == 'b':
            print_inventory(player, gemstone_values, modifier_values)
        else:
            general_command_logic(game_state, query, player)

def main():

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME VARIABLES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    game_state = {
        "gamemode": "start"
    }
    automate = False

    # STATS
    @dataclass
    class PlayerStats:
        money: int = 0
        total_spins: int = 0
        best_spin: str = "N/A"
        mult_chance: float = 1.0
        mult_luck: float = 1.0
        spin_luck: float = 1.0
        bag: dict = field(default_factory=dict)

    player = PlayerStats()

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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODIFIER COLORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    transcendent_text = stripe_text("Transcendent", Fore.CYAN + Style.BRIGHT, Fore.WHITE + Style.BRIGHT)
    eternal_text = stripe_text("Eternal", Fore.YELLOW + Style.BRIGHT, Fore.WHITE + Style.BRIGHT)
    mythic_text = stripe_text("Mythic", Fore.RED + Style.BRIGHT, Fore.BLACK + Style.BRIGHT)
    celestial_text = stripe_text("Celestial", Fore.CYAN + Style.BRIGHT, Fore.MAGENTA + Style.BRIGHT)
    divine_text = stripe_text("Divine", Fore.WHITE + Style.BRIGHT, Fore.BLUE + Style.BRIGHT)
    immortal_text = stripe_text("Immortal", Fore.MAGENTA, Fore.RED + Style.BRIGHT)
    anomalous_text = stripe_text("Anomalous", Fore.GREEN, Fore.BLACK + Style.BRIGHT)
    radiant_text = stripe_text("Radiant", Fore.YELLOW + Style.BRIGHT, Fore.MAGENTA)
    gilded_text = stripe_text("Gilded", Fore.YELLOW, Fore.GREEN + Style.BRIGHT)
    tempest_text = stripe_text("Tempest", Fore.CYAN, Fore.BLUE + Style.BRIGHT)
    glitched_text = stripe_text("Glitched", Fore.BLACK, Fore.WHITE + Style.BRIGHT)
    corrupted_text = stripe_text("Corrupted", Fore.BLUE, Fore.RED + Style.BRIGHT)
    astral_text = stripe_text("Astral", Fore.CYAN, Fore.GREEN + Style.BRIGHT)
    cataclysmic_text = stripe_text("Cataclysmic", Fore.RED, Fore.YELLOW + Style.BRIGHT)
    phantom_text = stripe_text("Phantom", Fore.BLACK + Style.BRIGHT, Fore.MAGENTA)
    quantum_text = stripe_text("Quantum", Fore.MAGENTA, Fore.WHITE + Style.BRIGHT)
    volcanic_text = stripe_text("Volcanic", Fore.RED + Style.BRIGHT, Fore.MAGENTA)
    overclocked_text = stripe_text("Overclocked", Fore.BLUE, Fore.YELLOW + Style.BRIGHT)
    luminous_text = stripe_text("Luminous", Fore.GREEN, Fore.WHITE + Style.BRIGHT)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODIFIER VALUES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    modifier_values = {
        "transcendent": {"name": transcendent_text, "val": 1000},
        "eternal": {"name": eternal_text, "val": 400},
        "mythic": {"name": mythic_text, "val": 300},
        "celestial": {"name": celestial_text, "val": 200},
        "divine": {"name": divine_text, "val": 100},
        "immortal": {"name": immortal_text, "val": 90},
        "anomalous": {"name": anomalous_text, "val": 80},
        "radiant": {"name": radiant_text, "val": 70},
        "gilded": {"name": gilded_text, "val": 60},
        "tempest": {"name": tempest_text, "val": 50},
        "glitched": {"name": glitched_text, "val": 30},
        "corrupted": {"name": corrupted_text, "val": 25},
        "astral": {"name": astral_text, "val": 20},
        "cataclysmic": {"name": cataclysmic_text, "val": 15},
        "phantom": {"name": phantom_text, "val": 10},
        "quantum": {"name": quantum_text, "val": 6},
        "volcanic": {"name": volcanic_text, "val": 5},
        "overclocked": {"name": overclocked_text, "val": 4},
        "luminous": {"name": luminous_text, "val": 3}
    }

    while True:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME MODE LOGIC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        if game_state["gamemode"] == "start":
            print("Welcome to Random Number Gemstones!")
            print("This is a probability based game where you will improve incrementally.")
            print("You will start by 'spinning' for gemstones, upon recieving them you will be able to sell them for cash.")
            print("Using the cash gained by selling gemstones, you can purchase upgrades that will allow you to not only spin")
            print("better gemstones but spin more efficiently and even automate the process.")
            print("Here is a list of all the commands you can use within the game and what they do:")
            print("spin    -> brings user to the spin menu.")
            print("upgrade -> brings user to the upgrade menu.")
            print("bag     -> brings user to their bag, this is where gemstones can be sold or simply marveled at.") 
            print("stats   -> prints user stats.")
            print("save    -> creates a save file that saves the state of the users game.")
            print("exit    -> exits the game, will ask user if they are sure they want to quit first.")
            print("Your 'gamemode' will now be set to 'spin', type s and then click enter to spin for your very first gemstone!")
            print("P.S if you ever get stuck simply type ? and hit enter and you should be pointed in the right direction.")
            game_state["gamemode"] = "spin"
            
        if game_state["gamemode"] == "spin":
            spin_logic(game_state, automate, gemstone_values, player, modifier_values)

        if game_state["gamemode"] == "upgrade":
            pass

        if game_state["gamemode"] == "bag":
            bag_logic(game_state, player, gemstone_values, modifier_values)

        if game_state["gamemode"] == "save":
            pass

        if game_state["gamemode"] == "exit":
            exit_logic(game_state)

        if game_state["gamemode"] == "quit":
            sys.exit()
            
main()