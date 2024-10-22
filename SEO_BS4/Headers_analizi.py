import requests
from colorama import Fore

def headers_analizi(url_link):
    response = requests.get(url_link)

    headers = response.headers

    # print("HTTP Header Informations:")
    # for header, value in headers.items():
    #     print(f"{header}: {value}")

    security_headers = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Frame-Options',
        'X-Content-Type-Options',
        'Referrer-Policy',
        'Permission_Policy',
        'X-XSS-Protection',
        'Content-Type'
    ]

    print(Fore.BLUE + "\nSecurity Headers:")
    for header in security_headers:
        if header in headers:
            print(Fore.GREEN + f"{header}: {headers[header]}")
        else:
            print(Fore.RED + f"{header} not available.")

    performance_headers = [
        'Cache-Control',
        'Expires',
        'Content-Encoding',
        'Keep-Alive'
    ]

    print(Fore.BLUE + "\nPerformance Headers:")
    for header in performance_headers:
        if header in headers:
            print(Fore.GREEN + f"{header}: {headers[header]}")
        else:
            print(Fore.RED + f"{header} not available.")
            print(Fore.RESET)

