# fine_tune_model.py
from datasets import load_dataset
from transformers import Trainer, TrainingArguments

def fine_tune_model(model, tokenizer, dataset_path):
    dataset = load_dataset('json', data_files=dataset_path)
    
    def preprocess_function(examples):
        return tokenizer(examples['input'], truncation=True, padding=True)

    tokenized_datasets = dataset.map(preprocess_function, batched=True)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets['train'],
        eval_dataset=tokenized_datasets['validation']
    )

    trainer.train()
