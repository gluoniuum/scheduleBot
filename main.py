import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, Message, InlineQuery
from aiogram import types
from datetime import datetime
# Замените токен на токен вашего бота
API_TOKEN = '7093731816:AAF-qmPKyI3Rd3oaC4yZkiP0ejwIMMfgDmk'

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()
router = Router()


###!
current_time = datetime.now()
scheldue = {
    '0' : 'm, p, e,', #pn
    '1' : 'p, e, m',  #vt
    '2' : 'a, f, e',  #sr
    '3' : 't, m, d',  #cht
    '4' : 'm, z, e',  #pt
}

###*
def afterday():
    current_time = datetime.now().weekday()
    

afterday()
@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'yay_ {message.from_user.first_name}, це бот для розкладу')

###?    

@router.inline_query()
async def handle_inline_query(inline_query: InlineQuery):
    
    
    result = InlineQueryResultArticle(
        id = 'unique_result_id_120',  
        title =' Розклад весь'  ,
        input_message_content = InputTextMessageContent(
            message_text = f'Вот ваш розклад: {scheldue.items()}'
        )  
    )
    result2 = InlineQueryResultArticle(
        id = 'unique_result_id_119',  
        title =' Розклад завтра'  ,
        input_message_content = InputTextMessageContent(
                
            message_text = f'Вот ваш розклад на <b> завтраa </b>: {scheldue}'
        ),
        
    )   
    await bot.answer_inline_query(inline_query.id, results=[result,result2])
    
dp.include_router(router)
###!
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print('щзх')
if __name__ == "__main__":
    asyncio.run(main())
    