from telegram.ext import Application, CommandHandler

TOKEN = '7178879290:AAH8ddZVYKaoqnrSdh8Cw0QsMGGwEACVgUA'

async def start(update, context):
    await update.message.reply_text('Salom! Men botman!')

# Application yaratish
application = Application.builder().token(TOKEN).build()

# Start komandasini qo‘shish
application.add_handler(CommandHandler("start", start))

# Botni ishga tushirish
application.run_polling()