import requests
from bs4 import BeautifulSoup

BRAINLOX_COURSE_LIST_URL = "https://brainlox.com/courses/category/technical"
BASE_URL = "https://brainlox.com"

def extract_courses():
    print("🔍 Fetching Brainlox course list...")
    response = requests.get(BRAINLOX_COURSE_LIST_URL, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code != 200:
        print(f"❌ Failed to fetch course list! Status Code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # ✅ Find all sections together
    course_elements = soup.find_all("div", class_="courses-content")

    if not course_elements:
        print("⚠️ No courses found! The website structure may have changed.")
        return []

    courses = []
    for course in course_elements:
        # ✅ Extract Title, Description, and Link
        title = course.find("h3").text.strip() if course.find("h3") else "Unknown Title"
        description = course.find("p").text.strip() if course.find("p") else "No description available"
        link = BASE_URL + course.find("a")["href"] if course.find("a") else "#"

        # ✅ Fetch full course details from the course page
        response = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code != 200:
            print(f"⚠️ Failed to fetch details for {link}")
            continue

        course_soup = BeautifulSoup(response.text, "html.parser")

        # ✅ Extract all sections at once
        overview_section = course_soup.find("div", class_="courses-overview")
        curriculum_section = course_soup.find("div", class_="courses-curriculum")
        details_section = course_soup.find("div", class_="courses-details-info")

        # ✅ Extract Overview
        overview = overview_section.find("p").text.strip() if overview_section else "No detailed description available."

        # ✅ Extract Curriculum (Fix: Ensure `find_all("li")` works properly)
        curriculum = ""
        if curriculum_section:
            curriculum_items = curriculum_section.find_all("li")
            if curriculum_items:
                for i, item in enumerate(curriculum_items, start=1):
                    curriculum += f"✅ **Session {i}:** {item.text.strip()}\n"
            else:
                curriculum = "No curriculum found in list."
        else:
            curriculum = "No curriculum provided."

        # ✅ Extract Additional Course Details (Fix: Handle missing details properly)
        extra_details = ""
        if details_section:
            detail_items = details_section.find_all("li")
            if detail_items:
                for detail in detail_items:
                    extra_details += f"- {detail.text.strip()}\n"
            else:
                extra_details = "No extra course details found."
        else:
            extra_details = "No extra course details available."

        # ✅ Format everything properly
        formatted_details = f"""
📌 **\nCourse Title:\n** {title}

📖 **Description:**  
{description}

🔗 **\nCourse Link:\n** {link}  

📜 **\nCourse Overview:\n**  
{overview}

📚 **\nCurriculum:\n**  
{curriculum}

💡 **\nAdditional Details:\n**  
{extra_details}
"""

        # ✅ Append formatted details
        courses.append({
            "title": title,
            "description": formatted_details
        })

    print(f"\n✅ Extracted {len(courses)} courses from Brainlox!\n")
    return courses

if __name__ == "__main__":
    all_courses = extract_courses()

    # ✅ Print a sample course to verify output
    if all_courses:
        print("\n🔍 Sample Extracted Course:")
        print(all_courses[0]["description"])  # Print formatted response for debugging
