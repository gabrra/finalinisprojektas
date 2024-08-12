from scrape import get_sorted_titles


def print_sorted_titles(url: str, tag_name: str, class_name: str):
    sorted_titles = get_sorted_titles(url, tag_name, class_name)
    for title in sorted_titles:
        print(title)


def main():
    print("Choose website to scrape:")
    print("1. BBC")
    print("2. CNN")
    print("3. Economist")
    print("4. LRT")
    print("5. 15min")

    choice = input("Enter website number to scrape (1-5): ")

    if choice == '1':
        url = "https://www.bbc.com"
        tag_name = "div"
        class_name = "sc-4fedabc7-0 kZtaAl"
    elif choice == '2':
        url = "https://edition.cnn.com"
        tag_name = "div"
        class_name = "container__text container_lead-plus-headlines__text"
    elif choice == '3':
        url = "https://www.economist.com"
        tag_name = "h3"
        class_name = "css-1jzypbl e7j57mt0"
    elif choice == '4':
        url = "https://www.lrt.lt"
        tag_name = "h3"
        class_name = "news__title"
    elif choice == '5':
        url = "https://www.15min.lt"
        tag_name = "h4"
        class_name = "vl-title item-no-front-style"
    else:
        print("Please choose a number from 1 to 5")
        return
 
    print_sorted_titles(url, tag_name, class_name)


if __name__ == "__main__":
    main()