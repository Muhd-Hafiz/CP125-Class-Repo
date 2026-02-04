def analyze_scores(score_records):
    all_scores = []
    
    for student_id, score in score_records:
        all_scores.append(score)
    
    highest = max(all_scores)
    
    average = sum(all_scores) / len(all_scores)
    
    above_average_count = 0
    for student_id, score in score_records:
        if score > average:
            above_average_count += 1
    
    return (highest, average, above_average_count)

scores = [("S1", 85), ("S2", 90), ("S3", 75)]
print(analyze_scores(scores))

