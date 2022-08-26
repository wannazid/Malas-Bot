#Malas Bot - Telegram Bot

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from menu.main import *
from about.main import *
from config import *
import qrcode
import requests
import os
import json
import base64
import logging
import random

def clearterminal():
	linux = 'clear'
	windows = 'cls'
	os.system([linux,windows][os.name == 'nt'])
clearterminal()

def banner():
	print('''

    __  __       _                 ____        _   
   |  \/  | __ _| | __ _ ___      | __ )  ___ | |_ 
   | |\/| |/ _` | |/ _` / __|_____|  _ \ / _ \| __|
   | |  | | (_| | | (_| \__ \_____| |_) | (_) | |_ 
   |_|  |_|\__,_|_|\__,_|___/     |____/ \___/ \__|
            
               MalasBot - Bot Telegram
               
                   Version : 0.2
                     
         Get MalasBot : github.com/wannazid                                                                                                                        
     ''')
banner()

input_token = input('[!] Token API > ')
print('\n')
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Try logged in !')
api = input_token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
disp = Dispatcher(bot=bot)

#Join And Leave Grup
@disp.message_handler(content_types=['new_chat_members'])
async def user_joined_grup(pesan: types.Message):
    await pesan.answer(f'Selamat Datang Di Grup, Semoga Betah Ya :)')

@disp.message_handler(content_types=['left_chat_member'])
async def user_leave_grup(pesan: types.Message):
	first_name = pesan.from_user.first_name
	last_name = pesan.from_user.last_name
	await pesan.answer('Sempai Jumpa Bro, Semoga Bertemu Kembali:)')

#Menu Tools
@disp.message_handler(commands=['ttaudio'])
async def tt_download_musik(pesan: types.Message):
	query = pesan.text.replace('/ttaudio','')
	req = requests.get(f'https://api.akuari.my.id/downloader/tiktok?link={query}')
	try:
		ps = req.json()['respon']
		video = ps['audio']
		await pesan.answer('Tunggu Sebentar!')
		await pesan.answer(f'''
		Klik Link Now
		
		{video}
		''')
	except:
		await pesan.answer('Error or URL Not Valid')
	
	
@disp.message_handler(commands=['tt'])
async def tt_download_versi2(pesan: types.Message):
	query = pesan.text.replace('/tt','')
	req = requests.get(f'https://api.akuari.my.id/downloader/tiktok?link={query}')
	try:
		ps = req.json()['respon']
		video = ps['video']
		await pesan.answer('Tunggu Sebentar!')
		await pesan.answer(f'''
		Klik Link Now
		
		{video}
		''')
	except:
		await pesan.answer('Error or URL Not Valid')
	
@disp.message_handler(commands=['pinterest'])
async def pinterest_download(pesan: types.Message):
	query = pesan.text.replace('/pinterest','')
	config = config_malasbot()
	req = requests.get(f'https://raku-web.herokuapp.com/api/pinterest?text={query}&apikey={config}')
	ps = req.json()
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(ps['result']))
	
@disp.message_handler(commands=['neko'])
async def neko_random(pesan: types.Message):
    url = pesan.text.replace('/neko','')
    config = config_malasbot()
    reqs = requests.get(f'https://raku-web.herokuapp.com/api/nsfw/nsfwNeko?apikey={config}')
    ps = reqs.json()
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer(ps['result'])
    
@disp.message_handler(commands=['blowjob'])
async def blowjob_random(pesan: types.Message):
    url = pesan.text.replace('/blowjob','')
    config = config_malasbot()
    reqs = requests.get(f'https://raku-web.herokuapp.com/api/nsfw/blowjob?apikey={config}')
    ps = reqs.json()
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer(ps['result'])
    
@disp.message_handler(commands=['gangbang'])
async def gangbang_random(pesan: types.Message):
    url = pesan.text.replace('/gangbang','')
    config = config_malasbot()
    reqs = requests.get(f'https://raku-web.herokuapp.com/api/nsfw/gangbang?apikey={config}')
    ps = reqs.json()
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer(ps['result'])
    
@disp.message_handler(commands=['bdsm'])
async def bdsm_random(pesan: types.Message):
    url = pesan.text.replace('/bdsm','')
    config = config_malasbot()
    reqs = requests.get(f'https://raku-web.herokuapp.com/api/nsfw/bdsm?apikey={config}')
    ps = reqs.json()
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer(ps['result'])
    
