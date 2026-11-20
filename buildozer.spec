[app]

title = Agent
package.name = agent
package.domain = org.termuxboy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,filetype

android.accept_sdk_license = True
android.api = 33
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET
