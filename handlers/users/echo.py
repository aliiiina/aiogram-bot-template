from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot


# @dp.message_handler(text="/start")
# async def bot_echo(message: types.Message):
#     await message.answer(f"Эхо без состояния. /start"
#                          f"Сообщение:\n"
#                          f"{message.text}")
#
#
#
# # Эхо хендлер, куда летят текстовые сообщения без указанного состояния
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     # chat_id = message.chat.id
#     # text = message.text
#     # await bot.send_message(chat_id=chat_id, text=text)
#     await message.answer(f"Эхо без состояния."
#                          f"Сообщение:\n"
#                          f"{message.text}")
#     await message.reply(message.text)
#
#
# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
