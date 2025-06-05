import requests
from bs4 import BeautifulSoup as bs

# W celu prezentacji możliwości 'BeautifulSoup' 
# wykorzystana została biblioteka 'Requests' jako klient HTTP

'''
    Przykład wyodrębnienia tytułu strony.
'''
def example_1():
    print('Example 1')
    url = "https://example.com"
    res = requests.get(url)
    soup = bs(res.text, "html.parser")

    title = soup.title.text
    print(f'Website Title: {title}')


'''
    Przykład wyodrębnienia wszystkich elementów na stronie 
    zawierająych dany znacznik (w tym przypadku <h3>) oraz 
    daną klasę (w tym przypadku 'country-name').
'''
def example_2():
    print('Example 2')
    url = "https://www.scrapethissite.com/pages/simple/"
    res = requests.get(url)
    soup = bs(res.text, "html.parser")

    headers = soup.find_all('h3', {'class': 'country-name'})
    
    countries = [h.text.strip() if not h == None else '' for h in headers]
    print(countries)



if __name__ == "__main__":
    example_1()
    example_2()