@disp.message_handler(commands=['yuri'])
async def yuri_random(pesan: types.Message):
    url = pesan.text.replace('/yuri','')
    config = config_malasbot()
    reqs = requests.get(f'https://raku-web.herokuapp.com/api/nsfw/yuri?apikey={config}')
    ps = reqs.json()
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer(ps['result'])
    
@disp.message_handler(commands=['hentai'])
async def hentai_random(pesan: types.Message):
    url = pesan.text.replace('/hentai','')
    config = config_malasbot()
    reqs = requests.get(f'https://raku-web.herokuapp.com/api/nsfw/hentai?apikey={config}')
    ps = reqs.json()
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer_photo(types.InputFile.from_url(ps['result']))
    
@disp.message_handler(commands=['animequote'])
async def random_quotes(pesan: types.Message):
	artinama = pesan.text.replace('/animequote','')
	req = requests.get('https://katanime.vercel.app/api/getrandom')
	randoms = random.randrange(1, 5)
	utuh = req.json()['result'][randoms]
	kata = utuh['indo']
	char = utuh['character']
	anim = utuh['anime']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(f'''
	{kata}
	
	By : {char}
	Anime : {anim}
	''')

@disp.message_handler(commands=['flamingtext5'])
async def flaming_text5(pesan: types.Message):
	flam = pesan.text.replace('/flamingtext5','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://flamingtext.com/net-fu/proxy_form.cgi?&imageoutput=true&script=birdy-logo&doScale=true&scaleWidth=800&scaleHeight=500&text={flam}'))

@disp.message_handler(commands=['flamingtext4'])
async def flaming_text4(pesan: types.Message):
	flam = pesan.text.replace('/flamingtext4','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://www6.flamingtext.com/net-fu/proxy_form.cgi?&imageoutput=true&script=sketch-name&doScale=true&scaleWidth=800&scaleHeight=500&fontsize=100&fillTextType=1&fillTextPattern=Warning!&fillColor1Color=%23f2aa4c&fillColor2Color=%23f2aa4c&fillColor3Color=%23f2aa4c&fillColor4Color=%23f2aa4c&fillColor5Color=%23f2aa4c&fillColor6Color=%23f2aa4c&fillColor7Color=%23f2aa4c&fillColor8Color=%23f2aa4c&fillColor9Color=%23f2aa4c&fillColor10Color=%23f2aa4c&fillOutlineColor=%23f2aa4c&fillOutline2Color=%23f2aa4c&backgroundColor=%23101820&text={flam}'))

@disp.message_handler(commands=['flamingtext3'])
async def flaming_text3(pesan: types.Message):
	flam = pesan.text.replace('/flamingtext3','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://www6.flamingtext.com/net-fu/proxy_form.cgi?&imageoutput=true&script=sketch-name&doScale=true&scaleWidth=800&scaleHeight=500&fontsize=100&fillTextType=1&fillTextPattern=Warning!&text={flam}'))

@disp.message_handler(commands=['flamingtext2'])
async def flaming_text2(pesan: types.Message):
	flam = pesan.text.replace('/flamingtext2','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://flamingtext.com/net-fu/proxy_form.cgi?&imageoutput=true&script=crafts-logo&fontsize=90&doScale=true&scaleWidth=800&scaleHeight=500&text={flam}'))

@disp.message_handler(commands=['flamingtext'])
async def flaming_text(pesan: types.Message):
	flam = pesan.text.replace('/flamingtext','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://flamingtext.com/net-fu/proxy_form.cgi?&imageoutput=true&script=water-logo&script=water-logo&fontsize=90&doScale=true&scaleWidth=800&scaleHeight=500&fontsize=100&fillTextColor=%23000&shadowGlowColor=%23000&backgroundColor=%23000&text={flam}'))

@disp.message_handler(commands=['gemamembiru'])
async def random_waifu(pesan: types.Message):
	artinama = pesan.text.replace('/gemamembiru','')
	gembi = open('tools/gembi.json','r').read()
	randoms = random.randrange(2, 40)
	utuh = json.loads(gembi)[randoms]
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_video(types.InputFile.from_url(utuh))

@disp.message_handler(commands=['waifu'])
async def random_waifu(pesan: types.Message):
	artinama = pesan.text.replace('/waifu','')
	waifu = open('tools/waifu.json','r').read()
	randoms = str(random.randrange(1, 200))
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(json.loads(waifu)[randoms]))

