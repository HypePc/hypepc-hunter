import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 HypePC Hunter запущен!\n\n"
        "Добро пожаловать в поиск лучших игровых ПК.\n\n"
        "Команды:\n"
        "/search — поиск ПК\n"
        "/settings — настройки\n"
        "/language — язык"
    )


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Поиск ПК будет подключён следующим обновлением."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search))

    print("HypePC Hunter запущен")

    app.run_polling()


if __name__ == "__main__":
    main()
