# gikes/bot/core/database/mongodb.py
from pymongo import MongoClient
from bot.config import MONGO_URI, DATABASE_NAME

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]

    def get_bot_status(self, chat_id):
        status_data = self.db.bot_status.find_one({'chat_id': chat_id})
        return status_data.get('is_active', True) if status_data else True

    def set_bot_status(self, chat_id, is_active):
        self.db.bot_status.update_one({'chat_id': chat_id}, {'$set': {'is_active': is_active}}, upsert=True)

    def add_free_user(self, user_id):
        self.db.daftar_free.insert_one({'user_id': int(user_id)})

    def delete_free_user(self, user_id):
        result = self.db.daftar_free.delete_one({'user_id': int(user_id)})
        return result.deleted_count

    def add_blacklisted_word(self, word):
        self.db.blacklist_kata.insert_one({'word': word})

    def delete_blacklisted_word(self, word):
        result = self.db.blacklist_kata.delete_one({'word': word})
        return result.deleted_count

    def get_blacklisted_words(self):
        return [item['word'] for item in self.db.blacklist_kata.find()]

    def add_blacklisted_user(self, user_id):
        self.db.blacklist_user.insert_one({'user_id': user_id})

    def delete_blacklisted_user(self, user_id):
        result = self.db.blacklist_user.delete_one({'user_id': user_id})
        return result.deleted_count

    def get_blacklisted_users(self):
        return [item['user_id'] for item in self.db.blacklist_user.find()]

    def add_user(self, user_id, role='user'):
        self.db.users.update_one({'user_id': user_id}, {'$set': {'role': role}}, upsert=True)

    def get_user_role(self, user_id):
        user_data = self.db.users.find_one({'user_id': user_id})
        return user_data.get('role', 'user') if user_data else 'user'

    def is_owner(self, user_id):
        return self.get_user_role(user_id) == 'owner'

    def is_sudo(self, user_id):
        role = self.get_user_role(user_id)
        return role in ['owner', 'sudo']

    def is_free(self, user_id):
        return self.get_user_role(user_id) in ['owner', 'sudo', 'free']

    def promote_user(self, user_id, role):
        if role in ['owner', 'sudo', 'free', 'admin']:
            self.add_user(user_id, role)
            return True
        return False

db = MongoDB() # Membuat instance database global