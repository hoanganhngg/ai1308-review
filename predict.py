THRESHOLD = 0.5


def predict(scores):
    """Nhãn có điểm cao nhất; trả về "unknown" khi độ tin cậy < THRESHOLD."""
    label = max(scores, key=scores.get)
    if scores[label] < THRESHOLD:
        return "unknown"
    return label
