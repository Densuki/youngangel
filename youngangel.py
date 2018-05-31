#===================================================
#IMPORT'S
#===================================================

import discord
import asyncio
import secreto
import random
#import cargos
#import moedas
#import reação
#import purge
#import music

#===================================================
client = discord.Client()
#===================================================
COR = 0x690FC3
Token = secreto.seu_token()
#cargos = cargos.cargos()
#coin = moedas.moeda()
#msg_id = None
msg_user = None

#===================================================
#IDENTIDADE PELO CONSOLE
#===================================================

@client.event
async def on_ready():
    print('===================================================')
    print('BOT ONLINE: - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('===================================================')
    print('Version - 1.1')
    print('===================================================')

#===================================================
#MODELO PARA COMANDOS
#===================================================

# ===================================================
# Mensagens Contínuas
# ===================================================

# ===================================================
# Respostas por Embed | Imagens
# ===================================================

#===================================================
#FLIP COIN
#===================================================

# ===================================================
#MUTE
# ===================================================

# ===================================================
#CARGOS
# ===================================================
@client.event
async def on_message(message): #Condição

    if message.content.lower().startswith('#cargos'):  #BASE PARA CARGOS
        ##if message.author.id == "336311215099740160":  # permissão por ID
     embed1 = discord.Embed(
        title="**Cargos Superiores**\n "
              "Escolha o cargo que será proposto!",
        color=COR,
        description="- Fundador = ⚡🌌⚡\n"
                    "- Dono(a)  =  ⭐⭐ \n"
                    "- ADM  = ⭐ \n" 
                    "- The Seven Emperor  = ⚜🔰 \n"
                    "- BOT Manager  = 🔧 \n"
                    "- MOD  = 🛠 \n"
                    "- STAFF  = 🔨",)

     botmsg = await client.send_message(message.channel, embed=embed1)

     await client.add_reaction(botmsg, "🌌")
     await client.add_reaction(botmsg, "⚡")
     await client.add_reaction(botmsg, "⭐")
     await client.add_reaction(botmsg, "⚜")
     await client.add_reaction(botmsg, "🔧")
     await client.add_reaction(botmsg, "🛠")
     await client.add_reaction(botmsg, "🔨")


     global msg_id
     msg_id = botmsg.id

     global msg_user
     msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🌌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "🌀⚡Fundador🌀⚡", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "⭐⭐Dono(a)⭐⭐", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⭐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "ADM", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚜" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "🔰💎🔰The Seven Emperor🔰💎🔰", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔧" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "BOT Manager", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛠" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "MOD", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "STAFF", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🌌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "🌀⚡Fundador🌀⚡", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "⭐⭐Dono(a)⭐⭐", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⭐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "ADM", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚜" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "🔰💎🔰The Seven Emperor🔰💎🔰", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔧" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "BOT Manager", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🛠" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "MOD", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "STAFF", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

#===================================================
#MÚSICA
#===================================================

#===================================================
#PARA FUNCIONAR
#===================================================
client.run(Token)
#===================================================
