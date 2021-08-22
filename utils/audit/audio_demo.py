import datetime
import os
import time

from pydub import AudioSegment
from scipy.io import wavfile
import json

# to_path = '/Users/wjj/DataCenter/单词wav'
# from_path = '/Users/wjj/DataCenter/单词mp3'
# mp3list = os.listdir(from_path)
# if not os.path.exists(to_path):
#     os.makedirs(to_path)

# for mp3 in mp3list:
#     if mp3 == '.DS_Store':
#         continue
#     fs = os.path.splitext(mp3)
#     name = fs[0]
#     wav_name = "莜蕾日语-" + name[name.index(".") + 1: name.index("_1")] + '.wav'
#     sound = AudioSegment.from_mp3(os.path.join(from_path, mp3))
#     sound.export(os.path.join(to_path, wav_name), format='wav')
# music = wavfile.read(r"/Users/wjj/DataCenter/单词wav-1/莜蕾日语-第1课单词朗读.wav")
# wavfile.write('/Users/wjj/DataCenter/单词wav-1/莜蕾日语-第1课单词朗读-sub3.wav', 44100, music[1][120 * 44100:300 * 44100])
from utils.myjson import JsonUtil


class SoundNode:
    def __init__(self, index, word, start_s, end_s):
        self.word = word
        self.index = index
        self.start_s = start_s
        self.end_s = end_s

    def __lt__(self, other):
        return self.index < other.index


class SoundInfo:
    def __init__(self, sound_nodes, f_name, sound_date):
        self.sound_nodes = sound_nodes
        self.f_name = f_name
        self.sound_date = sound_date


def edit_sound():
    sn1 = SoundNode(0, "aa", 2, 6)
    sn2 = SoundNode(1, "bb", 6, 9)
    sns = [sn1, sn2]
    si = SoundInfo(sns, "a.wav", time.time())
    print(JsonUtil.obj2json_str(si, JsonUtil.MyEncoder))


if __name__ == '__main__':
    edit_sound()
