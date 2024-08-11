from scraper_h3 import get_sorted_titles # change to scraper_h3 if economist or lrt or others

def print_sorted_titles(url: str, class_name: str):
    sorted_titles = get_sorted_titles(url, class_name)
    for title in sorted_titles:
        print(title)

def main():
    # Prompt user for URL and class name
    url = input("Enter the URL of the website to scrape: ")
    class_name = input("Enter the class name of the HTML element to scrape: ")
    
    # Print sorted titles 
    print_sorted_titles(url, class_name)

if __name__ == "__main__":
    main()

# https://www.bbc.com
# sc-4fedabc7-0 kZtaAl

# https://edition.cnn.com/
# container__text container_lead-plus-headlines__text

# https://www.economist.com/ #change from div to h3
# css-1jzypbl e7j57mt0

# https://www.lrt.lt/ #change from div to h3
# news__title


