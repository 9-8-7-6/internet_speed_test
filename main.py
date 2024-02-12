import math, time
import speedtest
import os


def bytes_to_MB(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mpbs"


wifi = speedtest.Speedtest()

print("==================================")
print("Test is running...")
print("Please wait for a moment!!!")
print("==================================")
download_speed = wifi.download()
upload_speed = wifi.upload()

print("Test is finished")
print(f"Download speed:{bytes_to_MB(download_speed)}")
print(f"Upload speed:{bytes_to_MB(upload_speed)}")
print("==================================")