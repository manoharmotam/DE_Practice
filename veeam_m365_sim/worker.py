import time, requests

while True:
    requests.post("http://127.0.0.1:8000/run_job/1")
    time.sleep(60)
