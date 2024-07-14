from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from agents.front_end_agent import FrontEndAgent
from agents.back_end_agent import BackEndAgent
from agents.database_agent import DatabaseAgent
from agents.devops_agent import DevOpsAgent
from agents.project_management_agent import ProjectManagementAgent
from integration.integration_layer import IntegrationLayer

app = Flask(__name__)

# Load the model and tokenizer
model_name = "gpt-3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize agents
front_end_agent = FrontEndAgent(model, tokenizer)
back_end_agent = BackEndAgent(model, tokenizer)
database_agent = DatabaseAgent(model, tokenizer)
devops_agent = DevOpsAgent(model, tokenizer)
project_management_agent = ProjectManagementAgent(model, tokenizer)
integration_layer = IntegrationLayer(front_end_agent, back_end_agent, database_agent, devops_agent, project_management_agent)

@app.route('/')
def home():
    return "Welcome to the Mixture of Agents Model API!"

@app.route('/process', methods=['POST'])
def process_task():
    data = request.json
    task_type = data.get('task_type')
    task_data = data.get('task_data')
    
    if not task_type or not task_data:
        return jsonify({"error": "task_type and task_data are required"}), 400

    try:
        result = integration_layer.process_task(task_type, task_data)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
