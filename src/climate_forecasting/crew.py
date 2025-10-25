from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool


@CrewBase
class ClimateForecasting():
    """ClimateForecasting crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def climate_researcher(self) -> Agent:
        return Agent(config=self.agents_config['climate_researcher'],verbose=True, tools=[SerperDevTool()])

    @agent
    def climate_reporting_agent(self) -> Agent:
        return Agent(config=self.agents_config['climate_reporting_agent'],verbose=True)


    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])
    
    @task
    def reporting_task(self) -> Task:
        return Task(config=self.tasks_config['reporting_task'])

    @crew
    def crew(self) -> Crew:
        """Creates the ClimateForecasting crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
            )
