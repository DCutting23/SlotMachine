import random

REELS = [["   X   ","  BAR  ","BAR BAR","   0   ","   X   "],
         ["BAR BAR","  BAR  ","   X   ","   0   ","   X   "], 
         ["  BAR  ","   X   ","BAR BAR","   0   ","   X   "]]
PAYOUT = {"   0   " : 0,"   X   " : 10, "  BAR  " : 20, "BAR BAR" : 50}
STAKE = 10

def get_deposit():
    amount = input("Deposit: ")
    return int(amount)

def spin():
    outcome = []
    global reel_indexes
    reel_indexes = [random.randint(0,len(REELS[0])-1), random.randint(0,len(REELS[1])-1), random.randint(0,len(REELS[2])-1)]
    outcome.append(REELS[0][reel_indexes[0]])
    outcome.append(REELS[1][reel_indexes[1]])
    outcome.append(REELS[2][reel_indexes[2]])
    return outcome

def check_spin(current_spin):
    print(f"| {current_spin[0]} | {current_spin[1]} | {current_spin[2]} |")
    if (current_spin[0] == current_spin[1] == current_spin[2]):
        print(f"you won {PAYOUT[current_spin[0]]}")
        if (PAYOUT[current_spin[0]] == "   0   "):
            print(":-(")
        else:
            print(":-)")
        return int(PAYOUT[current_spin[0]])
    else:
        return 0

def nudge(reel):
    global current_spin
    if (reel_indexes[reel-1]+1 == len(REELS[reel-1])):
        current_spin[reel-1] = REELS[reel-1][reel_indexes[reel-1]-len(REELS[reel-1])]
        reel_indexes[reel-1] = reel_indexes[reel-1]-len(REELS[reel-1])
        print("over index, resetting")
    else:
        current_spin[reel-1] = REELS[reel-1][reel_indexes[reel-1]+1]
        reel_indexes[reel-1] = reel_indexes[reel-1]+1

if __name__ == "__main__":
    print(f"main program, stake {STAKE}, 1 line")
    balance = 0
    balance += get_deposit()
    print(f"new balance is {balance}")
    loop = True
    while(loop == True):
        choice = input("\n\n\n\n\n\n\nEnter to spin, 2 to add funds or 3 to exit: ")
        if (choice == ""):
            if (balance >= STAKE):
                balance -= STAKE
                global current_spin 
                current_spin = spin()
                winnings = check_spin(current_spin)
                balance += winnings
                if ((winnings == 0) and (random.randint(0,5) == 1)):
                    for i in range(3):
                        print("nudge")
                        nudge_selection = input("nudge reel 1, 2 or 3: ")
                        nudge_selection = int(nudge_selection)
                        nudge(nudge_selection)
                        winnings = check_spin(current_spin)
                        balance += winnings
                        if (winnings != 0):
                            break
                print(f"new balance is {balance}")
            elif (balance < STAKE):
                print("please add funds to spin")
        elif (choice == "2"):
            balance += get_deposit()
            print(f"new balance is {balance}")
        elif (choice == "3"):
            loop = False
        else:
            print("please select options 1, 2 or 3")

            





    
    