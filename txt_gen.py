from google import genai

def txt_gen(query):

    # client = genai.Client(api_key="AIzaSyCe-Y1lMCa6FN--a7fERC4TUf03j8li4RQ")
    # client = genai.Client(api_key="AIzaSyC1mksaQ31e2X3Eu53wDgtLv3WRE82KGW4")
    # client = genai.Client(api_key="AIzaSyB4UkQ09znjJ_k4oNKX6gDB0fOQfHDW9lQ")
    client = genai.Client(api_key="AIzaSyB4UkQ09znjJ_k4oNKX6gDB0fOQfHDW9lQ")


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        # contents=f"「{query}」という文章からこの音楽の作者と曲名を調べ，「曲名-作者」という形で出力しなさい．生成する文章はこの　曲名-作者　のみです．",
        contents=f"「{query}」の文章から音楽の曲名と作者を検索し、「曲名 - 作者名」という形式で出力しなさい。\
                   出力は1行のみとし、「曲名 - 作者名」の形から外れてはならない。\
                   曲名・作者名は、**正式な表記（原題）**を用いること。\
                　・英語の曲は英語の原題\
　                ・日本語の曲は日本語のままでよい。\
                  和訳や説明、引用符（「」や""など）、補足、記号などは一切含めてはならない。\
                  ただし，作者名が不明の場合のみに限り，出力を曲名のみにすることを許す．\
                "
    )

    return_txt=response.text
 
    
    return return_txt


if __name__=="__main__":
    txt_gen("How long-  charlie")