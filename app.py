from bale import Bot, Message

bot = Bot(token="1123599427:SCNsRYHZEcGOIe30TbPs5iHvUs9qkC0qQ6A")

@bot.event
async def on_message(pm: Message):

    if pm.content == "/start":
        await pm.reply("من غلامرضام فرمایش")

    elif pm.content == "سلام":
        await pm.reply("سام علیک")

    elif pm.content == "چطوری":
        await pm.reply(" ب تو چه")

    elif pm.content == "چه خبر":
        await pm.reply("هیچی هاشم مرده")

    elif pm.content == "سازندت کیه":
        await pm.reply("اقای بنیامین محمدی کلاشمی")

    elif pm.content == "درست صحبت کن":
        await pm.reply("چشم عباس اقا")

    elif pm.content == "خداحافظ":
        await pm.reply ("ب سلامت")

    


    else:
        await pm.reply(pm.content)

bot.run()
