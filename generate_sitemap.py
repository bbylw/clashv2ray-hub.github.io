import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# Function to generate XML for each URL
def create_url_element(url):
    url_element = Element('url')
    loc = SubElement(url_element, 'loc')
    loc.text = url
    return url_element

# Function to generate sitemap XML
def generate_sitemap(urls):
    urlset = Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

    for url in urls:
        url_element = create_url_element(url)
        urlset.append(url_element)

    xml_str = minidom.parseString(tostring(urlset)).toprettyxml()
    with open('sitemap.xml', 'w') as f:
        f.write(xml_str)

# Directory containing your website content
content_directory = 'free-nodes'

# Get all URLs from content directory
urls = []
for root, dirs, files in os.walk(content_directory):
    for file in files:
        if file.endswith('.html'):
            url = os.path.relpath(os.path.join(root, file), content_directory)
            urls.append(f'https://clashv2ray-hub.github.io/{url}')

# Generate sitemap XML
generate_sitemap(urls)
