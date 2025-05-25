import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

def extract_keywords(text, keywords):
    text = clean_text(text)
    return [kw for kw in keywords if kw in text]

def filter_courses_by_level(course_list, level="beginner"):
    level = level.lower()
    return [course for course in course_list if level in " ".join(course.get("tags", [])).lower()]