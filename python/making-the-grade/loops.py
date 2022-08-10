"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    rounded_scores = []

    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    failed_count = 0

    for score in student_scores:
        if score <= 40:
            failed_count += 1

    return failed_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    best_scores = []

    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)

    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    lower_threshold_scores = [41]
    letter_grade_range = round((highest-40) / 4)

    for index in range(3):
        lower_threshold = lower_threshold_scores[index] + letter_grade_range
        lower_threshold_scores.append(lower_threshold)

    return lower_threshold_scores


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order."""
    rankings = []

    for index, score in enumerate(student_scores):
        rank = index + 1
        name = student_names[index]
        rankings.append(f'{rank}. {name}: {score}')

    return rankings


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam."""
    for info in student_info:
        name = info[0]
        score = info[1]

        if score == 100:
            return [name, score]

    return []
