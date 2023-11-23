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
                    "title": "Falcon-DCA Bot (Bull) [moderate]",
                    "description": "Falcon bot uses BB on  a larger time frame with 3 other signals to find a perfect entry. As it searches for the correct conditions to enter a trade, it will open deals with lesser frequency with a higher TP.",
                    "color": 0x00FFFF,
                    "fields": [
                        {
                            "name": "Avg-daily profit:",
                            "value": "11%",
                            "inline": True
                        },
                        {
                            "name": "Max draw-down:",
                            "value": "15%",
                            "inline": True
                        },
                        {
                            "name": "Net profit:",
                            "value": "140%",
                            "inline": True
                        },
                        {
                            "name": "Pairs:",
                            "value": "ALL",
                            "inline": True
                        },
                        {
                            "name": "Min capital:",
                            "value": "1280 USDT",
                            "inline": True
                        }
                    ],
                    "image": {
                        "url": "https://i.postimg.cc/yNZ3zbkp/Screenshot-2023-07-09-151730.jpg",
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
webhook_url = 'https://discord.com/api/webhooks/1119870667303702538/gSmm02Brb_UCvJLEm3h71Ei7iHeMuBvXtKMj5FYowvdH5IxJYvEjjcs4xAZMpLldlstZ'
send_embedded_message(webhook_url)
