from email.mime import audio
import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename:str):
    chunk = 1024 # number of bytes to read
    wf = wave.open(filename,'rb') # open file as binary
    pa = pyaudio.PyAudio() # instantiate pyaudio class

    # create a PyAudio data stream which we can write the binary data to 
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    print(f'Writing datastream...')
    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    print(f'Done writing stream.')
    stream.close()
    pa.terminate()


def initSpeech():
    print(f'Listening...')
    play_audio(filename)

if __name__ == "__main__":
    r = sr.Recognizer()
    print(f'Starting the code...')
    filename = "./audio/promise-616.wav"
    filename_end = "piece-of-cake-611.wav"
    # play_audio(filename)

    with sr.Microphone() as source:
        print("Say something...")
        audio=r.listen(source)
    
    print("Done listening to you boi.")
    # play_audio(filename_end)

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("couldn't understand you")

    print("--> Your commands")
    print(command)



