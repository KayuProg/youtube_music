import re
#original
import get_info
import txt_gen
import audio_make




def main():
    print("getting musics info")
    musics_info=get_info.get_info()
    print("end")
    #title change
    for music in musics_info:
        title=music["title"]
        #改行削除
        converted_title=txt_gen.txt_gen(title)
        simple_title = re.sub(r'\r?\n', '', converted_title)
        music["title"]=simple_title
        print(music)

    #audio make
    for music in musics_info:
        url=music["url"]
        name=music["title"]
        # audio_make.audio_make(url,name)
    

if __name__=="__main__":
    main()