from aiogram.dispatcher.filters.state import StatesGroup, State


class PlayerState(StatesGroup):
    player_hod = State()
    video_link = State()
    start_load = State()
