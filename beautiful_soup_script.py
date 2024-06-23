from bs4 import BeautifulSoup
import os

# Open the HTML file and parse it with BeautifulSoup
with open('CameronWellerresumeV14.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all elements with a 'style' attribute
elements_with_style = soup.select('[style]')

css_rules = []

# For each element, remove the 'style' attribute and save the CSS rules
for element in elements_with_style:
    css_rules.append(f'#{element["id"]} {{{element["style"]}}}')
    del element['style']

# Write the CSS rules to a new .css file
with open('styles.css', 'w') as f:
    f.write('\n'.join(css_rules))

# Write the modified HTML to a new .html file
with open('CameronWellerresumeV14_no_inline_css.html', 'w') as f:
    f.write(str(soup))