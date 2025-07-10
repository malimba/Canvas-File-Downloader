


import requests
import os

# === CONFIGURATION ===
ACCESS_TOKEN = 'YourAccessTokenHere'  # Paste your token here
COURSE_ID = 'yourCourseID'
BASE_URL = 'https://ashesi.instructure.com'
DOWNLOAD_FOLDER = 'canvas_files'

# === SETUP ===
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# Create download folder if it doesn't exist
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# === PAGINATED API REQUEST ===
def get_all_files():
    files = []
    url = f'{BASE_URL}/api/v1/courses/{COURSE_ID}/files?per_page=100'

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        files.extend(response.json())

        # Pagination support
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None

    return files

# === DOWNLOAD FILES ===
def download_file(file_info):
    file_url = file_info['url']
    file_name = file_info['display_name']
    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

    response = requests.get(file_url, headers=headers, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f'Downloaded: {file_name}')

# === MAIN ===
if __name__ == '__main__':
    print("Fetching file list...")
    all_files = get_all_files()
    print(f"Found {len(all_files)} files. Starting download...\n")

    for file_info in all_files:
        download_file(file_info)

    print("\n✅ All files downloaded successfully.")

