import requests

def run(args):
    if not args.strip():
        print("Usage: wget <URL>")
        return

    url = args.strip()
    filename = url.split("/")[-1] or "downloaded_file"
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"File saved as {filename}")
    except Exception as e:
        print(f"Error downloading file: {e}")
