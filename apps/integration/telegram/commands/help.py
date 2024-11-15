# apps/integration/telegram/commands/help.py
from apps.communication.telegram.commands.decorator import telegram_command
from telegram import Message


@telegram_command("help", response_type="text")
def help_command_list(telegram_bot_membership, message: Message, context):
    from apps.communication.telegram.commands.commands_index import public_commands

    return "\n".join(
        [
            "Available commands:",
        ]
        + [
            "/%s - %s" % (command.execution_handle, command.help_text)
            for command in public_commands
        ]
    )


help_command_list.help_text = "list of available commands"
