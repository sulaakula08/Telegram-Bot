import telebot
from telebot import types
bot=telebot.TeleBot('7861429268:AAHQh9hCuULEcR8zQCgEgf9ye8K9wbQXUcg')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am your hepler for writing B&C criterions in sciences. All strands and requirements are dedicated for 7th grade only. If you are ready, write /continue')

@bot.message_handler(commands=['abbreviation'])
def abbreviation(message):
    bot.send_message(message.chat.id, 'Independent Variable = IV\nDependent Variable = DV\nControlled Variable = CV\nResearch Question = RQ', parse_mode='html')

@bot.message_handler(commands=['continue'])
def send_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton('B criterion')
    btn2=types.KeyboardButton('C criterion')
    btn3=types.KeyboardButton('Interesting notes')
    btn4=types.KeyboardButton('Logics of the work')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    bot.reply_to(message, 'What are you looking for? (Buttons are on the keyboard)', reply_markup=markup)

@bot.message_handler(commands=['problems'])
def problem(message):
    bot.send_message(message.chat.id, 'If you have any problems with the bot, please restart the bot or contact khasan.a@nisa.edu.kz by school email.')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'B criterion':
        markupp=types.InlineKeyboardMarkup()
        btnn1=types.InlineKeyboardButton('Research Question', callback_data='R')
        btnn2=types.InlineKeyboardButton('Hypothesis', callback_data='H')
        btnn3=types.InlineKeyboardButton('Variables', callback_data='V')
        btnn4=types.InlineKeyboardButton('Method & Safety precautions', callback_data='M')
        markupp.row(btnn1)
        markupp.row(btnn2)
        markupp.row(btnn3)
        markupp.row(btnn4)
        bot.send_message(message.chat.id, 'B criterion Explanation', reply_markup=markupp)

    elif message.text == 'C criterion':
        mmarkup=types.InlineKeyboardMarkup()
        btm1=types.InlineKeyboardButton('Table', callback_data='T')
        btm2=types.InlineKeyboardButton('Interpreting the table', callback_data='I')
        btm3=types.InlineKeyboardButton('Evaluation of the hypothesis', callback_data='E')
        btm4=types.InlineKeyboardButton('Evaluation of the method', callback_data='EM')
        btm5=types.InlineKeyboardButton('Improvements', callback_data='Im')
        mmarkup.row(btm1)
        mmarkup.row(btm2)
        mmarkup.row(btm3)
        mmarkup.row(btm4)
        mmarkup.row(btm5)
        bot.send_message(message.chat.id, 'C criterion Explanation', reply_markup=mmarkup)
    
    elif message.text == 'Interesting notes':
        markup=types.InlineKeyboardMarkup()
        btn1=types.InlineKeyboardButton('YouTube video ▶', url='https://www.youtube.com/watch?v=5KKsLuRPsvU')
        btn3=types.InlineKeyboardButton('Short descriptors of B cr.', callback_data='D')
        btn4=types.InlineKeyboardButton('Short descriptors of C cr.', callback_data='D2')
        markup.row(btn1)
        markup.row(btn3, btn4)
        bot.send_message(message.chat.id, 'Interesting notes', reply_markup=markup)

    elif message.text == 'Logics of the work':
        markuup=types.InlineKeyboardMarkup()
        btt1=types.InlineKeyboardButton('Continue', callback_data='Con')
        markuup.row(btt1)
        bot.send_message(message.chat.id, 'B&C Criterions from sciences are way easier than you think about them! Press "Continue" to explore!', reply_markup=markuup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Con':
        bot.send_message(call.message.chat.id, 'Imagine that you are cooking a pizza for the teaparty at school. First of all, what do you have to do? Of course, you have to plan all the things regarding the cookin of pizza, which is the same as B criterion. But what about C criterion? It is a little bit different. You have to evaluate the taste of it. Is it too sour or spicy? Is it too hot or bitter? Generally, imagine the lab work and B&C Criterions as cooking a pizza. However, you use scientific terms and tools instead of the cooking ones! Try hard, party harder!')
    elif call.data == 'D':
        bot.send_message(call.message.chat.id, '<b>B criterion</b>\n\n<i>Strand 1:</i> Research Question.\n\n<i>Strand 2:</i> Hypothesis.\n\n<i>Strand 3:</i> Variables.\n\n<i>Strand 4:</i> Method and safety precautions.', parse_mode='html')
    elif call.data == 'D2':
        bot.send_message(call.message.chat.id,  '<b>C criterion</b>\n\n<i>Strand 1:</i> Plot the table with IV and DV.\n\n<i>Strand 2:</i> Interpret the table.\n\n<i>Strand 3:</i> Evaluate the hypotheis.\n\n<i>Strand 4:</i> Evaluate the method.\n\n<i>Strand 5:</i> Improve the method.', parse_mode='html')
    elif call.data == 'R':
        bot.send_message(call.message.chat.id, '<b>Strand 1: Research Question</b> \n\nShow the relationship between IV and DV in your RQ\n\nSample (highly recommended): How does IV affect DV?', parse_mode='html')
    elif call.data == 'H':
        bot.send_message(call.message.chat.id, '<b>Strand 2: Hypothesis</b> \n\n1) If IV increases / decreases, DV increases / decreases / stays constant) as well\n\n2) How did you get it? Provide proofs using class material\n\n3) Ideally, provide real-life examples as well', parse_mode='html')
    elif call.data == 'V':
        bot.send_message(call.message.chat.id, '<b>Strand 3: Variables</b> \n\nIV: State the range of changed values (1 ml - 3ml - 5ml) → Describe the way you measure it (instruments) → Mention units (ml, m, N, etc.) \n\nDV: Outline measured values (with units) → Outline the way you measure it → Number of trials (at least 3) \n\nCV: Name controlled variable → Describe the way you measure it (instruments) → Mention units (ml, m, sec, kg, etc.)', parse_mode='html')
    elif call.data == 'M':
        bot.send_message(call.message.chat.id, '<b>Strand 4: Method</b> \n\n1) Write step by step gradually (write each action as a full step)\n\n2) Imagine that you are writing it to your friend (write simply)\n\n3) Do not forget about units, measurements and apparatures with materials\n\n4) Include safety precautions within or out of the method', parse_mode='html')
    elif call.data == 'T':
        bot.send_message(call.message.chat.id, '<b>Strand 1: Table</b>\n\n1) Name the table "Values of DV in different ranges IV"\n\n2) First column: IV\n\n3) Other columns: DV\n\n4) Include number of trials', parse_mode='html')
    elif call.data == 'I':
        bot.send_message(call.message.chat.id, '<b>Strand 2: Interpreting table</b>\n\n1) What can you see on the table (relationships among results)?\n\n2) What is the relationship between IV and DV (when IV changes, what happens to DV)?\n\n3) Abnormal results detected/undetected and show it on the table', parse_mode='html')
    elif call.data == 'E':
        bot.send_message(call.message.chat.id, '<b>Strand 3: Evaluating hypothesis</b>\n\n1) Do results from the table support hypothesis from B criterion?\n\n2) Yes/No and provide proofs by showing a specific tendecy (results from the table)\n\n3) Add scientific reason behind the tendency (refer to presentations from the classroom or additional information from the documents in <i>"Interesting notes"</i>)', parse_mode='html')
    elif call.data == 'EM':
        bot.send_message(call.message.chat.id, '<b>Strand 4: Evaluating method</b>\n\n1) Do results from the table support method? from B criterion?\n\n2) Yes/No and provide proofs by showing a specific tendecy within the results from the table (refer to presentations from the classroom or additional information from the documents in <i>"Interesting notes"</i>)\n\n3) Outline the advantages and drawbacks of the method by providing rational reasons.', parse_mode='html')
    elif call.data == 'Im':
        bot.send_message(call.message.chat.id, '<b>Strand 5: Improvements</b>\n\n1) Suggest improvements for the weaknesses you identified in the previous section\n\n2) Suggestions should be realistic, not involving unavailable equipment\n\n3) Suggestions should be specific (not “more careful work”)',parse_mode='html')
    
bot.polling(non_stop=True)