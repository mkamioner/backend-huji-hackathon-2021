from contextlib import closing
from tempfile import gettempdir
import os
import sys
import subprocess

import boto3


def say_my_name(text, voice_id="Joey"):
    polly = boto3.session.Session(profile_name="prod").client("polly")
    response = polly.synthesize_speech(
        Engine="standard",
        LanguageCode="en-US",
        OutputFormat="mp3",
        Text=text,
        VoiceId=voice_id,
    )

    file_path = os.path.join(gettempdir(), "speech.mp3")

    with closing(response["AudioStream"]) as audio_stream:
        with open(file_path, "wb") as file:
            file.write(audio_stream.read())

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, file_path])
