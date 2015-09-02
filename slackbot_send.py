
import urllib
import urllib.parse
import urllib.request


class SlackbotSend:
    def __init__(self, domain, token):
        self.domain = domain
        self.token = token
        self.url_base = "https://{0}.slack.com/services/hooks/slackbot?token={1}&channel={2}"

    def debug_log(self, msg):
        print(msg)

    def send_message(self, channel, message):
        data = bytes(message, "utf-8")
        url = self.create_url(channel)
        response = urllib.request.urlopen(url, data)
        response_data = response.read().decode("utf-8")
        return response_data

    def create_url(self, channel):
        channel = urllib.request.quote(channel)
        return self.url_base.format(self.domain, self.token, channel)
