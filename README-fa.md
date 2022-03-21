<div dir=rtl>

# فونت دانلودر
این یک سورس کد پایتون هست که به شما در کاوش کردن و دانلود همه وزن‌های یک فونت که در وبسایتی میزبانی می‌شوند کمک می‌کند.

برای یادگیری استفاده از این کد، [دستورالعمل](#دستورالعمل) را بخوانید.

### اسکرین‌شات
![اسکرین‌شات](https://i.ibb.co/PrKmBvC/Font-Downloader-screenshot.jpg)
**نکته:** برای گرفتن اسکرین‌شات، کد ویرایش شده است تا ارتفاع تصویر کمتر شود.

## دستورالعمل
1. ترموکس را از [اینجا](https://f-droid.org/en/packages/com.termux) دانلود و نصب کنید. همچنین شما باید زبان پایتون را نصب کرده باشید‌ و کتابخانه‌های `requests` و `colorama` را نیز برای آن داشته باشید. برای یادگیری چگونگی نصب این کتابخانه‌ها، [اینجا](https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/) را بخوانید.

2. کدهای زیر را ترموکس اجرا کنید:
   ```
   pkg install python
   pip install requests
   pip install colorama
   termux-setup-storage
   cd /path/to/code
   python Font-Downloader.py
   ```

3. در اولین ورودی باید مشخص کنید که کد، با چه سرعتی وزن‌های فونت را کاوش کند. سرعت `1` تقریباً ۴ برابر سریع‌تر از سرعت `2` است؛ در نتیجه دقت آن کمتر خواهد بود.

4. در دومین ورودی باید نام فونتی که در URL فایل فونت استفاده شده را مشخص کنید. اگر URL فایل فونت بدین صورت باشد: `https://example.com/fonts/Arial/woff2/Arial-Bold.woff2`، شما باید نام فونت را بصورت `Arial` وارد کنید.
   این نام بعداً به عنوان `{NAME}` استفاده خواهد شد.


5. در سومین ورودی باید URL الگوی فایل فونت را وارد کنید. یک لینک فایل فونت را در وبسایتی بیابید و برخی از مقادیر آن را با متغیرهای زیر جایگزین کنید.
   ```
   {NAME}: The font name that you've entered before.
   {WEIGHT}: Weight names that will be generated automatically.
   {FORMAT}: Font formats that will be generated automatically.
   ```
   مثال:
   ```
   ✗ WRONG: https://example.com/fonts/Arial/woff2/Arial-Bold.woff2
   ✓ RIGHT: https://example.com/fonts/{NAME}/{FORMAT}/{NAME}-{WEIGHT}.{FORMAT}
   ```

6. برای چهارمین ورودی باید کوچک یا بزرگی حروف اسم وزن‌ها را با توجه به بررسی‌های خودتان در لینک فونت‌ها مشخص کنید. اگر بررسی انجام نداده‌اید، `all` را وارد کنید تا همه چیز تست شود.
   ```
   's' for Standard case (25-120 weight names)
   'l' for Lower case (17-70 weight names)
   'u' for Upper case (17-70 weight names)
   'all' for All cases (59-260 weight names)
   ```
   شما می‌توانید حروف را ترکیب کنید تا کوچک بزرگی ترکیبی داشته باشید. برای مثال با وارد کردن `lu` می‌توانید هم حروف کوچک و هم حروف بزرگ را برای کاوش کردن انتخاب کنید.

7. اکنون کار شما تمام شده است. فقط تا پایان کاوش صبر کنید.

## لیست برای-انجام
* به من ایده بدهید تا آن را کامل کنم :)

## داده‌ها
### اسامی وزن فونت
این‌ها با توجه به تحقیقات من در خانواده فونت‌های مختلف هستند.
* هیچ‌وقت چیزی نمیگیرند:

  **(سرعت 1)**
  ```
  Thin
  Hairline
  Regular
  Medium
  Heavy
  Fat
  ```
  **(سرعت 2)**
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
* ممکن است Extra، Ultra یا Very بگیرند:

  **(سرعت 1)** Very نمی‌گیرند
  ```
  Light
  Bold
  Black
  ```
  **(سرعت 2)**
  ```
  Thin
  Light
  Lite
  Thick
  Bold
  Dark
  Black
  ```
* ممکن است Semi یا Demi بگیرند:

  **(سرعت 1)**
  ```
  Bold
  ```
  **(سرعت 2)**
  ```
  Light
  Bold
  ```
### فرمت‌ها
این فرمت‌ها توسط کد کا‌وش خواهند شد:
```
ttf
woff
woff2
eot
svg (سرعت 2)
```

## خروجی
وقتی پروسه کامل شود، یک فولدر در محلی که فایل کد قرار دارد ساخته می‌شود که شامل همه فونت‌های دانلود شده است. در این فولدر یک فایل text هم با نام `FONTNAME-Links.txt` ساخته خواهد شد که لینک همه فونت‌های دانلود شده را دارا است.
یک فایل دیگر با نام `FONTNAME-Links-All.txt` وجود خواهد داشت که همه لینک‌های کاوش شده را دارا است. این بدرد افرادی می‌خورد که می‌خواهند همه لینک‌ها را بصورت دستی و با استفاده از دانلود منیجر بررسی کنند.

</div>