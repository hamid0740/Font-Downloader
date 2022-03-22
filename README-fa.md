<div align="center">
<a href="https://github.com/hamid0740/Font-Downloader/blob/main/README.md"><img title="English language" alt="English language" src="https://img.shields.io/badge/lang-en-50d890?labelColor=black&style=for-the-badge&logo=google-translate&logoColor=white"></a>
</div>

- - - -

<div dir=rtl align="right">

# فونت دانلودر
این یک اسکریپت پایتون هست که به شما توی کاوش کردن و دانلود همه وزن‌های یک فونت که توی بسایتی میزبانی می‌شن کمک می‌کنه.

برای یادگیری استفاده از این اسکریپت، [دستورالعمل](#دستورالعمل) رو بخونید.

### اسکرین‌شات

![اسکرین‌شات](https://i.ibb.co/PrKmBvC/Font-Downloader-screenshot.jpg)


**نکته:** برای گرفتن اسکرین‌شات، اسکریپت ویرایش شده تا ارتفاع تصویر کمتر بشه.

## دستورالعمل
1. ترموکس رو از [اینجا](https://f-droid.org/en/packages/com.termux) دانلود و نصب کنید. شما باید زبان پایتون رو هم از قبل نصب کرده باشید‌ و کتابخونه‌های `requests` و `colorama` رو هم برای پایتون داشته باشید. برای یادگیری روش نصب این کتابخونه‌ها، [اینجا](https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/) رو بخونید.

2. کدهای زیر رو تو ترموکس اجرا کنید:
   ```
   pkg install python
   pip install requests
   pip install colorama
   termux-setup-storage
   cd /path/to/code
   python Font-Downloader.py
   ```

3. در اولین ورودی باید مشخص کنید که اسکریپت با چه سرعتی وزن‌های فونت رو کاوش کنه. سرعت `1` تقریباً ۴ برابر سریع‌تر از سرعت `2` هست؛ در نتیجه دقتش کمتر میشه.

4. در دومین ورودی باید اسم فونتی که توی URL فایل فونت استفاده شده رو مشخص کنید. اگه URL فایل فونت به این شکل باشه: `https://example.com/fonts/Arial/woff2/Arial-Bold.woff2`، شما باید نام فونت را بصورت `Arial` وارد کنید.
   این اسم بعداً به عنوان `{NAME}` استفاده میشه.


5. در سومین ورودی باید URL الگوی فایل فونت رو وارد کنید. یک لینک فایل فونت رو توی وبسایتی پیدا کنید و بعضی از مقادیر اون را با متغیرهای زیر جایگزین کنید.
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

6. برای چهارمین ورودی باید کوچک یا بزرگی حروف اسم وزن‌ها را با توجه به بررسی‌های خودتون توی لینک فونت‌ها مشخص کنید. اگه تا حالا بررسی انجام ندادید، `all` رو وارد کنید تا همه چیز تست بشه.
   ```
   's' for Standard case (25-120 weight names)
   'l' for Lower case (17-70 weight names)
   'u' for Upper case (17-70 weight names)
   'all' for All cases (59-260 weight names)
   ```
   شما می‌تونید حروف رو ترکیب کنید تا کوچک بزرگی ترکیبی داشته باشید. مثلاً با وارد کردن `lu` می‌تونید هم حروف کوچک و هم حروف بزرگ رو برای کاوش کردن انتخاب کنید.

7. الآن کار شما تموم شده. فقط تا پایان کاوش صبر کنید.

## لیست برای-انجام
* [ ] جلوگیری از کرش شدن اسکریپت و نمایش دادن خطا بجاش
* به من ایده بدید تا این اسکریپت رو کامل و بهترش کنم :)

## داده‌ها
### اسامی وزن فونت
اینا با توجه به تحقیقات من توی خانواده فونت‌های مختلف هستند.
* هیچ‌وقت پیشوندی نمی‌گیرن:

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
* ممکنه Extra، Ultra یا Very بگیرن:

  **(سرعت 1)** Very نمی‌گیرن
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
* ممکنه Semi یا Demi بگیرن:

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
این فرمت‌های فونت توسط اسکریپت کاوش می‌شن:
```
eot
otf (سرعت 2)
svg (سرعت 2)
ttf
woff
woff2
```

## خروجی
وقتی پروسه کامل بشه، یه فولدر در جایی که فایل کد قرار داره ساخته می‌شه که شامل همه فونت‌های دانلود شده هست، تفکیک‌شده بر اساس فرمتشون. توی این فولدر یک فایل text هم به نام `FONTNAME-Links.txt` ساخته میشه که لینک همه فونت‌های دانلود شده رو داره.
یه فایل دیگه هم به نام `FONTNAME-Links-All.txt` وجود داره که همه لینک‌های کاوش شده رو داره. این بدرد کسایی می‌خوره که می‌خوان همه لینک‌ها رو بصورت دستی و با استفاده از دانلود منیجر بررسی کنند.

</div>
