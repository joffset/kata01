from telegram.ext import Updater


def main():
    # instanciamos el updater
    updater =  Updater(token=open("").read() , use_context=True)
    # añadiendo un manejador al comando start
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
    # empezamos a pedir notificaciones a telegram
    updater.start_polling()
    
    # capturamos señales telegram
    updater.idle()


main()