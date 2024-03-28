import random
from obs_adapter import OBSAdapter
from voicevox_adapter import VoicevoxAdapter
from opneai_adapter import LangChainAdapter
from comment_adapter import CommentAdapter
from play_sound import PlaySound
from dotenv import load_dotenv

load_dotenv(verbose=True)
import os


class AITuberSystem:
    def __init__(self) -> None:
        video_id = os.getenv("VIDEO_ID")
        self.comment_adapter = CommentAdapter(video_id)
        self.opneai_adapter = LangChainAdapter()
        self.voicevox_adapter = VoicevoxAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_devicee_name=os.getenv("OUTPUT_DEVICE_NAME"))

        pass

    def talk_with_comment(self):
        print("コメントを読み込みます...")
        comment = self.comment_adapter.get_comeent()
        if comment == None:
            print("コメントがありません")
            return None
        print(comment)
        response = self.opneai_adapter.create_chat(comment)
        print(response)
        data, rate = self.voicevox_adapter.get_voice(response)
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response)
        self.play_sound.play_scoud(data, rate)

        return True
