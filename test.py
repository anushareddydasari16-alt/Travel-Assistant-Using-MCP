from tools.tavily_tool import tavily_search

# res = tavily_search("best tourist attractions in Boston Massachusetts")
# print(res)

from tools.flight_tool import search_flights
# res = search_flights ("Plan a 7 days IND  trip from BOS")
# print(res)

from backend import run_travel_agent

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])