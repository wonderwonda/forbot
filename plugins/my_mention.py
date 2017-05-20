# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


@respond_to('メンション')
def mention_func(message):
    message.reply('メンションですよー')

@listen_to('リッスン')
def listen_func(message):
    message.send('聞いてほしいんですねー')
    message.reply('あなたからのリプライです。')


@respond_to('ほげほげ')
def mention_func(message):
    message.reply('ほげほげですよー')
