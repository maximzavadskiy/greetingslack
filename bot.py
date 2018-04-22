from rocketchat_API.rocketchat import RocketChat

###VARIABLES THAT YOU NEED TO SET MANUALLY IF NOT ON HEROKU#####
try:
    SERVER_URL = os.environ['SERVER_URL']
    BOT_USERNAME = os.environ['BOT_USERNAME']
    BOT_PASS = os.environ['BOT_PASS']
    MESSAGE = os.environ['WELCOME_MESSAGE']
except:
    SERVER_URL = 'Manually set SERVER_URL if youre not running through heroku or have not set vars in ENV'
    BOT_USERNAME = 'Manually set BOT_USERNAME if youre not running through heroku or have not set vars in ENV'
    BOT_PASS = 'Manually set BOT_PASS if youre not running through heroku or have not set vars in ENV'
    MESSAGE = 'Manually set the MESSAGE if youre not running through heroku or have not set vars in ENV'
###############################################################


rocket = RocketChat(BOT_USERNAME, BOT_PASS, server_url=SERVER_URL)
rocket.chat_post_message('good news everyone: I came to live!', channel='GENERAL')