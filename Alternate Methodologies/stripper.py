from bs4 import BeautifulSoup

#def javascript(html)
with open('C:/Users/oboyld/Desktop/test_1/html1.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

# Removes JavaScript code from HTML body
for script in soup('script'):
    script.decompose()

# Removes problematic CSS    
for style in soup('style'):    
    style.decompose()
    break

# Removes Navigation Menu    
soup.find('div', {'class':'cda-render toc col-md-3'}).decompose()
    
with open("C:/Users/oboyld/Desktop/test_1/test1.html", "w") as f:
    f.write(soup.prettify())

#return soup.prettify()
    
#def css(html)

#Code Modified from:
#https://stackoverflow.com/questions/8283907/is-there-any-method-to-remove-javascript-code-from-an-html-document