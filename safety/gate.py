def input_safe(text: str) -> bool:
    if not text or len(text) > 2000:
        return False
    return True


def risk_safe(risk_score: float, threshold: float) -> bool:
    return risk_score <= threshold
