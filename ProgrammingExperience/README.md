## 📖 Documentation

This adds the capabilities to send Slack Messages to a Slack Channel to the CodeAct Agent.

In order to run this you need to add your SLACK_BOT_TOKEN and CHANNEL_ID to openhands/runtime/base.py in writeSlackMessage.

In this I added:
    - SlackMessageObservation
    - SlackMessageAction
    - SlackMessageTool
    - support for new observation and action in eventStream
    - support for new observation in conversation memory
    - support for new tool in runtime

To add this to a Slack Channel you need to:
    1. Go to api.slack.com/apps
    2. create a new app
    3. OAuth & Permissions -> Scopes -> Bot Token Scopes -> Add the OAuth Scope "chat:write"
    4. Install App to Workspace
    5. Copy your Bot User OAuth Token
    6. /invite @your-bot-name to the desired channel
    7. Copy the channel id
