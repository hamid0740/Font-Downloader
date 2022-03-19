import requests
import os
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
print(color.purple + "Version:   " + color.reset + "1.2 beta")
print(color.purple + "Developer: " + color.reset + "hamid0740")
print(color.purple + "GitHub:    " + color.reset + "https://github.com/hamid0740/Font-Downloader" + "\n")

#Defining temporary variables for weight names
weights1 = ["Hairline", "Book", "Demi", "Regular", "Normal", "Text", "Medium", "Heavy", "Fat", "Poster"] #Weight names that don't ever get Extra or Ultra
weights2 = ["Thin", "Light", "Lite", "Thick", "Bold", "Dark", "Black"] #Weight names that may get Extra or Ultra
weights3 = ["Bold"] #Weight names that may get Semi or Demi
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

print(color.red + "✗ WRONG: https://example.com/font/Arial-Regular.ttf \n" + color.green + "✓ RIGHT: https://example.com/font/Arial- ")
main_url = input(color.yellow + "Enter the font file URL without weight name and file format: " + color.reset)
print(color.purple + "\n's' for Standard case (81 weight names)\n" + "'l' for Lower case (49 weight names)\n" + "'u' for Upper case (49 weight names)\n" + "'all' for All cases (179 weight names)\n" + color.blue + "You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.")
weights_case = input(color.yellow + "As you've inspected font URLs, how is their weight name case? " + color.reset)
weights = []
if "s" in weights_case.lower():
	weights += weights_standard
if "l" in weights_case.lower():
	weights += weights_lower
if "u" in weights_case.lower():
	weights += weights_upper
if weights_case.lower() == "all":
	weights = weights_standard + weights_lower + weights_upper
if "s" not in weights_case.lower() and "l" not in weights_case.lower() and "u" not in weights_case.lower():
	weights = weights_standard

font_name = main_url.split("/")[-1]
if font_name[-1] == "-" or font_name[-1] == "_" or font_name[-1] == " ":
	font_name = font_name[:-1]
if not os.path.exists(font_name):
	os.makedirs(font_name)
count = 0
count_d = 0
for j in range(len(formats)):
	if main_url[-1] == "-" or main_url[-1] == "_" or main_url[-1] == " ":
		url = main_url[:-1] + "." + formats[j]
	else:
		url = main_url + "." + formats[j]
	name = url.split("/")[len(url.split("/")) - 1]
	response = requests.head(url)
	if response.status_code == 200:
		request = requests.get(url, allow_redirects=True)
		open(font_name + "/" + name, 'wb').write(request.content)
		print(color.green + "[✓] " + name +" | Downloaded successfully!")
		count_d += 1
	elif response.status_code == 403:
		print(color.red + "[✗] " + name +" | (403) Access denied!")
	elif response.status_code == 404:
		print(color.red + "[✗] " + name +" | (404) Not found!")
	elif response.status_code == 408:
		print(color.red + "[✗] " + name +" | (408) Request time out!")
	else:
		print(color.red + "[✗]  " + name +" | (" + str(response.status_code) + ") There's a problem.")
	count += 1
for i in range(len(weights)):
	for j in range(len(formats)):
		url = main_url + weights[i] + "." + formats[j]
		name = url.split("/")[len(url.split("/")) - 1]
		response = requests.head(url)
		if response.status_code == 200:
			request = requests.get(url, allow_redirects=True)
			open(font_name + "/" + name, 'wb').write(request.content)
			print(color.green + "[✓] " + name +" | Downloaded successfully!")
			count_d += 1
		elif response.status_code == 403:
			print(color.red + "[✗] " + name +" | (403) Access denied!")
		elif response.status_code == 404:
			print(color.red + "[✗] " + name +" | (404) Not found!")
		elif response.status_code == 408:
			print(color.red + "[✗] " + name +" | (408) Request time out!")
		else:
			print(color.red + "[✗]  " + name +" | (" + str(response.status_code) + ") There's a problem.")
		count += 1

		
print(color.blue + "[!] Results: Successfully downloaded " + color.green + str(count_d) + " files" + color.blue + ", after inspecting " + str(count) + " files.")