@disp.message_handler(commands=['animequotes'])
async def anime_quotes(pesan: types.Message):
	question = pesan.text.replace('/animequotes','')
	req = requests.get('https://api.akuari.my.id/randomtext/quotesanime')
	await pesan.answer('Tunggu Sebentar!')
	parse = req.json()['result']
	nama_char = parse['char_name']
	nama_anime = parse['anime']
	quote = parse['quotes']
	await pesan.answer(f'''
	{quote}
	
	- {nama_char}
	anime : {nama_anime}
	''')
	
@disp.message_handler(commands=['couple'])
async def couple_pp(pesan: types.Message):
	cp_pp = pesan.text.replace('/couple','')
	req = requests.get('https://api.akuari.my.id/randomimage/ppcouple')
	parse = req.json()['respon']
	laki = parse['male']
	cewe = parse['female']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(laki))
	await pesan.answer_photo(types.InputFile.from_url(cewe))

@disp.message_handler(commands=['faktaunik'])
async def fakta_unik(pesan: types.Message):
	artinama = pesan.text.replace('/faktaunik','')
	req = requests.get(f'https://api.akuari.my.id/randomtext/faktaunik')
	parse = req.json()['hasil']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(parse)

@disp.message_handler(commands=['cosplay'])
async def cosplay_rand(pesan: types.Message):
	cosplayku = pesan.text.replace('/cosplay','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url('https://api.akuari.my.id/randomimganime/cosplay'))

@disp.message_handler(commands=['arti'])
async def arti_nama(pesan: types.Message):
	nama = pesan.text.replace('/arti','')
	req = requests.get(f'https://api.akuari.my.id/primbon/artinama?nama={nama}')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(req.json())

@disp.message_handler(commands=['dog'])
async def random_anjing(pesan: types.Message):
	gugug = pesan.text.replace('/dog','')
	req = requests.get('https://dog.ceo/api/breeds/image/random')
	parse = req.json()['message']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(parse))

@disp.message_handler(commands=['renungan'])
async def renungan_islam(pesan: types.Message):
	renung = pesan.text.replace('/renungan','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url('https://api.akuari.my.id/islami/renunganislam'))

@disp.message_handler(commands=['husbu'])
async def random_husbu(pesan: types.Message):
	husbuku = pesan.text.replace('/husbu','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url('https://api.akuari.my.id/randomimganime/husbu'))

@disp.message_handler(commands=['ph'])
async def logo_ph(pesan: types.Message):
	text = pesan.text.replace('/ph','')
	text2 = text.split('|')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://api.akuari.my.id/ephoto/pornhub?text={text2[0]}&text_2={text2[1]}'))

@disp.message_handler(commands=['qjamannow'])
async def bacot(pesan: types.Message):
	text = pesan.text.replace('/qjamannow','')
	req = requests.get('https://api.akuari.my.id/randomtext/bacot')
	parse = req.json()['hasil']
	hasil = parse['result']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(hasil)

@disp.message_handler(commands=['logoninja3'])
async def logo_ninja(pesan: types.Message):
	text = pesan.text.replace('/logoninja3','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://api.akuari.my.id/ephoto/team-logo-ninja-3?text={text}'))

@disp.message_handler(commands=['logoninja2'])
async def logo_ninja(pesan: types.Message):
	text = pesan.text.replace('/logoninja2','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://api.akuari.my.id/ephoto/team-logo-ninja-2?text={text}'))

@disp.message_handler(commands=['logoninja'])
async def logo_ninja(pesan: types.Message):
	text = pesan.text.replace('/logoninja','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://api.akuari.my.id/ephoto/team-logo-ninja-1?text={text}'))

@disp.message_handler(commands=['katabijak'])
async def kata_bijak(pesan: types.Message):
	kb = pesan.text.replace('/katabijak','')
	await pesan.answer('Tunggu Sebentar!')
	req = requests.get(f'https://api.akuari.my.id/randomtext/katabijak')
	parse = req.json()['hasil']
	quote = parse['quotes']
	by = parse['author']
	await pesan.answer(f'''
	{quote}
	- {by}
	''')

@disp.message_handler(commands=['ephoto'])
async def e_photo(pesan: types.Message):
	text = pesan.text.replace('/ephoto','')
	req = requests.get(f'https://api.akuari.my.id/ephoto/scraper-1?text={text}&link=https://en.ephoto360.com/online-blackpink-style-logo-maker-effect-711.html')
	parse = req.json()['respon']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(parse))
	
