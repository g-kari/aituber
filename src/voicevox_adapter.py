import json
import requests
import io
import soundfile
import requests


class VoicevoxAdapter:
    def __init__(self, host="localhost", port=50021):
        self.url = f"http://{host}:{port}/"

    def __create_audio_query(self, text, speaker) -> json:
        item_data = {"text": text, "speaker": speaker}
        response = requests.post(self.url + "audio_query", params=item_data)
        print(response.status_code)
        return response.json()

    def __create_request_audio(self, query_data, speaker) -> bytes:
        a_params = {"speaker": speaker}
        headers = {"Content-Type": "application/json", "Accept": "audio/wav"}
        response = requests.post(
            self.url + "synthesis",
            params=a_params,
            data=json.dumps(query_data),
            headers=headers,
        )
        print(response.status_code)
        return response.content

    def get_voice(self, text: str):
        speaker_id = 3
        query_data = self.__create_audio_query(text, speaker_id)
        audio = self.__create_request_audio(query_data, speaker_id)
        audio_stream = io.BytesIO(audio)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate


if __name__ == "__main__":
    adapter = VoicevoxAdapter()
    data, rate = adapter.get_voice("こんにちは")
    print(rate)
