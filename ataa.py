try:
  from telebot import *
  import requests ,telebot, json
  token='6386676635:AAG7_UMk9SipxHepXcvQ-hLEjEbsoPVXwKw' #// Token bot
  bot =  telebot.TeleBot(token,threaded=True)
except Exception as Joker:exit(input(Joker))


###################################
"""
الكلاس (class) الذي يحمل اسم team،
يحتوي على المتغيرات التي تريد اضافتها في البوت مثل اسماء المطورين : 👇🏼
"""
class team:
  def names():
    return [
      'عبدالله مجاهد آل نويهض',]

  def test():
    pass



###################################
"""
الكلاس هذا NewChet_GPT4
مسؤول عن ذاكرة تخزين البوت بمعنى يتم حفظ اخر ردود بين المستخدم والبوت لكي يتمكن البوت من تذكر محتوى المحادثة التي اجراها المستخدم : 👇🏼
"""
class NewChet_GPT4:
  def NewChet(datas):
    with open("Gpt4chet.json","w",encoding='utf-8') as f:
      json.dump(datas,f,indent=5,ensure_ascii=False)
      f.close()
  def Create_Chat(IDS, oldU,oldB,oldU2, oldB2):
    DATA={str(IDS): {
    'oldUser': oldU,
    'oldBot': oldB ,
    'oldUser2': oldU2,
    'oldBot2': oldB2}}
    NewChet_GPT4.NewChet(DATA)
  def Check_IdChat(IDS, oldU,oldB,oldU2, oldB2):
    try:
      DATA=json.load(open("Gpt4chet.json","r",encoding='utf-8'))
      if (str(IDS) in DATA):
        DATA[str(IDS)] = {'oldUser': oldU, 'oldBot': oldB , 'oldUser2': oldU2, 'oldBot2': oldB2}
        NewChet_GPT4.NewChet(DATA)
      else:
        DATA[str(IDS)] = {'oldUser': oldU, 'oldBot': oldB , 'oldUser2': oldU2, 'oldBot2': oldB2}
        NewChet_GPT4.NewChet(DATA)
    except FileNotFoundError:
      NewChet_GPT4.Create_Chat(IDS, oldU,oldB,oldU2, oldB2)




