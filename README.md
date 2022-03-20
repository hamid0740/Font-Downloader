# Font-Downloader
This is python source code, that helps you to check for all weights of a font which is hosted in a website.

Read the [instructions](#instructions), to learn how to use it.

### Screenshot
![Screenshot](https://i.ibb.co/hLdwthY/Font-Downloader-screenshot.jpg)

## Instructions
1. Downloas and install Termux from [here](https://f-droid.org/en/packages/com.termux)

2. Run codes below in Termux:
   ```
   pkg install python
   pip install requests
   termux-setup-storage
   cd /path/to/code
   python Font-Downloader.py
   ```

3. In the first input, you need to enter the font file url that you've found, but without weight name and foemat name (this method will be fixed in the next update).

   Make sure to enter the exact url like below:
   ```
   ✗ WRONG: https://example.com/font/Arial-Regular.ttf
   ✓ RIGHT: https://example.com/font/Arial-
   ```

4. For the second input, you need to enter the weight names case according to your inspections. If you haven't inspected, enter `all` and it will test everything.
   ```
   's' for Standard case (120 weight names)
   'l' for Lower case (70 weight names)
   'u' for Upper case (70 weight names)
   'all' for All cases (260 weight names)
   ```
   You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.

5. Now you're done. Just wait to finish the inspection.

## To-Do list (Maybe one day...)
* [X] Display the processing time (v1.3)
* [X] Make a file including all downloaded files links. (v1.3)
* [ ] Asking user for weight name place and format place in the url input as `{WEIGHT}` and `{FORMAT}`
* [ ] Ability to download fonts which are separated by their format into different folders.
* Give me ideas to make it better :)

## Datas
### Font weight names
These are by my researches through many font families.
* Never get anything:
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
  ```
  Thin
  Light
  Lite
  Thick
  Bold
  Dark
  Black
  ```
* May get Semi or Demi
  ```
  Light
  Bold
  ```
### Formats
These formats will be inspected by the code.
```
ttf
woff
woff2
eot
svg
```

## Output
After the process finishes, there will be a folder in the same directory as the code file, including every font file downloaded. There will also be a text file named `FONTNAME-Links.txt` that includes the link of all downloaded files.
There will be another text file named `FONTNAME-Links-All.txt` that contains every inspected link, even if not downloaded. This will help those who want to test the links manually with a download manager.
