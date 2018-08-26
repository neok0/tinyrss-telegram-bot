#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram

from settings import TELEGRAM, CHAT


class TelegramBot:
    def __init__(self):
        self.TOKEN = TELEGRAM.get('token')
        self.chat_id = TELEGRAM.get('chat_id')

        self.bot = self._bot()

    # ############### #
    # Private methods #
    # ############### #

    def _bot(self):
        """
        create Telegram bot instance
        :return:
        """
        return telegram.Bot(token=self.TOKEN)

    def _get_keyboard(self):
        """
        create inline keyboard actions. Optional buttons can be specified in settings file.
        :return:
        """
        button_list = []
        for button in CHAT.get('buttons', []):
            button_list.append(InlineKeyboardButton(button.get('name'), callback_data=button.get('data')))

        reply_markup = InlineKeyboardMarkup(self._build_menu(button_list, n_cols=2))
        return reply_markup

    # ############ #
    # Main methods #
    # ############ #

    def send_message(self, msg, chat_id=None, replay_markup=None):
        """
        wrapper function for sending messaged via bot to recipients. Markdown highlighting is used for text styling.
        :param msg: Text message to be send
        :param chat_id: Chat ID will receive the text message
        :param replay_markup: e.g. any inline buttons wanted?
        :return:
        """
        if not chat_id:
            chat_id = self.chat_id
        self.bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN,
                              reply_markup=replay_markup)

    # ############## #
    # Helper methods #
    # ############## #

    def _build_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
        """
        dynamically build inline buttons
        :param buttons:
        :param n_cols:
        :param header_buttons:
        :param footer_buttons:
        :return:
        """
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)
        return menu


if __name__ == '__main__':
    t = TelegramBot()
    t.send_message('hallo')
