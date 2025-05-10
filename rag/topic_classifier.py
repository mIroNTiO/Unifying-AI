def classify_topic(question: str) -> str:
    question = question.lower()

    if any(keyword in question for keyword in ["stoicism", "ethics", "virtue", "meaning", "philosophy"]):
        return "philosophy"
    elif any(keyword in question for keyword in ["evidence", "experiment", "physics", "biology", "science"]):
        return "science"
    elif any(keyword in question for keyword in ["fake news", "propaganda", "bias", "fact-check", "media"]):
        return "media_literacy"
    elif any(keyword in question for keyword in ["mind", "reason", "logic", "cognitive", "fallacy"]):
        return "critical_thinking"
    else:
        return "general"
