def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data["url"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching meme: {e}")
        return "Sorry, I couldn't fetch a meme at this time."
