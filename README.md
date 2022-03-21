# Font-Downloader
This is a python source code, that helps you with checking all weights of a font which is hosted in a website.

Read the [instructions](#instructions), to learn how to use it.

### Screenshot
![Screenshot](https://i.ibb.co/SRFTxt7/Font-Downloader-screenshot.jpg)

## Instructions
1. Download and install Termux from [here](https://f-droid.org/en/packages/com.termux).

2. Run codes below in Termux:
   ```
   pkg install python
   pip install requests
   termux-setup-storage
   cd /path/to/code
   python Font-Downloader.py
   ```

3. In the first input, you need to enter the font name used in the font file url. If the font file URL is like this: `https://example.com/fonts/Arial/woff2/Arial-Bold.woff2`, you need to enter Font Name as `Arial`.
   It will be used later as `{NAME}`.

4. In the second input, you need to enter the font file URL pattern. Find a font file URL in a website and replace some strings with variables below.
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

5. For the second input, you need to enter the weight names case according to your inspections. If you haven't inspected, enter `all` and it will test everything.
   ```
   's' for Standard case (120 weight names)
   'l' for Lower case (70 weight names)
   'u' for Upper case (70 weight names)
   'all' for All cases (260 weight names)
   ```
   You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.

6. Now you're done. Just wait to finish the inspection.

## To-Do list (Maybe one day...)
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
* May get Semi or Demi:
  ```
  Light
  Bold
  ```
### Formats
These formats will be inspected by the code:
```
ttf
woff
woff2
eot
svg
```

## Output
After the process finishes, there will be a folder in the same directory as the code file, including every font file downloaded. There will also be a text file named `FONTNAME-Links.txt` that includes the link of all downloaded files.
Another text file named `FONTNAME-Links-All.txt` exists, that contains every inspected link, even if not downloaded. This will help those who want to test the links manually using a download manager.
