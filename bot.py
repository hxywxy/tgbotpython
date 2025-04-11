from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from flask import Flask  # 新增
import threading  # 新增

# ----------- 你的原始代码完全保持不变 -----------
TOKEN = '8035331526:AAGXwavsmX7RdlI6faUzBLEOws_9KRC0YG0'
admin_id = "7637830394"
Keyboard = [[InlineKeyboardButton("宇少", callback_data="bth_1")]]
reply_markup = InlineKeyboardMarkup(Keyboard)

async def bth_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = '卡网：http://qmy.wlqwl.com/links/A556C7A1 频道https://t.me/yshaoNB 全球服推特八级号只要7r，一天之内有问题(开挂不换)包换，超出不负责(看情况)'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '你好，我是小宇少创造的机器人,需要什么帮助'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

async def kawang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '宇少八级号出售(http://qmy.wlqwl.com/links/A556C7A1)'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
# --------------------------------------------

# 新增极简 Flask 服务（仅用于 Render 端口检测）
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check():
    return "OK"  # 返回任意内容即可

if __name__ == '__main__':
    # 在子线程启动 Flask（不阻塞 Telegram 机器人）
    threading.Thread(target=lambda: flask_app.run(port=8000, host="0.0.0.0")).start()
    
    # 主线程运行原有机器人
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('kawang', kawang))
    application.add_handler(CallbackQueryHandler(bth_1, pattern="^bth_1$"))
    print("机器人已启动！")
    application.run_polling()
