from aiogram.types import *
from aiogram.utils.keyboard import *
from aiogram.filters.callback_data import *
main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Stickers"),
            KeyboardButton(text="links"),            
        ],
        [
            KeyboardButton(text="calc"),
            KeyboardButton(text="special"), 
        ],
        
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    input_field_placeholder = 'chose action',
    selective = True,

)

links_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'ytb', url = 'https://www.youtube.com/channel/UCZUrS0zDszsXI_5ir_tI3cg'),
            InlineKeyboardButton(text = "telegram", url = 'tg://resolve?domain=windy31room')
        ]
    ]
)

spec_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'send location', request_location = True),
            KeyboardButton(text = 'send contact', request_contact = True),
            KeyboardButton(text = 'create poll', request_pool = KeyboardButtonPollType())
    ],
    [
        KeyboardButton(text = 'back')
    ]
    
],
resize_keyboard = True
)

class Pagination(CallbackData, prefix = 'pag'):
    action: str
    page: int
    #

def paginator(page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text= '♂️', callback_data = Pagination(action = 'prev', page = page).pack()),
        InlineKeyboardButton(text= '🍆', callback_data = Pagination(action = 'next', page = page).pack()),
    
    )


def calc_kb():
    
    items = [
        '1', '2', '3','/',
        '4','5','6','*',
        '7','8','9','-',
        '0','.','=','+',
    ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text='back')
    builder.adjust(4,4,4,4)
    return builder.as_markup(resize_keyboard = True)
        