def calculate_result(correct_answers, total_questions):
    score = (correct_answers / total_questions) * 100
    return score

print("Score:", calculate_result(8,10))