@disp.message_handler(commands=['asmaulhusna'])
async def asmaul_husna(pesan: types.Message):
	linkurl = pesan.text.replace('/asmaulhusna','')
	await pesan.answer('Tunggu Sebentar!')
	req = requests.get(f'https://api.akuari.my.id/islami/asmaulhusna')
	parse = req.json()['result']
	no = parse['number']
	latin = parse['latin']
	arab = parse['arab']
	translate = parse['translate_id']
	await pesan.answer(f'''
	
	No : {no}
	
    Nama  : {latin} | {arab}
	
    Arti : {translate}
	''')
	
@disp.message_handler(commands=['doa'])
async def random_doa(pesan: types.Message):
	linkurl = pesan.text.replace('/doa','')
	await pesan.answer('Tunggu Sebentar!')
	req = requests.get(f'https://api.akuari.my.id/islami/doa')
	parse = req.json()['result']
	judul = parse['title']
	arab = parse['arabic']
	latin = parse['latin']
	translate = parse['translation']
	await pesan.answer(f'''
	{judul}
	
	{arab}
	
	{latin}
	
	{translate}
	''')

@disp.message_handler(commands=['igdl'])
async def ig_downloader(pesan: types.Message):
	linkurl = pesan.text.replace('/igdl','')
	await pesan.answer('Tunggu Sebentar, Jika Sudah Simpan Di Galeri!')
	req = requests.get(f'https://hadi-api.herokuapp.com/api/instagram?url={linkurl}')
	try:
		parse = req.json()['result']
	except:
		parse = 'URL Error!'
	await pesan.answer(parse)
	
@disp.message_handler(commands=['wiki'])
async def textpro3(pesan: types.Message):
	kata = pesan.text.replace('/wiki','')
	req = requests.get(f'https://hadi-api.herokuapp.com/api/wiki?query={kata}').text
	parse = json.loads(req)
	try:
		hasil = parse["result"]
	except:
		parse = 'Tidak ditemukan di wikipedia!'
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(hasil)
	
@disp.message_handler(commands=['cecan'])
async def textpro3(pesan: types.Message):
	text = pesan.text.replace('/cecan','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/randomImage/cecan')

@disp.message_handler(commands=['megumin'])
async def textpro3(pesan: types.Message):
	text = pesan.text.replace('/megumin','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/randomImage/img/megumin')

@disp.message_handler(commands=['fww'])
async def textpro3(pesan: types.Message):
	text = pesan.text.replace('/fww','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/canvas/attp?text={text}')

@disp.message_handler(commands=['tts'])
async def textpro3(pesan: types.Message):
	text = pesan.text.replace('/tts','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/canvas/ttp?text={text}')

@disp.message_handler(commands=['darkjokes'])
async def textpro3(pesan: types.Message):
	text = pesan.text.replace('/darkjokes','')
	req = requests.get('https://hadi-api.herokuapp.com/api/darkjokes')
	parse = req.json()['result']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(parse))

@disp.message_handler(commands=['textpro3'])
async def textpro3(pesan: types.Message):
	text = pesan.text.replace('/textpro3','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/photoxy/shadow-sky?text={text}')

@disp.message_handler(commands=['textpro2'])
async def textpro2(pesan: types.Message):
	text = pesan.text.replace('/textpro2','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/textpro/neon-devil-wings?teks={text}')

@disp.message_handler(commands=['textpro1'])
async def textpro1(pesan: types.Message):
	text = pesan.text.replace('/textpro1','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/textpro/futuristic-technology?teks={text}')

@disp.message_handler(commands=['ssweb'])
async def ss_website(pesan: types.Message):
	web = pesan.text.replace('/ssweb','')
	await pesan.answer('Tunggu Sebentar!')
	try:
		await pesan.answer_photo(f'https://hadi-api.herokuapp.com/api/ssweb2?url={web}')
	except:
		await pesan.answer('URL Error!')
	
