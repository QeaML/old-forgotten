//variables
var Discord = require('discord.io');
var auth = require('./auth.json');

//functions
function getRandom(max){
	var newMax = Number(max) + 1
	var num = Math.floor(Math.random() * newMax)
	return num
}

function print(txt){
	console.log(txt)
}

//create bot client
var bot = new Discord.Client({
	token: auth.token,
	autorun: true
});

function send(c, t) {
	bot.sendMessage({
		to: c,
		message: t
	});
}

//bot's "ready" event
bot.on('ready', function (evt) {
	//set the bot's presence
	bot.setPresence({
		//DO NOT DISTURB THE BOT WITH UNNECCESSARY CRAP
		status: "dnd",
		//haha funny
		game:{
			name: "Thelp me get my dad back"
		}
	});
	
	print('|||---===---|||');
	print('Connected');
	print('Logged in as: '+bot.username + ' - (' + bot.id + ')');
	print('|||---===---|||');
});

//bot's "message" event
bot.on('message', function (user, userID, channelID, message, evt) {
	//check the first substring to be "T", and then process the text
	if (message.substring(0, 1) == 'T') {
		//make args the list of arguments
		var args = message.substring(1).split(' ');
		//first argument = command itself
		var cmd = args[0];
		//to be used later
		var param = args[1];
		args = args.splice(1);
		//switch to the command
		switch(cmd) {		
			case('blend'):
				if (param == 'undefined' || param == undefined) {
					param = 'A THING';
				};
				send(channelID, '***LOUD SCREAMING OF '+param+'***')
			break;
			case 'jakesapples' :
				send(channelID, 'Jake has ' + getRandom(1000000) + ' apple(s)');
			break;
			case 'whoami' :
				send(channelID, 'this but is basic but i will try to make it good.basic')
			break;
			case 'seriesisgay' :
				send(channelID, 'Im not subbed to pewdiepie nor t-series')
			break;
			case 'series' :
				send(channelID, 'आपकी माँ समलैंगिक इकाई है')
			break;
			case 'gay' :
				send(channelID, 'your gay level is ' + getRandom(100) + '%')
			break;
			case 'uncensor' :
				send(channelID, 'Tf no u perv')
			break;
			case 'gimmepopcorn' :
				send(channelID, 'here u go :popcorn:')
			break;
			case 'whyamilikethis' :
				if ( userID > 396699211946655745) {
					send(channelID, 'true')
				} else {
					send(channelID, 'false')
				};
			break;
			case 'help' :
				send(channelID, '**Thelp**-shows this text\n**Tgimmepopcorn**-gives you popcorn\n**Tgay**-says how gay you are\n**Tuncensor**-uncensors an image\n**Tseries**-says something in Hindi\n**Tseriesisgay**-just see what happens\n**Tblend**-blends something\n**Throw**-YEET\n**Tspam**-made by QeaML#5450 and doesnt work even though he is the smart coder\n**Twhyamilikethis**-also made by QeaML#5450 and i dont remember what it does\n**Tcontact**-my owners contacts\n**Twhoami**-i cant describe it\n**Tjakesapples**-says how many apples Jake has\n')
			break;
			case 'contact' :
				send(channelID, 'Contact my owner at 01010100#7782 on discord. Thanks to QeaML#5450 for help with coding.')
			break;
			case 'liedetector' :
				if (getRandom(10) <= 5 ) {
					send(channelID, 'Lie detected!')
				} else {
					send(channelID, 'Truth detected!')
				};
			break;
			case('hrow'):
				if (param == 'undefined' || param == undefined) {
					param = 'air';
				};
				send(channelID, user+' threw '+param+' off a bridge')
			break;
			case('spam'):
				for(i=0;i==10;i++){
					send(channelID, getRandom(1000))
				}
			break;
			default:
				send(channelID, "That is *not* a command I know of!")
			break;
		}
	}
});
