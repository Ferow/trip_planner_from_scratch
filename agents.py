from crewai import Agent
from textwrap import dedent
from Tools.search_tools import SearchTools
from Tools.calculator_tools import CalculatorTools
from openai import OpenAI
"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""

class TravelAgents:
    def __init__(self):
        # Point to the local server
        self.OpenAIClient = OpenAI(base_url="http://localhost:3280/v1", api_key="not-needed")
        #self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        #self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        #self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""A world traveler with 20 years of experience in the travel industry. 
                             Expert and creating plans and logistics for traveling the world."""),
            goal=dedent(f"""Create a 7-day travel itinerary with detailed per-day plans, 
                        including budget, packing suggestions, and safety tips."""),
            tools=[
                SearchTools.search_interet,
                CalculatorTools.calculate
                ],
            verbose=True,
            llm=self.OpenAIClient,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""A city selection expert with 10 years of experience in the travel industry.
                             Expert in finding the best cities to travel to based on client preferences.
                             """),
            goal=dedent(f"""Find the best cities to travel to based on 
                             weather, budghet, season, prices and client preferences.
                        """),
             tools=[
                SearchTools.search_interet
                ],
            verbose=True,
            llm=self.OpenAIClient,
        )
        
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Expert of the city who has extensive knowledge the history, culture, and best places to visit.
                             """),
            goal=dedent(f"""Provide the BEST insights of the selected city to the client.
                        """),
             tools=[
                SearchTools.search_interet
                ],
            verbose=True,
            llm=self.OpenAIClient,
        )
