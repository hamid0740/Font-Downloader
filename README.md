# Font Downloader
This is a python script, that helps you with inspecting and downloading all weights of a font which is hosted on a website.

Read the [instructions](#instructions), to learn how to use it.

### Screenshot
![Screenshot](https://i.ibb.co/PrKmBvC/Font-Downloader-screenshot.jpg)
**Note:** Code is edited during screenshot to make its height smaller.

## Instructions
1. Download and install Termux from [here](https://f-droid.org/en/packages/com.termux). You'll also need to have Python language installed and also have `requests` and `colorama` libraries for it. Read [here](https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/) to learn how to install these libraries.

2. Run codes below in Termux:
   ```
   pkg install python
   pip install requests
   pip install colorama
   termux-setup-storage
   cd /path/to/code
   python Font-Downloader.py
   ```

3. In the 1st input you need to define what speed do you want the script to inspect font weights. Speed `1` is approximately 4 times faster than Speed `2`; as a result it will be less accurate.

4. In the 2nd input, you need to enter the font name used in the font file url. If the font file URL is like this: `https://example.com/fonts/Arial/woff2/Arial-Bold.woff2`, you need to enter Font Name as `Arial`.
   It will be used later as `{NAME}`.

5. In the 3rd input, you need to enter the font file URL pattern. Find a font file URL in a website and replace some strings with variables below.
   ```
   {NAME}: The font name that you've entered before.
   {WEIGHT}: Weight names that will be generated automatically.
   {FORMAT}: Font formats that will be generated automatically.
   ```
   Example:
   ```
   ✗ WRONG: https://example.com/fonts/Arial/woff2/Arial-Bold.woff2
   ✓ RIGHT: https://example.com/fonts/{NAME}/{FORMAT}/{NAME}-{WEIGHT}.{FORMAT}
   ```

6. For the 4th input, you need to enter the weight names case according to your inspections. If you haven't inspected, enter `all` and it will test everything.
   ```
   's' for Standard case (25-120 weight names)
   'l' for Lower case (17-70 weight names)
   'u' for Upper case (17-70 weight names)
   'all' for All cases (59-260 weight names)
   ```
   You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.

7. Now you're done. Just wait to finish the inspection.

## To-Do list
* [ ] Preventing crashes and show an error message instead. (Maybe later...)
* Give me ideas to make this script better :)

## Datas
### Font weight names
These are by my researches through many font families.
* Never get any prefixes:

  **(Speed 1)**
  ```
  Thin
  Hairline
  Regular
  Medium
  Heavy
  Fat
  ```
  **(Speed 2)**
  ```
  Hairline
  Line
  Book
  News
  Demi
  Regular
  Normal
  Text
  Medium
  Heavy
  Mass
  Fat
  Poster
  ```
* May get Extra, Ultra or Very:

  **(Speed 1)** no Very
  ```
  Light
  Bold
  Black
  ```
  **(Speed 2)**
  ```
  Thin
  Light
  Lite
  Thick
  Bold
  Dark
  Black
  ```
* May get Semi or Demi:

  **(Speed 1)**
  ```
  Bold
  ```
  **(Speed 2)**
  ```
  Light
  Bold
  ```
### Formats
These font formats will be inspected by the code:
```
eot
otf (Speed 2)
svg (Speed 2)
ttf
woff
woff2
```

## Output
After the process finishes, there will be a folder in the same directory as the code file, including every font file downloaded in separated folders by their font format. There will also be a text file named `FONTNAME-Links.txt` that includes the link of all downloaded files.
Another text file named `FONTNAME-Links-All.txt` exists, that contains every inspected link, even if not downloaded. This will help those who want to test the links manually using a download manager.
