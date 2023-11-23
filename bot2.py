import requests
import json

def send_embedded_message(webhook_url):
    try:
        payload = {
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "type": "rich",
                    "title": "Axton Bot(Bull/Bear)[Moderate]",
                    "description": "This bot uses the very famous trading view signals through 4 parameteres to start a deal and go into profits, proven to work",
                    "color": 0x00FFFF,
                    "fields": [
                        {
                            "name": "Avg-daily profit:",
                            "value": "0.6%",
                            "inline": True
                        },
                        {
                            "name": "Max draw-down:",
                            "value": "20.11%",
                            "inline": True
                        },
                        {
                            "name": "Net profit:",
                            "value": "30%",
                            "inline": True
                        },
                        {
                            "name": "Pairs:",
                            "value": "ALL",
                            "inline": True
                        },
                        {
                            "name": "Min capital:",
                            "value": "133 USDT",
                            "inline": True
                        }
                    ],
                    "image": {
                        "url": "https://i.postimg.cc/x11NpV7K/image.png",
                        "height": 0,
                        "width": 0
                    },
                    "footer": {
                        "text": "NOTE: The above simulation is done for only BTC but the bot deals with multi-pairs closing 5 deals at a time, so the above profits or loss might be better than displayed. (ex: if BTC gives 5% profit, other coins like ADA can give up to 30% or work vice versa )."
                    }
                }
            ]
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print('Embedded message sent successfully.')
    except requests.exceptions.RequestException as e:
        print('Error sending embedded message:', str(e))

# Example usage:
webhook_url = 'https://discord.com/api/webhooks/1121860896092848228/fWtbTVjL3UqQdwyLi51VP3rlNy2jJD85FWs6xLiT3a6J3f5cS9VrCAfJdLuDfZWxN_Ow'
send_embedded_message(webhook_url)
