import schedule
import requests, json, base64, time, threading, sys, cv2

server_url = "http://157.230.223.213:8194" # the URL the Slackbot server is running on

# res = requests.post(server_url+'/send_icebreakers_period')

def test():
    print("test")

def job():
    return requests.get(server_url+'/send_icebreakers_period')

if __name__ == "__main__":    
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)