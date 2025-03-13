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

    # Find courses in the category page
    course_elements = soup.find_all("div", class_="courses-content")
    description_section = soup.find("div", class_="courses-overview")
    curriculum_section = soup.find("div", class_="courses-curriculum")


    if not course_elements:
        print("⚠️ No courses found! The website structure may have changed.")
        return []

    courses = []
    for course in course_elements,description_section:
        title = course.find("h3").text.strip() if course.find("h3") else "Unknown Title"
        description = course.find("p").text.strip() if course.find("p") else "No description available"
        link = BASE_URL + course.find("a")["href"] if course.find("a") else "#"
        full_description = description_section.find("p").text.strip() if description_section else "No detailed description available."
        curriculum = "\n".join([li.text.strip() for li in curriculum_section.find_all("li")]) if curriculum_section else "No curriculum provided."
        details_section = soup.find("div", class_="courses-details-info")
        if details_section:
            details_list = [li.text.strip() for li in details_section.find_all("li")]
            extra_details = "\n".join(details_list)
        else:
            extra_details = "No extra course details available."

        # ✅ Fetch full course details (description, curriculum, pricing, features)
        # ✅ Compile all details properly
        course_info = {
            "title": title,
            "description": description,
            "link": link,
            "description": full_description,
            "curriculum": curriculum,
            "extra_details": extra_details
        }

        courses.append(course_info)

    print(f"\n✅ Extracted {len(courses)} courses from Brainlox!\n")
    return courses

if __name__ == "__main__":
    all_courses = extract_courses()

    # ✅ Print a sample course to verify output
    if all_courses:
        print("\n🔍 Sample Extracted Course:")
        print(all_courses[0])  # Print first course for debugging
