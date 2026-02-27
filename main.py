import re
#original
import get_info
import txt_gen
import audio_make
import time



def main():
    print("getting musics info")
    musics_info=get_info.get_urls()
    print("There are ",len(musics_info)," musics")
    print("end\n")
    #title change
    # for music in musics_info:
    #     title=music["title"]
    #     #改行削除
    #     converted_title=txt_gen.txt_gen(title)
    #     simple_title = re.sub(r'\r?\n', '', converted_title)
    #     music["title"]=simple_title
    #     print(simple_title)

    #audio make
    for music in musics_info:
        # print("text gen")
        #title change
        # original_title=music["title"]
        # converted_title=txt_gen.txt_gen(original_title)
        # simple_title = re.sub(r'\r?\n', '', converted_title)
        # music["title"]=simple_title
        # print("\n\nConverted ",original_title," to ",simple_title)
        
        name = music["title"]
        left, right = name.split("-")
        name_processed = right.strip() + " - " + left.strip()
        #特定の言葉を抜く
        remove_words = ["lyrics","Lyrics","LYRICS","和訳","【】","[]","«»","〘〙","()", "（）", "[]", "［］", "{}", "｛｝", "<>", "＜＞", "〈〉", "《》", "«»", "‹›", "【】", "〖〗", "〘〙", "〚〛", "〔〕", "「」", "『』", "〝〟", "〞〟", "⟨⟩", "⟪⟫", "⟮⟯", "⦅⦆", "⦃⦄"]
        for s in remove_words:
            name_processed = name_processed.replace(s, "")

        
        
        
        url=music["url"]
        music_id=music["id"]
        audio_make.audio_make(url,name_processed)
        print("Delete ",name," from playlist")
        get_info.delete_music(music_id)#delete audio
        time.sleep(3)
    

if __name__=="__main__":
    main()