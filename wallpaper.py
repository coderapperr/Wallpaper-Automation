import os
import requests
import wget
import ctypes

def get_wallpaper():
    access_key = os.environ.get('UNSPLASH_ACCESS_KEY')
    secret_key = os.environ.get('UNSPLASH_SECRET_KEY')
    # print(access_key)
    # print(secret_key)
    url = 'https://api.unsplash.com/photos/random/?client_id=' + access_key

    params = {
        'query': 'sports',
        'orientation': 'landscape'
    }

    response = requests.get(url, params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, r'.\tmp\wallpaper.jpg')
    return wallpaper

def main():
    image = get_wallpaper()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(image), 0)

if __name__ == '__main__':
    main()