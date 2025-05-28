# gikes/bot/main.py
import os
from pyrogram import import_module
from bot.core.bot import bot_instance

if __name__ == "__main__":
    # Import semua modul handler secara otomatis dari direktori bot/core/handlers
    handlers_package = "bot.core.handlers"
    for name in os.listdir(os.path.join(os.path.dirname(__file__), "core", "handlers")):
        if name.endswith(".py") and name != "__init__.py":
            module_name = name[:-3]
            try:
                import_module(f"{handlers_package}.{module_name}")
                print(f"Handler module '{module_name}' imported successfully.")
            except ImportError as e:
                print(f"Error importing handler module '{module_name}': {e}")

    print("Starting bot...")
    bot_instance.run()
    print("Bot stopped.")