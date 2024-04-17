# Audio Segment Combining Script

This script combines intro, outro, and recorded segments to batch edit episodes of a program or podcast.

## Requirements

- Python 3.x
- pydub library for audio manipulation
- ffmpeg
- Audio files for intro and outro
- Recorded segments in a folder

## Usage

1. **Set Paths:** Set the paths to the intro, outro, folder containing recorded segments, and output folder in the script.

2. **Run Script:** Run the script to combine the segments with the intro and outro, adding metadata.

## Script Overview

- The script loads intro and outro audio files.
- It iterates over the recorded segments in the specified folder.
- For each file, the intro, recording, and outro are combined with appropriate timing adjustments.
- The combined episode is exported to the output folder with metadata including artist name and episode title.

## Notes

- Ensure that the intro and outro files are correctly formatted and have valid durations.
- The script expects the recorded segments to be in the MP3 format.
- Metadata tags for artist name and episode title are added to each combined episode.

