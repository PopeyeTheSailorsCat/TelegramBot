import requests
import datetime
import os
from src.config import server_gateway_api
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

tg_bot_token = os.environ.get('tg_bot_token')
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
get_weather_api = server_gateway_api["root"] + server_gateway_api["open_weather"]


def msg_create_success(data):
    city = data["name"]
    cur_weather = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestap = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
        data["sys"]["sunrise"])
    msg = f"***{datetime.datetime.now().strftime('%d-%m-%Y- %H:%M')}(UTC)***\n" \
          f"Weather in the city: {city}\nTemperature: {cur_weather}C°\n" \
          f"Humidity: {humidity}%\nPressure: {pressure} mm Hg\n" \
          f"Wind: {wind}м/с\nSunrise(UTC): {sunrise_timestamp}\n" \
          f"Sunset(UTC): {sunset_timestap}\nDuration of the day: {length_of_the_day}\n" \
          f"Have a nice day!"
    return msg


def msg_create_error():
    msg = "Check how you wrote the name of the city."
    return msg


def msg_create_start():
    msg = "Hi! Write me the name of the city and I'll send you the weather forecast"
    return msg


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    msg = msg_create_start()
    await message.reply(msg)


@dp.message_handler()
async def get_weather(message: types.Message):  # if we get smth form user
    try:
        r = requests.get(
            get_weather_api + f"?city={message.text}")
        data = r.json()
        # print(data)
        msg = msg_create_success(data)
        await message.reply(msg)

    except:
        msg = msg_create_error()
        await message.reply(msg)


def main():
    executor.start_polling(dp)
