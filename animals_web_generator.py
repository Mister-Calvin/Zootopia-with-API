import json
import requests


def load_api_datas(animal):
    name = animal
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'WVLMZj5jLhWA4NTwxTClSg==U2mNnYWCrgb1D4uk'})
    as_json = response.json()
    return as_json


def serialize_animal(animal_info):
    """Return an HTML <li> card for a single animal"""
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_info.get('name','Unknown')}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_info['characteristics'].get('diet','Unknown')}<br/>\n"
    output += f"<strong>Location:</strong> {animal_info.get('locations',['Unknown'])[0]}<br/>\n"
    if animal_info["characteristics"].get("type","Unknown"):
        output += f"<strong>Type:</strong> {animal_info['characteristics'].get('type','Unknown')}<br/>\n"
    output += "</p>\n"
    output += "</li>\n"
    return output


def generate_html(animals_data):
    """Generates the complete HTML fragment for all animals."""
    output = ""
    for animal_info in animals_data:
        output += serialize_animal(animal_info)
    return output


def write_html(output):
    """Inserts the animal HTML into the template and writes the final HTML file."""
    with open("animals_template.html", "r") as file:
        template_html = file.read()
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)
    with open("animals.html", "w") as file:
        file.write(final_html)


def main():
    """Main function that loads data, generates HTML, and writes the result."""
    animals_data = load_api_datas("Fox")
    write_html(generate_html(animals_data))


if __name__ == "__main__":
    main()
