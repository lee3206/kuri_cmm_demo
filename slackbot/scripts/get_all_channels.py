from slack_bolt import App
import yaml

# Load the Slackbot configuration
slackbot_conf_filepath = "../cfg/slackbot.yaml"
with open(slackbot_conf_filepath, 'r') as f:
    slackbot_conf = yaml.load(f, Loader=yaml.FullLoader)

# Launch the Slack App
slack_app = App(
    token=slackbot_conf['slack_user_token'],
    signing_secret=slackbot_conf['slack_signing_secret']
)



# Request all the channels 
# get channles 
# allow kuri to join channles?
# use command in channels?
found_user_i = []
done = False
next_cursor = ''
while not done:
    response = slack_app.client.conversations_list(cursor=next_cursor)
    if response['ok']:
        for item in response['channels']:
            print(item)
        if 'next_cursor' in response['response_metadata'] and len(response['response_metadata']['next_cursor']) > 0:
            done = False
            next_cursor = response['response_metadata']['next_cursor']
        else:
            done = True
    else:
        print("response", response)
        print("Request failed. ")
        break


