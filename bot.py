from telegram.ext import Application, CommandHandler
import os

# TOKEN del bot
TOKEN = "token"

USER_ID = 3  # Mi ID

async def start(update, context):
    await update.message.reply_text("Hola\nUsa /apagar para apagar")

async def apagar(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("Apagando la PC en 3 segundos")
        os.system("shutdown /s /t 3")
    else:
        await update.message.reply_text("No tienes permiso.")

def main():
    # Crear aplicación del bot
    app = Application.builder().token(TOKEN).build()

    # Handlers: comandos que entiende el bot
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("apagar", apagar))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
