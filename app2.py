from bale import Bot, Message

bot = Bot(token="1123599427:SCNsRYHZEcGOIe30TbPs5iHvUs9qkC0qQ6A")

@bot.event
async def on_message(pm: Message):

    chat_id = pm.chat.id   # برای ارسال پیام معمولی باید chat_id داشته باشیم

    if pm.content == "/start":
        await bot.send_message(chat_id, "من غلامرضام فرمایش")

    elif pm.content == "سلام":
        await bot.send_message(chat_id, "سام علیک")

    elif pm.content == "چطوری":
        await bot.send_message(chat_id, "ب تو چه")

    elif pm.content == "چه خبر":
        await bot.send_message(chat_id, "هیچی هاشم مرده")

    elif pm.content == "سازندت کیه":
        await bot.send_message(chat_id, "اقای بنیامین محمدی کلاشمی")

    elif pm.content == "درست صحبت کن":
        await bot.send_message(chat_id, "چشم عباس اقا")

    elif pm.content == "خداحافظ":
        await bot.send_message(chat_id, "ب سلامت")

    elif pm.content == "کصکش":
        await bot.send_message(chat_id, "مادرجنده زر نزن")

    elif pm.content == "بگو صدام":
        await bot.send_message(chat_id, "باشه صدام")

    else:
        await bot.send_message(chat_id, "من این مقادیر رو نمی شناسم")

bot.run()
