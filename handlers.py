import pymorphy2
import re
import mysql.connector
from main import bot, dp
from aiogram.types import Message
from config import admin_id
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Active9898",
  port="3307",
  database="test2"
)



morph = pymorphy2.MorphAnalyzer()
async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler()
async def echo(message: Message):
    file_1 = open("text.txt", "a", encoding='utf8')
   
    text_clear = re.sub(r'[^\w\s]','',message.text)
    lst = text_clear.split()
    norm_lst = []
    for word in lst:  
        p=morph.parse(word)[0]
        norm_lst.append(p.normal_form)



        
        mycursor = mydb.cursor()
        placeholders= ', '.join(['%s']*len(norm_lst))  # "%s, %s, %s, ... %s"
        #sql = "SELECT idq FROM tag WHERE text IN ({})".format(placeholders)
        sql = "SELECT tag.text AS tag, question.text AS most FROM tag INNER JOIN question ON tag.idq = question.idq"
        mycursor.execute(sql,tuple(norm_lst))

        myresult = mycursor.fetchall()
        
        for x in myresult:
         print(x)
         text = f"Кажется, есть ответ на твой вопрос: : {x}"
         await message.reply(text=text)

    file_1.write(p.normal_form + " ")
    file_1.write('\n')
    file_1.close()

