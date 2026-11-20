[app]
title = MyApp
package.name = myapp
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,filetype

# ✅ নিচের লাইনটি যোগ করা অত্যন্ত গুরুত্বপূর্ণ, এটি স্বয়ংক্রিয়ভাবে Android SDK লাইসেন্স গ্রহণ করবে
android.accept_sdk_license = True
android.api = 33
android.ndk = 25b

# অন্যান্য প্রস্তাবিত সেটিংস (ঐচ্ছিক, তবে বিল্ডের জন্য উপকারী)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET
