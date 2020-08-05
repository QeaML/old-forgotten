const dscrd = require('discord.io');
const fsys = require('fs');
const os = require('os-utils');
const auth = require('./auth.json');
const textfrom = require('./strings_english.json');
const lggr = require('./logEvent');
const numop = require('./numop');
var lastcommand = 'nothing';
var timerSecond = 0;
var timerMinute = 0;
var timerHour = 0;
var statMsgs = 0;
var statCmds = 0;
var statCmdsR = 0;
var statCmdsU = 0; 
var xpAmt = 0;
var presenceNum = 0;

lggr.logEvent(0, 'load', 'Variables ready');

const bot = new dscrd.Client({
    token: auth.token,
    autorun: true
});

bot.on('ready', function (evt) {
    lggr.logEvent(0, this,'Bot ready');
	lggr.logEvent(0, this, 'Connected as '+bot.username+'('+bot.id+')');
	function cyclePresence() {
		switch(presenceNum){
			case(0):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.a
					}
				})
				presenceNum++;
			break;
			case(1):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.b
					}
				})
				presenceNum++;
			break;
			case(2):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.c
					}
				})
				presenceNum++;
			break;
			case(3):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.d
					}
				})
				presenceNum++;
			break;
			case(4):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.e
					}
				})
				presenceNum++;
			break;
			case(5):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.f
					}
				})
				presenceNum++;
			break;
			case(6):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.g
					}
				})
				presenceNum++;
			break;
			case(7):
				bot.setPresence({
					status: "online",
					game:{
						name: textfrom.presence.h
					}
				})
				presenceNum++;
			break;
			case(8):
				bot.setPresence({
					status: "online",
					game:{
						name: "after "+statCmds+" commands"
					}
				})
				presenceNum++;
			break;
			case(9):
				bot.setPresence({
					status: "online",
					game:{
						name: "after "+statMsgs+" messages"
					}
				})
				presenceNum++;
			break;
			case(10):
				bot.setPresence({
					status: "online",
					game:{
						name: "for "+timerHour+"h "+timerMinute+"m"
					}
				})
				presenceNum = 0;
			break;
			default:
				bot.setPresence({
					status: "dnd",
					game:{
						name: "with broken code"
					}
				})
			break;
		};
	};
    function timerCalculate() {
		if ( timerSecond == 30 || timerSecond == 60) {
			cyclePresence();
		};
        if ( timerSecond == 60 ) {
			timerSecond = 0;
			timerMinute++;
			if ( timerMinute == 60 ) {
				timerMinute = 0;
				timerHour++;
			};
		};
    };
    function timerAddSecond() {
        timerSecond++;
        timerCalculate();
	};
	setInterval(timerAddSecond, 1000);
	function errorHandler(e, i) {
		switch(e){

		};
	};
});

bot.on('message', function (usr, usrID, chnnlID, mssg, evt) {
	statMsgs++;
    if (mssg.substring(0, 2) == 'q?') {
        var args = mssg.substring(2).split(' '); 
        var cmd = args[0];
        var arg1 = args[1];
		var arg2 = args[2];
		var arg3 = args[3];
		statCmds++;
		args = args.splice(1);
        switch (cmd) {
            case ('sayhi'):
                bot.sendMessage({
                    to: chnnlID,
                    message: 'Hello, ' + usr + '!'
                });
				lastcommand = 'sayhi';
				statCmdsR++;
			break;
			case('reset'):
				switch(arg1){
					default:
						bot.sendMessage({
							to: chnnlID,
							message: usr+textfrom.command.reset.ask
						})
					break;
					case('confirm'):
						fsys.writeFile('rank/'+usrID+'.txt', 0, function (err) {
							if (err) {
								lggr.logEvent(2, 'reset', 'could not update rank for '+usrID);
							};
						});
						fsys.writeFile('vault/'+usrID+'.txt', 0, function(err) {
							if (err) {
								lggr.logEvent(2, 'reset', 'could not update vault for '+usrID);
							};
						});
						bot.sendMessage({
							to: chnnlID,
							message: textfrom.command.reset.deleted
						});
					break;
				};
			break;
			case ('news'):
				bot.sendMessage({
					to: chnnlID,
					message: textfrom.command.news
				});
			break;
            case ('sayhito'):
                bot.sendMessage({
                    to: chnnlID,
                    message: 'Hello, ' + arg1 + '!'
                });
				lastcommand = 'sayhito';
				statCmdsR++;
			break;
            case ('lastcommand'):
                bot.sendMessage({
                    to: chnnlID,
                    message: textfrom.misc.lc + '`' + lastcommand + '`.'
                });
				lastcommand = 'lastcommand';
				statCmdsR++;
            break;
            case ('help'):
                bot.sendMessage({
                    to: chnnlID,
                    message: textfrom.command.help
                });
				lastcommand = 'help';
				statCmdsR++;
            break;
			case ('status'):
				statCmdsR++;
				var osfm = os.freememPercentage();
				os.cpuUsage(function(osus){
                	bot.sendMessage({
                	    to: chnnlID,
               	     	message: 'Qudda Status:\nUptime: ' + timerHour + 'h' + timerMinute + 'm' + timerSecond + 's\nMessages recorded: '+statMsgs+'\nCommands recorded: '+statCmds+'\nCommands recognized: '+statCmdsR+'\nCommands unrecognized: '+statCmdsU+'\nCPU Usage: '+Math.floor(osus * 100)+"%\nMemory usage: "+Math.floor(100-Math.floor(Number(osfm) * 100))+'%'
					});
				});
				lastcommand = 'status';
            break;
            case ('xp'):
                if (usrID != 562008651217502240) {
                    fsys.readFile('rank/' + usrID + '.txt', function (err, data) {
                        xpAmt = data;
                        bot.sendMessage({
                            to: chnnlID,
                           message: usr + ', you have ' + xpAmt + ' XP points.'
                        });

                    });
					lastcommand = 'xp';
					statCmdsR++;
                }
            break;
            case('commands'):
                bot.sendMessage({
                    to: chnnlID,
                    message: textfrom.command.commands
                });
				lastcommand = 'commands';
				statCmdsR++;
			break;
			case('steal'):
				if (isNaN(arg1)) {
					lggr.logEvent(2, 'steal', 'arg1 != NUMBER');
				} else {
					stealXp(arg1);
				}
			break;
			case('turnoff'):
				if(usrID == 396699211946655745) {
					bot.setPresence({
						status: "idle",
						game: {
							name: "Shutting down!"
						}
					});
					bot.sendMessage({
						to: chnnlID,
						message: 'Bot shutting down in 10 seconds.'
					});
					lggr.logEvent(2, 'cmd', 'shutting down in 10 seconds');
					function tbo() {
						bot.sendMessage({
							to: chnnlID,
							message: "Goodbye!"
						})
						bot.setPresence({
							status: "invisible",
							game: {
								name: "off"
							}
						});
						process.exit()
					};
					setTimeout(tbo, 10000);
					statCmdsR++;
				} else {
					bot.sendMessage({
						to: chnnlID,
						message: usr + ', sorry but you cannot use this command.'
					});
				}
				lastcommand = 'turnoff';
				statCmdsR++;
			break;
			case('gamble'):
				statCmdsR++;
				lastcommand = 'gamble';
					bot.sendMessage({
						to: chnnlID,
						message: textfrom.unavilable.wip
					});
			break;
			case('vault'):
				switch(arg1) {
					default:
						bot.sendMessage({
							to: chnnlID,
							message: textfrom.command.vault.help
						});
						lastcommand = 'vault';
						statCmdsR++;
					break;
					case('help'):
						bot.sendMessage({
							to: chnnlID,
							message: textfrom.command.vault.help
						});
						lastcommand = 'vault help';
						statCmdsR++;
					break;
					case('bal'):
						fsys.readFile('vault/'+usrID+'.txt', function (err, data) {
							vaultBal = data;
							if (vaultBal == undefined) {
								vaultBal = 0;
								fsys.writeFile('vault/'+usrID+'.txt', vaultBal, function (err) {
									if (err) {
										lggr.logEvent(1, 'vault', 'could not update balance for '+usrID);
									};
									lggr.logEvent(0, 'vault', 'updated balance for '+usrID+' to '+newVaultBal);
								});
							}
							bot.sendMessage({
								to: chnnlID,
								message: usr+', you are currently storing '+vaultBal+' XP points in the vault. Your vault ID is '+usrID+'.'
							});
						});
						lastcommand = 'vault bal';
						statCmdsR++;
					break;
					case('deposit'):
						arg2 = Number(arg2);
						if (numop.isInvalidNum(arg2)) {
							bot.sendMessage({
								to: chnnlID,
								message: "I'm sorry, but "+arg2+" is not a number you can use here."
							});
						} else {
							fsys.readFile('rank/'+usrID+'.txt', function (err, dataX) {
								oldXpAmt = Number(dataX);
								if(arg2 > dataX){
									bot.sendMessage({
										to: channelID,
										message: "I'm sorry, but you do not have "+arg2+" XP points."
									});
								} else {
									fsys.readFile('vault/'+usrID+'.txt', function(err, dataV){
										oldVaultBal = Number(dataV);
										newVaultBal = oldVaultBal + arg2;
										newXpAmt = oldXpAmt - arg2;
										fsys.writeFile('rank/'+usrID+'.txt', newXpAmt, function (err){
											if (err) throw err;
											lggr.logEvent(0, 'rank', 'updated xp for '+usrID+' to '+newXpAmt);
										});
										fsys.writeFile('vault/'+usrID+'.txt', newVaultBal, function (err){
											if (err) throw err;
											lggr.logEvent(0, 'vault', 'updated balance for '+usrID+' to '+newVaultBal);
										});
									});
								};
							});
						};
						lastcommand = 'vault deposit';
						statCmdsR++;
					break;
					case('withdraw'):
						arg2 = Number(arg2);
						if (numop.isInvalidNum(arg2)) {
							bot.sendMessage({
								to: chnnlID,
								message: "I'm sorry, but "+arg2+" is not a number you can use here."
							});
						} else {
							fsys.readFile('vault/'+usrID+'.txt', function (err, dataV) {
								oldVaultBal = Number(dataV);
								if(arg2 > dataV){
									bot.sendMessage({
										to: channelID,
										message: "I'm sorry, but you do not have "+arg2+" XP points in the vault."
									});
								} else {
									fsys.readFile('rank/'+usrID+'.txt', function(err, dataX){
										oldXpAmt = Number(dataX);
										newVaultBal = oldVaultBal - arg2;
										newXpAmt = oldXpAmt + arg2;
										fsys.writeFile('rank/'+usrID+'.txt', newXpAmt, function (err){
											if (err) throw err;
											lggr.logEvent(0, 'rank', 'updated xp for '+usrID+' to '+newXpAmt);
										});
										fsys.writeFile('vault/'+usrID+'.txt', newVaultBal, function (err){
											if (err) throw err;
											lggr.logEvent(0, 'vault', 'updated balance for '+usrID+' to '+newVaultBal);
										});
									});
								};
							});
						};
						lastcommand = 'vault withdraw';
						statCmdsR++;
					break;
					case('transfer'):
						bot.sendMessage({
							to: chnnlID,
							message: textfrom.unavilable.wip
						});
						lastcommand = 'vault transfer';
						statCmdsR++;
					break;
				}
			break;
			default:
				bot.sendMessage({
					to: chnnlID,
					message: textfrom.unavilable.unrecognized
				});
				statCmdsU++;
			break;
		};
        lggr.logEvent(0, 'cmd', usr+' executed '+lastcommand);
    } else {
		if (usrID != 562008651217502240) {
			fsys.readFile('rank/' + usrID + '.txt', function (err, data) {
				xpAmt = data;
				xpAmt = Number(xpAmt);
				if (isNaN(xpAmt)) {
					xpAmt = 1;
				} else {
					xpAmt++;
				}
				fsys.writeFile('rank/' + usrID + '.txt', xpAmt, function (err) {
					if (err) {
						lggr.logEvent(1, 'rank', 'could not update xp for '+usrID+'('+usr+')');
					};  
					lggr.logEvent(0, 'rank', 'updated xp for '+usrID+'('+usr+') to '+xpAmt);
				});
			});
		};
	};
});