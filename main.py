import speedtest 

st = speedtest.Speedtest()

download_speed = st.download()
upload_speed = st.upload()

new_download_speed = download_speed / 1_000_000
new_upload_speed = upload_speed / 1_000_000

ping = st.results.ping

print(f"Download: {new_download_speed} bps")
print(f"Upload: {new_upload_speed} bps")
print(f"Ping: {ping} ms")