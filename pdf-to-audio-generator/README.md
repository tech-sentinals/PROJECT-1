# PDF-to-Audio Generator

Flask web service that extracts text from uploaded PDFs and converts it to MP3 using Google Cloud Text-to-Speech.

## Setup
1. Create a Google Cloud project and enable Text-to-Speech.
2. Configure application credentials locally; never commit credentials.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `python app.py`.

## API
`POST /api/convert` with multipart field `pdf`.

The sample implementation limits synthesis input to a safe request size. Production versions should add authentication, file-size limits, malware scanning, background jobs, and persistent object storage.
