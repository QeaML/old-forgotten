//constats
const Discord = require('discord.io');
const file = require('fs');
const cfg = require("./config.json");

//bot's discord client
const bot = new Discord.Client({
   token: require("./auth.json").token,
   autorun: true
});

/*send function, to minimalize the code
* instead of using bot.sendMessage({<JSON here>}), we'd use send()
*/
function send(c, t) {
	bot.sendMessage({
		to: c,
		message: t
	})
}

/*log function, logging everything the bot does
* if log.console is enabled in cofig.json, everything is printed to the console
* if log.file is enabled in config.json, everything is saved to log.txt
*/
function log(text){
	if(cfg.log.console == true){
		console.log(txt)
	}
	if(cfg.log.file == true){
		fs.openFile('log.txt', function(data, err) {
			if(err){
				throw(err)
			}else{
				fs.writeFile('log.txt', data + "\n" + txt, function(err){
					if(err){
						throw(err)
					}
				})
			}
		})
	}
}

//bot's "ready" event
bot.on('ready', function (evt) {
	bot.setPresence({
		status: "dnd",
		game:{
			name: "Lhelp"
		}
	});
	log('|||[[[ Ready ')
   	log('|||[[[ Connected ');
    	log('|||[[[ Logged in as: ' + bot.username + ' - (' + bot.id + ')');
	log('|||[[[ Start of log')
});

//bot's "message" event
bot.on('message', function (user, userID, channelID, message, evt) {
    if (message.substring(0, 1) == 'L') {
        var args = message.substring(1).split(' ');
        var cmd = args[0];
        args = args.splice(1);
        switch(cmd) {
		case 'hi':
			send(channelID, 'Hi, my name is LuigiBot.')
		break;
		case 'blah':
			send(channelID, 'Blahblahblah.')
		break;
		case 'macandcheese':
			send(channelID, 'Here, have some mac and cheese.')
		break;
		case 'fastfood':
			send(channelID, ':hamburger: :fries:')
		break;
		case 'spam':
			send(channelID, 'HOURHN4I UHNEUO GJETIOHE O HOETTOEOGHJO EO GETOG JGHJ RTJG ORTJHG ORTH ORTJH ORJH ORTJ ORTJHTJHORTJGHIORJHIOJBO RRTREFSFG')
		break;
		case 'pingeveryone':
			send(channelID, '@everyone')
		break;
		case 'randomnumber':
			send(channelID, Math.floor(Math.random() * 101))
		break;
		case 'help':
			send(channelID, '**Commands:**\nl?hi - says hi to you\nl?blah does the blahblahblah thing\nl?macandcheese gives you mac and cheese\nl?fastfood gives you fast food\nl?spam spammity spam spam\nl?pingeveryone pings everyone\nl?randomnumber gives you a random number\nl?help shows this thing\nl?kill kills stuff\nl?succ s u c c\nl?howlongyourdickis shows how long it is\nl?votepewdiepie votes for pewdiepie\nl?votetseries votes for t-series\nl?credits shows the credits thing')
		break;
		case 'kill':
			send(channelID, '***LOUD FUCKING SCREAMS OF HELL***')
		break;
		case 'succ':
			send(channelID, 'You have succed **' + Math.floor(Math.random() * 31) + '** dicks')
		break;
		case 'howlongyourdickis':
			send(channelID, 'Your dick is **' + Math.floor(Math.random() * 31) + '** centimeter(s) long')
		break;
		case 'credits':
			send(channelID, '**Credits:**\nLuigiTV#7793 - made the bot originally\nQeaML#5450 - took the bot from it and mad eit better')
		break;
        }
	log(user+' executed '+cmd)
    }
});
