from tokenize import group

import lab_chat as lc


def get_username():
    username = input("Username: ")
    username = username.strip()
    username = username.upper()
    return username


def get_group():
    group = input("Group: ")
    group = group.strip()
    group = group.upper()
    return group


def get_message():
    message = input("Message: ")
    message = message.strip()
    return message

def initialize_chat():
    user = get_username()
    selected_group = get_group()

    user_node = lc.get_peer_node(user)

    lc.join_group(user_node, selected_group)

    selected_channel = lc.get_channel(user_node, selected_group)
    return selected_channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()