
from ibm_watson import SpeechToTextV1

import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(Key)
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(Url)

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

file_path_ = 'E:\audio.wav'

class Main():

    def seperation(file_path, ff):

        with open(file_path,'rb') as audio_file:
            #audio_source = AudioSource(audio_file)
            speech_recognition_results = speech_to_text.recognize(#.recognize can also be used  
                audio=audio_file,     #audio_source,
                content_type= ff,  #'audio/wav',
                recognize_callback=myRecognizeCallback,
                model='en-US_BroadbandModel',
                speaker_labels = True, timestamps = True).get_result() #'audio/flac'
            transcript = ''
            for chunks in speech_recognition_results['results']:
                if 'alternatives' in chunks.keys():
                    alternatives = chunks['alternatives'][0]
                    if 'transcript' in alternatives:
                        transcript = transcript + \
                            alternatives['transcript']
                        transcript += '\n'
            print(transcript)

            speakerLabels = speech_recognition_results["speaker_labels"]
            #print("Done Processing ...\n")
            #print(speakerLabels)
            extractedData = []
            
            for chunks in speech_recognition_results['results']:
                if 'alternatives' in chunks.keys():
                    alternatives = chunks['alternatives'][0]
                    if 'timestamps' in alternatives:
                        for i in alternatives['timestamps']:          
                            mydict = {'from': i[:][1], 'transcript': i[:][0]
                                , 'to': i[:][2]} #.replace("%HESITATION", "")
                            extractedData.append(mydict)
                        extractedData.append({'newline': '\n'})
            
            finalOutput = []
            
            for i in extractedData:
                if 'newline' in i.keys():
                        finalOutput.append({'newline': '\n'})
                else:

                    for j in speakerLabels:          
                        if i["from"] == j["from"] and i["to"] == j["to"]:
                            mydictTemp = {"from": i["from"],
                                        "to": i["to"],
                                        "transcript": i["transcript"],
                                        "speaker": j["speaker"],
                                        "confidence": j["confidence"],
                                        "final": j["final"],
                                        }
                            finalOutput.append(mydictTemp)
        return finalOutput
                
