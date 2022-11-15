import math
import speedtest

test = speedtest.Speedtest()

def get_server():
    print("Getting server list...")
    server_list = test.get_servers() # TODO : Convert output into more readable format
    print(server_list)
    print("Choosing the best server")
    best_server = test.get_best_server()
    print(f"Best Server: {best_server['host']} located in {best_server['country']}")

def get_download_speed():
    print("Getting download speed ...")
    print("Please wait ...")
    download_speed = test.download()
    print(f"Download Speed : {bytes_to_mb(download_speed)}")
    
def get_upload_speed():
    print("Getting upload speed ...")
    print("Please wait ...")
    upload_speed = test.upload()
    print(f"Upload Speed : {bytes_to_mb(upload_speed)}")

def bytes_to_mb(size_of_bytes):
    i = int(math.floor(math.log(size_of_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_of_bytes / power, 2)
    return f"{size} Mpbs"

if __name__ == "__main__":    
    print("----- INTERNET SPEED TEST -----")
    get_server()
    get_download_speed()
    get_upload_speed()
