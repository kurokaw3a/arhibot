import database
data = database.get_bot_data()


bot_admin = data["admin"] or "none"
bot_props = data["props"] or "none"
bot_new_props = data["new_props"] or "none"

channel = "-1002665316791"
channel_link = "https://t.me/ArhiPayNews"

chat = ""

replenish_chat_id = "-4965250408"
withdraw_chat_id = "-4874156588"
