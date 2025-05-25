from utils import clean_text, extract_keywords

def get_course_recommendations(user_input, course_data):
    user_input_clean = clean_text(user_input)

    # Build a set of all course tags
    all_keywords = set()
    for course in course_data:
        all_keywords.update([clean_text(tag) for tag in course.get("tags", [])])

    matched_keywords = extract_keywords(user_input_clean, all_keywords)

    matched_courses = []
    for course in course_data:
        tags = [clean_text(tag) for tag in course.get("tags", [])]
        if any(tag in matched_keywords for tag in tags):
            matched_courses.append(course)

    if not matched_courses:
        return "Sorry, I couldn't find any matching courses. Can you try rephrasing or choosing a different topic?"

    response = "Here are some courses I found for you:\n\n"
    for i, course in enumerate(matched_courses[:5], start=1):
        response += f"{i}. [{course['title']}]({course['link']}) – *{course['platform']}*\n"

    return response