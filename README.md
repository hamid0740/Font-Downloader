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
   's' for Standard case (81 weight names)
   'l' for Lower case (49 weight names)
   'u' for Upper case (49 weight names)
   'all' for All cases (179 weight names)
   ```
   You can combine letters for combined cases. like 'lu' to have Lower and Upper cases.

5. Now you're done. Just wait to finish the inspection.

## To-Do list (Maybe one day...)
* [X] Display the processing time (v1.3)
* [X] Make a file including all downloaded files links. (v1.3)
* [ ] Asking user for weight name place and format place in the url input as `{WEIGHT}` and `{FORMAT}`
* [ ] Ability to download fonts which are separated by their format into different folders.
* Give me ideas to make it better :)

## Output
After the process finishes, there will be a folder in the same directory as the code file, including every font file downloaded. There will also be a text file named `FONTNAME-Links.txt` that includes the link of all downloaded files.
