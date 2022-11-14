import math
import speedtest

wifi = speedtest.Speedtest()

def bytes_to_mb(size_of_bytes):
    i = int(math.floor(math.log(size_of_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_of_bytes / power, 2)
    return f"{size} Mpbs"

print("----- INTERNET SPEED TEST -----")

print("Getting download speed ...")
print("Please wait ...")
download_speed = wifi.download()

print("Getting upload speed ...")
print("Please wait ...")
upload_speed = wifi.upload()

print(f"Download Speed : {bytes_to_mb(download_speed)}")
print(f"Upload Speed : {bytes_to_mb(upload_speed)}")
