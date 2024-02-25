from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py

"""
Creating task cheat sheet:
    - Begin with the end in mind.  Idenify the specific outcome your tasks are aiming to achieve.
    - Beak down the outcome into actionable tasks, assigning each task to the apprropriate agent
    - Ensure tasks are descriptive, providing clear instructions and expected deliverables.
    
Goal:
    - Develop a detailed itineary, including city selection, attractions, and practical travel advice.
    
    Key Steps for Task Creation:
    1. Identify the Desired Outcome:  Define what success looks like for your projects
        - A detailed 7 day travel itenerary
        
    2. Task Breakdown: Divide the goal into smaller, managable tasks that the agents can execute
        - Itenerary Planning: develop a detailed plan for each day of the trip
        - City Selection: Analyze and pick the best cities to visit
        - Local Tour Guide - Find a local expert to provide insights and recommendations
        
    3. Assign tasks to agents: Match tasks with agents based on their roles and expertise

    
    4. Task Description template:
        - Use this temaplate as a guide to define each task for your crew
        - This template helps ensure that each task is clearly defined, actionable and aligned with specific results
        
Template:
---------
    def [task_name](self, agent, [parameters])
        return Task(description=dedent(f'''
        **Task**: [Provide a concise name of summary of the task.]
        **Description**: [Detailed description of what the agent is expected to do, including actionaable steps and examples.]
        
        **Parameters**:
        - [Parameter 1]: [Description]
        - [Parameter 2]: [Description]
        
        **Note**: [Optional section for incentives or encouragement for high-quality work.  This can include tips, bonuses, etc.]
        '''), agent=agent)
"""

class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 7-Day Travel Itinerary
            **Description**: Expand the city guide into a full 7-day travel itinerary with detailed per-day plans, 
            including weather forecasts, places to eat, packing suggestions, and a budget breakdown.  You MUST suggest
            actual places to visit, actual hotels to stay, and actual restaurants to go to.  This itinerary should cover all
            aspects of the trip from arrival to departure, integrating the city guide information with practical 
            travel logistics.
            
            **Parameters**:
           - City: {city}
           - Trip Date: {travel_dates}
           - Travel Interests: {interests}
            
            **Note**: {self.__tip_section}
        """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the best city for the trip
            **Description**: Analyze and select the best city for the trip based on specific criteria such as weather
            patterns, seasonal events, and travel costs.  This task involves comparing multiple cities, considering
            factors like current weather conditions, upcoming cultural or seasonal events and overall travel expenses.
            Your final answer must be a detailed report on the chosen city, including actual flight costs, weather forecasts
            and attractions.
            
            **Parameters**:
           - Origin: {origin}
           - Cities: {cities}
           - Interests: {interests}
           - Travel Date: {travel_dates}
            
            **Note**: {self.__tip_section}
        """
            ),
            agent=agent,
        )
    
    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Gather In-depth City Guide Information
            **Description**: Compile and ind-depth guide for the selected city, gathering information aabout
                key attactions, local customers, special events, and daily activity recommendations.  
                This guide should provide a thorough overview of what the city has to offer, including 
                hidden gems, culture hotspots, must-visit landmarks, weather forecasts and high-level 
                cost estimates. 
            
            **Parameters**:
           - Cities: {city}
           - Interestes: {interests}
           - Travel Date: {travel_dates}
            
            **Note**: {self.__tip_section}
        """
            ),
            agent=agent,
        )