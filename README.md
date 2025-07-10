# Canvas File Downloader

A Python utility script to download all files from a specific Canvas course (e.g., from Ashesi University's Canvas instance) to a local folder on your device.

## 🔧 Features

* Downloads **all course files** using the official Canvas API.
* Automatically handles **API pagination**.
* Saves files into a local folder of your choice.
* Supports secure **token-based authentication**.

## 🚀 Setup & Usage

### 1. Clone or Download This Repository

```bash
git clone https://github.com/your-username/Canvas-File-Downloader.git
cd Canvas-File-Downloader
```

### 2. Install Dependencies

This script requires the `requests` library:

```bash
pip install requests
```

### 3. Get Your Canvas Access Token

1. Log in to [https://ashesi.instructure.com](https://ashesi.instructure.com)
2. Click **Account** → **Settings**
3. Scroll down to **Approved Integrations**
4. Click **+ New Access Token**
5. Fill in:

   * **Purpose**: `Script download`
   * **Expires**: Any future date
6. Click **Generate Token** and copy it

### 4. Configure and Run the Script

Open the Python script and replace the placeholder with your token:

```python
ACCESS_TOKEN = 'your_token_here'
```

Run the script:

```bash
python canvas_downloader.py
```

All files will be downloaded to a folder named `canvas_files/` by default.

## 📁 Folder Structure

```
Canvas-File-Downloader/
├── canvas_downloader.py      # Main script
├── README.md                 # This file
└── canvas_files/             # Folder where files will be saved
```

## ⚠️ Security Notes

* **Never share your token** in public repositories
* Store tokens in environment variables or `.env` files for added safety
* Tokens can expire — regenerate when needed

## 🧩 TODO

* [ ] Add filtering by file type (e.g., PDF only)
* [ ] Add CLI support for setting course ID and output folder
* [ ] Enable multi-course file downloads

## 📜 License

This project is licensed under the MIT License.
Free to use, modify, and share.

## ✨ Contributing

Pull requests are welcome!
If you find bugs or want to improve the script, feel free to fork and contribute.

