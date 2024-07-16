import unittest
from transformers import AutoModelForCausalLM, AutoTokenizer
from agents.front_end_agent import FrontEndAgent

class TestFrontEndAgent(unittest.TestCase):
    def setUp(self):
        self.tokenizer = AutoTokenizer.from_pretrained("gpt-3")
        self.model = AutoModelForCausalLM.from_pretrained("gpt-3")
        self.agent = FrontEndAgent(self.model, self.tokenizer)

    def test_process(self):
        task_data = {"task": "Create a responsive HTML layout with CSS"}
        result = self.agent.process(task_data)
        self.assertIn("<html>", result)

if __name__ == "__main__":
    unittest.main()
