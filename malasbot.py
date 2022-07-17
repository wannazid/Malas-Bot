#Malas Bot - Telegram Bot

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import hashlib
import qrcode
import requests
import os
import json
import base64
import logging

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

# Menu Tools

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

@disp.message_handler(commands=['md5'])
async def sha256_encrypt(pesan: types.Message):
	string = pesan.text.replace('/md5','')
	enc = string.encode('utf-8')
	hex = hashlib.md5(enc)
	str_hex = hex.hexdigest()
	await pesan.answer('Proses Encrypt!')
	await pesan.answer(str_hex)

@disp.message_handler(commands=['sha256'])
async def sha256_encrypt(pesan: types.Message):
	string = pesan.text.replace('/sha256','')
	enc = string.encode('utf-8')
	hex = hashlib.sha256(enc)
	str_hex = hex.hexdigest()
	await pesan.answer('Proses Encrypt!')
	await pesan.answer(str_hex)
	
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

@disp.message_handler(commands=['tt'])
async def tiktokdown(pesan: types.Message):
	link = pesan.text.replace('/tt','')
	req = requests.get(f'https://rasenmedia.my.id/api/tiktok?url={link}')
	try:
		parse = req.json()['result']
		parse2 = parse['video']
	except:
		parse2 = 'Error URL atau Error API'
	await pesan.answer('Tunggu Sebentar, Perlu Download Dahulu!')
	await pesan.answer_video(types.InputFile.from_url(parse2))

@disp.message_handler(commands=['ttmusik'])
async def tiktokmusik(pesan: types.Message):
	link = pesan.text.replace('/ttmusik','')
	req = requests.get(f'https://rasenmedia.my.id/api/tiktok?url={link}')
	try:
		parse = req.json()['result']
		parse2 = parse['musik']
	except:
		parse2 = 'Error URL atau Error API'
	await pesan.answer('Tunggu Sebentar, Perlu Download Dahulu!')
	await pesan.answer_audio(types.InputFile.from_url(parse2))

@disp.message_handler(commands=['nulis'])
async def nuliskanan(pesan : types.Message):
    tulisan = pesan.text.replace('/nulis','')
    await pesan.answer('Tunggu Sebentar!')
    await pesan.answer_photo(types.InputFile.from_url(f'https://rasenmedia.my.id/api/ngtdnulis?apikey=baka&text={tulisan}'))

button1 = KeyboardButton('𝗛𝗲𝗹𝗽 𝗕𝗼𝘁 🤖')
button2 = KeyboardButton('𝗠𝗲𝗻𝘂 𝗕𝗼𝘁🤖')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

@disp.message_handler(commands=['start', 'help'])
async def start_bot(pesan: types.Message):
	await pesan.reply('𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗮𝗹𝗮𝘀𝗕𝗼𝘁, 𝗦𝗲𝗹𝗲𝗰𝘁 𝗠𝗲𝗻𝘂 ❗',reply_markup=keyboard1)

