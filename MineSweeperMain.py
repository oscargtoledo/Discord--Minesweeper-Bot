import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random


prefix = "¿"


client = commands.Bot(prefix)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # client.activity = discord.Activity(name='¿h for help')
    await client.change_presence(activity=discord.Game(name='¿h for help'))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
@client.command(pass_context=True)
async def h(ctx):
    output = "> **Minesweeper Bot Help**\n> For generating a new board, use the command:\n> ¿ms difficulty\n> where difficulty can be easy, normal, or hard."
    await ctx.message.channel.send(output)
@client.command(pass_context=True)
async def ms(ctx, *args):
    mineAmount = 10
    xSize = 8
    ySize = 8
    if len(args) == 1:
        #Only difficulty
        if args[0] == 1 or args[0] == "normal":
            mineAmount = 40
            xSize = 16
            ySize = 16
        elif args[0] == 2 or args[0] == "hard":
            mineAmount = 99
            xSize = 30
            ySize = 30
    elif len(args) == 3 and (RespresentsInt(xSize) and RespresentsInt(ySize) and RespresentsInt(mineAmount)):
        #Custom width, height, and mineAmount
        xSize = int(args[0])
        ySize = int(args[1])
        mineAmount = int(args[2])
        mineAmount = max(min(mineAmount,xSize * ySize),0)

    # await ctx.message.channel.send("Generating a MineSweeper table. Difficulty: " + (str(level) if level != None else "easy"))
    
    
    
    await mineSweeperGeneration(ctx,xSize,ySize,mineAmount)

def RespresentsInt(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def incrementPos(pos):
    return pos + 1 if pos >=0 else (1 if pos != -2 else -2)

async def mineSweeperGeneration(ctx, xSize, ySize, mineAmount):

    table = [[-1 for x in range(xSize)] for y in range(ySize)]
    

    previousAmount = None
    #Pase para meter minas
    while mineAmount > 0:
        if previousAmount == mineAmount:
            await ctx.message.channel.send("There was an error fitting all bombs in the board, sending last possible option.")
            await sendTable(ctx,table)
            return
        previousAmount = mineAmount
        print("Mines remaining: " + str(mineAmount))
        xPos = random.randint(0,xSize-1)
        yPos = random.randint(0,ySize-1)

        
        # if table[xPos][yPos] == -2:
        #     pass
        # elif table[xPos][yPos] == -1:
        while not table[xPos][yPos] != -2:
            xPos = random.randint(0,xSize-1)
            yPos = random.randint(0,ySize-1)
        if table[xPos][yPos] != -2:
            table[xPos][yPos] = -2
            mineAmount -= 1

            #Banda derecha, derecha arriba y derecha abajo
            if xPos-1 >= 0:
                wPos = table[xPos-1][yPos]
                table[xPos-1][yPos] = incrementPos(wPos)
                if yPos-1 >= 0:
                    nwPos = table[xPos-1][yPos-1]
                    table[xPos-1][yPos-1] = incrementPos(nwPos)
                if yPos+1 <= ySize-1:
                    swPos = table[xPos-1][yPos+1]
                    table[xPos-1][yPos+1] = incrementPos(swPos)

            #Banda izquierda, izquierda arriba y izquierda abajo
            if xPos+1 <= xSize-1:
                
                ePos = table[xPos+1][yPos]
                
                

                table[xPos+1][yPos] = incrementPos(ePos)
                if yPos-1 >= 0:
                    nePos = table[xPos+1][yPos-1]
                    table[xPos+1][yPos-1] = incrementPos(nePos)
                if yPos+1 <= ySize-1:
                    sePos = table[xPos+1][yPos+1]
                    table[xPos+1][yPos+1] = incrementPos(sePos)


            #Arriba y abajo
            if yPos-1 >= 0:
                tPos = table[xPos][yPos-1]
                table[xPos][yPos-1] = incrementPos(tPos)
            if yPos+1 <= ySize-1:
                sPos = table[xPos][yPos+1]
                table[xPos][yPos+1] = incrementPos(sPos)
    
    await sendTable(ctx,table)
    
async def sendTable(ctx, table):
    # for x in table:
    #     print()
    #     for y in x:
    #         if y == -2: print("M", end=" ")
    #         elif y == -1: print("O", end=" ")
    #         else: print(y, end = " ")
    #     print()
   
    output = ""
    for x in table:
        output += "\n"
        for y in x:
            if y == -2: output += "||:bomb:|| "
            elif y == -1: output += "||:zero:|| "
            else: 
                number = "||:zero:||"
                if y == 1:
                    number = "||:one:||"
                elif y == 2:
                    number = "||:two:||"
                elif y == 3:
                    number = "||:three:||"
                elif y == 4:
                    number = "||:four:||"
                elif y == 5:
                    number = "||:five:||"
                elif y == 6:
                    number = "||:six:||"
                elif y == 7:
                    number = "||:seven:||"
                elif y == 8:
                    number = "||:eight:||"
                elif y == 9:
                    number = "||:nine:||"
                else: pass
                output += number + " "
        if len(output) >= 1000:
            await ctx.message.channel.send(output) 
            output = ""
    if output != "":
        await ctx.message.channel.send(output) 



    #Pase para contar minas cercanas

    # for x in range(xSize):
    #     for y in range(ySize):
    #         if x-1 >= xSize and x+1 <=xSize and y-1 >= ySize and y+1 <= ySize:
    #             count = 0;
    #             for xL in range (-1,1):
    #                 for yL in range(-1,1):
    #                     if table[x]
    


client.run('NzIxODI5MzQzNjg4MzkyODM2.XuaQtw.VnisDFTkmu17wKPjDU8pNdqVd8c')