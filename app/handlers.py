from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import  FSMContext
import app.DataBase.requests as rq

import app.keyboards as kb

router = Router()





@router.message(CommandStart())
async  def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Привет!',reply_markup=kb.main)
