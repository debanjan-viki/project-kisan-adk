# Multi-Agent AI Chatbot Backend

This project is a backend service for a multi-agent AI chatbot, built using [FastAPI](https://fastapi.tiangolo.com/) and integrated with Google ADK for advanced conversational capabilities.

## Features

- Multi-agent architecture for handling diverse conversational tasks
- FastAPI-powered RESTful API for efficient request handling
- Google ADK integration for robust AI and NLP features
- Scalable and modular codebase

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Google ADK SDK and credentials
- [uv](https://github.com/astral-sh/uv) (package manager)

## Installation

```bash
git clone https://github.com/your-org/project-kisan-adk.git
cd project-kisan-adk
```

## Configuration

1. Set up your Google ADK credentials as environment variables or in a `.env` file and add the following:
    GOOGLE_GENAI_USE_VERTEXAI=true
    GOOGLE_CLOUD_PROJECT={your-project-id}
    GOOGLE_CLOUD_LOCATION={your-project-location}
    PORT={your-port-number} (Default 8000)

## Running the Server

```bash
uv run main.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `POST /chat/`: Send a message and receive a response from the chatbot multi-agent system.

## License

MIT License

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google ADK](https://developers.google.com/adk)
- [uv](https://github.com/astral-sh/uv)
