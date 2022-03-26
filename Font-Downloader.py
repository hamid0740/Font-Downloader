import requests
import os
import time
from colorama import init, Fore, Back, Style
os.system("cls" if os.name=="nt" else "clear")
init()

#App title and info
print(               "               " + Fore.CYAN + " ___        _   " + ""          + "                ")
print(Fore.YELLOW  + "     Dev:      " + Fore.CYAN + "| __|__ _ _| |_ " + Fore.YELLOW + "    Version:    ")
print(Fore.GREEN   + "   hamid0740   " + Fore.CYAN + "| _/ _ \ ' \  _|" + Fore.GREEN  + "      1.9       ")
print(               "               " + Fore.CYAN + "|_|\___/_||_\__|" + ""          + "                ")
print(Fore.CYAN    + " ___                  _              _         ")
print(Fore.CYAN    + "|   \ _____ __ ___ _ | |___  __ _ __| |___ _ _ ")
print(Fore.CYAN    + "| |) / _ \ V  V / ' \| / _ \/ _` / _` / -_) '_|")
print(Fore.CYAN    + "|___/\___/\_/\_/|_||_|_\___/\__,_\__,_\___|_|  ")
print(Fore.MAGENTA + "  https://github.com/hamid0740/Font-Downloader " + "\n")

#Asking inspection speed
speed_codes = ["2"]
print(Fore.GREEN + "code 1: " + Fore.RED + "Fastest speed, least accurate (Default)\n" + Fore.GREEN + "code 2: " + Fore.RED + "Slower speed, more accurate")
print(Fore.YELLOW + "Enter inspection speed:" + Style.RESET_ALL, end = " ")
speed = input()

#Defining temporary variables for weight names
##Weight names that don't ever get Extra, Ultra, Very, Semi or Demi
weights1 = ["Hairline", "Line", "Book", "News", "Demi", "Regular", "Normal", "Text", "Medium", "Heavy", "Mass", "Fat", "Poster"]
##Weight names that may get Extra, Ultra or Very
weights2 = ["Thin", "Light", "Lite", "Thick", "Bold", "Dark", "Black"]
##Weight names that may get Semi or Demi
weights3 = ["Light", "Bold"]
#Creating temporary weight names that may get Extra, Ultra or Very
weights2_temp = []
for i in range(len(weights2)):
	weights2_temp.append(weights2[i])
	weights2_temp.append("Extra" + weights2[i])
	weights2_temp.append("Extra" + weights2[i].lower())
	weights2_temp.append("Ultra" + weights2[i])
	weights2_temp.append("Ultra" + weights2[i].lower())
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
	weights3_temp.append("Semi-" + weights3[i])
	weights3_temp.append("Semi-" + weights3[i].lower())
	weights3_temp.append("Demi-" + weights3[i])
	weights3_temp.append("Demi-" + weights3[i].lower())

#Defining font formats
formats = ["eot", "otf", "svg", "ttf", "woff", "woff2"]

#Asking font name
print(Fore.GREEN + "\nThis name will be used to save font files as.")
print(Fore.YELLOW + "Enter the font name:" + Style.RESET_ALL, end = " ")
font_name = input()

#Asking font file URL
print(Fore.CYAN + "\nFind a font file URL in a website and enter it below. You may use these variables to create the URL pattern yourself.\n" + Fore.MAGENTA + "{WEIGHT}: Thin, Regular, Bold ...\n{FORMAT}: eot, ttf, woff2 ...\n" + Fore.RED + "Direct: " + Fore.GREEN + "https://example.com/fonts/Arial/woff2/Arial-Bold.woff2\n" + Fore.RED + "Pattern: " + Fore.GREEN + "https://example.com/fonts/Arial/{FORMAT}/Arial-{WEIGHT}.{FORMAT}")
print(Fore.YELLOW + "Enter the font file Direct or Pattern URL:" + Style.RESET_ALL, end = " ")
pattern_url = input()

#Creating pattern URL
for i in range(len(weights1)):
	pattern_url = pattern_url.replace(weights1[i], "{WEIGHT}")
for i in range(len(weights2)):
	pattern_url = pattern_url.replace(weights2[i], "{WEIGHT}")
for i in range(len(weights3)):
	pattern_url = pattern_url.replace(weights3[i], "{WEIGHT}")
frmts_rplc = ["eot", "otf", "svg", "ttf", "woff2", "woff"]
for i in range(len(frmts_rplc)):
	pattern_url = pattern_url.replace(frmts_rplc[i], "{FORMAT}")

#Applying speed code
if not speed in speed_codes:
	weights1 = [e for e in weights1 if e not in ["Line", "Book", "News", "Demi", "Normal", "Text", "Mass", "Poster"]]
	#weights1.extend(["Thin"])
	weights2 = [e for e in weights2 if e not in ["Thin", "Lite", "Thick", "Dark"]]
	weights3 = [e for e in weights3 if e not in ["Light"]]
	formats = [e for e in formats if e not in ["otf", "svg"]]
for i in range(len(weights2)):
	if not speed in speed_codes:
		weights2_temp.remove("Extra-" + weights2[i])
		weights2_temp.remove("Extra-" + weights2[i].lower())
		weights2_temp.remove("Ultra-" + weights2[i])
		weights2_temp.remove("Ultra-" + weights2[i].lower())
		weights2_temp.remove("Very" + weights2[i])
		weights2_temp.remove("Very" + weights2[i].lower())
		weights2_temp.remove("Very-" + weights2[i])
		weights2_temp.remove("Very-" + weights2[i].lower())
