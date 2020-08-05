// Code fixed up by QeaML. No thanks needed.
// Discord: QeaML#5450   Twitter: @AEmpi0r
var Discord = require('discord.io');
// better logger would be var logger = 'console'
var logger = require('winston');
var auth = require('./auth.json');

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
               name: "Thelp me get my dad back"
        }
    });
    logger.info('Connected');
    logger.info('Logged in as: ');
    logger.info(bot.username + ' - (' + bot.id + ')');
});
bot.on('message', function (user, userID, channelID, message, evt) {
    if (message.substring(0, 1) == 'T') {
        var args = message.substring(1).split(' ');
        var cmd = args[0];
	  var param = args[1];
        args = args.splice(1);
        switch(cmd) {

		
case('blend'):
    if (param == 'undefined' || param == undefined) {
        param = 'A THING';
    };
    bot.sendMessage({
        to: channelID,
        message: '***LOUD SCREAMING OF '+param+'***'
    });
break;
case 'Jakesapples' :
    bot.sendMessage({
        to: channelID,
        message: 'Jake has ' + Math.floor(Math.random() * 3756) + ' apple(s)'
    });
break;
case 'whoami' :
    bot.sendMessage({
        to: channelID,
        message: 'this but is basic but i will try to make it good.basic'
    });
break;
case 'seriesisgay' :
    bot.sendMessage({
        to: channelID,
        message: 'Im not subbed to pewdiepie nor t-series'
    });
break;
case 'series' :
    bot.sendMessage({
        to: channelID,
        message: 'आपकी माँ समलैंगिक इकाई है'
    });
break;
case 'gay' :
    bot.sendMessage({
        to: channelID,
        message: 'your gay level is ' + Math.floor(Math.random() * 101) + '%'
    });
break;
case 'uncensor' :
    bot.sendMessage({
        to: channelID,
        message: 'Tf no u perv'
    });
break;
case 'gimmepopcorn' :
    bot.sendMessage({
        to: channelID,
        message: 'here u go :popcorn:'
    });
break;
case 'whyamilikethis' :
if ( userID > 396699211946655745) {
bot.sendMessage({
to: channelID,
message: 'true'
});
} else {
bot.sendMessage({
to: channelID,
message: 'false'
});
};
break;
case 'help' :
    bot.sendMessage({
        to: channelID,
		message: '**Thelp**-shows this text\n**Tgimmepopcorn**-gives you popcorn\n**Tgay**-says how gay you are\n**Tuncensor**-uncensors an image\n**Tseries**-says something in Hindi\n**Tseriesisgay**-just see what happens\n**Tblend**-blends something\ni wont show the last command'
    });
	break;
	case 'contact' :
    bot.sendMessage({
        to: channelID,
        message: 'Contact my owner at 01010100#7782 on discord. Thanks to QeaML#5450 for help with coding.'
    });
break;
case 'liedetector' :
	var randomTo10 = Math.floor(Math.random * 10);
    	if (randomTo10 <= 5 ) {
bot.sendMessage({
to:channelID,
message: 'Lie detected!'
});
} else {
bot.sendMessage({
to:channelID,
message: 'Truth detected!'
});
};break;
case('throw'):
    if (param == 'undefined' || param == undefined) {
        param = 'air';
    };
    bot.sendMessage({
        to: channelID,
        message: user+' threw '+param+' off a bridge'
    });
break;
         }
     }
});
