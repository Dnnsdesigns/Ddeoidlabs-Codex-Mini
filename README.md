# Ddroidlabs-Codex-Mini
small agentic model designed as a coding assistant

# Mixture of Agents Model (MAM) - Full-Stack Development Team

## Overview

The Mixture of Agents Model (MAM) is an AI-driven full-stack development team that integrates specialized agents for front-end development, back-end development, database management, DevOps, and project management. This unified model leverages a pretrained transformer and fine-tuned datasets to handle a variety of software development tasks efficiently.

## Folder Structure

```
mixture_of_agents/
├── app.py
├── colab_notebook.ipynb
├── dataset/
│   └── code_finetune_dataset.json
├── agents/
│   ├── front_end_agent.py
│   ├── back_end_agent.py
│   ├── database_agent.py
│   ├── devops_agent.py
│   └── project_management_agent.py
├── integration/
│   └── integration_layer.py
└── model/
    ├── load_pretrained_model.py
    └── fine_tune_model.py
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Flask
- Google Colab account (for running the notebook)
- Libraries: `transformers`, `datasets`, `numpy`, `pandas`

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/mixture_of_agents.git
   cd mixture_of_agents
   ```

2. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Upload to Google Drive:**
   - Upload the `mixture_of_agents` folder to your Google Drive.

4. **Open Colab Notebook:**
   - Open `colab_notebook.ipynb` in Google Colab.

### Running the Model

1. **Mount Google Drive:**
   - Mount your Google Drive in Colab by running the first cell of the notebook:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

2. **Install Necessary Packages:**
   - Install the required packages in the Colab environment:
     ```python
     !pip install transformers datasets
     ```

3. **Load and Fine-Tune the Model:**
   - Follow the steps in the Colab notebook to load the pretrained model and fine-tune it using the provided dataset:
     ```python
     from model.load_pretrained_model import load_model_and_tokenizer
     model, tokenizer = load_model_and_tokenizer()

     from model.fine_tune_model import fine_tune_model
     fine_tune_model(model, tokenizer, '/content/drive/MyDrive/mixture_of_agents/dataset/code_finetune_dataset.json')
     ```

4. **Initialize and Use the Agents:**
   - Initialize the agents and use the integration layer to process tasks:
     ```python
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
     ```

### Running the Web Application

1. **Ensure All Agent Files and Integration Layer Are Available:**
   - Make sure the `agents` and `integration` directories with their respective Python files (`front_end_agent.py`, `back_end_agent.py`, `database_agent.py`, `devops_agent.py`, `project_management_agent.py`, and `integration_layer.py`) are in the same directory as `app.py`.

2. **Run the Application:**
   - Execute the `app.py` script to start the Flask web server:
     ```bash
     python app.py
     ```

3. **Using the API:**
   - Open your web browser and navigate to `http://127.0.0.1:5000/` to see the welcome message.
   - Use a tool like `curl` or Postman to send a POST request to the `/process` endpoint with JSON payload to process tasks.

### Example POST Request
You can use the following example JSON payload to test the `/process` endpoint:

```json
{
  "task_type": "front_end",
  "task_data": {
    "task": "Create a responsive website layout"
  }
}
```

**Using `curl`:**
```bash
curl -X POST http://127.0.0.1:5000/process -H "Content-Type: application/json" -d '{"task_type": "front_end", "task_data": {"task": "Create a responsive website layout"}}'
```

## Agent Descriptions

### Front-End Agent
- **File:** `agents/front_end_agent.py`
- **Responsibilities:** UI/UX design, HTML, CSS, JavaScript frameworks (React, Vue).

### Back-End Agent
- **File:** `agents/back_end_agent.py`
- **Responsibilities:** Server-side logic, API development, frameworks like Node.js, Django.

### Database Agent
- **File:** `agents/database_agent.py`
- **Responsibilities:** Database design, query optimization, data migration.

### DevOps Agent
- **File:** `agents/devops_agent.py`
- **Responsibilities:** CI/CD pipelines, server management, deployment automation.

### Project Management Agent
- **File:** `agents/project_management_agent.py`
- **Responsibilities:** Requirement gathering, task management, progress tracking.

### Integration Layer
- **File:** `integration/integration_layer.py`
- **Responsibilities:** Ensures seamless communication and coordination between agents.

## Fine-Tuning Dataset

### Dataset File
- **File:** `dataset/code_finetune_dataset.json`
- **Description:** Contains examples of various coding tasks to fine-tune the model for development-related tasks.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's style guidelines and includes appropriate tests.

## License

This project is licensed under the apache-2.0  License.

## Contact

For any questions or issues, please open an issue on GitHub or contact the repository maintainer.
