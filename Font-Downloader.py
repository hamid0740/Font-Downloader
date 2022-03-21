import requests
import os
import time
from colorama import init, Fore, Back, Style
init()
	
#App info
print(Fore.MAGENTA + "App name:  " + Style.RESET_ALL + "Font Downloader")
print(Fore.MAGENTA + "Version:   " + Style.RESET_ALL + "1.7")
print(Fore.MAGENTA + "Developer: " + Style.RESET_ALL + "hamid0740")
print(Fore.MAGENTA + "GitHub:    " + Style.RESET_ALL + "https://github.com/hamid0740/Font-Downloader" + "\n")

speed_codes = ["2"]
print(Fore.GREEN + "code 1: " + Fore.RED + "Fastest speed, less accurate (default)\n" + Fore.GREEN + "code 2: " + Fore.RED + "Slower speed, more accurate")
speed = input(Fore.YELLOW + "Enter inspecting speed: " + Style.RESET_ALL)

#Defining temporary variables for weight names
##Weight names that don't ever get Extra or Ultra
weights1 = ["Hairline", "Line", "Book", "News", "Demi", "Regular", "Normal", "Text", "Medium", "Heavy", "Mass", "Fat", "Poster"]
if not speed in speed_codes:
	weights1 = [e for e in weights1 if e not in ["Line", "Book", "News", "Demi", "Normal", "Text", "Mass", "Poster"]]
	weights1.extend(["Thin"])
##Weight names that may get Extra, Ultra or Very
weights2 = ["Thin", "Light", "Lite", "Thick", "Bold", "Dark", "Black"]
if not speed in speed_codes:
	weights2 = [e for e in weights2 if e not in ["Thin", "Lite", "Thick", "Dark"]]
##Weight names that may get Semi or Demi
weights3 = ["Light", "Bold"]
if not speed in speed_codes:
	weights3 = [e for e in weights3 if e not in ["Light"]]
#Creating temp weight names that may get Extra, Ultra or Very
weights2_temp = []
for i in range(len(weights2)):
	weights2_temp.append(weights2[i])
	weights2_temp.append("Extra" + weights2[i])
	weights2_temp.append("Extra" + weights2[i].lower())
	weights2_temp.append("Ultra" + weights2[i])
	weights2_temp.append("Ultra" + weights2[i].lower())
	##Speed code 2
	if speed == "2":
		weights2_temp.append("Extra-" + weights2[i])
		weights2_temp.append("Extra-" + weights2[i].lower())
		weights2_temp.append("Ultra-" + weights2[i])
		weights2_temp.append("Ultra-" + weights2[i].lower())
		weights2_temp.append("Very" + weights2[i])
		weights2_temp.append("Very" + weights2[i].lower())
		weights2_temp.append("Very-" + weights2[i])
		weights2_temp.append("Very-" + weights2[i].lower())
#Creating temp weight names that may get Semi or Demi
weights3_temp = []
for i in range(len(weights3)):
	weights3_temp.append(weights3[i])
	weights3_temp.append("Semi" + weights3[i])
	weights3_temp.append("Semi" + weights3[i].lower())
	weights3_temp.append("Demi" + weights3[i])
	weights3_temp.append("Demi" + weights3[i].lower())
	##Speed code 2
	if speed == "2":
		weights3_temp.append("Semi-" + weights3[i])
		weights3_temp.append("Semi-" + weights3[i].lower())
		weights3_temp.append("Demi-" + weights3[i])
		weights3_temp.append("Demi-" + weights3[i].lower())

#Defining final variables
weights_standard = list(dict.fromkeys(weights1 + weights2_temp + weights3_temp))
weights_lower = list(dict.fromkeys([w.lower() for w in weights_standard]))
weights_upper = list(dict.fromkeys([w.upper() for w in weights_standard]))
formats = ["ttf", "woff", "woff2", "eot", "svg"]
if not speed in speed_codes:
	formats = [e for e in formats if e not in ["svg"]]

print(Fore.GREEN + "\nIf the font file URL is like this: " + Fore.RED + "'https://example.com/fonts/Arial/woff2/Arial-Bold.woff2'" + Fore.GREEN + ", you need to enter Font Name as " + Fore.RED + "'Arial'" + Fore.GREEN + ".\n" + "It can be used later as " + Fore.MAGENTA + "{NAME}")
font_name = input(Fore.YELLOW + "Enter the font name: " + Style.RESET_ALL)

print(Fore.CYAN + "\nFind a font file url in a website and enter it below. You can use variables below, in the url pattern. Also check the example below.\n" + Fore.MAGENTA + "{NAME}: The font name that you entered above.\n{WEIGHT}: Weight names that will be generated automatically.\n{FORMAT}: Font formats that will be generated automatically.\n" + Fore.RED + "✗ WRONG: https://example.com/fonts/Arial/woff2/Arial-Bold.woff2 \n" + Fore.GREEN + "✓ RIGHT: https://example.com/fonts/{NAME}/{FORMAT}/{NAME}-{WEIGHT}.{FORMAT} ")
pattern_url = input(Fore.YELLOW + "Enter the font file URL pattern: " + Style.RESET_ALL)
print(Fore.MAGENTA + "\n's' for Standard case (" + str(len(weights_standard)) + " weight names)\n" + "'l' for Lower case (" + str(len(weights_lower)) + " weight names)\n" + "'u' for Upper case (" + str(len(weights_upper)) + " weight names)\n" + "'all' for All cases (" + str(len(weights_standard) + len(weights_lower) + len(weights_upper)) + " weight names)\n" + Fore.CYAN + "You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.")
weights_case = input(Fore.YELLOW + "As you've inspected font URLs, how is their weight name case? " + Style.RESET_ALL)
weights = []
if "all" in weights_case.lower():
	weights = weights_standard + weights_lower + weights_upper
