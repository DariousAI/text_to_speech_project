# Text-to-Speech Project

## Project Overview
This project is a simple Text-to-Speech (TTS) application built with Python. It takes a given text input and converts it into a speech audio file using the Google Text-to-Speech (`gTTS`) library. The generated audio file can then be played back, providing a spoken version of the input text.

## Features
- Converts text into speech using Google Text-to-Speech (`gTTS`).
- Saves the speech as an MP3 file.
- Plays the generated MP3 audio using the `playsound` library.

## Requirements
To run this project, you need to have the following installed:
- Python 3.x
- `gtts` library
- `playsound` library

To install the required libraries, run:
```sh
pip install gtts
pip install playsound
```

## Project Structure
```
text_to_speech_project/
│
├── text_to_speech.py       # Main Python script for TTS functionality
└── audio/                  # Folder to store generated audio files
    └── output.mp3          # Output audio file (created when the script runs)
```

## Usage
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/YourUsername/text_to_speech_project.git
   ```

2. Navigate to the project directory:
   ```sh
   cd text_to_speech_project
   ```

3. Run the Python script:
   ```sh
   python text_to_speech.py
   ```
   This will generate an audio file (`output.mp3`) in the `audio/` folder and play it.

## How It Works
1. The script uses the `gTTS` library to convert the specified text into speech.
2. The generated audio is saved as an MP3 file in the `audio/` folder.
3. The `playsound` library is then used to play the generated audio.

## Customizing the Text
You can change the text that is converted to speech by modifying the `text` variable in `text_to_speech.py`:
```python
text = "Your custom text here."
```

## Contributing
Feel free to fork this repository and make your own changes. Pull requests are welcome if you have improvements to suggest.

## License
This project is open source and available under the [MIT License](LICENSE).

