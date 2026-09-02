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

def rainbow_text(text):

    colors = [
        Fore.LIGHTRED_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX
    ]
    
    striped_result = ""

    for index, char in enumerate(text):

        if char == " ":
            striped_result += char
            continue
            

        color = colors[index % len(colors)]
        striped_result += f"{color}{Style.BRIGHT}{char}"

    return striped_result + Style.RESET_ALL

def print_inventory_quantity(player, gemstone_values, modifier_values, flag):
    print(f"\n{Style.BRIGHT}=== YOUR GEM BAG ===")
    
    if not player.bag:
        print("Your bag is empty!")
        return
        
    for (gem_id, modifier_id), quantity in sorted(
        player.bag.items(),
        key=lambda item: item[1],
        reverse=flag
        ):

        # Get standard gemstone name and color
        gem_name = gemstone_values[gem_id]['name']
        gem_col = gemstone_values[gem_id]['col']
        
        # Check if there is a modifier to append
        if modifier_id is not None:
            mod_name = modifier_values[modifier_id]['name']
            full_display = f"{mod_name} {gem_col}{gem_name}{Style.RESET_ALL}"
        else:
            full_display = f"{gem_col}{gem_name}{Style.RESET_ALL}"
            
        print(f"- {full_display} x{quantity}")
    print("====================\n")

def get_bag_item_value(item, gemstone_values, modifier_values, single):
    (gem_id, modifier_id), quantity = item

    value = gemstone_values[gem_id]['val']

    if modifier_id is not None:
        value *= modifier_values[modifier_id]['val']

    if single:
        final_value = value
    else:
        final_value = (value * quantity)

    return (final_value)

