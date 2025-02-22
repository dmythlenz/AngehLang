from transformers import AutoModelForSequenceClassification
from sklearn.metrics import fairness_metrics
import torch
import os

class EthicalAutoML:
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "microsoft/codebert-base",
            num_labels=2
        )
        self.max_model_size = 5 * 1024 * 1024  # 5MB limit
        self.fairness_threshold = 0.9
        
    def validate_model(self, model, test_data):
        # Check model size
        torch.save(model.state_dict(), "temp.pt")
        model_size = os.path.getsize("temp.pt")
        if model_size > self.max_model_size:
            return False
            
        # Check fairness metrics
        predictions = model(test_data)
        fairness_score = fairness_metrics.equal_opportunity_difference(
            test_data.labels, predictions
        )
        return fairness_score >= self.fairness_threshold 