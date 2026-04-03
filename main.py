#!/usr/bin/env python3

import sys
import random
import parser
from Player import Player
from GameState import GameState

JACKET_DESC = "The jacket is warm and comforting."
STARTING_ITEMS_DESC = "You have a shiny coin and a few scraps of paper."

KAREN_CALLS = ["Karen: Hey, are you there?", "Karen: I hope you’re ready for another adventure!"]

def build_world():
    pass  # World building logic goes here


def karen_interrupts():
    for call in KAREN_CALLS:
        print(call)


def handle_go(direction):
    pass  # Logic for going in a direction


def handle_look():
    pass  # Logic for looking around


def handle_examine(item):
    pass  # Logic for examining an item


def handle_take(item):
    pass  # Logic for taking an item


def handle_drop(item):
    pass  # Logic for dropping an item with coin logic integrated


def handle_drop_coin():
    pass  # Logic for dropping coin


def handle_listen():
    pass  # Logic for listening


def handle_wait():
    pass  # Logic for waiting


def handle_open(item):
    pass  # Logic for opening something with donations logic integrated


def handle_open_donations():
    pass  # Logic for handling donations


def handle_examine_donations():
    pass  # Special case for examining donations


def handle_eat():
    pass  # Logic for eating


def handle_drink():
    pass  # Logic for drinking


def handle_read(item):
    pass  # Logic for reading


def handle_postit_read():
    pass  # Logic for reading post-it notes


def handle_reverse():
    pass  # Logic for reversing action


def handle_write():
    pass  # Logic for writing


def handle_call():
    pass  # Logic for making a call


def handle_use(item):
    pass  # Logic for using an item


def handle_turn_on(device):
    pass  # Logic for turning on a device


def handle_turn_off(device):
    pass  # Logic for turning off a device


def handle_talk():
    pass  # Logic for talking


def handle_kiss():
    pass  # Logic for kissing


def handle_hug():
    pass  # Logic for hugging


def handle_ask():
    pass  # Logic for asking


def handle_sit():
    pass  # Logic for sitting


def handle_flip_coin():
    pass  # Logic for flipping a coin


def handle_help():
    pass  # Logic for help

WAIT_MESSAGES = ["You wait patiently.", "Time passes..."]
WAIT_DREAD_MESSAGES = ["You feel a sense of dread.", "Something is not right..."]
WAIT_DEATH = "You are dead. Game over."


def dispatch(command):
    command_map = {
        'go': handle_go,
        'look': handle_look,
        'examine': handle_examine,
        'take': handle_take,
        'drop': handle_drop,
        'wait': handle_wait,
        'listen': handle_listen,
        'open': handle_open,
        'call': handle_call,
        'help': handle_help,
    }
    if command in command_map:
        command_map[command]()
    else:
        print("Unknown command!")


def main():
    while True:
        command = input("Enter command: ")
        dispatch(command)


if __name__ == "__main__":
    main()