import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

#from langchain.tools import DuckDuckGoSearchRun

#search_tool = DuckDuckGoSearchRun()


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests
        
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_expert_agent = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary_task = tasks.plan_itinerary(
            expert_travel_agent, 
            self.cities,
            self.date_range,
            self.interests
        )
        
        identify_city_task = tasks.identify_city(
            city_expert_agent, 
            self.origin,
            self.cities,
            self.interests,
            self.date_range
            
        )
        
        gather_city_info_task = tasks.gather_city_info(
            local_tour_guide, 
            self.cities,
            self.date_range,
            self.interests
        )
        
        

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, 
                    city_expert_agent, 
                    local_tour_guide],
            tasks=[plan_itinerary_task, 
                   identify_city_task, 
                   gather_city_info_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Ferow's Trip Pllaner Crew")
    print("-------------------------------")
    origin = input(
        dedent("""
      From where will you be traveling from?
    """))
    
    cities = input(
        dedent("""
       What cities are you are are interested in visiting?
    """))
    
    date_range = input(
        dedent("""
       What date range are you are are interested in traveling?
    """))
    
    interests = input(
        dedent("""
       What are some of your high level interests and hobbies?
    """))

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is your custom trip plan:")
    print("########################\n")
    print(result)
