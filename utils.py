import requests
def download_pdf_from_drive(file_id: str, save_path: str):
  
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    resp = requests.get(download_url)
    resp.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(resp.content)

    print(f"[!] PDF downloaded → {save_path}")
