# -*- coding: utf-8 -*-
import os
from google.auth.transport.requests import Request
import google_auth_oauthlib.flow # type: ignore
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

#for audio make
import yt_dlp
import random
import threading
import sys

#for audio play
from playsound3 import playsound
import time
import random

def audio_make(url, output_name):
    print("\n\nDown loading "+output_name,"\n")
    # カスタムUser-Agentを設定（YouTubeに自動スクリプトとバレにくくする）
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    # yt-dlp のオプションを設定
    ydl_opts = {
        'format': 'worstaudio',  # 最高品質の音声を選択
        # 'outtmpl': output_name + ".mp3",  # 保存ファイル名
        'outtmpl': "./audio/"+output_name,  # 保存ファイル名
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # ビットレート設定
        }],
        'nocheckcertificate': True,  # 証明書エラーを無視
        'noplaylist': True,  # プレイリスト全体のダウンロードを防ぐ
        'quiet': True,  # 不要なログを抑える
        'user_agent': user_agent, # カスタムUser-Agentを設定
        # 'ffmpeg_location': "/usr/local/bin/ffmpeg",
        #for windows
        'ffmpeg_location': r'C:\Program Files\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin',
    }

    # ランダムな遅延を入れてアクセスを分散（Bot対策）
    # # delay = random.uniform(1.5, 3.0)
    # print(f"Waiting for {delay:.2f} seconds before download...")
    # time.sleep(delay)

    # YouTubeの音声をダウンロード
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download successful")
    #保存したとき，ファイルは上書きされる．
    return 0

if __name__ == "__main__":
    #for debug
    audio_make("https://www.youtube.com/watch?v=h1fekckH8uI","テルーの唄")

