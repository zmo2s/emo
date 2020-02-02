import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# -*- coding: utf-8 -*-

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        channel = message.channel
        message.content = message.content.replace("!", "")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rn'):

        channel = message.channel
        message.content = message.content.replace("$rn", "")

        enter = message.content
        print()
        enter = enter.replace(" ", "%20")
        # enter=enter.replace("!","__")
        print(enter)
        import re
        import requests
        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        page = urllib.request.urlopen('https://myanimelist.net/search/all?q=' + enter)
        print(page)
        soup = BSHTML(page, "html.parser")
        images = soup.findAll('img')
        i = 0
        for image in images:
            i += 1
            if i == 2:
                # print(image['src'])
                response1 = image['src']
                # Haikyuu!To the Top
        texte = soup.findAll(class_='picSurround di-tc thumb')
        # print(texte)
        p = 0
        for cle in texte:

            test = cle.find(class_='hoverinfo_trigger')
            # expr = re.match(r"href=\"[^ ]+\"",cle)
            # if expr is not None :
            #  print(expr)
            if p == 0:
                expr = re.search(r"href=\"[^ ]+\"", str(test))
                print(expr.group(0))
                start = re.search(r"(?<=href=\")[a-zA-Z-0-9-/-_-.-]+", str(expr.group(0)))
                print(start.group(0))
                reg = start.group(0)
                # print(test)
                # print(cle)
                # print(cle['href'])
                # print(cle.get('href'))
            p += 1
            # print(test)
            # expr = re.match(r"href=\"[^ ]+\"",test)
            # if expr is not None :
            #  print(expr)
            # [^href=\"][a-zA-Z-0-9-/-_-.-]+
            page = urllib.request.urlopen(reg)
            print(page)
            soup = BSHTML(page, "html.parser")
            res = soup.find(itemprop="description")
            a = res.get_text()

            # print(res)

            from googletrans import Translator
            translator = Translator()
            result = translator.translate(str(a), dest='fr')
            de = result.text
            # print(result.text)

            await channel.send(response1)
            await channel.send("```" + a + "```")

            def check(m):
                return m.content == 'hello' and m.channel == channel

            msg = await client.wait_for('message', check=check)
            await channel.send('Hello {.author}!'.format(msg))

    if message.content.startswith('$gre'):

        channel = message.channel
        message.content = message.content.replace("$gre", "")
        from requests_html import HTMLSession
        import re
        import requests
        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        session = HTMLSession()
        r = session.get('http://onnada.com/search/?q=' + message.content)
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")
        images = soup.findAll('img')
        # print(images)
        i = 0
        for image in images:
            i += 1
            if i == 2:
                print(image['src'])
                response1 = image['src']

        images = soup.findAll(class_='thumb')
        p = 0
        for image in images:
            if p == 0:
                expr = re.search(r"href=\"[^ ]+\"", str(image))
                print(expr.group(0))
                start = re.search(r"(?<=href=\")[a-zA-Z-0-9-/-_-.-]+", str(expr.group(0)))

                reg = start.group(0)
            p += 1
        print(reg)
        page = urllib.request.urlopen(reg)
        print(page)
        soup = BSHTML(page, "html.parser")
        res = soup.find(id="animeContents")
        a = res.get_text()
        print(a)
        await channel.send(response1)
        await channel.send("```" + a + "```")

    if message.content.startswith('$en'):

        channel = message.channel
        message.content = message.content.replace("$en", "")

        enter = message.content
        print()
        enter = enter.replace(" ", "%20")
        # enter=enter.replace("!","__")
        print(enter)
        import re
        import requests
        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        page = urllib.request.urlopen('https://myanimelist.net/search/all?q=' + enter)
        print(page)
        soup = BSHTML(page, "html.parser")
        images = soup.findAll('img')
        i = 0
        for image in images:
            i += 1
            if i == 2:
                print(image['src'])
                response1 = image['src']
                # Haikyuu!To the Top
        texte = soup.findAll(class_='picSurround di-tc thumb')
        # print(texte)
        p = 0
        for cle in texte:

            test = cle.find(class_='hoverinfo_trigger')
            # expr = re.match(r"href=\"[^ ]+\"",cle)
            # if expr is not None :
            #  print(expr)
            if p == 0:
                expr = re.search(r"href=\"[^ ]+\"", str(test))
                print(expr.group(0))
                start = re.search(r"(?<=href=\")[a-zA-Z-0-9-/-_-.-]+", str(expr.group(0)))
                print(start.group(0))
                reg = start.group(0)
                # print(test)
                # print(cle)
                # print(cle['href'])
                # print(cle.get('href'))
            p += 1
            # print(test)
            # expr = re.match(r"href=\"[^ ]+\"",test)
            # if expr is not None :
            #  print(expr)
            # [^href=\"][a-zA-Z-0-9-/-_-.-]+
            page = urllib.request.urlopen(reg)
            print(page)
            soup = BSHTML(page, "html.parser")
            res = soup.find(itemprop="description")
            a = res.get_text()

            # print(res)

            from googletrans import Translator
            translator = Translator()
            result = translator.translate(str(a), dest='fr')
            de = result.text
            print(result.text)

            await channel.send(message.content)
            await channel.send(response1)
            await channel.send("```" + de + "```")
            await channel.send(reg)

            def check(m):
                return m.content == 'hello' and m.channel == channel

            msg = await client.wait_for('message', check=check)
            await channel.send('Hello {.author}!'.format(msg))

    if message.content.startswith('$pt'):

        channel = message.channel
        message.content = message.content.replace("$pt", "")

        enter = message.content
        print()
        enter = enter.replace(" ", "%20")
        # enter=enter.replace("!","__")
        print(enter)
        import re
        import requests
        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        page = urllib.request.urlopen('https://myanimelist.net/search/all?q=' + enter)
        print(page)
        soup = BSHTML(page, "html.parser")
        images = soup.findAll('img')
        i = 0
        for image in images:
            i += 1
            if i == 2:
                # print(image['src'])
                response1 = image['src']
                # Haikyuu!To the Top
        texte = soup.findAll(class_='picSurround di-tc thumb')
        # print(texte)
        p = 0
        for cle in texte:

            test = cle.find(class_='hoverinfo_trigger')
            # expr = re.match(r"href=\"[^ ]+\"",cle)
            # if expr is not None :
            #  print(expr)
            if p == 0:
                expr = re.search(r"href=\"[^ ]+\"", str(test))
                print(expr.group(0))
                start = re.search(r"(?<=href=\")[a-zA-Z-0-9-/-_-.-]+", str(expr.group(0)))
                print(start.group(0))
                reg = start.group(0)
                # print(test)
                # print(cle)
                # print(cle['href'])
                # print(cle.get('href'))
            p += 1
        # print(test)
        # expr = re.match(r"href=\"[^ ]+\"",test)
        # if expr is not None :
        #  print(expr)
        # [^href=\"][a-zA-Z-0-9-/-_-.-]+
        page = urllib.request.urlopen(reg)
        print(page)
        soup = BSHTML(page, "html.parser")
        res = soup.find(itemprop="description")
        a = res.get_text()

        # print(res)

        from googletrans import Translator
        translator = Translator()
        result = translator.translate(str(a), dest='pt')
        de = result.text
        # print(result.text)
        a = de[0:250]

        await channel.send(response1)
        embed = discord.Embed(description=a, color=0x00ff00)
        await message.channel.send(embed=embed)
        await channel.send(reg)

    if message.content.startswith('!hello'):
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('*c'):

        channel = message.channel

        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        v = random.randint(0, 68)

        session = HTMLSession()
        r = session.get('http://bbs2.onnada.com/E000002')
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")
        images = soup.findAll('img')
        print(images)
        i = 0

        page = urllib.request.urlopen('http://bbs2.onnada.com/E000002/919' + str(v))
        print(page)
        soup = BSHTML(page, "html.parser")
        res = soup.find(id="description")
        try:
            a = res.get_text()
        except:
            a = None

        de = res.findAll('img')

        print(de)
        response3 = ""
        i = 0
        for image in de:

            if i == 0:
                response1 = image['data-original']
            if i == 1:
                response2 = image['data-original']
            print(response1)
            responseu = image['data-original']
            response3 = responseu + " " + response3
            i = i + 1

        if i == 0:
            response3 = image['data-original']
        print(a)

        await channel.send(response3)
        await channel.send("```" + a + "```")

    if message.content.startswith('*p'):

        channel = message.channel

        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        v = random.randint(0, 608)
        session = HTMLSession()
        r = session.get('http://konachan.com/post?page=1')
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")
        images = soup.findAll('img')
        print(images)
        i = 0

        page = urllib.request.urlopen('https://konachan.com/post?page=' + str(v) + '&tags=pussy')
        print(page)
        soup = BSHTML(page, "html.parser")

        de = soup.findAll('img')
        i = 1
        response3 = ""
        for image in de:

            if i == 1:
                response2 = image['src']

            if i < 5:
                responseu = image['src']
                response3 = responseu + " " + response3
            i = i + 1

        if i == 0:
            response3 = image['src']

        response3 = response3.replace("/images/blank.gif /images/logo_small.png", " ")
        await channel.send(response3)

    if message.content.startswith('*v'):

        channel = message.channel

        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        v = random.randint(0, 68)
        session = HTMLSession()
        r = session.get("https://hentaisun.com/Calendar")
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")

        er = soup.findAll('img')

        i = 0
        p = ""
        response3 = ""
        for image in er:

            if i < 25 and i > 15:
                responseu = image['src']

                response3 = response3 + " " + responseu

            i = i + 1

        er = soup.findAll('div', class_='boxTextWrapper')

        for image in er:

            if i > 34:
                expr = re.search(r"[0-9]+[\/][0-9]+[\/][0-9]{4}", str(image))
                response3 = response3 + " " + str(expr.group(0))

            i = i + 1

        if i == 0:
            response3 = image['src']

        response3 = response3.replace("//sstatic1.histats.com/0.gif?2665875&101", " ")
        response3 = response3.replace("/Content/Uploads/Cover/", "https://hentaisun.com/Content/Uploads/Cover/")
        await channel.send(response3)

    if message.content.startswith('*re'):

        channel = message.channel
        message.content = message.content.replace("*re", "")
        message.content = message.content.replace(";", "%3B")
        message.content = message.content.replace(" ", "_")

        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        v = random.randint(0, 10)
        session = HTMLSession()
        r = session.get('http://konachan.com/post?page=1')
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")
        images = soup.findAll('img')
        print(images)
        i = 0

        page = urllib.request.urlopen('https://konachan.com/post?page=' + str(v) + '&tags=' + message.content)
        print(page)
        soup = BSHTML(page, "html.parser")

        de = soup.findAll('img')
        i = 1
        response3 = ""
        for image in de:

            if i == 1:
                response2 = image['src']

            if i < 5:
                responseu = image['src']
                response3 = responseu + " " + response3
            i = i + 1

        if i == 0:
            response3 = image['src']

        response3 = response3.replace("/images/blank.gif /images/logo_small.png", " ")
        await channel.send(response3)

    if message.content.startswith('*re'):

        channel = message.channel
        message.content = message.content.replace("*re", "")
        message.content = message.content.replace(";", "%3B")
        message.content = message.content.replace(" ", "_")

        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        v = random.randint(0, 10)
        o=str(v)
        session = HTMLSession()
        r = session.get('http://konachan.com/post?page=1')
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")
        images = soup.findAll('img')
        print(images)
        i = 0

        page = urllib.request.urlopen('https://konachan.com/post?page=' + o + '&tags=' + message.content)
        print(page)
        soup = BSHTML(page, "html.parser")

        de = soup.findAll('img')
   
        i = 1
        response3 = ""
        for image in de:

            if i == 1:
                response2 = image['src']

            if i < 5:
                responseu = image['src']
                response3 = responseu + " " + response3
            i = i + 1

        if i == 0:
            response3 = image['src']

        response3 = response3.replace("/images/blank.gif /images/logo_small.png", " ")
        await channel.send(response3)

    if message.content.startswith('*k'):

        channel = message.channel
        message.content = message.content.replace("*k", "")
        message.content = message.content.replace(";", "%3B")
        message.content = message.content.replace(" ", "_")
        

        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        w = ""
        

        v = random.randint(0, 10)
        q = random.randint(0, 10)
        o=str(v)
        while q == v:
            q = random.randint(0, 10)
        session = HTMLSession()
        r = session.get('http://konachan.com/post?page=1')
        r.encoding = 'utf-8'
        e = r.text
        soup = BSHTML(e, "html.parser")
        images = soup.findAll('img')
        print(images)
        i = 0

        page = urllib.request.urlopen('https://konachan.com/post?page=' + o + '&tags=' + message.content)
        print(page)
        soup = BSHTML(page, "html.parser")

        list = []
        de = soup.findAll('img')
        i = 1
        response3 = ""
        for image in de:

            if i < 1000:
                responseu = image['src']
                response3 = responseu + " " + response3
                if image['src'] != "/images/blank.gif" and image['src'] != "/images/logo_small.png":
                    list.append(image['src'])

            i = i + 1
        j = 0
        for i in list:
            if j == v or j == q:
                w = w + " " + i
                print("la valeur v=", v, "la valeur q=", q)
                print(w)

            j += 1

        w = w.replace("/images/blank.gif /images/logo_small.png", " ")
        w = w.replace("/images/logo_small.png", " ")
        w = w.replace("/images/blank.gif", " ")
        await channel.send(w)

    if message.content.startswith('*help'):
        embed = discord.Embed(
        title="$gre anime_name search info on an anime \n*kanime_name hentai picture of an anime \n*kcharacter_name hentai picture of an anime character \n*p  give hentai picture of hentai \n*c funny things from anime \n *reddit for fun things reddit ",colour=discord.Color.gold())

        await message.channel.send(embed=embed)
    

    
    if message.content.startswith('*fun'):

        channel = message.channel
   

        import praw
        import re
        import requests
        import random
        from requests_html import HTMLSession

        from bs4 import BeautifulSoup as BSHTML
        import urllib.request
        reddit = praw.Reddit(client_id='pJHcuxpiL64Rhg',
                     client_secret='MkjdzRQk55mIRqOBnpS2Nwuwsqk',
                     user_agent='my user agent')




        response3=""
        o=""
        i=0
        e=""
        list = []
        v = random.randint(0, 20)
        for submission in reddit.subreddit('animereactionimages').hot(limit=1000):
         if i < 30 :
          list.append(submission.url)

        p=0
        
        j = random.randint(0, 25)
        for cle in list :

          if cle.endswith('.jpg') or cle.endswith('.png') or cle.endswith('.gif'):
           if p==j : 
            o=o+" "+cle
          p+=1
         
        await channel.send(o)
        




client.run(token)

