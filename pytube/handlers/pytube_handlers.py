from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold
from loader import dp, bot
from keyboards import konfeta_keyboard
from keyboards import start_ik, konfeta_levels_ik
from keyboards import start_callback, konfeta_callback, calc_callback, vsbot, vsplayer, youtube_callback
from states import PlayerState
from pytube import YouTube


@dp.message_handler(text=['привет', 'Привет', 'Начать'])  # Message_handler - обрабатывет сообщения
@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет, {hbold(message.from_user.first_name)}! 👋\n',
                         reply_markup=start_ik)
    # await message.answer(reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)


@dp.callback_query_handler(konfeta_callback.filter())
async def call_confeta(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)
    await call.message.answer(text='Выберите уровень',
                              reply_markup=konfeta_levels_ik)


@dp.callback_query_handler(vsbot.filter())
async def call_confeta(call: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)
    common_num = 2021
    await call.message.answer(text=f'{hbold("ПРАВИЛА ИГРЫ")}'
                                   '\nНа столе лежит 2021 конфета. Игроки ходят поочереди.'
                                   '\nВ свой ход игрок может взять до 28 конфет включительо'
                                   '\nПобеждает тот, кто возьмет последню конфету со стола'
                                   '\n'
                                   f'\nНа столе {common_num}. Cколько конфет возьмете? (не больше 28 и не больше {common_num})',
                              reply_markup=konfeta_keyboard)
    await PlayerState.player_hod.set()
    await state.update_data(common_num=2021)


@dp.message_handler(text='Начать с начала')
async def call_confeta(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)
    common_num = 2021
    await message.answer(text=f'{hbold("ПРАВИЛА ИГРЫ")}'
                              '\nНа столе лежит 2021 конфета. Игроки ходят поочереди.'
                              '\nВ свой ход игрок может взять до 28 конфет включительо'
                              '\nПобеждает тот, кто возьмет последню конфету со стола'
                              '\n'
                              f'\nНа столе {common_num}. Cколько конфет возьмете? (не больше 28 и не больше {common_num})',
                         reply_markup=konfeta_keyboard)
    await PlayerState.player_hod.set()
    await state.update_data(common_num=2021)


@dp.message_handler(text='Выйти из игры')
async def call_confeta(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id)
    await message.answer(text=':)',
                         reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text='Главное меню',
                         reply_markup=start_ik)


@dp.message_handler(state=PlayerState.player_hod)
async def get_item_name(message: types.Message, state: FSMContext):
    global bot_hod
    result = await state.get_data()
    common_num = result['common_num']
    if message.text == 'Начать с начала':
        await state.reset_state()
        await call_confeta()
    elif message.text == 'Выйти из игры':
        await message.answer(text='Привет',
                             reply_markup=types.ReplyKeyboardRemove())
        await bot.delete_message(chat_id=message.chat.id,
                                 message_id=message.message_id)
        await message.answer(text='Главное меню',
                             reply_markup=start_ik)
        await state.reset_state()
    elif int(message.text) > 28:
        await message.answer(text=f'Ну вообще-то {message.text} больше 28. Меня не проведешь! '
                                  '\nПопробуй еще разок')
    elif int(message.text) > common_num:
        await message.answer(text=f'На столе нет столько конфет. Сейчас на столе осталось {common_num} конфет.'
                                  f'Меня не проведешь! '
                                  '\nПопробуй еще разок')
    else:
        common_num -= int(message.text)
        if common_num == 0:
            await message.answer(text=f'ПОЗРАВЛЯЮ!'
                                      f'\nТы победил!',
                                 reply_markup=start_ik)
            await state.reset_state()
        if common_num > 28:
            bot_hod = 29 - int(message.text)
            common_num -= bot_hod
            await bot.delete_message(chat_id=message.chat.id,
                                     message_id=message.message_id)
            await message.answer(
                text=f'\nТы взял: {message.text}'
                     f'\nBot взял: {bot_hod}'
                     f'\nОстаток на столе: {common_num}'
                     f'\n'
                     f'\nCколько конфет возьмете? (не больше 28 и не больше {common_num})')
            await PlayerState.player_hod.set()
            await state.update_data(common_num=common_num)
        elif common_num < 28:
            await message.answer(text=f'Увы, Bot взял последние {common_num} конфет'
                                      '\nТы проиграл :(',
                                 reply_markup=start_ik)
            await state.reset_state()


@dp.callback_query_handler(youtube_callback.filter())
async def call_youtube(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Вставьте ссылку на видео для его скачивания')
    await PlayerState.video_link.set()


@dp.message_handler(state=PlayerState.video_link)
async def get_item_name(message: types.Message, state: FSMContext):
    my_video = YouTube(message.text)
    print(message.text)
    await message.answer(text=f'Информация по видео:'
                              f'\nНаименование: {my_video.title}'
                              f'\nДлительность: {my_video.length}'
                              f'\n'
                              f'\nНачать скачивание? (Да / Нет)')
    await PlayerState.start_load.set()
    await state.update_data(my_video=message.text)


@dp.message_handler(state=PlayerState.start_load)
async def get_item_name(message: types.Message, state: FSMContext):
    result = await state.get_data()
    my_link = result['my_video']
    save_path = '/Users/nikolaishpagin/Desktop'
    my_video = YouTube(my_link).streams.first()
    my_video.download(save_path)
    if message.text == 'Да ':
        await message.answer(text=f'Скачивание началось',
                             reply_markup=start_ik)
        await state.reset_state()
    else:
        await message.answer(text=f'Скачивание видео отменено',
                             reply_markup=start_ik)
        await state.reset_state()