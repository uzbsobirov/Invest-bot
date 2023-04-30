from aiogram.dispatcher.filters.state import StatesGroup, State

class Panel(StatesGroup):
    admin_menu = State() #Admin menu

    statics = State() # Statics

    datas = State() # Send message datas

    sponsor = State() # Set channel
    get_id = State()
    chat_id = State()

    check_is_sub = State()

