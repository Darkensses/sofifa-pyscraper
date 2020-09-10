# SoFIFA-pyScraper

Scraper hecho en python para obtener la información importante y habilidades de todos los jugadores (por ahora de una liga determinada) de la pagina de sofifa.

El motivo del desarrollo de esta herramineta fue porque sofifa no cuenta con alguna API para obtener información de forma rápida, por lo que obtener datos sobre equipos o jugadores era un proceso muy lento, asi que decidí automatizarlo ya que actualmente la información de los jugadores se utiliza para generar los equipo para un parche de Winning Eleven 2002.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

- Una computadora 💻 (por ahora solo ha sido probado en Windows 10)
- Python 3 🐍
- pip 🧪
- PyCharm 📝 (preferible) o cualquier otro IDE


### Instalación 🔧

Descarga o clona el repo:
`git clone https://github.com/Darkensses/sofifa-pyscraper.git`

Si descargaste el repo:
- descomprime el .zip
- Abre tu IDE preferido (como PyCharm)
- Instala la libreria de parsel
- Ejecuta el script

En caso de que hayas clonado el repo:
- Abre tu consola y navega a la carpeta
- Instala la libreria parsel: `pip instal parsel --user`
- Ejecuta el script: `python main.py`

Al terminar la ejecucion del script podrás notar que tu consola estará llena de toda la información recolectada 🧐 y que además en tu escritorio se habrá creado un archivo json con toda esa información 😮

## Diviertete
Por el momento puedes cambiar la liga para obtener otros equipos, tan solo debes poner el indice de la liga que se imprime en la consola:

```python
#Liga MX = 26
response = requests.get(base_url + "/league/" + arr_leagues[26].get("id_league"))
```

Puedes encontrar el index de la liga que quieras utilizar el script en la siguiente tabla. El index puede variar cada cierto tiempo debido a los cambios que sofifa realiza en su página, sin embargo el id de cada liga es único y siempre será el mismo.

### Ligas
| index | id | nombre |
|---|---|---|
0 | 13 | English Premier League
1 | 16 | French Ligue 1
2 | 19 | German 1. Bundesliga
3 | 31 | Italian Serie A
4 | 53 | Spain Primera División
5 | 353 | Argentina Primera División
6 | 351 | Australian Hyundai A-League
7 | 80 | Austrian Football Bundesliga
8 | 4 | Belgian Jupiler Pro League
9 | 7 | Campeonato Brasileiro Série A
10 | 335 | Chilian Campeonato Nacional
11 | 2012 | Chinese Super League
12 | 336 | Colombian Liga Postobón
13 | 317 | Croatian Prva HNL
14 | 319 | Czech Republic Gambrinus Liga
15 | 1 | Danish Superliga
16 | 2018 | Ecuadorian Serie A
17 | 14 | English League Championship
18 | 60 | English League One
19 | 61 | English League Two
20 | 322 | Finnish Veikkausliiga
21 | 17 | French Ligue 2
22 | 20 | German 2. Bundesliga
23 | 2076 | German 3. Bundesliga
24 | 63 | Greek Super League
25 | 10 | Holland Eredivisie
26 | 78 | International
27 | 32 | Italian Serie B
28 | 349 | Japanese J. League Division 1
29 | 83 | Korean K League Classic
30 | 2017 | Liga de Fútbol Profesional Boliviano
32 | 341 | Mexican Liga MX
32 | 41 | Norwegian Eliteserien
33 | 337 | Paraguayan Primera División
34 | 2020 | Peruvian Primera División
35 | 66 | Polish T-Mobile Ekstraklasa
36 | 308 | Portuguese Liga ZON SAGRES
37 | 65 | Rep. Ireland Airtricity League
38 | 330 | Romanian Liga I
39 | 67 | Russian Premier League
40 | 350 | Saudi Abdul L. Jameel League
41 | 50 | Scottish Premiership
42 | 347 | South African Premier Division
43 | 54 | Spanish Segunda División
44 | 56 | Swedish Allsvenskan
45 | 189 | Swiss Super League
46 | 68 | Turkish Süper Lig
47 | 2013 | UAE Arabian Gulf League
48 | 39 | USA Major League Soccer
49 | 332 | Ukrainian Premier League
50 | 338 | Uruguayan Primera División
51 | 2019 | Venezuelan Primera División


## Construido con 🛠️

* Python - El lenguaje del script
* pip - Instalador depaquetes
* PyCharm - IDE para python
* [editor.md](https://pandao.github.io/editor.md/en.html) - Usado para crear este bonito readme.md

## Contribuyendo 🖇️

Puedes contribuir a este repo con mejores y cosas que creas que sean de gran utilidad, tan solo hay x pequeñas restricciones:

* Los atributos de los jugadores que y están en el código se tienen que quedar con el mismo nombre.
* Se pueden agregar nuevos atrubutos o información siempre y cuando se mantengan los atributos que ya existen.
* Nada de codigo dañino. Es un simple e inocente scraper a una muy buena página con excelente información.

## Autores ✒️

* **Jasiel Guillen** - *Trabajo Inicial* - [Darkensses](https://github.com/Darkensses)
* **MexWE** - *la mejor inspiracion para crear esto*


## Licencia 📄

Este código es libre y completamente abierto para todo el público, pero no olvides mencionarnos en alguna parte de tu proyecto 😉. Úsalo como quieras, siempre y cuando no se utilice para cosas maliciosas. Como ya dije más arriba, es un scraper simple e inocente, dejemoslo así.

## Expresiones de Gratitud 🎁

* Apoya la página de [MexWE](https://www.facebook.com/MexWEdition)
* Suscribte al canal de [MewWE](https://www.youtube.com/channel/UC-QTa6viKQvBu4hitWfE0oQ/featured)
* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un sushi 🍣 a alguien del equipo.
* Da las gracias públicamente 🤓.



---
⌨️ con ❤️ por [Jasiel Guillen](https://github.com/Darkensses) 😊