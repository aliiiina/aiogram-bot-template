from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


# state = None
@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование\n"
                         "Вопрос № 1\n\n"
                         "Вы часто занимаетесь бессмысленными делами \n"
                         "(бесцельно блуждаете по интеренту, клацаете пультом телевизора, просто смотрите в потолок)")

    await Test.Q1.set()


# await Test.first()
# фильтр ответа на первый вопрос
@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    # await state.update_data(
    #     {
    #         "answer1": answer
    #     }
    # )

    # async with state.proxy() as data:
    #     data["answer1"] = answer

    await message.answer("Вопрос № 2\n\n"
                         "Ваша память ухудшилась\n"
                         "и вы помните то, что давно было, но забываете недавние события")

    # await Test.Q2.set()
    # await Test.previous()
    # Вариант установить состояние
    # await state.set_state("")
    await Test.next()


# фильтр ответа на второй вопрос
@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы!")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    # Вариант завершения состояния
    # await state.finish()
    await state.reset_state()
    # сбросить сотояние, но не сбрасывать данные
    # await state.reset_state(with_data=False)


# @dp.message_handler(state="enter_email")
# async def answer_q2(message: types.Message, state: FSMContext):
#     await message.answer("")
#     await state.reset_state()
#
#
# @dp.message_handler()
# async def answer_q2(message: types.Message, state: FSMContext):
#     await message.answer("")
#     await state.set_state("enter_email")
