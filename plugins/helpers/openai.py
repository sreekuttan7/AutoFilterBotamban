import requests
from HorridAPI.AiGenerativeContent import AiGenerativeContent
from pyrogram import Client, filters

@Client.on_message(filters.command("openai"))
async def openai(client, message):
    text = " ".join(message.command[1:])
    if len(message.command) < 2:
        return await message.reply_text("Please provide a query!")
    
    if message.reply_to_message:
        query = f"{message.reply_to_message.text}\n{text}"
    else:
        query = text
    
    mes = await message.reply_text("💻 Processing...")

    # Role isn't needed in payload, unless you wish to use it differently
    role = "My owner name is 𝙕𝙀𝙉𝙄𝙏𝙎𝙐[𝙍𝘾𝙈]"

    payload = {
        "messages": [
            {            
                "role": "user", 
                "content": query
            }
        ]
    }
    
    try:    
        openai = AiGenerativeContent()  # Ensure you're correctly instantiating the class
        response = openai.gen_content(payload, model="gpt-3.5")  # Ensure this matches your API's model
        content = response.get('content', "No content returned")
        
        await mes.edit(f"Hey {message.from_user.mention},\n\nQuery: {text}\n\nResult:\n\n{content}")

    except Exception as e:  
        error_message = f"Something went wrong: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)
