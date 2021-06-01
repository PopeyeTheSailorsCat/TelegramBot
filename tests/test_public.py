import pytest
from unittest.mock import AsyncMock
from src.weather_tg_bot import *


class TestWeatherTgBot:
    def setup(self):
        self.text_mock = "Moscow"
        self.message_mock = AsyncMock(text=self.text_mock)

    @pytest.mark.asyncio
    async def test_get_weather_city_exist(self):
        # write here what you expected in response
        expected_element = 'Pressure'
        expected_element_2 = self.text_mock

        await get_weather(message=self.message_mock)
        self.message_mock.reply.assert_awaited()  # check if reply was awaited
        result = self.get_str_from_message_mock(self.message_mock)
        # Checking return msg
        assert expected_element in result
        assert expected_element_2 in result

    @pytest.mark.asyncio
    async def test_get_weather_city_dont_exist(self):
        # wrute here what you expected in response
        exp_elem = 'Check how you wrote'

        self.message_mock.text = "Does Not exist"
        await get_weather(message=self.message_mock)
        self.message_mock.reply.assert_awaited()  # check if reply was awaited
        result = self.get_str_from_message_mock(self.message_mock)

        # checking return msg
        assert exp_elem in result

    @pytest.mark.asyncio
    async def test_start_command(self):
        # write here what you expected in response
        expected_element = 'Write'

        await start_command(message=self.message_mock)
        self.message_mock.reply.assert_awaited()  # check if reply was awaited
        result = self.get_str_from_message_mock(self.message_mock)
        assert expected_element in result

    def get_str_from_message_mock(self, message_mock):
        result, *_ = message_mock.reply.call_args[0]  # get from call first element(tuple) and unpack it, get str
        return result
