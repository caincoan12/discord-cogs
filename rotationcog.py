import discord
from datetime import date
from discord.ext import commands

class rotationcog:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def rotation(self, ctx):
        image = "pictures/giphy.gif"
        channel = ctx.message.channel
        '''Payout list for squad arena'''
        self.today = date.today()
        eu = open('cogs/order-eu.txt', 'r')
        uk = open('cogs/order-uk.txt', 'r')
        est = open('cogs/order-est.txt', 'r')
        euorder = []
        ukorder = []
        estorder = []

        for euline in eu:
            euorder.append(euline.strip())
        for ukline in uk:
            ukorder.append(ukline.strip())
        for estline in est:
            estorder.append(estline.strip())

        eu.close()
        uk.close()
        est.close()
        
        await self.bot.send_file(channel, image)
        await self.bot.say("Rotation list for " + str(self.today) + ':\n' +
                           'Viva: ' + ', '.join(euorder) + '\n' +
                           'UK: ' +', '.join(ukorder) + '\n' +
                           'EST: ' +', '.join(estorder)+ '\n')

            
    @commands.command(pass_context=True)
    async def newday(self): 
        '''Newday routine to change the payout order'''
    
        eufile = open('cogs/order-eu.txt', 'r')
        ukfile = open('cogs/order-uk.txt', 'r')
        estfile = open('cogs/order-est.txt', 'r')

        eulist = []
        uklist = []
        estlist = []
        
        for euname in eufile:
            eulist.append(euname.strip())
        eulist += [eulist.pop(0)]
        eufile.close()
        
        for estname in estfile:
            estlist.append(estname.strip())
        estlist += [estlist.pop(0)]
        estfile.close()
        
        for ukname in ukfile:
            uklist.append(ukname.strip())
        uklist += [uklist.pop(0)]
        ukfile.close()        
        
        writeeu_file = open('cogs/order-eu.txt','w')
        for item in eulist:
            writeeu_file.write('%s\n' % item)
        writeeu_file.close()
        
        writeest_file = open('cogs/order-est.txt','w')
        for item in estlist:
            writeest_file.write('%s\n' % item)
        writeest_file.close()
        
        writeuk_file = open('cogs/order-uk.txt','w')
        for item in uklist:
            writeuk_file.write('%s\n' % item)
        writeuk_file.close()
        
        await self.bot.say( 'New day routine complete')

def setup(bot):
    bot.add_cog(rotationcog(bot))