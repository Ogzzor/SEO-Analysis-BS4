import requests
from bs4 import BeautifulSoup

def meta_analizi(url_link):
    response = requests.get(url_link)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "Title not found"
    meta_tags = soup.find_all("meta")

    description = None
    keywords = None

    for tag in meta_tags:
        if tag.get("name", "").lower() == "description":
            description = tag.get("content", "Description not found")
        if tag.get("name", "").lower() == "keywords":
            keywords = tag.get("content", "Keywords not found")

    print(f"Title: {title if title else 'Title not found!'}")
    print(f"Description: {description if description else 'Description not found!'}")
    print(f"Keywords: {keywords if keywords else 'Keywords not found!'}")

    def seo_analysis(title, description, keywords):
        issues = []

        if title:
            if len(title) < 50:
                issues.append(f"Title should be bigger than 50 characters ({len(title)}) characters.")
            elif len(title) > 60:
                issues.append(f"Title should be smaller than 60 characters ({len(title)}) characters. ")
        else:
            issues.append("Title not found.")

        if description:
            if len(description) < 150:
                issues.append(f"According to Google, the meta description must be greater than 150 characters and less than 160 characters: ({len(description)})")
            elif len(description) > 160:
                issues.append(f"According to Google, the meta description must be greater than 150 characters and less than 160 characters: ({len(description)})")
        else:
            issues.append("Meta description not found.")

        if not keywords:
            issues.append("Meta Keywords not found.")

        return issues

    seo_issues = seo_analysis(title, description, keywords)

    if seo_issues:
        print("Problems according to SEO compatibility:")
        for issue in seo_issues:
            print(f"- {issue}")
    else:
        print("There is no serious problem in terms of SEO.")
