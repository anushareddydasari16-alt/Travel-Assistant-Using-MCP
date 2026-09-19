
## ✈️ AI Travel Assistant -A Multi-Agent Travel Planner With MCP (Model Context Protocol)

TripMate AI is an open-source AI-powered travel planning application that transforms a natural-language trip request into a practical travel plan with flight information, hotel recommendations, weather details, and a structured day-by-day itinerary.

This version extends the original LangGraph travel planner by introducing **Model Context Protocol (MCP)** integrations for external tools and services. The application combines LangGraph, LangChain, FastAPI, PostgreSQL, Groq, and MCP-based tooling to demonstrate how multiple AI agents can coordinate with external capabilities in a modular way.

## Why this project?

Planning a trip often requires switching between multiple websites and services for flights, hotels, weather, and itinerary planning. This makes the overall process fragmented and time-consuming.

TripMate AI simplifies this experience by coordinating specialized AI agents within a single workflow. The system includes:

- flight research,
- hotel and accommodation research,
- weather information,
- itinerary planning, and
- final response generation,

all coordinated through LangGraph with MCP-based tool integrations.

This project demonstrates how multi-agent AI systems can use MCP to connect external tools, APIs, and local services through a standardized interface.

## Features

- ✈️ Flight research using AviationStack through MCP
- 🏨 Hotel and accommodation recommendations using Tavily MCP search
- 🌤 Current weather and forecast information using a custom Weather MCP server
- 🧠 Multi-agent workflow orchestration with LangGraph
- 🔌 MCP-based integration for external tools and services
- 📝 Personalized and structured day-by-day travel itineraries
- 🌐 FastAPI backend with an interactive web interface
- 💾 Conversation and thread persistence using PostgreSQL
- ⚡ AI-generated travel recommendations powered by Groq
- 💬 Natural-language travel request processing

## Tech Stack

- Python 3.10+
- FastAPI
- Jinja2 + HTML/CSS/JavaScript frontend
- LangGraph
- LangChain
- Model Context Protocol (MCP)
- `langchain-mcp-adapters`
- Groq LLMs
- PostgreSQL
- Tavily API
- AviationStack API
- OpenWeather API

## State and MCP Integration

This version of TripMate AI extends the original LangGraph implementation by moving several external integrations into MCP-based tools.

The application currently uses:

- `Tavily` through a remote MCP endpoint at `https://mcp.tavily.com/mcp/`
- `AviationStack` through a local stdio MCP server using `uvx aviationstack-mcp`
- `Weather` through a custom local MCP server implemented in `custom_weather_mcp_server.py`

The MCP client configuration is maintained in `mcp_client.py`.

It provides helper functions for:

- `tavily_mcp_search`
- `aviation_mcp_call`
- `weather_mcp_search`
- `forecast_mcp_search`
- `extract_destination`

These MCP-backed functions are used by the specialized agents in `backend.py` to retrieve external information and generate the final travel plan.

## Project Structure

```text
.
├── app.py                       # FastAPI app entry point
├── backend.py                   # LangGraph multi-agent travel workflow
├── mcp_client.py                # MCP client and external tool configuration
├── custom_weather_mcp_server.py # Custom local Weather MCP server
├── requirements.txt             # Python dependencies
├── static/                      # Static frontend assets
├── templates/                   # HTML templates
└── tools/                       # Additional travel tool integrations
````

## Prerequisites

Before running the project locally, make sure you have:

* Python 3.10 or newer installed
* PostgreSQL running and accessible
* `uvx` installed and available for the AviationStack MCP server
* API keys for:

  * Groq
  * Tavily
  * AviationStack
  * OpenWeather

These services are used for AI-generated responses, flight information, hotel research, weather information, and persistent conversation state.

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
DEFAULT_ORIGIN_IATA=DAC
```

The `.env` file stores the credentials and configuration required by the application.

Make sure `.env` is included in `.gitignore` and is not committed to a public GitHub repository.

## Installation

Create a virtual environment and install the required dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Make sure `uvx` is available if you are using the AviationStack MCP integration.

You can verify it with:

```bash
uvx --version
```

## Running the App

Start the FastAPI server:

```bash
python app.py
```

Then open your browser at:

```text
http://127.0.0.1:8000/
```

From the web interface, enter a travel request describing your destination, trip duration, budget, and preferences.

TripMate AI will process the request through the multi-agent workflow and use MCP tools to gather travel-related information before generating the final response.

## Using MCP Tools

The application uses MCP behind the scenes, so no additional frontend setup is required.

The MCP configuration is defined in:

```text
mcp_client.py
```

The current MCP integrations include:

```text
Tavily MCP
    ├── tavily_search
    ├── tavily_extract
    ├── tavily_crawl
    ├── tavily_map
    └── tavily_research

AviationStack MCP
    └── Flight-related AviationStack tools

Weather MCP
    ├── get_current_weather
    └── get_forecast
```

The Weather MCP server is launched using the same Python environment as the main application.

The AviationStack MCP server is started through:

```bash
uvx aviationstack-mcp
```

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
2. The flight agent uses the AviationStack MCP integration to gather relevant flight information.
3. The hotel agent uses Tavily MCP search to identify accommodation and destination information.
4. The weather agent calls the custom Weather MCP server for current weather and forecast data.
5. The itinerary agent combines the available information into a practical day-by-day travel plan.
6. The final agent organizes the information into a clear, user-friendly response.
7. LangGraph coordinates the workflow while PostgreSQL maintains conversation state across requests.

## Contributing

Contributions are welcome. If you would like to improve the application, add additional MCP servers, integrate new travel services, enhance the user interface, or fix an issue:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Open a pull request

When contributing, keep changes focused and document any new dependencies, MCP servers, APIs, or environment variables introduced by your update.

## Acknowledgments

TripMate AI was developed as a practical implementation of a multi-agent AI system using LangGraph and Model Context Protocol integrations.

This version builds on the original LangGraph travel planner by introducing MCP-based tool communication for Tavily, AviationStack, and weather services.

The project demonstrates how LangGraph, LangChain, MCP, FastAPI, PostgreSQL, Groq, and external APIs can work together to build a modular and extensible real-world AI application.

```
