import re
import time
from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import pandas as pd


@dataclass
class Vacancy:
    title: str
    company: str = None
    experience_years: int = None
    salary: int = None
    english_level: str = None
    skills: [str] = None


SKILLS = [
    "Python", "WSL", "SQL", "REST", "API", "Docker", "Linux", "Django",
    "Pandas", "PostgreSQL", "Artificial Learning", "Js", "Machine Learning",
    "React", "SQLAlchemy", "OOP", "Flask", "NoSQL", "networking", "HTML",
    "CSS", "DRF", "FastAPI", "FullStack", "asyncio", "GraphQL", "algorithms",
    "MongoDB", "microservice", "Tableau", "Typescript", "ORM", "Git",
    "GitHub", "Kafka", "RabbitMQ", "SOLID"
]


ENGLISH_LEVELS = [
    "Beginner", "Pre-Intermediate", "Intermediate",
    "Intermediate-Upper", "Upper-Intermediate"
]


# Step 1: Obtain links from common soup to detailed pages using BeautifulSoup
base_url = "https://djinni.co/jobs/?primary_keyword=Python"

try:
    response = requests.get(base_url)
    response.raise_for_status()
    page = response.content
    soup = BeautifulSoup(page, "html.parser")

    vacancies_links = []
    for vacancy_div in soup.select("li.mb-5 h3 a.job-item__title-link"):
        vacancy_url = vacancy_div.get("href")
        if vacancy_url:
            if not vacancy_url.startswith("http"):
                vacancy_url = urljoin(base_url, vacancy_url)
            vacancies_links.append(vacancy_url)

    print(vacancies_links)

except requests.RequestException as e:
    print(f"Error fetching the page: {e}")

time.sleep(5)


# Step 2: Visit each detailed page and extract information
vacancies_data = []

for vacancy_url in vacancies_links:
    vacancy_response = requests.get(vacancy_url)
    vacancy_soup = BeautifulSoup(vacancy_response.content, "html.parser")


    # Extract the job title
    title_element = vacancy_soup.select_one(".detail--title-wrapper .col h1")
    if title_element and title_element.get_text(strip=True):
        title = title_element.get_text(strip=True)
    else:
        title = None


    # Extract the company name
    company = vacancy_soup.select_one(".job-details--title").text.strip()


    # Extract years of experience required
    experience_years_div = vacancy_soup.select(".card-body")[0]
    experience_text = experience_years_div.get_text(separator=' ', strip=True)
    experience_years_match = re.search(r'\b(\d+)\s*років досвіду\b', experience_text)
    if experience_years_match:
        experience_years = int(experience_years_match.group(1))
    else:
        experience_years = None


    # Extract English level requirement
    strong_element = vacancy_soup.select_one("strong.font-weight-600.capitalize-first-letter").text.strip().lower()
    english_level = None
    if strong_element:
        for eng_level in ENGLISH_LEVELS:
            if eng_level.strip().lower() in strong_element:
                english_level = eng_level


    # Extract salary information
    salary_element = vacancy_soup.select_one(".public-salary-item")
    if salary_element:
        try:
            salary_text = salary_element.text.strip()
            salary = int(salary_text.split(" ")[-1].replace("$", "").replace(",", ""))
        except (IndexError, ValueError):
            salary = None
    else:
        salary = None


    # Extract required skills
    skills_required = []
    body_element = vacancy_soup.select_one(".mb-4.job-post-description").text.strip().lower()

    for skill in SKILLS:
        if skill.strip().lower() in body_element:
            skills_required.append(skill)

    skills_required_str = ', '.join(skills_required)


    vacancies_data.append({
        "title": title,
        "company": company,
        "experience_years": experience_years,
        "salary": salary,
        "english_level": english_level,
        "skills_required": skills_required_str,
    })


    print(f"Vacancy Title: {title}")
    print(f"Company: {company}")
    print(f"Experience years: {experience_years}")
    print(f"English Level: {english_level}")
    print(f"Salary: {salary}")
    print(f"Skills required: {skills_required_str}")

    time.sleep(5)


columns = ["title", "company", "experience_years", "salary", "english_level", "skills_required"]
df = pd.DataFrame(vacancies_data, columns=columns)
df.to_csv("vacancies.csv", index=False)

print("Data successfully saved to vacancies.csv")
