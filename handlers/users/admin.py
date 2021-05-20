from aiogram import types
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), user_id=[321846604], text="admin")
@dp.message_handler(IsPrivate(), user_id=[321846604], text="secret")
async def admin_chat_secret(message: types.Message):
    await message.answer("Это секретное сообщение вызванное одним из администраторов"
                         "в личной переписке")