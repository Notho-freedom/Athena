#!/usr/bin/python

# -- coding: utf-8 --



import time

import random

import os

import sys

import pickle

import pprint

import urllib.request

import urllib.parse

#import urlparse

import re



CHAT_GPT_URL = "https://www.chatgpt.com/gateway.php"



def get_random_chat_member(chat_gpt_url):

    request = urllib.request.Request(CHAT_GPT_URL)

    response = urllib.request.urlopen(request)

    data = response.read()

    parse_data = urllib.parse.urlparse(CHAT_GPT_URL)

    return parse_data.pathname[random.randint(0, len(parse_data.pathname) - 1)]



def load_chat_gpt(chat_gpt_url, user_id, chat_id, chat_name, chat_message):

    request = urllib.request.Request(CHAT_GPT_URL)

    response = urllib.request.urlopen(request)

    data = response.read()

    parse_data = urllib.parse.urlparse(CHAT_GPT_URL)

    user_id = parse_data.query.get('user_id')

    chat_id = parse_data.query.get('chat_id')

    chat_name = parse_data.query.get('chat_name')

    chat_message = parse_data.query.get('chat_message')

    with open('chat_gpt.pkl', 'wb') as f:

        pickle.dump( {

        'chat_gpt_url': chat_gpt_url,

        'user_id': user_id,

        'chat_id': chat_id,

        'chat_name': chat_name,

        'chat_message': chat_message,

        }, f)

    return



def main():

    print("Chat with other members on Chatgpt.com")

    print("Enter the user id of the person you want to chat with")

    user_id = input()

    print("Enter the chat id of the chat you want to join")

    chat_id = input()

    print("Enter the chat name")

    chat_name = input()

    print("Enter your chat message")

    chat_message = input()

    load_chat_gpt(CHAT_GPT_URL, user_id, chat_id, chat_name, chat_message)



if __name__ == "__main__":

    main()