if "s" in weights_case.lower() and not "all" in weights_case.lower():
	weights += weights_standard
if "l" in weights_case.lower() and not "all" in weights_case.lower():
	weights += weights_lower
if "u" in weights_case.lower() and not "all" in weights_case.lower():
	weights += weights_upper
if "s" not in weights_case.lower() and "l" not in weights_case.lower() and "u" not in weights_case.lower() and not "all" in weights_case.lower():
	weights = weights_standard
print("")

#Download function
count = 0
count_d = 0
r_headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36", "referer": "https://github.com/hamid0740/Font-Downloader" }
def dl(url):
	global count
	global count_d
	name = url.split("/")[len(url.split("/")) - 1]
	response = requests.head(url, allow_redirects = True, headers = r_headers)
	if not os.path.exists(font_name + "/" + font_name + "-Links.txt"):
		open(font_name + "/" + font_name + "-Links.txt", "a").write("")
	if not os.path.exists(font_name + "/" + font_name + "-Links-All.txt"):
		open(font_name + "/" + font_name + "-Links-All.txt", "a").write("")
	if response.status_code in range(200, 299) and not response.headers.get("content-type") in ["text/html"]:
		if not url.lower() in open(font_name + "/" + font_name + "-Links.txt", "r").read().lower():
			request = requests.get(url, allow_redirects = True, headers = r_headers)
			open(font_name + "/" + name, "wb").write(request.content)
			print(Fore.GREEN + "[✓] " + name +" | Downloaded!")
			open(font_name + "/" + font_name + "-Links.txt", "a").write(url + "\n")
			count_d += 1
		else:
			print(Fore.MAGENTA + "[!] " + name +" | File already exists!")
	elif response.status_code == 403:
		print(Fore.RED + "[✗] " + name +" | (403) Access denied!")
	elif response.status_code == 404:
		print(Fore.RED + "[✗] " + name +" | (404) Not found!")
	elif response.status_code == 408:
		print(Fore.RED + "[✗] " + name +" | (408) Request time out!")
	elif response.headers.get("content-type") in ["text/html"]:
		print(Fore.RED + "[✗] " + name +" | Returned HTML page!")
	else:
		print(Fore.RED + "[✗] " + name +" | (" + str(response.status_code) + ") Problem!")
	open(font_name + "/" + font_name + "-Links-All.txt", "a").write(url + "\n")
	count += 1

#Starting inspection and downloading process
if not os.path.exists(font_name):
	os.makedirs(font_name)
open(font_name + "/" + font_name + "-Links.txt", "w").write("")
open(font_name + "/" + font_name + "-Links-All.txt", "w").write("")
#Check for font file without any weight name (as Regular weight)
start_time = time.time_ns()
for j in range(len(formats)):
	url = pattern_url.replace("{NAME}", font_name).replace("{WEIGHT}", "").replace("{FORMAT}", formats[j])
	url = url.replace("-.", ".").replace("_.", ".").replace(" .", ".")
	dl(url)
#Check for selected weight names
for i in range(len(weights)):
	for j in range(len(formats)):
		url = pattern_url.replace("{NAME}", font_name).replace("{WEIGHT}", weights[i]).replace("{FORMAT}", formats[j])
		dl(url)
end_time = time.time_ns()
processing_time = (end_time - start_time) / (10**9)
pt_min, pt_sec = divmod(processing_time, 60)
pt_sec = round(pt_sec, 2)
#remove extra empty line in Links.txt file
l_text = open(font_name + "/" + font_name + "-Links.txt", "r").read().rstrip()
open(font_name + "/" + font_name + "-Links.txt", "w").write(l_text)
#remove extra empty line in Links-all.txt file
la_text = open(font_name + "/" + font_name + "-Links-All.txt", "r").read().rstrip()
open(font_name + "/" + font_name + "-Links-All.txt", "w").write(la_text)

print(Fore.YELLOW + "\n[!] Results:")
if pt_min == 0:
	print(Fore.CYAN + "[!] Processing time: " + Fore.YELLOW + str(pt_sec) + " seconds")
else:
	print(Fore.CYAN + "[!] Processing time: " + Fore.YELLOW + str(int(pt_min)) + " minutes and " + str(pt_sec) + " seconds")
print(Fore.CYAN + "[!] Downloaded: " + Fore.YELLOW + str(count_d) + " files")
print(Fore.CYAN + "[!] Inspected: " + Fore.YELLOW + str(count) + " files")