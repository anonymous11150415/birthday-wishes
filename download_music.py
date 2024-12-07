import requests
import os

def download_file(url, filename):
    # 确保目录存在
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 确保请求成功
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Successfully downloaded {filename}")
        return True
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return False

# 尝试多个音乐源
music_urls = [
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www2.cs.uic.edu/~i101/SoundFiles/BachGavotteShort.mid",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
]

# 设置保存路径
save_path = "music/happy-birthday.mp3"

# 尝试下载，直到成功或所有源都尝试过
for url in music_urls:
    print(f"Trying to download from: {url}")
    if download_file(url, save_path):
        print("Music download successful!")
        break
    else:
        print("Trying next source...")