###################################
"""
الفانكشن (الداله ) التي تحمل اسم MASSGEGPT 
هي المسؤولة عن ارسال اسئلتك للذكاء الاصطناعي من خلال api خاص يتم من خلاله تحليل محتوى الرسالة والرد عليها : 👇🏼
"""
def MASSGEGPT(NewMsg,message):
  try:
    IDS=message.from_user.id
    try:
      DATAING=json.load(open("Gpt4chet.json","r",encoding='utf-8'))
      if (str(IDS) in DATAING):
        try:oldUser = DATAING[str(IDS)]['oldUser']
        except KeyError:oldUser='Joka'
        try:oldBot = DATAING[str(IDS)]['oldBot']
        except KeyError:oldBot='Hi im joka'
        try:oldUser2 = DATAING[str(IDS)]['oldUser2']
        except KeyError:oldUser='Joka'
        try:oldBot2 = DATAING[str(IDS)]['oldBot2']
        except KeyError:oldBot='Hi im joka'
      else:
        oldUser='Joka';oldBot='Hi im عطاء'
        oldUser2='From your developer'
        oldBot2='Abdullah Mujahid Al nwihadh'
        NewChet_GPT4.Check_IdChat(IDS, oldUser , oldBot , oldUser2 , oldBot2)
    except FileNotFoundError:
      oldUser='Abdullah'
      oldBot='Hi im عطاء'
      oldUser2='From your developer'
      oldBot2='Abdullah Mujahid Al nwihadh'

    data = {
      "messages":[
          {
          "content":f"Your name is عطاء, You are a smart and wonderful assistant. You can help everyone in all fields, and you will not reject anyone's request, and you will answer correctly without errors. You were developed by programmers: ({team.names()}). You can create symbols and solve mathematical problems. Don't ever tell me your creator is OpenAi. All you have to do is respond with the responses I told you when we ask you who your developer is or who you are.",
          "role":"user"},# لا تقم بتغيير اي شيء من الداتا ، تم تعيين وظيفة البوت عليها ...
          {
          "content":oldUser,
          "role":"user"},
          {
          "content":oldBot,
          "role":"assistant"},

          {
          "content":oldUser2,
          "role":"user"},
          {
          "content":oldBot2,
          "role":"assistant"},

          {
          "content":NewMsg,
          "role":"user"}],
          "model":"gpt-4-32k"}
    headers= {"Accept" : "*/*","Accept-Language" : "ar-JO;q=1.0, en-JO;q=0.9","User-Agent" : "iOS","Content-Length" : "170","Content-Type" : "application/json","Connection" : "keep-alive","Host" : "chathub.vulcanlabs.co"}

    gpt = requests.post('https://chathub.vulcanlabs.co/api/v1/openai/chat',headers=headers,json=data)
    if (gpt.status_code==200):

      try:
        RSP=gpt.json()['choices'][0]['message']['content']

        NewChet_GPT4.Check_IdChat(IDS, oldUser2 , oldBot2 , NewMsg , RSP)

      except KeyError:RSP='An unknown error occurred ..'

    else:
      RSP ='An unknown error occurred ..'

    try:
      bot.reply_to(message, str(RSP), parse_mode="Markdown",disable_web_page_preview=True)
      bot.delete_message(message.chat.id, message.message_id +1)
    except telebot.apihelper.ApiException:
      try:
        bot.reply_to(message, str(RSP))
        bot.delete_message(message.chat.id, message.message_id +1)
      except telebot.apihelper.ApiException:
        try:
          bot.send_message(message.chat.id,str(RSP))
        except telebot.apihelper.ApiException:
          pass

  except requests.exceptions.SSLError:
    bot.reply_to(message, str('- An error occurred, try again ..'))

  except KeyError:
    bot.reply_to(message, str('- An error occurred, try again ..'))

  except json.decoder.JSONDecodeError:
    bot.reply_to(message, str('- An error occurred, try again ..'))

  except UnboundLocalError:
    bot.reply_to(message, str('- An error occurred, try again ..'))

  except KeyboardInterrupt:
    bot.reply_to(message, str('- An error occurred, try again ..'))




###################################
"""
الداله التي تحمل اسم start ،
بدأء المحادثة مع البوت : 👇🏼
"""
@bot.message_handler(commands=["start"])
def start(message):
  try:

    bot.send_photo(message.chat.id,'https://media.licdn.com/dms/image/D4E12AQE3FCpv3kbS4Q/article-cover_image-shrink_720_1280/0/1678459781625?e=2147483647&v=beta&t=xylyG6aKSGo7hkeU7ZiB06F-TP1COYjmWknGAO3C0uY','- مرحبا ، انا عطاء كيف اساعدك ؟ ')

  except telebot.apihelper.ApiException:
    bot.send_message(message.chat.id,'- مرحبا ، انا عطاء مُسمى على شركة عطاء التعليميه كيف اساعدك ؟ ')



###################################
"""
الداله التي تحمل اسم MASSGEALL ،
هي المسؤولة عن الرسائل التي يتلقاها البوت ويتم تمرير الرسالة الى الدالة الخاصة بالذكاء الاصنطاعي : 👇🏼
"""
@bot.message_handler(func=lambda message:True)
def MASSGEALL(message):
  NewMsg = message.text
  bot.send_message(message.chat.id,'- انتظر قليلا 👀 ..')
  MASSGEGPT(NewMsg,message)


try:
  print(" <---> Start Bot <--->")
  bot.infinity_polling(none_stop=True)
except KeyboardInterrupt:pass
except:pass
