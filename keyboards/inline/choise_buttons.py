from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



"""
choise = InlineKeyboardMarkup(
    inline_keyboard=[

            InlineKeyboardButton(text="Показать фанфики, которые появились в топе сегодня", callback_data=saw_names(0)),
            InlineKeyboardButton(text="Показать фанфики, которые появились в топе гет за сегодня", callback_data=saw_names(1)),
            InlineKeyboardButton(text="Показать фанфики, которые появились в топе джен за сегодня", callback_data=saw_names(2))

    ]
)
"""

choise = InlineKeyboardMarkup(row_width=1)

ce_help = InlineKeyboardButton(text="Помощь", callback_data="help")
choise.insert(ce_help)

ce_myw = InlineKeyboardButton(text="Вывести слова которые я выучил", callback_data="my_w")
choise.insert(ce_myw)

ce_data = InlineKeyboardButton(text="Вывести дату на английском", callback_data="data")
choise.insert(ce_data)

