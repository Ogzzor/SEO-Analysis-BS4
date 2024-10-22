import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def style_analizi(url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, "html.parser")

    internal_styles = soup.find_all("style")
    external_styles = soup.find_all("link", rel="stylesheet")

    print(f"Number of internal style files: {len(internal_styles)}")

    external_stylesheets = []
    for style in external_styles:
        href = style.get("href")
        full_url = urljoin(url_link, href)
        external_stylesheets.append(full_url)

    print(f"Number of external style files: {len(external_stylesheets)}")
    # print("Dış stil dosyaları:")
    # for stylesheet in external_stylesheets:
    #     print(stylesheet)

    def style_analysis(internal_styles, external_stylesheets):
        issues = []

        if len(internal_styles) > 3:
            issues.append(f"({len(internal_styles)}) There are too many internal style files on the web page. This may negatively impact page loading time.")

        if len(external_stylesheets) > 5:
            issues.append(
                f"({len(external_stylesheets)}) There are too many external style files on the web page. This may negatively impact page loading time.")

        return issues

    style_issues = style_analysis(internal_styles, external_stylesheets)
    if style_issues:
        print("Performance issues with CSS:")
        for issue in style_issues:
            print(f"- {issue}")
    else:
        print("There is no serious performance problem with CSS.")
