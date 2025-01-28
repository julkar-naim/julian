import random
import time

import mesop as me
import mesop.labs as mel
from langchain_core.messages import AIMessage, HumanMessage

from model import chat

def on_load(e: me.LoadEvent):
  me.set_theme_mode("light")


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io", "https://huggingface.co"]
  ),
  path="/",
  title="Chat With Julian",
  on_load=on_load,
)
def page():
  mel.chat(transform, title="Chat With Julian", bot_user="Julian")


def transform(input: str, history: list[mel.ChatMessage]):
    for chunk in chat.stream(convert_messages(input, history)):
      yield chunk.content


def convert_messages(input, messages: list[mel.ChatMessage]):
  langchain_message_list = []
  for message in messages:
    if message.role == "assistant":
      langchain_message_list.append(AIMessage(content=message.content))
    else:
        langchain_message_list.append(HumanMessage(content=message.content))
  langchain_message_list.append(AIMessage(content=input))
  return langchain_message_list