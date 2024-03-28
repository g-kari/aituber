from langchain.globals import (
    set_llm_cache,
)  # We can do the same thing with a SQLite cache
from langchain.cache import SQLiteCache

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class LangChainAdapter:
    def __init__(self) -> None:
        with open("./src/system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        set_llm_cache(SQLiteCache(database_path=".langchain.db"))
        pass

    def _create_messsage(self, username: str, content: str):
        return HumanMessage(content=content)

    def _create_system_message(self, content: str):
        return SystemMessage(content=content)

    def create_chat(self, username, question):
        system_message = self._create_system_message(self.system_prompt)
        user_message = self._create_messsage(username, question)
        messages = [system_message, user_message]
        client = ChatOpenAI()
        client.openai_api_key = os.environ.get("LANGCHAIN_API_KEY")
        client.model_name = "gpt-3.5-turbo"
        for chunk in client.stream(messages):
            if chunk.content:
                print(chunk.content, end="", flush=True)

        # return res.choices[0].message.content


if __name__ == "__main__":
    adapter = LangChainAdapter()
    response = adapter.create_chat(
        "ユーザー１",
        "適当で構わないから、タロットカード占いをして。引いたカードも詳細に教えて",
    )
    print(response)
    response = adapter.create_chat(
        "ユーザ２",
        "適当で構わないから、タロットカード占いをして。引いたカードも詳細に教えて",
    )
    print(response)
    response = adapter.create_chat(
        "ユーザー２",
        "適当で構わないから、タロットカード占いをして。引いたカードも詳細に教えて",
    )
    print(response)
    response = adapter.create_chat(
        "ユーザー２",
        "適当で構わないから、タロットカード占いをして。引いたカードも詳細に教えて",
    )
    print(response)