def print_inventory_value(player, gemstone_values, modifier_values, flag, single):
    print(f"\n{Style.BRIGHT}=== YOUR GEM BAG ===")
    
    if not player.bag:
        print("Your bag is empty!")
        return
        
    for (gem_id, modifier_id), quantity in sorted(
        player.bag.items(),
        key=lambda item: get_bag_item_value(
            item,
            gemstone_values,
            modifier_values,
            single
        ),
        reverse=flag
    ):

        # Get standard gemstone name and color
        gem_name = gemstone_values[gem_id]['name']
        gem_col = gemstone_values[gem_id]['col']
        
        # Check if there is a modifier to append
        if modifier_id is not None:
            mod_name = modifier_values[modifier_id]['name']
            full_display = f"{mod_name} {gem_col}{gem_name}{Style.RESET_ALL}"
        else:
            full_display = f"{gem_col}{gem_name}{Style.RESET_ALL}"
            
        print(f"- {full_display} x{quantity}")
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
        print(f"Best spin:  {player.best_spin} worth {Fore.GREEN}${player.best_spin_cost:,}")
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
        print(f"\n{rainbow_text("*******************************************************************************************************")}")
        print(f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}   Valid commands within the {Fore.LIGHTMAGENTA_EX}spin{Style.RESET_ALL} gamemode:                                                          {Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}   {Fore.LIGHTRED_EX}s{Style.RESET_ALL}       -> {Fore.LIGHTMAGENTA_EX}spins{Style.RESET_ALL} a gemstone                                                                       {Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}   {Fore.LIGHTBLUE_EX}a{Style.RESET_ALL}       -> {Fore.YELLOW}automates{Style.RESET_ALL} the process of spinning gemstones (must be bought from {Fore.BLACK}upgrades{Style.RESET_ALL} first)       {Fore.LIGHTRED_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}   {Fore.MAGENTA}spin{Style.RESET_ALL}    -> brings user to the {Fore.MAGENTA}spin{Style.RESET_ALL} menu.                                                          {Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTRED_EX}*{Style.RESET_ALL}   {Fore.BLACK}upgrade{Style.RESET_ALL} -> brings user to the {Fore.BLACK}upgrade{Style.RESET_ALL} menu.                                                       {Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}   {Fore.GREEN}bag{Style.RESET_ALL}     -> brings user to their {Fore.GREEN}bag{Style.RESET_ALL}, this is where gemstones can be sold or simply marveled at.   {Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}") 
        print(f"{Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}   {Fore.RED}stats{Style.RESET_ALL}   -> prints user {Fore.RED}stats{Style.RESET_ALL}.                                                                     {Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}   {Fore.YELLOW}save{Style.RESET_ALL}    -> creates a {Fore.YELLOW}save{Style.RESET_ALL} file that {Fore.YELLOW}saves{Style.RESET_ALL} the state of the users game.                            {Fore.LIGHTRED_EX}*{Style.RESET_ALL}")
        print(f"{Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}   {Fore.BLUE}exit{Style.RESET_ALL}    -> {Fore.BLUE}exits{Style.RESET_ALL} the game, will ask user if they are sure they want to {Fore.BLACK}quit{Style.RESET_ALL} first.                {Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}")
        print(f"{rainbow_text("*******************************************************************************************************")}\n")
    elif query == '?' and game_state["gamemode"] == "bag":
        # BAG HELP
        print(f"\n{rainbow_text("************************************************************************************************************************************************")}")
        print(f"*   Valid commands within the {Fore.LIGHTGREEN_EX}bag{Style.RESET_ALL} gamemode:                                                                                                    *")
        print(f"*   {Fore.LIGHTRED_EX}bq{Style.RESET_ALL}      -> prints bag contents in order of quantity from most to least held {Fore.LIGHTRED_EX}(bq => bag quantity){Style.RESET_ALL}                                           *")
        print(f"*   {Fore.LIGHTMAGENTA_EX}bqr{Style.RESET_ALL}     -> prints bag contents in order of quantity from least to most held {Fore.LIGHTMAGENTA_EX}(bqr => bag quantity reverse){Style.RESET_ALL}                                  *")
        print(f"*   {Fore.LIGHTBLUE_EX}bv{Style.RESET_ALL}      -> prints bag contents in order of individual gemstone value from most to least expensive {Fore.LIGHTBLUE_EX}(bv => bag value){Style.RESET_ALL}                        *")
        print(f"*   {Fore.LIGHTCYAN_EX}bvr{Style.RESET_ALL}     -> prints bag contents in order of individual gemstone value from least to most expensive {Fore.LIGHTCYAN_EX}(bvr => bag value reverse){Style.RESET_ALL}               *")
        print(f"*   {Fore.LIGHTYELLOW_EX}bvc{Style.RESET_ALL}     -> prints bag contents in order of cumulative gemstone value from most to least expensive {Fore.LIGHTYELLOW_EX}(bvc => bag value cumulative){Style.RESET_ALL}            *")
        print(f"*   {Fore.LIGHTBLACK_EX}bvcr{Style.RESET_ALL}    -> prints bag contents in order of cumulative gemstone value from least to most expensive {Fore.LIGHTBLACK_EX}(bvcr => bag value cumulative reverse){Style.RESET_ALL}   *")
        print(f"*   {Fore.MAGENTA}spin{Style.RESET_ALL}    -> brings user to the {Fore.MAGENTA}spin{Style.RESET_ALL} menu.                                                                                                   *")
        print(f"*   {Fore.BLACK}upgrade{Style.RESET_ALL} -> brings user to the {Fore.BLACK}upgrade{Style.RESET_ALL} menu.                                                                                                *")
        print(f"*   {Fore.GREEN}bag{Style.RESET_ALL}     -> brings user to their {Fore.GREEN}bag{Style.RESET_ALL}, this is where gemstones can be sold or simply marveled at.                                            *") 
        print(f"*   {Fore.RED}stats{Style.RESET_ALL}   -> prints user {Fore.RED}stats{Style.RESET_ALL}.                                                                                                              *")
        print(f"*   {Fore.YELLOW}save{Style.RESET_ALL}    -> creates a {Fore.YELLOW}save{Style.RESET_ALL} file that {Fore.YELLOW}saves{Style.RESET_ALL} the state of the users game.                                                                     *")
        print(f"*   {Fore.BLUE}exit{Style.RESET_ALL}    -> {Fore.BLUE}exits{Style.RESET_ALL} the game, will ask user if they are sure they want to {Fore.BLACK}quit{Style.RESET_ALL} first.                                                         *")
        print(f"{rainbow_text("************************************************************************************************************************************************")}\n")
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

    if player.best_spin_cost <= final_value:
        player.best_spin = display_name
        player.best_spin_cost = final_value

