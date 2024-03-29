from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound

input_text = input("こんにちは")
vv_adater = VoicevoxAdapter()
play_sound = PlaySound()
data, rate = vv_adater.get_voice(input_text)

play_sound.play_scoud(data, rate)
