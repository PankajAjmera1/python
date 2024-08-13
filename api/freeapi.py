import requests

def fetch_data():
    url ="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username=user_data["login"]["username"]
        return username
    else:
        raise Exception("Failed to fetch data")

def main():
    try:
        username = fetch_data()
        print(f"Random username: {username}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

    