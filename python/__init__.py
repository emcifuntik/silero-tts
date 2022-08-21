from tts import textToSpeech, getSpeakers
import fileinput
import argparse

speakers = getSpeakers()

parser = argparse.ArgumentParser(description='Proceed text to speech.')
parser.add_argument('voice', type=str, help='TTS Voice [' + ' | '.join(speakers) + ']')
parser.add_argument('output', type=str, help='Path to output file')

args = parser.parse_args()

voice = args.voice
text = input()
outputPath = args.output

speech = textToSpeech(voice, text)
f = open(outputPath, "wb")
f.write(speech)
f.close()
