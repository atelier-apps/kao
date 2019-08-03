
texts={
    "ja":{
        "copyright":"本アプリのURLを第三者に共有することは固く禁じます。",
        "title":"Mr. 黒電話",
        "subtitle":"AI画像判定",
        "select_image":"画像を選択する",
        "reselect_image":"画像を選びなおす",
        "judge":"判定する",
        "judging":"判定中...",
        "tweet":"結果をツイートする",
        "description":"AIが金正恩か黒電話かを判定します",
        "try_again":"別の画像で試す",
        "answer_description":"この画像は",
        "kim":"金正恩",
        "phone":"黒電話",
        "other":"その他",
        "hashtag":"Mr.黒電話",
        "image_missing":"画像は見つかりませんでした。"
    },
    "en":{
        "copyright":"Sharing this app is strictly prohibited.",
        "title":"Mr. Phone",
        "subtitle":"AI Image Recognition",
        "select_image":"Select image",
        "reselect_image":"Change image",
        "judge":"Judge",
        "judging":"Judging...",
        "tweet":"Tweet this result",
        "description":"This AI judges your image whether Kim or Phone.",
        "try_again":"Try another image",
        "answer_description":"This is ",
        "kim":"Kim",
        "phone":"Phone",
        "other":"Other",
        "hashtag":"Mr.Phone",
        "image_missing":"Image Not Found."
    },
    "es":{
        "copyright":"Avisar este APP es prohibido",
        "title":"Mr. Phone",
        "subtitle":"IA Reconocimiento de imagen",
        "select_image":"Seleccionar el image",
        "reselect_image":"Cambiar el mage",
        "judge":"Juzgar",
        "judging":"Juzgando...",
        "tweet":"Tuitea este resultado",
        "description":"El IA juzga ya sea Kim o Teléfono.",
        "try_again":"Tratar otro image",
        "answer_description":"Este es",
        "kim":"Kim",
        "phone":"Teléfono",
        "other":"Otro",
        "hashtag":"Mr.Phone",
        "image_missing":"No busca el image."
    }
}


def get_textdef(language):
    if texts.get(language)!=None:
        return texts.get(language)
    else:
        return texts.get("en")
