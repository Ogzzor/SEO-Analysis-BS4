import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def script_analizi(url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all("script")

    internal_scripts = []
    external_scripts = []

    for script in scripts:
        src = script.get("src")  # Eğer src varsa bu dış script'tir
        if src:
            # Eğer src tam URL değilse, ana domain ile birleştir
            full_url = urljoin(url_link, src)
            external_scripts.append(full_url)
        else:
            internal_scripts.append(script)

    print(f"Number of internal scripts: {len(internal_scripts)}")

    print(f"Numebr of external scripts: {len(external_scripts)}")
    # print("Dış script dosyaları:")
    # for ext_script in external_scripts:
    #     print(ext_script)

    def script_analysis(internal_scripts, external_scripts):
        issues = []

        if len(internal_scripts) > 3:
            issues.append(
                f"Sayfada {len(internal_scripts)} iç script bulunuyor. Bu, sayfa performansını olumsuz etkileyebilir.")

        if len(external_scripts) > 5:
            issues.append(
                f"Sayfada {len(external_scripts)} dış script bulunuyor. Bu, sayfanın yükleme süresini uzatabilir.")

        for script in external_scripts:
            if "async" not in script and "defer" not in script:
                issues.append(
                    f"{script} dosyası async veya defer kullanmıyor. Bu, sayfanın yükleme süresini olumsuz etkileyebilir.")

        return issues

    script_issues = script_analysis(internal_scripts, external_scripts)

    if script_issues:
        print("Script'lerle ilgili performans sorunları:")
        for issue in script_issues:
            print(f"- {issue}")
    else:
        print("Script'lerle ilgili ciddi bir performans sorunu bulunmamaktadır.")

    start_time = time.time()
    for i in external_scripts:
        dis = requests.get(i)
        BeautifulSoup(dis.text, "html.parser")
    end_time = time.time()
    load_time = end_time - start_time
    print(f"External scripts loading time: { (round(load_time*1000, 2))/load_time} ms")