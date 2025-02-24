from aif360.metrics import ClassificationMetric

class BiasDetector:
    def audit_dataset(self, dataset):
        metric = ClassificationMetric(
            dataset, 
            dataset,
            unprivileged_groups=[{"sex": 0}],
            privileged_groups=[{"sex": 1}]
        )
        return {
            "disparate_impact": metric.disparate_impact(),
            "statistical_parity": metric.statistical_parity_difference(),
            "threshold": 0.8  # SDG 5.1 threshold
        }

    def audit_model(self, model, test_data):
        predictions = model.predict(test_data.features)
        return self.audit_dataset(test_data.copy(predicted_labels=predictions))