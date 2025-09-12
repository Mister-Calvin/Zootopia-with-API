import data_fetcher
import requests

def read_template():
    """Read and return the content of the HTML template."""
    with open("animals_template.html", "r") as file:
        return file.read()


def insert_animals_into_template(template_html, animals_html):
    """Insert the animals HTML into the template placeholder."""
    return template_html.replace("__REPLACE_ANIMALS_INFO__", animals_html)


def save_html(final_html):
    """Save the final HTML content to animals.html."""
    with open("animals.html", "w") as file:
        file.write(final_html)


def serialize_animal(animal_info):
    """Return an HTML <li> card for a single animal."""
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_info.get("name", "Unknown")}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_info['characteristics'].get('diet', 'Unknown')}<br/>\n"
    output += f"<strong>Location:</strong> {(animal_info.get('locations') or ['Unknown'])[0]}<br/>\n"
    if animal_info["characteristics"].get("type", "Unknown"):
        output += f"<strong>Type:</strong> {animal_info['characteristics'].get('type', 'Unknown')}<br/>\n"
    output += "</p>\n"
    output += "</li>\n"
    return output


def generate_animals_html(animals_data):
    """Generate the complete HTML fragment for all animals."""
    if not animals_data:
        return '<li class="cards__item"><div class="card__title">No animals found</div></li>\n'

    output = ""
    for animal_info in animals_data:
        output += serialize_animal(animal_info)
    return output


def write_html(animals_html):
    """Build the full HTML page and save it as animals.html."""
    template_html = read_template()
    final_html = insert_animals_into_template(template_html, animals_html)
    save_html(final_html)


def main():
    """Main function that loads data, generates HTML, and writes the result."""
    try:
        input_animals_search = input("Which animals do you want to search? (Enter animals names): ")
        animals_data = data_fetcher.fetch_data(input_animals_search)
        if not animals_data:
            print(f"*{input_animals_search}* does not exist. An empty page will be generated.")

        animals_html = generate_animals_html(animals_data)
        write_html(animals_html)
        print("Website was successfully generated to the file animals.html.")

    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print("Key not found.")
    except requests.exceptions.ConnectionError:
        print("No connection to the API (ConnectionError).")
    except requests.exceptions.Timeout:
        print("API request took too long (Timeout).")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP-Error: {e.response.status_code}")


if __name__ == "__main__":
    main()
