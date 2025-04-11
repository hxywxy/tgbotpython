from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
import os

# 从环境变量读取 TOKEN（更安全）
TOKEN = os.getenv('TELEGRAM_TOKEN', '8035331526:AAHmyjCLPn1oBzo-NaJoZn_exyXD9DA1I-8')  # 默认值备用

admin_id = "7637830394"
Keyboard = [
    [InlineKeyboardButton("宇少", callback_data="bth_1")]
]
reply_markup = InlineKeyboardMarkup(Keyboard)

async def bth_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = '卡网：http://qmy.wlqwl.com/links/A556C71 频道https://t.me/yshaoNB 全球服推特八级号只要7r，一天之内有问题(开挂不换)包换，超出不负责(看情况)'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '你好，我是小宇少创造的机器人,需要什么帮助'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

async def kawang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '宇少八级号出售(http://qmy.wlqwl.com/links/A556C7A1)'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('kawang', kawang))
    application.add_handler(CallbackQueryHandler(bth_1, pattern="^bth_1$"))
    print("机器人已启动！")
    application.run_polling()
