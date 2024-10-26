class Crew:
    def __init__(self, agents, tasks, process):
        self.agents = agents
        self.tasks = tasks
        self.process = process

    def kickoff(self, inputs):
        # Example logic for kicking off tasks
        results = {}
        for task in self.tasks:
            result = task(inputs)  # Assuming tasks are callable functions
            results[task.__name__] = result
        return results

class Process:
    sequential = 'sequential'
    parallel = 'parallel'