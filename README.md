Half of the fourth laboratory work in a cycle on the subject of User Interface Development
Other half located here: https://github.com/PopeyeTheSailorsCat/TelegramBotServer
# Telegram Bot
This is a student project in which we create a Telegram bot, 
and a Django server to work with this bot. Interaction is carried out via the REST API. 
The server and bot are deployed on Heroku.

The interaction between this repository and the heroku repository is carried out via Jenkins with the push project build.
Programming language is Python 3.7

## Repository content
In this repository, we have two main folder:  
 * TelegramBot source (src)
 * Tests for TelegramBot (tests)

Also in this repository there are files related to the launching the bot on the heroku.

## Getting Telegram Bot token
To make your bot in telegram register him : 'https://core.telegram.org/bots' to BotFather.
After that you will have Bot Token so Telegram can give your info from dialog with bot.
Set your token at environment variable called tg_bot_token, so it can be called by:
```python
tg_bot_token = os.environ.get('tg_bot_token')
```
How to do it on Heroku:https://devcenter.heroku.com/articles/config-vars

## Running Telegram Bot locally
To start bot on you local machine you will need python at first.
From project root run
```commandline
    > python src/main.py
```
## Deploy Telegram  Bot on heroku
Repository already have all needed for running django application on heroku. All you need is to create heroku repo for your project and push this repo there (https://devcenter.heroku.com/articles/getting-started-with-python).
After pushing project to heroku run from project root.
```commandline
    > heroku scale worker = 1
```
## Additional step
In order for the bot to interact with your server, you need to specify the url of your server in the bot's config.
### Running on server
Write yours server url at bot repository 'src/config.py' in server_gateway_api["root"], so it will look like this.
```python
    server_gateway_api = {"root": "your_server_url", "open_weather": "openweather"}
```
### Running on local
To allow the bot to access the local server, you need to make the local server available from the network/
There are several ways to achieve this. One of them is to use localhost.run to host access to your local server (https://localhost.run/).
On their website, you can find a simple guide to the host. 
After you want your local address, you should be given your url.
It should be added as indicated in 'Running on server'
## Using Bot
To interact with the bot we raised, write to it in a telegram : @spbstu_check_weather_bot
### Examples of interaction

   ![PIC_1](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/tg_bot_1.png)
   
   ![PIC 2](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/tg_bot_2.png)

# Development team
1. Mamaeva Anastasia

     work email: mamaeva.as@edu.spbstu.ru
    
2. Vedenichev Dmitry

     work email: vedenichev.da@edu.spbstu.ru 
