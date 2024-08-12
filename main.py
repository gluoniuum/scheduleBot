import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, Message, InlineQuery
from aiogram import types
from datetime import datetime
from aiogram.client.bot import DefaultBotProperties
# Замените токен на токен вашего бота
API_TOKEN = '7093731816:AAF-qmPKyI3Rd3oaC4yZkiP0ejwIMMfgDmk'

bot = Bot(token=API_TOKEN,default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
router = Router()

allWeek_schedule = 0

###!
current_time = datetime.now()
print('yay')
monday = {
1: 'math',
2: 'geo',
3: 'ukr',
4: 'eng',
5: 'chem',
}
tuesday = {
1: 'geo',
2: 'math',
3: 'chem',
4: 'eng',
5: 'ukr',
}

wednesday = {
1: ' math ',
2: ' ukr ',
3: ' geo ',
4: ' eng ',
5: 'art ',
}

thursday = {
1: 'chem',
2: 'IT',
3: 'eng',
4: 'art',
5: 'geo',
}

friday = {
1: 'ukr',
2: 'art',
3: 'IT',
4: 'chem',
5: 'ukr',
}

f_monday = '\n'.join(f'{key}: {value}' for key, value in monday.items())
f_tuesday = '\n'.join(f'{key}: {value}' for key, value in tuesday.items())
f_wednesday = '\n'.join(f'{key}: {value}' for key, value in wednesday.items())
f_thursday = '\n'.join(f'{key}: {value}' for key, value in thursday.items())
f_friday = '\n'.join(f'{key}: {value}' for key, value in friday.items())

intToDay ={
    0: f_monday,
    1: f_tuesday,
    2: f_wednesday,
    3: f_thursday,
    4: f_friday,}

daysWeek ={
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',}
###*



def allWeek():

    allWeek_schedule = ''
    for number in range(0, 4):  
        week_schedule = intToDay[number]
        allWeek_schedule = f''' 
{allWeek_schedule} 

*{daysWeek[number] }*        
{week_schedule} '''
    return allWeek_schedule


def afterDay():
    current_time = int(datetime.now().weekday() + 1) 
    after_schedule = intToDay[current_time]
    return after_schedule

def toDay():
    current_time = int(datetime.now().weekday()) 
    today_schedule = intToDay[current_time]
    return today_schedule
    

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'yay_ {message.from_user.first_name}, це бот для розкладу')

###?    

@router.inline_query()
async def handle_inline_query(inline_query: InlineQuery):
    
    
    result = InlineQueryResultArticle(
        id = 'unique_result_id_120',  
        title = 'Schedule for a Week'  ,
        cache_time = 1,
        is_personal = 1,
        input_message_content = InputTextMessageContent(
            message_text = f'''Week:  
{allWeek()}'''

        ) 
    )
    result2 = InlineQueryResultArticle(
        id = 'unique_result_id_119',  
        title = ('Tomorrow Schedule')  ,
        cache_time = 1,
        is_personal = 1,
        input_message_content = InputTextMessageContent(
            message_text = f'''Tomorrow:
{afterDay()}'''
            
        ),
        
    )   
    result3 = InlineQueryResultArticle(
        id = 'unique_result_id_125',  
        title ='Today schedule '  ,
        cache_time = 1,
        is_personal = 1,
        input_message_content = InputTextMessageContent(
            message_text = f'''Today:
{toDay()}''' 
        ) 
    )
    await bot.answer_inline_query(inline_query.id, results=[result,result2, result3])
    


dp.include_router(router)
###!
async def main():
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)
    print('щзх')
if __name__ == '__main__':
    asyncio.run(main())
    