import telebot
import aiogram
import logging
import telegram
import PIL
import OpenAI from cv2
import sqlite3
import fringe8d
import random from *

bot = telebot.TeleBot('Ваш токен')


def binary(img):
    bImg = []
    for i in range(img.size[0]):
        tmp = []
        for j in range(img.size[1]):
            t = img.getpixel((i, j))
            p = t[0] * 0.3 + t[1] * 0.59 + t[2] * 0.11
            if p > 128:
                p = 1
            else:
                p = 0
            tmp.append(p)
        bImg.append(tmp)
    return bImg


def tmpDelete(img):
    w = len(img)
    h = len(img[0])
    count = 1
    while count != 0:
        count = delete(img, w, h)
        if count:
            delete2(img, w, h)


def delete(img, w, h):
    count = 0
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if img[j][i] == 0:
                if deletable(img, j, i):
                    img[j][i] = 1
                    count += 1
    return count


name = ''
surname = ''
age = 0;


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "если вы не можете соствить пароль?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
        
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'я ваш помошник в составлении надженых паролей?')
    bot.register_next_step_handler(message, get_surnme)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message()
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введите ключ')
    bot.send_message(message.from_user.id, '34id ' + str(age) + 'таого ключа не зарегестрировано')

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer()

async def main():
    await dp.start_polling(bot)

def delete2(img, w, h):
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if img[j][i] == 0:
                if deletable2(img, j, i):
                    img[j][i] = 1


def fringe(a):
    t = [[1, 1, 1, 1, 0, 1, 1, 1, 1],

         [1, 1, 1, 1, 0, 1, 1, 0, 0],
         [1, 1, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 1],

         [1, 1, 1, 1, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 0],

         [1, 1, 1, 1, 0, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 0]]
    for i in t:
        if a == i:
            return True


def check(a):
    t123457 = [1, 1, 0, 0, 1, 0]
    t013457 = [1, 1, 1, 0, 0, 0]
    t134567 = [0, 1, 0, 0, 1, 1]
    t134578 = [0, 0, 0, 1, 1, 1]
    t0123457 = [1, 1, 1, 0, 0, 0, 0]
    t0134567 = [1, 0, 1, 0, 0, 1, 0]
    t1345678 = [0, 0, 0, 0, 1, 1, 1]
    t1234578 = [0, 1, 0, 0, 1, 0, 1]

    t = [a[1], a[2], a[3], a[4], a[5], a[7]]
    if t == t123457:
        return True
    t = [a[0], a[1], a[3], a[4], a[5], a[7]]
    if t == t013457:
        return True
    t = [a[1], a[3], a[4], a[5], a[6], a[7]]
    if t == t134567:
        return True
    t = [a[1], a[3], a[4], a[5], a[7], a[8]]
    if t == t134578:
        return True
    t = [a[0], a[1], a[2], a[3], a[4], a[5], a[7]]
    if t == t0123457:
        return True
    t = [a[1], a[3], a[4], a[5], a[6], a[7], a[8]]
    if t == t1345678:
        return True
    t = [a[0], a[1], a[3], a[4], a[5], a[6], a[7]]
    if t == t0134567:
        return True
    t = [a[1], a[2], a[3], a[4], a[5], a[7], a[8]]
    if t == t1234578:
        return True


def deletable(img, x, y):
    a = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            a.append(img[j][i])
    return check(a)


def deletable2(img, x, y):
    a = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            a.append(img[j][i])
    return fringe(a)


def checkThisPoint(img, x, y):
    c = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if img[i][j] == 0:
                c += 1
    return c - 1


def findCheckPoint(img):
    x = len(img)
    y = len(img[0])
    branchPoint = []
    endPoint = []
    for i in range(x):
        for j in range(y):
            if img[i][j] == 0:
                t = checkThisPoint(img, i, j)
                if t == 1:
                    endPoint.append((i, j))
                if t == 3:
                    branchPoint.append((i, j))
    return (branchPoint, endPoint)


def __removeDouble(x, y):
    z = []
    for i in x:
        c = True
        for j in y:
            if i == j:
                c = False
        if c:
            z.append(i)
    for i in y:
        c = True
        for j in x:
            if i == j:
                c = False
        if c:
            z.append(i)
    return z


def delNoisePoint(r):
    tmp = []
    tmp2 = []
    for i in r[1]:
        x = range(i[0] - 5, i[0] + 5)
        y = range(i[1] - 5, i[1] + 5)
        for j in r[0]:
            if j[0] in x and j[1] in y:
                tmp.append(i)
                tmp2.append(j)
    return (__removeDouble(r[0], tmp2), __removeDouble(r[1], tmp))


def matchingPoint(r, v):
    all = 0
    match = 0
    for i in v[0]:
        x = range(i[0] - 15, i[0] + 15)
        y = range(i[1] - 15, i[1] + 15)
        all += 1
        for j in r[0]:
            if j[0] in x and j[1] in y:
                match += 1
                break
    for i in v[1]:
        x = range(i[0] - 15, i[0] + 15)
        y = range(i[1] - 15, i[1] + 15)
        all += 1
        for j in r[1]:
            if j[0] in x and j[1] in y:
                match += 1
                break

    return (match, all)
