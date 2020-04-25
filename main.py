import json
import math
import os

import requests
from parsel import Selector
import time
import re

# function to convert string to camelCase
def camelCase(string):
  string = re.sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]

# function to get all the important player stats
def getPlayerStats(id_player):
    response = requests.get(base_url + "/player/" + id_player)
    selector = Selector(response.text)
    pDict = {}

    # Get general info about Player
    pInfo = selector.xpath("//div[@class='info']/div/text()[last()]").get()

    pDict["age"] = re.search("[0-9]{2}(?=y.o)", pInfo).group(0)

    # Get height and weight in Imperial System
    feet = int(re.search("[0-9]*(?=')", pInfo).group(0))
    inches = int(re.search("[0-9]*(?=\")", pInfo).group(0))
    lbs = int(re.search("[0-9]*(?=lbs)", pInfo).group(0))

    # Then convert them to Metric System and add to dictionary
    pDict["height"] = math.floor((feet * 30.48) + (inches * 2.54))
    pDict["weight"] = math.floor(lbs * 0.453592)

    # Get the data (position, preferred foot, weak foot and shirt number) from the second section
    pDict["position"] = selector.xpath("//div[@class='info']//span[contains(@class, 'pos')]/text()").get()
    pDict["preferredFoot"] = selector.xpath("//label[text()='Preferred Foot']/following-sibling::text()").get()
    weakFoot = selector.xpath("//label[text()='Weak Foot']/preceding-sibling::text()").get().replace(" ", "")
    jerseyNumber = selector.xpath("//label[text()='Jersey Number']/following-sibling::text()").getall()
    if len(jerseyNumber) > 1:
        jerseyNumber = jerseyNumber[1].replace(" ", "")
    else:
        jerseyNumber = jerseyNumber[0].replace(" ", "")
    pDict["weakFoot"] = int(weakFoot)
    pDict["jerseyNumber"] = int(jerseyNumber)

    # The last part about players info is theri skills.
    # Based on scrapi.R code taken from SoFIFA API for R
    # https://github.com/valentinumbach/SoFIFA/blob/master/R/scrapi.R#L93
    # Please support to Valentin Umbach.
    score_labels = [
        "Crossing",
        "Finishing",
        "Heading Accuracy",
        "Short Passing",
        "Volleys",
        "Dribbling",
        "Curve",
        "FK Accuracy",
        "Long Passing",
        "Ball Control",
        "Acceleration",
        "Sprint Speed",
        "Agility",
        "Reactions",
        "Balance",
        "Shot Power",
        "Jumping",
        "Stamina",
        "Strength",
        "Long Shots",
        "Aggression",
        "Interceptions",
        "Positioning",
        "Vision",
        "Penalties",
        "Composure",
        "Defensive Awareness",  # change Marking to Defensive Awareness since API V3 and SOFIFA [FIFA 20 Oct 2019 04]
        "Standing Tackle",
        "Sliding Tackle",
        "GK Diving",
        "GK Handling",
        "GK Kicking",
        "GK Positioning",
        "GK Reflexes"
    ]

    for label in score_labels:
        score_value = selector.xpath("//*[text()[contains(.,'{}')]]//preceding-sibling::span//text()".format(label)).get()
        pDict[camelCase(label)] = int(score_value)

    return pDict

# START TO SCRAPY >:D
start = time.time()

base_url = "http://sofifa.com"

response = requests.get(base_url + "/leagues")
selector = Selector(response.text)

# leagues_href = selector.xpath("//a[contains(@href,'/league/')]/@href").getall()
# leagues_name = selector.xpath("//a[contains(@href,'/league/')]/text()").getall()
leagues = selector.xpath("//a[contains(@href,'/league/')]").getall()
arr_leagues = []
arr_teams = []
arr_players = []

for index, league in enumerate(leagues):
    item = {"id_league": Selector(league).xpath("//@href").get().replace("/league/", ""),
            "name_league": re.sub("(\s)(\\xa0)?(\(\d\))", "", Selector(league).xpath("//text()").get())}

    arr_leagues.append(item)
    print(f"{index} : {arr_leagues[index]}")
# end for
print("---------------")
# Liga MX
response = requests.get(base_url + "/league/" + arr_leagues[39].get("id_league"))
selector = Selector(response.text)
teams = selector.xpath("//a[contains(@href,'/team/')]").getall()
for index, team in enumerate(teams):
    item = {"id_team": re.sub("\D", "", Selector(team).xpath("//@href").get()),
            "name_team": Selector(team).xpath("//text()").get()}

    arr_teams.append(item)
    print(f"{index} : {arr_teams[index]}")
# end for
print("---------------")

dataleague = {}
dataPlayer = {}

# Santos Laguna: 10, Tigres: 7
for team in arr_teams:
    response = requests.get(base_url + "/team/" + team["id_team"])
    print(base_url + "/team/" + team["id_team"])
    selector = Selector(response.text)
    players = selector.xpath("//*[@id='adjust']/div/div[2]/table/tbody/tr//a[contains(@href,'/player/')]").getall()
    for index, player in enumerate(players):
        item = {"id_player": Selector(player).xpath("//@href").get().split('/')[2],
                "name": Selector(player).xpath("//text()").get().lstrip()}

        stats = getPlayerStats(item.get("id_player"))
        item.update(stats)
        dataPlayer["{}".format(item.get("id_player"))] = item
        print(f"{index} : {item}")
    # end for player
    dataleague["{}".format(team["name_team"])] = (dataPlayer.copy())
    dataPlayer.clear()
#end for team

# Save the dictonary into a JSON file in your Desktop!
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
with open(desktop + "\\ligaMX.json", 'w', encoding='utf-8') as fp:
    json.dump(dataleague, fp, sort_keys=True, indent=4, ensure_ascii=False)

end = time.time()

print(f"It takes {end - start} seconds")
