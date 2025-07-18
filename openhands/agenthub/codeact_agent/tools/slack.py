from litellm import ChatCompletionToolParam, ChatCompletionToolParamFunctionChunk

_SLACK_MESSAGE_DESCRIPTION = """Use this tool to send a message to the Slack channel.

Common use cases:
1. The user asks you to write a Slack message.
2. Notify a team about the completion of a CI job, deployment, or automated workflow.
3. Share updates, alerts, or summaries during a debugging or refactoring process.
4. Inform the team of discovered issues, test results, or important logs.
5. Send reminders or actionable messages directly into a workspace during development.

This tool will send the message immediately to the Slack channel for visibility and team alignment.
"""

SlackMessageTool = ChatCompletionToolParam(
    type='function',
    function=ChatCompletionToolParamFunctionChunk(
        name='send_slack_message',
        description=_SLACK_MESSAGE_DESCRIPTION,
        parameters={
            'type': 'object',
            'properties': {
                'slack_message': {
                    'type': 'string',
                    'description': 'The message content to send to the Slack channel.'
                },
            },
            'required': ['slack_message'],
        },
    ),
)
