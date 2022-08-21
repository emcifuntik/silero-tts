import os
import torch
from IPython.display import Audio
from time import perf_counter

torch.set_num_threads(2)

language = 'ru'
model_id = 'v3_1_ru'
device = torch.device('cpu')
sample_rate = 48000

local_file = 'v3_1_ru.pt'
if not os.path.isfile(local_file):
  torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt', local_file)

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

def getSpeakers():
  return model.speakers

def textToSpeech(speaker, text):
  t1_start = perf_counter()
  audio = model.apply_tts(text=text, speaker=speaker, sample_rate=sample_rate)
  t1_stop = perf_counter()
  print("Elapsed time:", t1_stop - t1_start)
  wavAudio = Audio(audio, rate=sample_rate)
  return wavAudio.data

def ssmlToSpeech(speaker, ssml):
  t1_start = perf_counter()
  audio = model.apply_tts(ssml_text=ssml, speaker=speaker, sample_rate=sample_rate)
  t1_stop = perf_counter()
  print("Elapsed time:", t1_stop - t1_start)
  wavAudio = Audio(audio, rate=sample_rate)
  return wavAudio.data
