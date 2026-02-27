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

def get_urls():
    SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

    json_pass="./jsons/token.json"
    client_secrets_file = "./jsons/client.json"
     # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Get credentials and create an API client
  
    creds = None#認証情報を格納する変数

    if os.path.exists(json_pass):
        creds = Credentials.from_authorized_user_file(json_pass, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # flow = InstalledAppFlow.from_client_secrets_file("./jsons/client.json", SCOPES)
            # creds = flow.run_local_server(port=0)
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        print("\n",creds,"\n")
        with open(json_pass, "w") as token:
            token.write(creds.to_json())
    
    youtube = googleapiclient.discovery.build("youtube","v3", credentials=creds)
    
    #playlist id取得
    # request = youtube.playlists().list(
    #     part="snippet,contentDetails",
    #     # maxResults=25,
    #     mine=True  # 認証されたアカウントのプレイリストを取得
    # )
    # response = request.execute()

    # # 結果を表示
    # for playlist in response.get("items", []):
    #     print(f"{playlist['snippet']['title']} (ID: {playlist['id']})")

    #プレイリストidから中の情報取得
    urls=[]
    try:
        # 指定されたプレイリストの動画を取得
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=25,  # 取得する最大件数（最大50）
            # playlistId="PL8G4Ylahsmrrf6_uMWaQGNUBOf8COtlK5"  #favoriteのplaylist ID
            playlistId="PL8G4YlahsmrqI2v3HEFaHfxiY1FaHPb0c"
        )
        response = request.execute()

        # 結果を表示
        # print(f"🎵 プレイリスト内の動画一覧（ID: PL8G4Ylahsmrrf6_uMWaQGNUBOf8COtlK5）:")
        for item in response.get("items", []):
            # print(item["snippet"])
            video_title = item["snippet"]["title"]
            video_id = item["contentDetails"]["videoId"]
            # print(f"URL is (https://www.youtube.com/watch?v={video_id})")
            url=f"https://www.youtube.com/watch?v={video_id}"
            info={"title":video_title,"url":url,"id":video_id}
            urls.append(info)

        # print("This is urls : ",urls)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
    return urls

    
def delete_music(target_video_id):
    SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    #musicを削除する用のtokenファイルはdelete_token.jsonとして作成する．
    json_pass = "./jsons/delete_token.json"
    client_secrets_file = "./jsons/client.json"
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    creds = None
    if os.path.exists(json_pass):
        creds = Credentials.from_authorized_user_file(json_pass, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(json_pass, "w") as token:
            token.write(creds.to_json())

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    try:
        playlist_id = "PL8G4YlahsmrqI2v3HEFaHfxiY1FaHPb0c"
        request = youtube.playlistItems().list(
            part="id,contentDetails",
            playlistId=playlist_id,
        )
        response = request.execute()

        for item in response["items"]:
            # print(item)
            video_id = item["contentDetails"]["videoId"]
            playlist_item_id = item["id"]
            # print(video_id)
            if video_id == target_video_id:
                print(f"Deleting video: {video_id} (playlist item id: {playlist_item_id})")
                del_request = youtube.playlistItems().delete(id=playlist_item_id)
                del_request.execute()
                print("Deleted successfully.")
                return
        print("Video not found in playlist.")

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
    

if __name__ == "__main__":
    # urls=get_urls()    
    # get_info()
    delete_music("3INrX5vzQeE")
