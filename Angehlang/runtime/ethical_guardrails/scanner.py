def scan_security(code):  
    from bandit import core  
    results = core.scan(code)  
    return [r for r in results if r.severity > core.ISSUE_SEVERITY.MEDIUM]  

def check_bias(dataset):  
    from aif360 import metrics  
    return metrics.DisparateImpactRatio().compute(dataset)  