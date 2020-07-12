from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    MAX_LOAD = 3

    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NoAgentFoundException

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) <= 0:
            raise NoAgentFoundException
        return agents[0]


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        least_agent = None
        tmp = self.MAX_LOAD
        for agent in agents:
            if agent.load < tmp:
                least_agent = agent
                tmp = agent.load
        if not least_agent:
            raise NoAgentFoundException
        return least_agent


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if not agents:
            raise NoAgentFoundException

        restrictions = sorted(ticket.restrictions)

        tmp = self.MAX_LOAD
        tmp_agent = None
        for agent in agents:
            if sorted(agent.skills) == restrictions and tmp > agent.load:
                tmp = agent.load
                tmp_agent = agent

        if tmp_agent:
            return tmp_agent
        else:
            raise NoAgentFoundException
