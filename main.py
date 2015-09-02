
import os
import sys
import json
import slackbot_send


def run():
    args = sys.argv[1:]
    config = get_config()
    if not config:
        return False
    if len(args) < 2:
        print("Provide channel name without # and the message you would like to send. Example: general Hello from Slackbot!")
        return False
    channel = "#" + args.pop(0)
    message = " ".join(args)

    ss = slackbot_send.SlackbotSend(config["domain"], config["token"])
    print("Sending '{}' to '{}'...".format(message, channel))
    status = ss.send_message(channel, message)
    print("Status: {}".format(status))


def get_config():
    config = read_config()
    if validate_config(config):
        return config
    return False


def read_config():
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        f = open(os.path.join(script_dir, "config.json"))
        data = f.read()
        f.close()
        return json.loads(data)
    except:
        return False


def validate_config(config):
    if not config:
        print("Config file not found or couldn't be parsed.")
        return False
    if "domain" not in config.keys() or "token" not in config.keys():
        print("Config is missing domain and/or token.")
        return False
    if not config["domain"] or not config["token"]:
        print("Domain and/or token is empty in config. Please fill them in.")
        return False
    return True

if __name__ == "__main__":
    run()
