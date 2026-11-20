[app]

# (str) অ্যাপ্লিকেশনের শিরোনাম
title = MyApp

# (str) প্যাকেজের নাম (শুধুমাত্র ছোট হাতের অক্ষর এবং সংখ্যা)
package.name = myapp

# (str) প্যাকেজ ডোমেইন (যেমন org.yourname)
package.domain = org.myapp

# (str) অ্যাপ্লিকেশনের সোর্স কোড ডিরেক্টরি
source.dir = .

# (list) সোর্স ডিরেক্টরিতে অন্তর্ভুক্ত ফাইলের এক্সটেনশন
source.include_exts = py,png,jpg,kv,atlas

# (list) বাদ দেওয়া ফাইল/ফোল্ডার
source.exclude_dirs = tests, bin, venv, .github, .backups

# (str) অ্যাপ্লিকেশনের সংস্করণ
version = 0.1

# (list) অ্যাপ্লিকেশনের নির্ভরতা (requirements)
# main.py তে kivy এবং filetype ব্যবহার করা হয়েছে, তাই এখানে দুটোই থাকতে হবে
requirements = python3,kivy,filetype

# (str) অ্যাপ্লিকেশনের এন্ট্রি পয়েন্ট (ডিফল্ট main.py)
# যদি আপনার এন্ট্রি ফাইলের নাম main.py হয়, তাহলে এই লাইনটি দরকার নেই

# (list) অ্যান্ড্রয়েড আর্কিটেকচার (arm64-v8a আধুনিক ফোনের জন্য, armeabi-v7a পুরোনো ফোনের জন্য)
android.archs = arm64-v8a, armeabi-v7a

# (int) Android API লেভেল (৩৩ সাধারণত সবচেয়ে স্থিতিশীল)
android.api = 33

# (int) সর্বনিম্ন API লেভেল (২১ মানে Android 5.0 এবং তার উপরে সমর্থিত)
android.minapi = 21

# (str) Android NDK সংস্করণ
android.ndk = 25b

# (bool) স্বয়ংক্রিয়ভাবে Android SDK লাইসেন্স গ্রহণ করুন (অত্যন্ত গুরুত্বপূর্ণ!)
android.accept_sdk_license = True

# (list) অ্যান্ড্রয়েড অনুমতি (INTERNET যোগ করা হয়েছে ভবিষ্যতে নেটওয়ার্ক ব্যবহারের জন্য)
android.permissions = INTERNET

# (str) অ্যাপের আইকন (যদি না থাকে তাহলে ডিফল্ট Kivy আইকন ব্যবহার হবে)
# icon.filename = %(source.dir)s/data/icon.png

# (bool) সম্পূর্ণ স্ক্রিন মোড সক্রিয় করুন (ঐচ্ছিক)
# fullscreen = 0

[buildozer]

# (int) লগ লেভেল (২ মানে ত্রুটি এবং সতর্কতা)
log_level = 2

# (str) বিল্ড ডিরেক্টরি
build_dir = .buildozer

# (str) বিল্ড করা APK এর আউটপুট ডিরেক্টরি
bin_dir = ./bin

# (bool) প্রতিবার বিল্ড করার সময় প্যাকেজ পুনরায় ডাউনলোড করবেন কিনা
# warn_on_root = 0
