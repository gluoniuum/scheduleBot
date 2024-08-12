import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, Message, InlineQuery
from aiogram import types
from datetime import datetime
from aiogram.client.bot import DefaultBotProperties
# Замените токен на токен вашего бота
API_TOKEN = '7093731816:AAF-qmPKyI3Rd3oaC4yZkiP0ejwIMMfgDmk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()


###!
current_time = datetime.now()

monday = '''
Monday: 
1. math
2. geo
3. ukr
4. eng
5. chem
'''
tuesday = '''
Tuesday: 
1. geo
2. math
3. chem
4. eng
5. ukr
'''
wednesday = '''
Wednesday: 
1. math
2. ukr
3. geo
4. enf
5. art
'''
thursday = '''
Thursday: 
1. chem
2. IT
3. eng
4. art
5. geo
'''
friday = '''
Thursday: 
1. ukr
2. art
3. IT
4. chem
5. ukr
'''


intToDay ={
    0: monday,
    1: tuesday,
    2: wednesday,
    3: thursday,
    4: friday,

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
        cache_time = 1,
        is_personal = 1,
        input_message_content = InputTextMessageContent(
            message_text = f'Вот ваш розклад:  {ponedilok}'
        ) 
    )
    result2 = InlineQueryResultArticle(
        id = 'unique_result_id_119',  
        title =' Розклад завтра'  ,
        cache_time = 1,
        is_personal = 1,
        input_message_content = InputTextMessageContent(
            message_text = f'Вот ваш розклад: {ponedilok}'
            
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
    