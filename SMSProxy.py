#!/usr/bin/env python


import ConfigParser
import os
import datetime
import web # from: http://webpy.org/
from twilio.rest import TwilioRestClient # from: https://github.com/twilio/twilio-python

config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/SMSProxy.cfg'))

credentials = {'APP_ID': config.get("Twilio","APP_ID"), 'APP_SECRET':config.get("Twilio","APP_SECRET"), 'FROM':config.get("Twilio", "FROM")}

def valid(d, expects):
    for key in expects:
        if not d.has_key(key):
            return False
    return True

urls = (
    '/', 'index',
    '/sms/send', 'send'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return str(datetime.datetime.now())

class send:
    def POST(self):
        i = web.input()
        client = TwilioRestClient(credentials['APP_ID'], credentials['APP_SECRET']) 
        return client.messages.create(to=i.To, from_=credentials['FROM'], body=i.Body)

if __name__ == "__main__":
    if valid(credentials, ['APP_ID', 'APP_SECRET', 'FROM']):
        app.run()
    else:
        print 'You need a file called ~/SMSProxy.cfg with the following contents:'
        print '  [Twilio]'
        print '  APP_ID=######'
        print '  APP_SECRET=######'
        print '  FROM=###########'