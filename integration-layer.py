# integration_layer.py
class IntegrationLayer:
    def __init__(self, front_end_agent, back_end_agent, database_agent, devops_agent, project_management_agent):
        self.agents = {
            'front_end': front_end_agent,
            'back_end': back_end_agent,
            'database': database_agent,
            'devops': devops_agent,
            'project_management': project_management_agent
        }

    def process_task(self, task_type, task_data):
        if task_type in self.agents:
            return self.agents[task_type].process(task_data)
        else:
            raise ValueError("Unknown task type")