for i in range(len(weights3)):
	if not speed in speed_codes:
		weights3_temp.remove("Semi-" + weights3[i])
		weights3_temp.remove("Semi-" + weights3[i].lower())
		weights3_temp.remove("Demi-" + weights3[i])
		weights3_temp.remove("Demi-" + weights3[i].lower())

#Defining final weight names
weights_standard = list(dict.fromkeys(weights1 + weights2_temp + weights3_temp))
weights_lower = list(dict.fromkeys([w.lower() for w in weights_standard]))
weights_upper = list(dict.fromkeys([w.upper() for w in weights_standard]))

#Asking weight names case
print(Fore.MAGENTA + "\n's' for Standard case (" + str(len(weights_standard)) + " weight names)\n" + "'l' for Lower case (" + str(len(weights_lower)) + " weight names)\n" + "'u' for Upper case (" + str(len(weights_upper)) + " weight names)\n" + "'all' for All cases (" + str(len(weights_standard) + len(weights_lower) + len(weights_upper)) + " weight names)\n" + Fore.CYAN + "You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.")
print(Fore.YELLOW + "As you've inspected font URLs, how is their weight name case?" + Style.RESET_ALL, end = " ")
weights_case = input()
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

#Generate links for inspection
if not os.path.exists(font_name):
	os.makedirs(font_name)
links = []
links_format = []
for j in range(len(formats)):
	url = pattern_url.replace("{WEIGHT}", "").replace("{FORMAT}", formats[j])
	url = url.replace("-." + formats[j], "." + formats[j]).replace("_." + formats[j], "." + formats[j]).replace(" ." + formats[j], "." + formats[j])
	links.append(url)
	links_format.append(formats[j])
for i in range(len(weights)):
	for j in range(len(formats)):
		url = pattern_url.replace("{WEIGHT}", weights[i]).replace("{FORMAT}", formats[j])
		links.append(url)
		links_format.append(formats[j])
##Writing links in Links-All.txt
links_text = ""
for i in range(len(links)):
	links_text += links[i] + "\n"
open(font_name + "/" + font_name + "-Links-All.txt", "w").write(links_text.rstrip())

#Download function
count = 0
r_headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36", "referer": "https://github.com/hamid0740/Font-Downloader" }
def dl(url, frmt):
	global count
	name = url.split("/")[-1]
	response = requests.head(url, allow_redirects = True, headers = r_headers)
	r_sc = response.status_code
	r_ct = response.headers.get("content-type")
	if r_sc in range(200, 299) and not r_ct in ["text/html"]:
		if not url.lower() in open(font_name + "/" + font_name + "-Links.txt", "r").read().lower():
			request = requests.get(url, allow_redirects = True, headers = r_headers)
			open(font_name + "/" + frmt + "/" + name, "wb").write(request.content)
			print(Fore.GREEN + "[✓] " + name +" | Downloaded!")
			open(font_name + "/" + font_name + "-Links.txt", "a").write(url + "\n")
			count += 1
		else:
			print(Fore.MAGENTA + "[!] " + name +" | File already exists!")
	elif r_sc == 403:
		print(Fore.RED + "[X] " + name +" | (403) Access denied!")
	elif r_sc == 404:
		print(Fore.RED + "[X] " + name +" | (404) Not found!")
	elif r_sc == 408:
		print(Fore.RED + "[X] " + name +" | (408) Request timed out!")
	elif r_ct in ["text/html"]:
		print(Fore.RED + "[X] " + name +" | Returned HTML page!")
	else:
		print(Fore.RED + "[X] " + name +" | (" + str(r_sc) + ") Problem!")

#Starting inspection and downloading process
open(font_name + "/" + font_name + "-Links.txt", "w").write("")
for j in range(len(formats)):
	if not os.path.exists(font_name + "/" + formats[j]):
		os.makedirs(font_name + "/" + formats[j])

#Checking and downloading links that were generated before
start_time = time.time_ns()
for i in range(len(links)):
	dl(links[i], links_format[i])
end_time = time.time_ns()

#Counting processing time
processing_time = (end_time - start_time) / (10**9)
pt_min, pt_sec = divmod(processing_time, 60)
pt_sec = round(pt_sec, 2)

#Removing extra empty lines in Links.txt file
l_text = open(font_name + "/" + font_name + "-Links.txt", "r").read().rstrip()
open(font_name + "/" + font_name + "-Links.txt", "w").write(l_text)

#Removing empty font format folders
for j in range(len(formats)):
	if not os.listdir(font_name + "/" + formats[j]):
		os.rmdir(font_name + "/" + formats[j])

#Showing results
print(Fore.YELLOW + "\n[!] Results:")
if pt_min == 0:
	print(Fore.CYAN + "[!] Processing time: " + Fore.YELLOW + str(pt_sec) + " seconds")
else:
	print(Fore.CYAN + "[!] Processing time: " + Fore.YELLOW + str(int(pt_min)) + " minutes and " + str(pt_sec) + " seconds")
print(Fore.CYAN + "[!] Downloaded: " + Fore.YELLOW + str(count) + " files")
print(Fore.CYAN + "[!] Inspected: " + Fore.YELLOW + str(len(links)) + " files")