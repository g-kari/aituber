import sounddevice as sd
from typing import TypedDict


class PlaySound:
    def __init__(
        self,
        output_devicee_name="VoiceMeeter Output (VB-Audio Vo",
    ) -> None:
        # 指定された出力デバイス名に基づいてデバイスIDを種痘
        id = self._search_output_device_id(output_devicee_name)
        pass

    def _search_output_device_id(
        self, output_device_name: str, output_device_host_api=0
    ) -> int:
        # 出力デバイス名からデバイスIDを取得する
        devices = sd.query_devices()
        id = None
        for device in devices:
            print(device["name"], device["hostapi"])
            if (
                device["name"] == output_device_name
                and device["hostapi"] == output_device_host_api
            ):
                id = device["index"]
                break
        if id is None:
            print("デバイスみつかんねーよ")
            exit()
        return id

    def play_scoud(self, data, rate) -> bool:
        # 音声データを再生する
        sd.play(data, rate)
        sd.wait()
        return True
