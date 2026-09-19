
## ✈️ AI Travel Assistant -A Multi-Agent Travel Planner With LangGraph

TripMate AI is an open-source AI-powered travel planning application that transforms a natural-language travel request into a complete and practical trip plan. It provides flight information, hotel recommendations, and a structured day-by-day itinerary through a coordinated multi-agent workflow.

The application is built using LangGraph, LangChain, FastAPI, PostgreSQL, and external travel APIs to demonstrate how multiple AI agents can work together to solve a real-world planning task.

## Why this project?

Planning a trip often requires searching across multiple websites for flights, hotels, attractions, and itinerary ideas. This can make the planning process time-consuming and fragmented.

TripMate AI simplifies this process by bringing multiple travel-planning tasks into a single AI-powered experience. The system uses specialized agents for:

- flight research,
- hotel and accommodation research,
- itinerary planning, and
- final response generation,

with all agents coordinated through a LangGraph workflow.

This project demonstrates how multi-agent AI systems can combine external APIs, web search, persistent memory, and large language models to produce useful real-world results.

## Features

- ✈️ Flight research using AviationStack
- 🏨 Hotel and accommodation recommendations using Tavily search
- 🧠 Multi-agent workflow orchestration with LangGraph
- 📝 Personalized and structured day-by-day travel itineraries
- 🌐 FastAPI backend with an interactive web interface
- 💾 Conversation and thread persistence using PostgreSQL
- ⚡ AI-generated travel recommendations powered by Groq
- 🔄 Specialized agents working together within a single workflow
- 💬 Natural-language travel request processing

## Tech Stack

- Python 3.10+
- FastAPI
- Jinja2 + HTML/CSS/JavaScript frontend
- LangGraph
- LangChain
- Groq LLMs
- PostgreSQL
- Tavily API
- AviationStack API

## Project Structure

```text
.
├── app.py                # FastAPI app entry point
├── backend.py            # LangGraph travel workflow
├── requirements.txt      # Python dependencies
├── static/               # Static frontend assets
├── templates/            # HTML templates
└── tools/                # Flight and web search integrations
````

## Prerequisites

Before running the project locally, make sure you have:

* Python 3.10 or newer installed
* PostgreSQL running and accessible
* API keys for:

  * Groq
  * Tavily
  * AviationStack

These services are used by the application for AI-generated responses, travel research, flight information, and persistent conversation storage.

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db
GROQ_API_KEY=your_groq_api_key
AVIATION_API_KEY=your_aviation_api_key
TAVILY_API_KEY=your_tavily_api_key
DEFAULT_ORIGIN_IATA=USA
```

The `.env` file stores the credentials and configuration required by the application. Make sure this file is not committed to a public GitHub repository.

## Installation

Create a virtual environment and install the required Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Once the dependencies are installed, confirm that PostgreSQL is available and that all required API keys have been added to the `.env` file.

## Running the App

Start the FastAPI server:

```bash
python app.py
```

Then open your browser at:

```text
http://127.0.0.1:8000/
```

From the web interface, enter a travel request describing your destination, trip duration, budget, and preferences. TripMate AI will process the request through the multi-agent workflow and generate a personalized travel plan.

## API Endpoints

* `GET /health` - Checks whether the application service is running
* `POST /api/travel` - Submits a travel request to the multi-agent workflow

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

## How the Workflow Works

1. The user submits a natural-language travel request through the web interface or API.
2. The flight agent gathers relevant flight-related information using the configured travel data source.
3. The hotel agent uses web search to identify suitable accommodation options and travel information.
4. The itinerary agent combines the available information into a practical day-by-day travel plan.
5. The final agent organizes and formats the information into a clear, user-friendly response.
6. LangGraph coordinates the agent workflow while PostgreSQL maintains conversation state across requests.

## Contributing

Contributions are welcome. If you would like to improve the application, add new travel capabilities, integrate additional APIs, enhance the user interface, or fix an issue:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Open a pull request

When contributing, keep changes focused and document any new dependencies, APIs, or environment variables introduced by your update.

## Acknowledgments

TripMate AI was developed as a practical implementation of a multi-agent AI system using LangGraph and modern LLM technologies.

The project combines LangGraph, LangChain, FastAPI, PostgreSQL, Groq, Tavily, and AviationStack to demonstrate how AI agents, external tools, APIs, and persistent memory can work together in a real-world travel-planning application.

```
```
