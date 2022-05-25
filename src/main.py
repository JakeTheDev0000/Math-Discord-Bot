import discord

TOKEN = "CHANGE ME"

client = discord.Client()
uses_advanced_math = False # advanced_math is able to use () and ** (power) but may not be stable and not secure, be warned

def numeric(equation):
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0])+int(y[1])
    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0])-int(y[1])
    elif '*' in equation:
        y = equation.split('*')
        x = int(y[0])*int(y[1])
    elif '/' in equation:
        y = equation.split('/')
        x = int(y[0])/int(y[1])
    return x

@client.event
async def on_ready():
    print(f"the math bot is logged in as {client.user}")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = message.content
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return
    
    if uses_advanced_math == False:
        try:
            await message.channel.send(numeric(user_message))
        except:
            pass
    else:
        try:
            await message.channel.send(eval(user_message))
        except:
            pass



try:
    client.run(TOKEN)   
except:
    print("token is invalid")