@disp.message_handler()
async def keyboard_answer(pesan: types.Message):
    if pesan.text == '𝗛𝗲𝗹𝗽 𝗕𝗼𝘁 🤖':
    	await pesan.answer('''
    	 𝗠𝗮𝗹𝗮𝘀𝗕𝗼𝘁 - 𝗕𝗼𝘁 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺🤖
    	• 𝘮𝘦𝘮𝘶𝘥𝘢𝘩𝘬𝘢𝘯 𝘶𝘴𝘦𝘳 𝘫𝘪𝘬𝘢 𝘪𝘯𝘨𝘪𝘯
    	  𝘮𝘦𝘮𝘣𝘶𝘢𝘵 𝘣𝘰𝘵 𝘵𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘵𝘢𝘯𝘱𝘢 
    	  𝘱𝘦𝘳𝘭𝘶 𝘴𝘶𝘴𝘢𝘩² 𝘯𝘨𝘰𝘥𝘪𝘯𝘨.
    	  
    	𝗟𝗮𝗽𝗼𝗿📩
    	• 𝘫𝘪𝘬𝘢 𝘢𝘥𝘢 𝘦𝘳𝘳𝘰𝘳 𝘱𝘢𝘥𝘢 𝘣𝘰𝘵 𝘴𝘪𝘭𝘢𝘩𝘬𝘢𝘯
       𝘭𝘢𝘱𝘰𝘳 𝘥𝘪 𝘸𝘢.𝘮𝘦/6288226946972
    	
    	𝗪𝗲𝗯𝘀𝗶𝘁𝗲 & 𝗕𝗹𝗼𝗴 🌐
    	• www.malastech.my.id
    	• www.rasenmedia.my.id
    	
    	𝗖𝗼𝗱𝗲⚙️
    	• 𝘥𝘪𝘣𝘶𝘢𝘵 𝘥𝘦𝘯𝘨𝘢𝘯 𝘱𝘺𝘵𝘩𝘰𝘯
       𝘮𝘦𝘯𝘨𝘨𝘶𝘯𝘢𝘬𝘢𝘯 𝘮𝘰𝘥𝘶𝘭𝘦 𝘢𝘪𝘰𝘨𝘳𝘢𝘮
    	   
    	𝗪𝗮𝗿𝗻𝗶𝗻𝗴❗
    	• 𝘴𝘪𝘭𝘢𝘩𝘬𝘢𝘯 𝘦𝘥𝘪𝘵 𝘴𝘦𝘴𝘶𝘢𝘪 𝘬𝘢𝘭𝘪𝘢𝘯
    	  𝘵𝘢𝘱𝘪 𝘫𝘢𝘯𝘨𝘢𝘯 𝘩𝘪𝘭𝘢𝘯𝘨𝘬𝘢𝘯
       𝘤𝘳𝘦𝘢𝘵𝘰𝘳 𝘔𝘢𝘭𝘢𝘴𝘉𝘰𝘵
    	  
    	𝗞𝗼𝗻𝘁𝗿𝗶𝗯𝘂𝘁𝗼𝗿 𝗠𝗮𝗹𝗮𝘀𝗕𝗼𝘁🧑‍💻
    	• 𝘙𝘪𝘥𝘸𝘢𝘯 𝘕𝘢𝘻𝘢𝘳𝘶𝘥𝘪𝘯
    	• 𝘈𝘳𝘪𝘧 𝘙𝘢𝘩𝘮𝘢𝘯 𝘍𝘪𝘳𝘮𝘢𝘯𝘴𝘺𝘢𝘩
    	• 𝘔𝘶𝘩𝘢𝘮𝘮𝘢𝘥 𝘙𝘪𝘥𝘩𝘰 𝘐𝘭𝘢𝘩𝘪
    	
    	©2022 MalasBot - Telegram Bot.
    	
    	''')
    elif pesan.text == '𝗠𝗲𝗻𝘂 𝗕𝗼𝘁🤖':
    	await pesan.answer('''
    	🗒️ 𝗙𝗶𝘁𝘂𝗿 𝗕𝗼𝘁 𝗗𝗮𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗕𝗼𝘁 :
    		
    	𝗜𝗺𝗮𝗴𝗲 🖼️
    	
    	• Bot Nulis : /nulis (text)
    	• Quotes Creator V1 : /quote (kata)
    	• Quotes Creator V2 : /quote2 kata|wm
    	• Quotes Creator V3 /quote3 kata|wm
    	• TTS Font : /tts (text)
    	• Font Warna-Warni : /fww (text)
    	• Ephoto BlackPink : /ephoto (text)
    	• TextPro V1 : /textpro1 (text)
    	• TextPro V2 : /textpro2 (text)
    	• TextPro V3 : /textpro3 (text)
    	• Logo Ninja V1 : /logoninja (text)
    	• Logo Ninja V2 : /logoninja2 (text)
    	• Logo Ninja V3 : /logoninja3 (text)
    	• Text PornHub : /ph text1|text2
    		
    	𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 📁
    	
    	• Tiktok Download No WM : /tt (link)
    	• TT Musik Download : /ttmusik (link)
    	• IG Download (photo/video) : /igdl (link)
    	
    	𝗔𝗻𝗶𝗺𝗲 👩‍❤️‍👨
    	
    	• Random Gif Cium : /cium
    	• Random Gif Tampol : /tampol
    	• Random Gif Peluk : /peluk
    	• Wallpaper Anime : /wpanime
    	• Gambar Loli : /loli
    	• Random Foto Megumin : /megumin
    	• Random Foto Husbu : /husbu
    	
    	𝗦𝗲𝗻𝗲𝗻𝗴-𝗦𝗲𝗻𝗲𝗻𝗴😹
    	
    	• Random Foto Kucing : /kucing
    	• Dark Jokes /darkjokes
    	• Random Foto Cewe Cantik : /cecan
    	• Random Foto Anjing : /dog
    	• Arti Nama : /arti (namamu)
    	• Kata² Jaman Now : /qjamannow
    	• Random Foto Cosplay : /cosplay
    	
    	𝗣𝗲𝗻𝗴𝗲𝘁𝗮𝗵𝘂𝗮𝗻🙋
    	
    	• Search Wikipedia : /wiki (text)
    	• Fakta Unik : /faktaunik
    	• Kata Bijak : /katabijak
    	
    	𝗜𝘀𝗹𝗮𝗺𝗶🕌
  
       • Renungan Islam : /renungan
       • Random Doa : /doa
       • Asmaul Husna : /asmaulhusna
  
    	𝗠𝘂𝘀𝗶𝗸 🎵
    	
    	• Lirik Lagu : /lirik (judul lagu)
    	
    	𝗨𝗥𝗟 🌐
    	
    	• Short URL : /short (link)
    	• QR Code : /qr (link/tujuan)
    	
    	𝗛𝗮𝘀𝗵🔐
    	
    	• Base64 Encode : /b64encode (string)
    	• Base64 Decode : /b64decode (b64)
    	• Sha256 Encode : /sha256 (string)
    	• Md5 Encode : /md5 (string)
    	
    	
    	©2022 MalasBot - Telegram Bot.
    	''')
if __name__ == '__main__':
	executor.start_polling(disp,skip_updates=True)
