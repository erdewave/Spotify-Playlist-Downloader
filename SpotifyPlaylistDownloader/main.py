import spotube
from spotube import download_manager

# Uygulamayı kullanabilmek için Spotify'a kayıtlı hesabınızdan API anahtarı oluşturmanız gerekmektedir.
# Şarkılar Default olarak Uygulamanın yer aldığı Mevcut Dizinde /Songs adlı bir klasör oluşturacak ve altına eklenecektir.

spotify_id = input("Enter Spotify Client ID: ")
spotify_secret = input("Enter Spotify Secret ID: ")
genius_token = input("Enter Genius Token: ")
spotify_link = input("Please Enter Your Download Link: ")

my_downloaded = spotube.DownloadManager(spotify_id, spotify_secret, genius_token, normalize_sound= False )

my_downloaded.start_downloader(spotify_link)

