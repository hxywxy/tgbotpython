from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import os  # 新增：用于读取环境变量

# 保持您原有的变量和键盘设置
admin_id = "7637830394"
Keyboard = [[InlineKeyboardButton("宇少", callback_data="bth_1")]]
reply_markup = InlineKeyboardMarkup(Keyboard)

# 保持您原有的处理函数
async def bth_1(update: Update, context):
    query = update.callback_query
    await query.answer()
    text = '卡网：http://qmy.wlqwl.com/links/A556C71 频道https://t.me/yshaoNB'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def start(update: Update, context):
    text = '你好，我是小宇少创造的机器人,需要什么帮助'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

async def kawang(update: Update, context):
    text = '宇少八级号出售(http://qmy.wlqwl.com/links/A556C7A1)'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# 唯一必要修改：从环境变量读取Token
TOKEN = os.getenv('TELEGRAM_TOKEN')  # 优先读环境变量

# 保持您原有的初始化逻辑
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('kawang', kawang))
application.add_handler(CallbackQueryHandler(bth_1, pattern="^bth_1$"))

# 启动方式保持不变
if __name__ == "__main__":
    application.run_polling()
