
# def delete_music(video_id):
#     SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

#     json_pass="./jsons/token.json"
#     client_secrets_file = "./jsons/client.json"
#      # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     # Get credentials and create an API client
  
#     creds = None#認証情報を格納する変数

#     if os.path.exists(json_pass):
#         creds = Credentials.from_authorized_user_file(json_pass, SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             # flow = InstalledAppFlow.from_client_secrets_file("./jsons/client.json", SCOPES)
#             # creds = flow.run_local_server(port=0)
#             flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         print("\n",creds,"\n")
#         with open(json_pass, "w") as token:
#             token.write(creds.to_json())
    
#     youtube = googleapiclient.discovery.build("youtube","v3", credentials=creds)
    
#     try:
#         # 指定されたプレイリストの動画を取得
        
#         request = youtube.playlistItems().delete(
#         # id=f"{video_id}",
#         id="3INrX5vzQeE",
#         # playlistId="PL8G4YlahsmrqI2v3HEFaHfxiY1FaHPb0c"
#         )
        
#         # request = youtube.playlistItems().list(
#         #     part="snippet,contentDetails",
#         #     maxResults=25,  # 取得する最大件数（最大50）
#         #     # playlistId="PL8G4Ylahsmrrf6_uMWaQGNUBOf8COtlK5"  # 取得したいプレイリストのID
#         #     playlistId="PL8G4YlahsmrqI2v3HEFaHfxiY1FaHPb0c"
#         # )
#         response = request.execute()

#         print(response)
#     except HttpError as e:
#         print(f"An HTTP error {e.resp.status} occurred: {e.content}")
    
#     return 0
    