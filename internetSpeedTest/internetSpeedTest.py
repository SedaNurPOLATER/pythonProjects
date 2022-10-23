import speedtest

test = speedtest.Speedtest()

download_result = test.download()
upload_result = test.upload()

ping_result = test.results.ping

print(f"İndirme Hızı: {download_result / 1024 / 1024:.2f} Mbps")
print(f"Yükleme Hızı: {upload_result / 1024 / 1024:.2f} Mbps")
print(f"Ping: {download_result:.2f} ms")