@disp.message_handler(commands=['loli'])
async def gambar_loli(pesan: types.Message):
	lolicon = pesan.text.replace('/loli','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo('https://hadi-api.herokuapp.com/api/loli')

@disp.message_handler(commands=['wpanime'])
async def wp_anime(pesan: types.Message):
	random = pesan.text.replace('/wpanime','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo('https://hadi-api.herokuapp.com/api/walpaperanime')

@disp.message_handler(commands=['kucing'])
async def random_kucing(pesan: types.Message):
	meong = pesan.text.replace('/kucing','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url('https://thecatapi.com/api/images/get?format=src&type=jpg'))

@disp.message_handler(commands=['cium'])
async def random_peluk(pesan: types.Message):
	rand = pesan.text.replace('/cium','')
	req = requests.get('https://api.rei.my.id/v3/kiss')
	parse = req.json()['url']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_animation(parse)

@disp.message_handler(commands=['tampol'])
async def random_peluk(pesan: types.Message):
	rand = pesan.text.replace('/tampol','')
	req = requests.get('https://api.rei.my.id/v3/slap')
	parse = req.json()['url']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_animation(parse)

@disp.message_handler(commands=['peluk'])
async def random_peluk(pesan: types.Message):
	rand = pesan.text.replace('/peluk','')
	req = requests.get('https://api.rei.my.id/v3/hug')
	parse = req.json()['url']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_animation(parse)

@disp.message_handler(commands=['qrcode'])
async def make_qrcode(pesan: types.Message):
	link = pesan.text.replace('/qrcode','')
	qr = qrcode.QRCode(version=1,box_size=10,border=4)
	qr.add_data(link)
	qr.make(fit=True)
	img = qr.make_image(fill='black',back_color='white')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.file(img))
	
@disp.message_handler(commands=['b64decode'])
async def base64_decode(pesan: types.Message):
	hash = pesan.text.replace('/b64decode','')
	hashing = base64.b64decode(hash).decode()
	await pesan.answer('Proses Decode!')
	await pesan.answer(hashing)

@disp.message_handler(commands=['b64encode'])
async def base64_encode(pesan: types.Message):
	hash = pesan.text.replace('/b64encode','')
	hashing = base64.b64encode(bytes(hash.encode())).decode()
	await pesan.answer('Proses Encode!')
	await pesan.answer(hashing)

@disp.message_handler(commands=['short'])
async def short_url(pesan: types.Message):
	link = pesan.text.replace('/short','')
	req = requests.get(f'https://rasenmedia.my.id/api/slink?apikey=baka&url={link}')
	parse = req.json()['result']
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(parse)

@disp.message_handler(commands=['lirik'])
async def lirik_lagu(pesan: types.Message):
	judul = pesan.text.replace('/lirik','')
	req = requests.get(f'https://freerestapi.herokuapp.com/api/lirik?l={judul}')
	try:
		parse = req.json()['data']
	except:
		parse = 'Lirik lagu tidak ditemukan!'
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer(parse)
	
@disp.message_handler(commands=['quote3'])
async def quote2(pesan: types.Message):
	kata = pesan.text.replace('/quote3','')
	wm = kata.split('|')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://rasenmedia.my.id/api/quotes4?apikey=baka&text={wm[0]}&watermark={wm[1]}'))

@disp.message_handler(commands=['quote2'])
async def quote2(pesan: types.Message):
	kata = pesan.text.replace('/quote2','')
	wm = kata.split('|')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://rasenmedia.my.id/api/quotes2?apikey=baka&text={wm[0]}&watermark={wm[1]}'))

@disp.message_handler(commands=['quote'])
async def quote1(pesan: types.Message):
	kata = pesan.text.replace('/quote','')
	await pesan.answer('Tunggu Sebentar!')
	await pesan.answer_photo(types.InputFile.from_url(f'https://rasenmedia.my.id/api/quotes5?apikey=baka&text={kata}'))

@disp.message_handler(commands=['nulis'])
async def nuliskanan(pesan : types.Message):
    tulisan = pesan.text.replace('/nulis','')
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer_photo(types.InputFile.from_url(f'https://rasenmedia.my.id/api/ngtdnulis?apikey=baka&text={tulisan}'))

@disp.message_handler(commands=['menu'])
async def nuliskanan(pesan : types.Message):
    await pesan.answer(menu_bot())
    
button1 = KeyboardButton('𝗛𝗲𝗹𝗽 𝗕𝗼𝘁 🤖')
button2 = KeyboardButton('𝗠𝗲𝗻𝘂 𝗕𝗼𝘁🤖')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

@disp.message_handler(commands=['start', 'help'])
async def start_bot(pesan: types.Message):
	await pesan.reply('𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗮𝗹𝗮𝘀𝗕𝗼𝘁, 𝗦𝗲𝗹𝗲𝗰𝘁 𝗠𝗲𝗻𝘂 ❗',reply_markup=keyboard1)

@disp.message_handler()
async def keyboard_answer(pesan: types.Message):
    if pesan.text == '𝗛𝗲𝗹𝗽 𝗕𝗼𝘁 🤖':
    	await pesan.answer(about_bot())
    elif pesan.text == '𝗠𝗲𝗻𝘂 𝗕𝗼𝘁🤖':
    	await pesan.answer(menu_bot())
    	
if __name__ == '__main__':
	executor.start_polling(disp,skip_updates=True)
