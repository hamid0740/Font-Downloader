import requests
import os
import time
#Color for texts
class color:
	red = "\33[91m"
	green = "\33[92m"
	yellow = "\33[93m"
	purple = "\33[95m"
	blue = "\33[96m"
	reset = "\33[0m"
	
#App info
print(color.purple + "App name:  " + color.reset + "Font Downloader")
print(color.purple + "Version:   " + color.reset + "1.5")
print(color.purple + "Developer: " + color.reset + "hamid0740")
print(color.purple + "GitHub:    " + color.reset + "https://github.com/hamid0740/Font-Downloader" + "\n")

#Defining temporary variables for weight names
weights1 = ["Hairline", "Line", "Book", "News", "Demi", "Regular", "Normal", "Text", "Medium", "Heavy", "Mass", "Fat", "Poster"] #Weight names that don't ever get Extra or Ultra
weights2 = ["Thin", "Light", "Lite", "Thick", "Bold", "Dark", "Black"] #Weight names that may get Extra or Ultra
weights3 = ["Light", "Bold"] #Weight names that may get Semi or Demi
weights2_temp = []
for i in range(len(weights2)):
	weights2_temp.append(weights2[i])
	weights2_temp.append("Extra" + weights2[i])
	weights2_temp.append("Extra" + weights2[i].lower())
	weights2_temp.append("Extra-" + weights2[i])
	weights2_temp.append("Extra-" + weights2[i].lower())
	weights2_temp.append("Ultra" + weights2[i])
	weights2_temp.append("Ultra" + weights2[i].lower())
	weights2_temp.append("Ultra-" + weights2[i])
	weights2_temp.append("Ultra-" + weights2[i].lower())
	weights2_temp.append("Very" + weights2[i])
	weights2_temp.append("Very" + weights2[i].lower())
	weights2_temp.append("Very-" + weights2[i])
	weights2_temp.append("Very-" + weights2[i].lower())
weights3_temp = []
for i in range(len(weights3)):
	weights3_temp.append(weights3[i])
	weights3_temp.append("Semi" + weights3[i])
	weights3_temp.append("Semi" + weights3[i].lower())
	weights3_temp.append("Semi-" + weights3[i])
	weights3_temp.append("Semi-" + weights3[i].lower())
	weights3_temp.append("Demi" + weights3[i])
	weights3_temp.append("Demi" + weights3[i].lower())
	weights3_temp.append("Demi-" + weights3[i])
	weights3_temp.append("Demi-" + weights3[i].lower())

#Defining final variables
weights_standard = list(dict.fromkeys(weights1 + weights2_temp + weights3_temp))
weights_lower = list(dict.fromkeys([w.lower() for w in weights_standard]))
weights_upper = list(dict.fromkeys([w.upper() for w in weights_standard]))
formats = ["ttf", "woff", "woff2", "eot", "svg"]

print(color.green + "If the font file URL is like this: " + color.red + "'https://example.com/fonts/Arial/woff2/Arial-Bold.woff2'" + color.green + ", you need to enter Font Name as " + color.red + "'Arial'" + color.green + ".\n" + "It can be used later as " + color.purple + "{NAME}")
font_name = input(color.yellow + "Enter the font name: " + color.reset)

print(color.blue + "\nFind a font file url in a website and enter it below. You can use variables below, in the url pattern. Also check the example below.\n" + color.purple + "{NAME}: The font name that you entered above.\n{WEIGHT}: Weight names that will be generated automatically.\n{FORMAT}: Font formats that will be generated automatically.\n" + color.red + "✗ WRONG: https://example.com/fonts/Arial/woff2/Arial-Bold.woff2 \n" + color.green + "✓ RIGHT: https://example.com/fonts/{NAME}/{FORMAT}/{NAME}-{WEIGHT}.{FORMAT} ")
pattern_url = input(color.yellow + "Enter the font file URL pattern: " + color.reset)
print(color.purple + "\n's' for Standard case (120 weight names)\n" + "'l' for Lower case (70 weight names)\n" + "'u' for Upper case (70 weight names)\n" + "'all' for All cases (260 weight names)\n" + color.blue + "You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.")
weights_case = input(color.yellow + "As you've inspected font URLs, how is their weight name case? " + color.reset)
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
def dl(url):
	global count
	global count_d
	name = url.split("/")[len(url.split("/")) - 1]
	response = requests.head(url, allow_redirects = True)
	if not os.path.exists(font_name + "/" + font_name + "-Links.txt"):
		open(font_name + "/" + font_name + "-Links.txt", "a").write("")
	if not os.path.exists(font_name + "/" + font_name + "-Links-All.txt"):
		open(font_name + "/" + font_name + "-Links-All.txt", "a").write("")
	if response.status_code in range(200, 299) and not response.headers["content-type"] in ["text/html"]:
		if not url.lower() in open(font_name + "/" + font_name + "-Links.txt").read().lower():
			request = requests.get(url, allow_redirects = True)
			open(font_name + "/" + name, 'wb').write(request.content)
			print(color.green + "[✓] " + name +" | Downloaded!")
			open(font_name + "/" + font_name + "-Links.txt", "a").write(url + "\n")
			count_d += 1
		else:
			print(color.purple + "[!] " + name +" | File already exists!")
	elif response.status_code == 403:
		print(color.red + "[✗] " + name +" | (403) Access denied!")
	elif response.status_code == 404:
		print(color.red + "[✗] " + name +" | (404) Not found!")
	elif response.status_code == 408:
		print(color.red + "[✗] " + name +" | (408) Request time out!")
	elif response.headers["content-type"] in ["text/html"]:
		print(color.red + "[✗] " + name +" | Returned HTML page!")
	else:
		print(color.red + "[✗] " + name +" | (" + str(response.status_code) + ") Problem!")
	open(font_name + "/" + font_name + "-Links-All.txt", "a").write(url + "\n")
	count += 1

#Starting inspection and downloading process
if not os.path.exists(font_name):
	os.makedirs(font_name)
if os.path.exists(font_name + "/" + font_name + "-Links.txt"):
	open(font_name + "/" + font_name + "-Links.txt", "r+").truncate(0)
if os.path.exists(font_name + "/" + font_name + "-Links-All.txt"):
	open(font_name + "/" + font_name + "-Links-All.txt", "r+").truncate(0)
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
with open(font_name + "/" + font_name + "-Links.txt", "r+") as links_file:
	links_txt = links_file.read().rstrip()
	links_file.truncate(0)
	links_file.write(links_txt)
#remove extra empty line in Links-all.txt file
with open(font_name + "/" + font_name + "-Links-All.txt", "r+") as links_all_file:
	links_all_txt = links_all_file.read().rstrip()
	links_all_file.truncate(0)
	links_all_file.write(links_all_txt)

print(color.yellow + "\n[!] Results:")
if pt_min == 0:
	print(color.blue + "[!] Processing time: " + color.yellow + str(pt_sec) + " seconds")
else:
	print(color.blue + "[!] Processing time: " + color.yellow + str(int(pt_min)) + " minutes and " + str(pt_sec) + " seconds")
print(color.blue + "[!] Downloaded: " + color.yellow + str(count_d) + " files")
print(color.blue + "[!] Inspected: " + color.yellow + str(count) + " files")