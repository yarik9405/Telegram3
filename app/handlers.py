from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import  FSMContext


import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()



@router.message(CommandStart())
async  def cmd_start(message: Message):
    await message.answer('Привет!',reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await  message.answer('Вы нажали кнопку помощи')


@router.message(F.text == 'Каталог')
async  def catalog(message: Message):
    await message.answer('я очень рад',reply_markup=kb.catalog)

@router.callback_query(F.data == 'bmw' )
async  def bmw(callback: CallbackQuery):
    await  callback.answer('Vy byrali', show_alert = True)
    await callback.message.answer('Вы выбрали бмв')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('VVedite vashe imya')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
     await  state.update_data(name=message.text)
     await state.set_state(Register.age)
     await message.answer('Введите ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
     await  state.update_data(age=message.text)
     await state.set_state(Register.number)
     await message.answer('Введитe nomer telefona',reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Vasje imya: {data["name"]} \n Ваш возраст: {data["age"]} \n ваш номер телефона: {data["number"]}')
    await state.clear()