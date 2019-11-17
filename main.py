import requests
from parsel import Selector
import time
import re

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
response = requests.get(base_url + "/league/" + arr_leagues[37].get("id_league"))
selector = Selector(response.text)
teams = selector.xpath("//a[contains(@href,'/team/')]").getall()
for index, team in enumerate(teams):
    item = {"id_team": re.sub("\D", "", Selector(team).xpath("//@href").get()),
            "name_team": Selector(team).xpath("//text()").get()}

    arr_teams.append(item)
    print(f"{index} : {arr_teams[index]}")
# end for
print("---------------")
# Santos Laguna
response = requests.get(base_url + "/team/" + arr_teams[10].get("id_team"))
selector = Selector(response.text)
players = selector.xpath("//table[preceding-sibling::h6[contains(text(),'Squad')]]/tbody/tr//a[contains(@href,'/player/')]").getall()
for index, player in enumerate(players):
    item = {"id_player":  Selector(player).xpath("//@href").get().split('/')[2],
            "name": Selector(player).xpath("//text()").get()}

    arr_players.append(item)
    print(f"{index} : {arr_players[index]}")
# end for

end = time.time()

print(f"It takes {end - start} seconds")
