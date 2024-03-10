import re

import requests



url = "https://image.baidu.com/search/acjson?"

headers = {
        "Host": "image.baidu.com",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
,       'Cookie': 'BAIDUID=FEED836F1E68AAD8E7C77E2E5D8B65BE:FG=1; BAIDUID_BFESS=FEED836F1E68AAD8E7C77E2E5D8B65BE:FG=1; BDUSS=EFxQWRPSGJyUUFYTGlhaTRIV2FzRnhlY0cxOXUwOXRrZlBsWlNPVGUwQXU1YWxrSVFBQUFBJCQAAAAAAQAAAAEAAAC5GDpXzfVX1Ma6~rK7uekAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5YgmQuWIJkS; BDUSS_BFESS=EFxQWRPSGJyUUFYTGlhaTRIV2FzRnhlY0cxOXUwOXRrZlBsWlNPVGUwQXU1YWxrSVFBQUFBJCQAAAAAAQAAAAEAAAC5GDpXzfVX1Ma6~rK7uekAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5YgmQuWIJkS; BIDUPSID=FEED836F1E68AAD8E7C77E2E5D8B65BE; PSTM=1686398132; __bid_n=188ece5794e641685f9a62; MCITY=-137%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDU_WISE_UID=wapp_1692256218237_629; arialoadData=false; ZFY=OE7DRFXFpGcc:ADgFHsi9qcNR3AlKAIXnuNhFSOmDpxU:C; RT="z=1&dm=baidu.com&si=8f66b89f-a2c3-42b0-884c-efaf09e65a01&ss=lletnokn&sl=a&tt=f4h&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4a7j&nu=7se0zjra&cl=15b4&ul=4ldl7&hd=4ldop"; BA_HECTOR=202k24a5a12h0h25858h0lar1idt3qa1o; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=7; delPer=0; H_PS_PSSID=36561_39097_39199_26350_39138_39139_39137_39101; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; ab_sr=1.0.1_NjhkNzVlNjNkNzMyZWIzNzE0NWM2YmZjNThhZTRjNTcyY2M0N2Y5OWQxMGE0MWYwMjY2ODFjYmIwMGYyZGJmNmJjZWNmMWM3ZmI5NWNkNjNlNGM4NzUwYjk4Zjc5YmJiYzE1NTVjNjE5YjNhOGE4NDZkNTNlYmEyYjg2YmY2ZDBkODZjYTRhMjZjODM0N2ExNTg4MDM3YmIyMGExMmY2Zg=='
,       'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwxLDMsNiw0LDUsMiw4LDcsOQ%3D%3D&word=%E4%BA%91'

}

params = {
"tn":" resultjson_com",
"logid":" 10433475432186691461",
"ipn":" rj",
"ct":" 201326592",
"is":" ",
"fp":" result",
"fr":" ",
"word":" 云",
"queryWord":" 云",
"cl":" 2",
"lm":" -1",
"ie":" utf-8",
"oe":" utf-8",
"adpicid":" ",
"st":" ",
"z":" ",
"ic":" ",
"hd":" ",
"latest":" ",
"copyright":" ",
"s":" ",
"se":" ",
"tab":" ",
"width":" ",
"height":" ",
"face":" ",
"istype":" ",
"qc":" ",
"nc":" 1",
"expermode":" ",
"nojc":" ",
"isAsync":" ",
"pn":" 30",
"rn":" 30",
"gsm":" 1e",
"1692307337050":" ",
}

resp = requests.get(url,headers=headers,params=params)
re.findall('"thumurl":"(.*?)"',resp.text)
print(resp.text)






