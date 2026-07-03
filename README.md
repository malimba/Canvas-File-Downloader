# Canvas File Downloader

Bulk-download **all files** from a Canvas LMS course using the Canvas REST API — built for students who need offline copies of lecture materials.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Canvas](https://img.shields.io/badge/Canvas-LMS-E72429?style=flat-square)

## Features

- Paginated API traversal — fetches every file in a course
- Saves to a local `canvas_files/` directory
- Configurable `ACCESS_TOKEN`, `COURSE_ID`, and `BASE_URL`
- Simple single-script design

## Prerequisites

1. Log into your institution's Canvas (e.g. Instructure).
2. Generate a personal **access token** (Account → Settings → Approved Integrations).
3. Note your **course ID** from the course URL.

## Quick start

```bash
pip install requests
```

Edit `canvasDownloaderScript.py`:

```python
ACCESS_TOKEN = "your_token_here"
COURSE_ID = "12345"
BASE_URL = "https://your-school.instructure.com"
```

Run:

```bash
python canvasDownloaderScript.py
```

## Security

- **Never commit** your access token to a public repo.
- Tokens grant access to your Canvas account — rotate if leaked.

## TODO

- [ ] CLI flags for course ID and output directory
- [ ] Resume interrupted downloads

---

[malimba](https://github.com/malimba)
