from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, JobQueue,CallbackQueryHandler
import datetime
admin_id ="7637830394"
Keyboard=[
    [
        InlineKeyboardButton("宇少",callback_data ="bth_1"),
        ]
]
reply_markup=InlineKeyboardMarkup(Keyboard)
async def bth_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # 告诉 Telegram 服务器按钮点击事件已处理
    text = '卡网：http://qmy.wlqwl.com/links/A556C71 频道https://t.me/yshaoNB 全球服推特八级号只要7r，一天之内有问题(开挂不换)包换，超出不负责(看情况)'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

bth_1_handler = CallbackQueryHandler(bth_1, pattern="^bth_1$")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '你好，我是小宇少创造的机器人,需要什么帮助'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text,reply_markup=reply_markup)

start_handler = CommandHandler('start', start)

async def kawang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '宇少八级号出售(http://qmy.wlqwl.com/links/A556C7A1)'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)

kawang_handler = CommandHandler('kawang', kawang)


TOKEN='8035331526:AAHmyjCLPn1oBzo-NaJoZn_exyXD9DA1I-8'
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(start_handler)
application.add_handler(kawang_handler)
application.add_handler(bth_1_handler)
application.run_polling()