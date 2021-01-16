from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.RED)
print("Script by Zevi/Скрипт сделан Zevi")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█")
print("█▀█ █░█░█ █ █░▀█ █░█ ░▀▄ █░█ █▀█ █░█░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀▀░ █▀░ ▀░▀ ▀░░░▀")
import amino
#инпут почты и пароля для входа в аккаунт
email=input("Email/Почта:")
password=input("Password/Пароль:")
chatid=input("Type chatid/Введите чат айди:")
comid='156542274'
#клиент логин это вход бота в аккаунт
client = amino.Client() 
client.login(email=email, password=password)
sub_client = amino.SubClient(comId=comid,profile=client.profile)
print('\nLogged in/Бот зашел!')
#джойн чат это вход бота в чат
sub_client.join_chat(chatId=chatid)
print("\nJoined Chatroom/Бот зашел в чат")
#инпут сообщения и типа сообщения
message=input("Message/Сообщение:")
mType=input("Message Type/Тип Сообщения:")
#While это цикл для спама а сенд мессейдж отправка сообщения
while True:
		try: sub_client.send_message(message=message, chatId=chatid, messageType=mType)
		except: pass
		print("\nMessage Sended/Сообщение отправлено")