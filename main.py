import os
import logging
import asyncio
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes, CallbackQueryHandler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# ==== Логирование ====
logging.basicConfig(level=logging.INFO)

# ==== НАСТРОЙКИ ====
TOKEN = "7339504860:AAEFEXix0Q10SSWSzDk6mfOfVOdwsRnrras"
SPREADSHEET_ID = "1npURWdH4IkFp3C01ZAmLS4PZyhRXqzy-tvmD7QqSNvA"
SHEET_NAME = "Заявки клиента"
MASTER_SHEET = "Мастера"
ADMIN_CHAT_ID = "6126002181"

# ==== Подключение Google Таблицы ====
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
import json
creds_json = os.getenv("GOOGLE_CREDS_JSON")
creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
master_sheet = client.open_by_key(SPREADSHEET_ID).worksheet(MASTER_SHEET)

# ==== Состояния ====
NAME, PHONE, SERVICE, MASTER, RESTART_CONFIRMATION = range(5)
user_data_dict = {}
CANCEL_HINT = "\n\nВы можете ввести /cancel, чтобы отменить заявку."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data_dict[update.effective_chat.id] = {"chat_id": update.effective_chat.id}
    context.user_data.clear()
    await update.message.reply_text("\U0001F44B Привет! Давайте оформим заявку.\nВведите ваше имя:" + CANCEL_HINT)
    return NAME

# Остальной код опущен для компактности (будет таким же в файле)
