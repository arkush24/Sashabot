from aiogram.dispatcher.filters.state import StatesGroup, State


class RegIn(StatesGroup):
    nickname = State()
    password = State()
