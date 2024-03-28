import obsws_python as obs
import os
from dotenv import load_dotenv


class OBSAdapter:
    def __init__(self) -> None:
        load_dotenv(verbose=True)
        password = os.environ.get("OBS_WS_PASSWORD")
        host = os.environ.get("OBS_WS_HOST")
        port = os.environ.get("OBS_WS_PORT")

        if password == None or host == None or port == None:
            print("OBS_WS_PASSWORD, OBS_WS_HOST, OBS_WS_PORT is not set in .env")
            raise Exception(
                "OBS_WS_PASSWORD, OBS_WS_HOST, OBS_WS_PORT is not set in .env"
            )

        self.ws = obs.ReqClient(host, port, password)
        pass

    def set_question(self, text: str):
        self.ws.set_input_settings(
            name="question", settings={"text": text}, overlay=True
        )

    def set_answer(self, text: str):
        self.ws.set_input_settings(name="answer", settings={"text": text}, overlay=True)


if __name__ == "__main__":
    adapter = OBSAdapter()
    adapter.set_question("Hello")
