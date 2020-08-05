var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
   token: auth.token,
   autorun: true
});
bot.on('ready', function (evt) {
	bot.setPresence({
		status: "dnd",
		game:{
			name: "l?help"
		}
		});
	

    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + ' - (' + bot.id + ')');
});
bot.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with !
    if (message.substring(0, 1) == 'l') {
        var args = message.substring(1).split(' ');
        var cmd = args[0];

        args = args.splice(1);
        switch(cmd) {
            // Just add any case commands if you want to..
			case '?hi':
bot.sendMessage({
to: channelID,
message: 'Hi, my name is LuigiBot.'
});
logger.info(user + ' has executed the command hi')
break;
			case '?blah':
bot.sendMessage({
to: channelID,
message: 'Blahblahblah.'
});
logger.info(user + ' has executed the command blah')
break;
			case '?macandcheese':
bot.sendMessage({
to: channelID,
message: 'Here, have some mac and cheese.'
});
logger.info(user + ' has executed the command macandcheese')
break;
			case '?fastfood':
bot.sendMessage({
to: channelID,
message: ':hamburger: :fries:'
});
logger.info(user + ' has executed the command fastfood')
break;
			case '?spam':
bot.sendMessage({
to: channelID,
message: 'HOURHN4I UHNEUO GJETIOHE O HOETTOEOGHJO EO GETOG JGHJ RTJG ORTJHG ORTH ORTJH ORJH ORTJ ORTJHTJHORTJGHIORJHIOJBO RRTREFSFG'
});
logger.info(user + ' has executed the command spam')
break;
			case '?pingeveryone':
bot.sendMessage({
to: channelID,
message: '@everyone'
});
logger.info(user + ' has executed the command pingeveryone')
break;
			case '?randomnumber':
bot.sendMessage({
to: channelID,
message: Math.floor(Math.random() * 101)
});
logger.info(user + ' has executed the command randomnumber')
break;
			case '?help':
bot.sendMessage({
to: channelID,
message: '**Commands:**\nl?hi - says hi to you\nl?blah does the blahblahblah thing\nl?macandcheese gives you mac and cheese\nl?fastfood gives you fast food\nl?spam spammity spam spam\nl?pingeveryone pings everyone\nl?randomnumber gives you a random number\nl?help shows this thing\nl?kill kills stuff\nl?succ s u c c\nl?howlongyourdickis shows how long it is\nl?votepewdiepie votes for pewdiepie\nl?votetseries votes for t-series\nl?credits shows the credits thing'
});
logger.info(user + ' has executed the command help')
break;
			case '?kill':
bot.sendMessage({
to: channelID,
message: '***LOUD FUCKING SCREAMS OF HELL***'
});
logger.info(user + ' has executed the command kill')
break;
			case '?succ':
bot.sendMessage({
to: channelID,
message: 'You have succed **' + Math.floor(Math.random() * 31) + '** dicks'
});
logger.info(user + ' has executed the command succ')
break;
			case '?howlongyourdickis':
bot.sendMessage({
to: channelID,
message: 'Your dick is **' + Math.floor(Math.random() * 31) + '** centimeter(s) long'
});
logger.info(user + ' has executed the command howlongyourdickis')
break;
			case '?votepewdiepie':
bot.sendMessage({
to: channelID,
message: 'You voted for pewdiepie!'
});
logger.info(user + ' has executed the command votepewdiepie')
break;
			case '?votetseries':
bot.sendMessage({
to: channelID,
message: 'You voted for tseries!'
});
logger.info(user + ' has executed the command votetseries')
break;
			case '?credits':
bot.sendMessage({
to: channelID,
message: '**Credits:**\nQeaML#5450 for the helping of making a bot'
});
logger.info(user + ' has executed the command credits')
break;
         }
     }
});
