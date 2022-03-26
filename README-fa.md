<div align="center">
<a href="https://github.com/hamid0740/Font-Downloader/blob/main/README.md"><img alt="English language" src="https://img.shields.io/badge/lang-en-50d890?labelColor=black&style=for-the-badge&logo=google-translate&logoColor=white"></a>
</div>

- - - -

<div dir=rtl align="right">

# 📥فونت دانلودر[![ورژن](https://img.shields.io/github/v/release/hamid0740/Font-Downloader?color=purple&label=Version)](#فونت-دانلودر)
این یه اسکریپت پایتون هست که به شما توی کاوش کردن و دانلود همه وزن‌های یک فونت که توی وبسایتی میزبانی می‌شن کمک می‌کنه.

برای یادگیری استفاده از این اسکریپت، [دستورالعمل](#دستورالعمل) رو بخونید.

**[📥 دانلود ورژن 1.9](https://github.com/hamid0740/Font-Downloader/releases/download/v1.9/Font-Downloader.py)**

<div align="center">
<a href="https://github.com/hamid0740/Font-Downloader/releases/download/v1.9/Font-Downloader.py"><img alt="دانلودها" src="https://img.shields.io/github/downloads/hamid0740/Font-Downloader/total?color=green&label=Downloads&logo=bookmeter&logoColor=green"></a>
<a href="https://github.com/hamid0740/Font-Downloader/blob/main/LICENSE"><img alt="لایسنس" src="https://img.shields.io/github/license/hamid0740/Font-Downloader?color=blue&label=License&logo=quicklook&logoColor=blue"></a>
<a href="https://github.com/hamid0740/Font-Downloader/stargazers"><img alt="ستاره‌ها" src="https://img.shields.io/github/stars/hamid0740/Font-Downloader?color=gold&label=Stars&logo=apachespark&logoColor=gold"></a>
<a href="https://github.com/hamid0740/Font-Downloader/issues"><img alt="اشکالات گزارش‌شده" src="https://img.shields.io/github/issues/hamid0740/Font-Downloader?color=orange&label=Issues&logo=openbugbounty&logoColor=orange"></a>
</div>

### 📸اسکرین‌شات

![اسکرین‌شات](https://i.ibb.co/dMnrTvG/Font-Downloader-screenshot.jpg)

**نکته:** برای گرفتن اسکرین‌شات، اسکریپت ویرایش شده تا ارتفاع تصویر کمتر بشه.

## 👣دستورالعمل
1. ترموکس رو از [اینجا](https://f-droid.org/en/packages/com.termux) دانلود و نصب کنید. شما باید زبان پایتون رو هم از قبل نصب کرده باشید و کتابخونه‌های `requests` و `colorama` رو هم برای پایتون داشته باشید. برای یادگیری روش نصب این کتابخونه‌ها، [اینجا](https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/) رو بخونید.

2. کدهای زیر رو توی ترموکس اجرا کنید:
   ```
   pkg install python
   pip install requests
   pip install colorama
   termux-setup-storage
   cd /path/to/code
   python Font-Downloader.py
   ```

3. در اولین ورودی باید مشخص کنید که اسکریپت با چه سرعتی وزن‌های فونت رو کاوش کنه. سرعت `1` تقریباً ۴ برابر سریع‌تر از سرعت `2` هست؛ در نتیجه دقتش کمتر میشه.

4. در دومین ورودی باید اسم فونتی که قراره سیو بشه رو وارد کنید.

5. در سومین ورودی باید باید لینک مستقیم یا الگوی فایل فونت رو وارد کنید. یه فایل فونت رو توی وبسایتی پیدا کنید و لینکش رو اونجا وارد کنید. می‌تونید از این متغیرها استفاده‌ کنید تا لینک الگو رو خودتون بسازید.
   ```
   {WEIGHT}: Thin, Regular, Bold ...
   {FORMAT}: eot, ttf, woff2 ...
   ```
   مثال:
   ```
   Direct: https://example.com/fonts/Arial/woff2/Arial-Bold.woff2
   Pattern: https://example.com/fonts/Arial/{FORMAT}/Arial-{WEIGHT}.{FORMAT}
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

## 🗃داده‌ها
### ⚖اسامی وزن فونت
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
### 📁فرمت‌ها
این فرمت‌های فونت توسط اسکریپت کاوش می‌شن:
```
eot
otf (سرعت 2)
svg (سرعت 2)
ttf
woff
woff2
```

## 📝لیست برای-انجام
* [ ] جلوگیری از کرش شدن اسکریپت و نمایش دادن خطا بجاش (شاید یه روزی...)
* به من ایده بدید تا این اسکریپت رو کامل و بهترش کنم :)

## 📤خروجی
وقتی پروسه کامل بشه، یه فولدر در جایی که فایل کد قرار داره ساخته می‌شه که شامل همه فونت‌های دانلود شده هست، تفکیک‌شده بر اساس فرمتشون. توی این فولدر یک فایل text هم به نام `FONTNAME-Links.txt` ساخته میشه که لینک همه فونت‌های دانلود شده رو داره.
یه فایل دیگه هم به نام `FONTNAME-Links-All.txt` وجود داره که همه لینک‌های کاوش شده رو داره. این بدرد کسایی می‌خوره که می‌خوان همه لینک‌ها رو بصورت دستی و با استفاده از دانلود منیجر بررسی کنند.

</div>
