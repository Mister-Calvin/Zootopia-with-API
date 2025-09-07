# Zootopia with API

This project generates a simple website that shows animal information using data from the [API Ninjas Animal API](https://api-ninjas.com/api/animals).

It is based on the original Zootopia project but refactored into a cleaner structure:
- `data_fetcher.py`: handles the API requests.
- `animals_web_generator.py`: builds the website using the data.

You can enter an animal name in the terminal, and the program fetches the info and creates an `animals.html` file with the results.

The API key is stored securely in a `.env` file and loaded using `python-dotenv`. The `.env` file is ignored via `.gitignore` to keep the key private.

### To run the project:
1. Install dependencies with: `pip install -r requirements.txt`
2. Create a `.env` file with your API key:  
   `API_KEY=your_api_key_here`
3. Run the script: `python animals_web_generator.py`

If no animal is found, the program prints a message and stops. Otherwise, it generates the HTML.

