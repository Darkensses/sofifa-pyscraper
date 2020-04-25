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
#Liga MX = 39
response = requests.get(base_url + "/league/" + arr_leagues[39].get("id_league"))
```


## Construido con 🛠️

* Python - El lengujae del script
* pip - Instaldor depaquetes
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