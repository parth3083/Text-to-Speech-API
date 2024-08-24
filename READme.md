# Project Description: Text-to-Speech API

## Overview
The Text-to-Speech API is a service that provides text translation and speech synthesis capabilities. It is designed to convert input text into speech in various languages, allowing users to receive spoken translations of their text in their desired language. This API is ideal for applications requiring real-time language translation and speech conversion functionalities.

## API 
https://text-to-speech-api-136n.onrender.com/

## Key Features
- **Text Translation**: Converts input text into a specified target language.
- **Speech Synthesis**: Generates speech from the translated text using text-to-speech (TTS) technology.
- **Multi-Language Support**: Supports a variety of languages for translation and speech synthesis.
- **Asynchronous Processing**: Provides feedback that the translation and speech synthesis process is in progress.

## Technical Stack
- **Backend**: Node.js with Express.js
- **Python**: Used for handling text-to-speech and translation functionalities
- **Deployment**: Render.com for hosting the API
- **Integration**: Postman for testing and load simulation

## Endpoints
- **POST /translate**:
  - **Description**: Receives text and target language, processes the text to generate speech in the specified language.
  - **Request Body**:
    ```json
    {
      "text": "String of text to be translated and converted to speech",
      "language": "Language code (e.g., 'en' for English, 'gu' for Gujarati)"
    }
    ```
  - **Response**:
    - **Success**: `"Translation and speech conversion in progress."`
    - **Error**: Error message if something goes wrong.


### Prerequisites
- **Node.js**: Ensure Node.js is installed on your system. You can download it from [nodejs.org](https://nodejs.org/).
- **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

