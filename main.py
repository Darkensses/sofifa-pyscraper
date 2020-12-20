import json
import math
import os

import requests
from parsel import Selector
import time
import re

import unicodedata

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text,'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def text_to_id(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(text.lower())
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    return text

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

    pDict["age"] = int(re.search("[0-9]{2}(?=y.o)", pInfo).group(0))

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
print("START")
response = requests.get(base_url)
selector = Selector(response.text)

arr_leagues = []
arr_teams = []
arr_players = []

leagues = selector.xpath("//select[@data-placeholder='Leagues']//option").getall()

for index, league in enumerate(leagues):
    item = {"id_league": int(Selector(league).xpath("//@value").get()),
            "name_league": re.sub("(\s)(\\xa0)?(\(\d\))", "", Selector(league).xpath("//text()").get())}

    item["data"] = text_to_id(item.get("name_league")) + ".json";
    arr_leagues.append(item)
    print(f"{index} : {arr_leagues[index]}")
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    with open(desktop + "\\leagues.json", 'w', encoding='utf-8') as fp:
        json.dump(arr_leagues, fp, sort_keys=True, indent=4, ensure_ascii=False)
# end for
print("---------------")

# Check the leagues indexes at https://github.com/Darkensses/sofifa-pyscraper#ligas
# Change the league index in the line below: arr_leagues[FAV_INDEX]
response = requests.get(base_url + "/teams?type=all&lg%5B%5D=" + str(arr_leagues[2].get("id_league")))
selector = Selector(response.text)
teams = selector.xpath("//a[contains(@href,'/team/')]").getall()
for index, team in enumerate(teams):
    item = {"id_team": Selector(team).xpath("//@href").get().split("/")[2],
            "name_team": Selector(team).xpath("//text()").get()}

    arr_teams.append(item)
    print(f"{index} : {arr_teams[index]}")
# end for
print("---------------")

dataPlayer = {}
arr_league = []

for team in arr_teams:
    response = requests.get(base_url + "/team/" + team["id_team"])
    print(base_url + "/team/" + team["id_team"])
    selector = Selector(response.text)
    players = selector.xpath("//text()[.='Squad']/following::table[1]/tbody/tr//a[contains(@href,'/player/')]").getall()
    for index, player in enumerate(players):
        item = {"id_player": Selector(player).xpath("//@href").get().split('/')[2],
                "name": Selector(player).xpath("//text()").get().lstrip()}

        stats = getPlayerStats(item.get("id_player"))
        item.update(stats)
        dataPlayer["{}".format(item.get("id_player"))] = item
        arr_players.append(item)
        print(f"{index} : {item}")
    # end for player
    arr_league.append({"name_team": team["name_team"], "players": arr_players.copy()})
    dataPlayer.clear()
    arr_players.clear()

#end for team

# Save the dictonary into a JSON file in your Desktop!
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
with open(desktop + "\\ligaMX.json", 'w', encoding='utf-8') as fp:
    json.dump(arr_league, fp, sort_keys=True, indent=4, ensure_ascii=False)

end = time.time()

print(f"It takes {end - start} seconds")
