""" 
This simple python script uses the pydub library to combine intro, outro, and recorded segments to do simple batch edits to episodes of a program or podcast.

For pydub docs see: https://github.com/jiaaro/pydub
ffmpeg is also a required dependency for this library.
"""

from pydub import AudioSegment
import os

# Load intro and outro files
intro = AudioSegment.from_file("path/to/intro.wav", format="wav")
outro = AudioSegment.from_file("path/to/outro.wav", format="wav")

# Set paths to recorded segments and output folder
recordings_folder = "path/to/recorded_segments"
processed_folder = "path/to/output_folder"

# Iterate through files in recordings folder
for file_name in os.listdir(recordings_folder):
    # Assumes recordings are .mp3 files. Change if needed
    if file_name.endswith(".mp3"):
        recording_path = os.path.join(recordings_folder, file_name)
        # I set start_second to 0.2 seconds to trim out silence in the beginning of the recording
        recording = AudioSegment.from_file(recording_path, format="mp3", start_second=0.2)

        # Calculate duration of intro, recording, and outro in milliseconds. I set episode length to total_length minus 13500ms to account for intro and outro overlapping
        outro_length_in_ms = outro.duration_seconds * 1000
        total_length = intro.duration_seconds + recording.duration_seconds + outro.duration_seconds
        total_length_in_ms = total_length * 1000
        episode_length = total_length_in_ms - 13500

        # Create a silent canvas equal to episode length on which to add intro, recording, and outro
        canvas = AudioSegment.silent(duration=episode_length)

        # Add intro, recording, and outro to canvas. In my case the intro and outro files are already faded so no crossfade is needed, I simply overlay one file on top of the other.
        add_intro = canvas.overlay(intro, position=0)
        # Recording is added 44 seconds into the canvas because my intro is 48 seconds long and i want 4 seconds of overlap. You could also set it to start at "intro_length_in_ms - 4000" or whatever overlap you desire.
        add_recording = add_intro.overlay(recording, position=44000)
        add_outro = add_recording.overlay(outro, position=episode_length - outro_length_in_ms)

        # Apply fade out at the end of the combined audio file
        episode = add_outro.fade_out(500)

        # Set output filename and path
        output_filename = file_name
        output_path = os.path.join(processed_folder, output_filename)

        # Export the final episode to the output path. You can change the bitrate and tags to suit your needs.
        episode.export(output_path, format="mp3", bitrate="320k", tags={"artist": "artist", "title": "title"})
