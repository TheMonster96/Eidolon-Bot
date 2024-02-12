import requests
import json
from datetime import datetime



arb_tier_list = ["S",
                 "S",
                 "S",
                 "A",
                 "A",
                 "A",
                 "A",
                 "B",
                 "B",
                 "B",
                 "B",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "C",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D",
                 "D"]

arb_tileset= ["Casta",
               "Cinxia",
               "Sensei",
               "Odin",
               "Sechura",
               "Hydron",
               "Helene",
               "Tessera",
               "Ose",
               "Hyf",
               "Outer Terminus",
               "Larzac",
               "Sinai",
               "Sangeru",
               "Gulliver",
               "Alator",
               "Stephano",
               "Io",
               "Kala-azar",
               "Lares",
               "Lith",
               "Paimon",
               "Callisto",
               "Bellinus",
               "Cerberus",
               "Spear",
               "Umbriel",
               "Coba",
               "Kadesh",
               "Romula",
               "Rhea",
               "Berehynia",
               "Oestrus",
               "Proteus",
               "Xini",
               "Cytherean",
               "Stöfler",
               "Taranis",
               "Mithra",
               "Gaia",
               "Caelus",
               "Akkad"]

enemy_types=["Orokin",
             "Grineer",
             "Corpus",
             "Infested"]

def printArb() -> str:
    responseArb = requests.get("https://api.warframestat.us/pc/arbitration")
    string = json.dumps(responseArb.json(), sort_keys=True, indent=4)
    print(string)
    current_time=datetime.now().strftime("%H:%M:%S")
    current_minutes=int(current_time.split(":")[1])
    print(current_time)
    indexName = int(string.find("nodeKey") + 11)
    indexType = int(string.find("typeKey") + 11)
    indexEnemy = int(string.find("enemy") + 9)
    indexTime= int(string.find("expiry")+ 24)
    print(string[indexName])
    print(string[indexType])
    print(string[indexEnemy])
    print(string[indexTime])
    substring_Name: str=string[indexName:indexName+14]
    substring_Type: str=string[indexEnemy:indexEnemy+8]
    substring_Time: int=int(string[indexTime:indexTime+2]) -4
    print(substring_Time)
    #print(substring)
    # print(string[indexName:indexName+ 14])
    current_minutes_copy=current_minutes
    while current_minutes_copy < 60:
        current_minutes_copy+=1

    index = 0

    message: str

    for arbitration in arb_tileset:
        if arbitration.lower().strip() in substring_Name.lower().strip():
            message= (f'Mission is {arbitration}. Tier: {arb_tier_list[index]} \n')
        index += 1

    for enemy in enemy_types:
        if enemy.lower().strip() in substring_Type.lower().strip():
            message+= f'Enemy Type: {enemy}\n'
        #      break
        # print(i)

    current_minutes=current_minutes_copy-current_minutes
    message+= f'Time left: {current_minutes}'
    print(message)
    return message


def printArchon():
    responseArchon = requests.get("https://api.warframestat.us/pc/archonHunt")
    string = json.dumps(responseArchon.json(), sort_keys=True, indent=4)
    print(string)


def printCetusStatus():
    responseCetusStatus = requests.get("https://api.warframestat.us/pc/cetusCycle")
    string = json.dumps(responseCetusStatus.json(), sort_keys=True, indent=4)
    print(string)
    indexState = int(string.find("state")) + 9
    indexTimeLeft = int(string.find("shortString") + 15)
    accurateTimeLeft = string[len(string) - 10:len(string) - 3]
    if (string[indexState:indexState + 5] == "night"):
        return "State: Night\n" + "Time left to day:  " + string[indexTimeLeft:indexTimeLeft + 3]

    elif (string[indexState:indexState + 3] == "day"):
        return "State: Day\n" + "Time left to night:  " + string[indexTimeLeft:indexTimeLeft + 3]


# response= requests.get("http://content.warframe.com/dynamic/worldState.php")

# print(response.json())

number = int(input("1->Arb 2->Archon 3->PoE cycle:  \n"))

if (number != 0):

    while number != 0:

        match number:
            case 1:
              printArb()

            case 2:
                printArchon()

            case 3:
                printCetusStatus()

        number = int(input("1->Arb 2->Archon 3->PoE cycle:  \n"))
