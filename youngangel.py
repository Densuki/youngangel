#===================================================
#IMPORT'S
#===================================================

import discord
import asyncio
import secreto
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
msg_id = None
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
     if message.author.id == "336311215099740160":  # permissão por ID [EU]
     if message.author.id == "286206456108154880":  # permissão por ID [DinoSPACE]
      embed1 = discord.Embed(
        title="**Cargos Superiores**\n "
              ,
        color=COR,
        description="Escolha o cargo que será proposto!"
                    "- Fundador = ⚡🌌⚡\n"
                    "- Dono(a)  =  ⭐⭐ \n"
                    "- adm  = ⭐ \n" 
                    "- Bomber Rank S  = ⚜🔰 \n"
                    "- Bomber Rank A  = 🔧 \n"
                    "- Bomber Rank B  = 🛠 \n"
                    "- Bomber Rank C  = 🔨",)

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
     role = discord.utils.find(lambda r: r.name == "adm", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚜" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank S", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔧" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank A", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛠" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank B", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank C", msg.server.roles)
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
     role = discord.utils.find(lambda r: r.name == "adm", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚜" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank S", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔧" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank A", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🛠" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank B", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank C", msg.server.roles)
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
