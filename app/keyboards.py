from  aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardButton, InlineKeyboardMarkup)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                           [KeyboardButton(text='Korzina')],
                           [KeyboardButton(text='Kontacts'),
                           KeyboardButton(text='O nas')]],

                          resize_keyboard=True,
                          input_field_placeholder='vybor')
catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='porsh', callback_data='mash1')],
                                                [InlineKeyboardButton(text='bmw', callback_data='bmw')],
                                                [InlineKeyboardButton(text='mercedes', callback_data='mash3')]
                                                ])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Otpravit nomer ',request_contact=True )]],
                                 resize_keyboard=True)