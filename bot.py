from telegram.ext import Application, CommandHandler
import os
from dotenv import load_dotenv


load_dotenv()
# TOKEN del bot
TOKEN = os.getenv("TOKEN")

USER_ID = int(os.getenv("USER_ID"))  # Mi ID

async def mi_id(update, context):
    await update.message.reply_text(f"Tu ID es: {update.effective_user.id}")

async def start(update, context):
    await update.message.reply_text("Hola, el PC esta prendido.\nUsa /comandos para ver comandos")

async def comandos(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("/apagar - Apagar la PC\n"
                                        "/reiniciar - Reiniciar la PC\n"
                                        "/id - Ver tu ID")
    else:
        await update.message.reply_text("No tienes permiso.")

async def apagar(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("Apagando la PC en 3 segundos")
        os.system("shutdown /s /t 3")
    else:
        await update.message.reply_text("No tienes permiso.")
async def reiniciar(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("Reiniciando la PC en 3 segundos")
        os.system("shutdown /r /t 3")
    else:
        await update.message.reply_text("No tienes permiso.")

def main():
    # Crear aplicación del bot
    app = Application.builder().token(TOKEN).build()

    # Handlers: comandos que entiende el bot
    app.add_handler(CommandHandler("Id", mi_id))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CommandHandler("apagar", apagar))
    app.add_handler(CommandHandler("reiniciar", reiniciar))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
