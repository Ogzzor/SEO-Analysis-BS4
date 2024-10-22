from H_Tags import h_tags
from Headers_analizi import headers_analizi
from Image_analizi import image_analizi
from link_request import link_req
from Load_time import load_time
from Meta_analizi import meta_analizi
from Metin_analizi import metin_analizi
from Script_analizi import script_analizi
from Size_analizi import size_analizi
from Style_analizi import style_analizi

def main():
    url_link = input("Please enter the URL of the site you want to perform SEO analysis: ")

    print("1. Image Analysis:")
    image_analizi(url_link)

    print("\n2. H Tags Analysis:")
    h_tags(url_link)

    print("\n3. Headers Analysis:")
    headers_analizi(url_link)

    print("\n4. Link Analysis:")
    link_req(url_link)

    print("\n5. Load Time:")
    load_time(url_link)

    print("\n6. Meta Analysis:")
    meta_analizi(url_link)

    print("\n7. Text Analysis:")
    metin_analizi(url_link)

    print("\n8. Script Analysis:")
    script_analizi(url_link)

    print("\n9. Size of Page:")
    size_analizi(url_link)

    print("\n10. Style Analysis:")
    style_analizi(url_link)

if __name__ == "__main__":
    main()