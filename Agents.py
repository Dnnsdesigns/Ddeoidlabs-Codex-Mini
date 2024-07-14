from agents.front_end_agent import FrontEndAgent
from agents.back_end_agent import BackEndAgent
from agents.database_agent import DatabaseAgent
from agents.devops_agent import DevOpsAgent
from agents.project_management_agent import ProjectManagementAgent
from integration.integration_layer import IntegrationLayer

front_end_agent = FrontEndAgent(model, tokenizer)
back_end_agent = BackEndAgent(model, tokenizer)
database_agent = DatabaseAgent(model, tokenizer)
devops_agent = DevOpsAgent(model, tokenizer)
project_management_agent = ProjectManagementAgent(model, tokenizer)
integration_layer = IntegrationLayer(front_end_agent, back_end_agent, database_agent, devops_agent, project_management_agent)

task_data = {'task': 'Create a responsive website layout'}
result = integration_layer.process_task('front_end', task_data)
print(result)
