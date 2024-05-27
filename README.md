This is a Discord bot created for the purpose of web scraping search results from the movie database website Letterboxd. To run this you will need to have a discord account and a discord server setup to deploy the bot.

**Note: You will need to have a discord account, discord server you want to place the bot in, and python 3 installed on your computer
**
------------------------------------------------------------------------------------------------------------------------------------
You will need to complete 3 steps before downloading the repository to run a bot (Not including creating a discord account and discord server):

1. Create an application: Go to the Discord developer portal (https://discord.com/developers/applications) and sign in with your Discord account. Click the "New Application" button at the top right corner.
2. Create a Bot: After the application is created, go to the "Bot" page located in the left-hand sidebar. Give your bot a name, you don't really need to worry about the bot configuration settings for now.
3. Add the bot to a server: Click OAuth2 on the left-hand sidebar and check the "bot" box under "SCOPES". After the box is checked, you will see "BOT PERMISSIONS" appear. For now, just check all the boxes under "TEXT PERMISSIONS" and "View Channels" box under "GENERAL PERMISSIONS"

Copy the URL shown in "SCOPES" and paste it into your browser. You will be brought to a webpage where you can choose which server to add your bot to. After selecting the server and hitting continue, congrats you have a bot on your server!

**Note: You will need to install the Discord package. Through the command line type "pip3 install discord.py" 
**
------------------------------------------------------------------------------------------------------------------------------------
Now you're ready to download this repository! Type into the command line "git clone [url of repository]" into the location you want your repository to be located in.

Once your repository is downloaded use any IDE or directly open the .env file. To bring your bot online you will need to copy your bot token from the Discord developer's application page and paste that into the .env file

After, open the file startup.py and now your bot should be running! (Assuming you have python 3 and the discord package installed)

Use the command on the discord server you invited your bot to: "$search [name of movie]" to receive the first 5 URLs that come up on letterboxd. 

When your done using your bot just close the console window opened from startup.py.
