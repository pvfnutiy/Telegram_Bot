import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from parser import ozon_parsing


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Getting Price bot!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Enter your link to ozon:")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usrdata = update.message.text
    op = ozon_parsing(usrdata)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=op.get_info(op.url))
    

if __name__ == '__main__':
    application = ApplicationBuilder().token("TOKEN").build()

    start_handler = CommandHandler('start', start)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(start_handler)
    
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)