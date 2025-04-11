import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from fastapi import FastAPI
import uvicorn

TOKEN = os.getenv('TELEGRAM_TOKEN')  # 必须通过环境变量设置

# Telegram 机器人逻辑
keyboard = [[InlineKeyboardButton("宇少", callback_data="bth_1")]]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context):
    await update.message.reply_text('你好！需要什么帮助？', reply_markup=reply_markup)

async def handle_button_1(update: Update, context):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text='卡网：http://qmy.wlqwl.com/links/A556C71\n频道：https://t.me/yshaoNB'
    )

# HTTP 保活服务
app_fastapi = FastAPI()
@app_fastapi.get("/")
def home():
    return "Bot is alive!"

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button_1, pattern="^bth_1$"))
    await app.initialize()
    await app.start()
    await asyncio.Event().wait()  # 永久运行

if name == 'main':
    # 启动 HTTP 服务和机器人
    threading.Thread(target=lambda: uvicorn.run(app_fastapi, host="0.0.0.0", port=8000)).start()
    asyncio.run(run_bot())
