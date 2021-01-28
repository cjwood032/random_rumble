import random
import os
def main():
    entrants = [i for i in range(1,31)]
    participants = []
    participant_name=""
    while participant_name!="END":
            participant_name=raw_input("\n Type in a participant's name or \"END\" to assign numbers\n")
            if participant_name!="END":
                position=int(len(participants))
                participants.append([participant_name])
    os.system("clear")
    while len(entrants)!=0:
        for p in participants:
            if len(entrants)!=0:
                entrant = random.choice(entrants)
                p.append(entrant)
                entrants.remove(entrant)
    for p in participants:
        print(p)
    if len(entrants)!=0:
        print ("The following were not added"+entrants)
main()