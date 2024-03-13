from pathlib import Path
import json

URL_GETAWS = "https://labs.vocareum.com/util/vcput.php"

COOKIES_FILENAME = "cookies.txt"
try:
    COOKIES = json.loads(Path(COOKIES_FILENAME).read_text())
except json.decoder.JSONDecodeError as e:
    if "double quotes" in e.msg:
        string = Path(COOKIES_FILENAME).read_text()
        COOKIES = json.loads(string.replace("'", '"'))
    else:
        raise e


HEADERS = {
    "authority": "labs.vocareum.com",
    "accept": "*/*",
    "accept-language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "referer": "https://labs.vocareum.com/main/main.php?m=clabide&mode=s&asnid=1899604&stepid=1899605&hideNavBar=1",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "x-requested-with": "XMLHttpRequest",
}

PARAMS_GETAWS = {
    "a": "getaws",
    "type": "1",
    "stepid": "1899605",
    "version": "0",
    "v": "0",
    "vockey": "3h2zju23ZCRfHzOqtarKDA==",
}
PARAMS_STARTAWS = {
    "a": "startaws",
    "stepid": "1899605",
    "version": "0",
    "mode": "s",
    "type": "1",
    "vockey": "3h2zju23ZCRfHzOqtarKDA==",
}