def spin_logic(game_state, automate, gemstone_values, player, modifier_values):
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
        if query == 'bq': # sorts by quantity from most to least held
            flag = True
            print_inventory_quantity(player, gemstone_values, modifier_values, flag)
        elif query == 'bv': # sorts by individual gemstone value from most expensive to least expensive
            flag = True
            single = True
            print_inventory_value(player, gemstone_values, modifier_values, flag, single)
        elif query == 'bqr': # sorts by quantity from least to most held
            flag = False
            print_inventory_quantity(player, gemstone_values, modifier_values, flag)
        elif query == 'bvr': # sorts by individual gemstone value from least expensive to most expensive
            flag = False
            single = True
            print_inventory_value(player, gemstone_values, modifier_values, flag, single)
        elif query == 'bvc': # sorts by cumulative gemstone value from most expensive to least expensive
            flag = True
            single = False
            print_inventory_value(player, gemstone_values, modifier_values, flag, single)
        elif query == 'bvcr': # sorts by cumulative gemstone value from least expensive to most expensive
            flag = False
            single = False
            print_inventory_value(player, gemstone_values, modifier_values, flag, single)
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
        best_spin_cost: int = 0
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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  UNIQUE  TEXT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    welcome_msg = rainbow_text("Welcome to Random Number Gemstones!!!")
    stars_msg = rainbow_text("*********************************************************************************************************************")
    probability_msg = stripe_text("probability", Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX)
    game_msg = rainbow_text("game")
    gamemode_msg = stripe_text("'gamemode'", Fore.MAGENTA, Fore.LIGHTRED_EX)
    gemstone_msg = rainbow_text("gemstone")

    while True:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GAME MODE LOGIC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        if game_state["gamemode"] == "start":
            print(f"\n{stars_msg}")
            print(f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}   {welcome_msg}                                                                           {Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}   This is a {probability_msg} based game where you will improve incrementally.                                          {Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}   You will start by {Fore.LIGHTMAGENTA_EX}'spinning'{Style.RESET_ALL} for gemstones, upon recieving them you will be able to sell them for {Fore.LIGHTGREEN_EX}cash{Style.RESET_ALL}.         {Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}   Using the {Fore.LIGHTGREEN_EX}cash{Style.RESET_ALL} gained by selling gemstones, you can purchase {Fore.LIGHTBLACK_EX}upgrades{Style.RESET_ALL} that will allow you to not only spin      {Fore.LIGHTRED_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}*{Style.RESET_ALL}   better gemstones but spin more efficiently and even {Fore.LIGHTYELLOW_EX}automate{Style.RESET_ALL} the process.                                       {Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}   Here is a list of all the commands you can use within the {game_msg} and what they do:                                {Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}   {Fore.MAGENTA}spin{Style.RESET_ALL}    -> brings user to the {Fore.MAGENTA}spin{Style.RESET_ALL} menu.                                                                        {Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}   {Fore.BLACK}upgrade{Style.RESET_ALL} -> brings user to the {Fore.BLACK}upgrade{Style.RESET_ALL} menu.                                                                     {Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}   {Fore.GREEN}bag{Style.RESET_ALL}     -> brings user to their {Fore.GREEN}bag{Style.RESET_ALL}, this is where gemstones can be sold or simply marveled at.                 {Fore.LIGHTRED_EX}*{Style.RESET_ALL}") 
            print(f"{Fore.LIGHTRED_EX}*{Style.RESET_ALL}   {Fore.RED}stats{Style.RESET_ALL}   -> prints user {Fore.RED}stats{Style.RESET_ALL}.                                                                                   {Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}   {Fore.YELLOW}save{Style.RESET_ALL}    -> creates a {Fore.YELLOW}save{Style.RESET_ALL} file that {Fore.YELLOW}saves{Style.RESET_ALL} the state of the users game.                                          {Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTGREEN_EX}*{Style.RESET_ALL}   {Fore.BLUE}exit{Style.RESET_ALL}    -> {Fore.BLUE}exits{Style.RESET_ALL} the game, will ask user if they are sure they want to {Fore.BLACK}quit{Style.RESET_ALL} first.                              {Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLUE_EX}*{Style.RESET_ALL}   Your {gamemode_msg} will now be set to {Fore.MAGENTA}'spin'{Style.RESET_ALL}, type {Fore.MAGENTA}s{Style.RESET_ALL} and then click enter to spin for your very first {gemstone_msg}!    {Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}*{Style.RESET_ALL}   {Fore.CYAN}P.S{Style.RESET_ALL} if you ever get {Fore.BLACK}stuck{Style.RESET_ALL} simply type {Fore.GREEN}?{Style.RESET_ALL} and hit {Fore.CYAN}enter{Style.RESET_ALL} and you should be pointed in the right direction.         {Fore.LIGHTRED_EX}*{Style.RESET_ALL}")
            print(f"{stars_msg}\n")
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