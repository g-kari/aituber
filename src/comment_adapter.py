import pytchat
import json


class CommentAdapter:
    def __init__(self, video_id) -> None:
        self.chat = pytchat.create(video_id=video_id, interruptable=False)
        pass


def get_comeent(self):
    comments = self.__get_comment()
    if comments == None:
        return None

    comment = comments[-1]  # saisin
    message = comment.get("message")

    return message


def __get_comment(self):
    if self.chat.is_alive() == False:
        print("開始してない")
        return None
    cs = json.loads(self.chat.get().json())
    if cs == []:
        print("コメントなし")
        return None
    return cs
    # while self.chat.is_alive():
    #     for c in self.chat.get().sync_items():
    #         print(json.dumps(c, ensure_ascii=False, indent=2))
    #         pass
    #     pass
    # pass


if __name__ == "__main__":
    import time

    video_id = "dQw4w9WgXcQ"
    adapter = CommentAdapter(video_id)
    time.sleep(10)
    print(adapter.get_comeent())
