import random
import sys

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

def main():
    #print(random.randint(1,50000000))

    # gameplay loop spin numbers ->
    # buy upgrades -> 
    # spin better numbers ->
    # specific button probably 's' will be used for spin 
    # 'u' will probably be used for upgrades

    gamemode = "spin"

    while gamemode != "exit":
            
        # spin gameplay loop
        while gamemode == "spin":
            print("spin menu!!") # used for debugging
            query = input()
            if query == 'u':
                gamemode = "upgrade"
            elif query == "save":
                pass # will eventually be save logic
            elif query == 's':
                print("You're already spinning twin.")
            elif query == "exit":
                gamemode = "exit"
            elif query == "stats":
                pass # print user stats
            else:
                print("Invalid command, valid commands are:")
                print("stats -> prints user stats.")
                print("u -> brings user to the upgrade menu.")
                print("s -> brings user to the spin menu.")
                print("save -> creates a save file that saves the state of the users game.")
                print("exit -> exits the game, will ask user if they would like to save first.")

        while gamemode == "upgrade":
            print("upgrade menu!!") # used for debugging
            query = input()
            if query == 'u':
                print("You're already upgrading twin.")
            elif query == "save":
                pass # will eventually be save logic
            elif query == 's':
                gamemode = "spin"
            elif query == "exit":
                gamemode = "exit"
            elif query == "stats":
                pass # print user stats
            else:
                print("Invalid command, valid commands are:")
                print("stats -> prints user stats.")
                print("u -> brings user to the upgrade menu.")
                print("s -> brings user to the spin menu.")
                print("save -> creates a save file that saves the state of the users game.")
                print("exit -> exits the game, will ask user if they would like to save first.")

        if gamemode == "exit":
            print("Are you sure you want to quit? Y/N?")
            while gamemode == "exit":
                query = input()
                if query == 'Y':
                    gamemode = "quit"
                elif query == 'N':
                    gamemode = "spin"
                else:
                    print("Please answer either Y or N.")

        if gamemode == "quit":
            sys.exit()
            
main()