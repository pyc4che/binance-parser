from discord import SyncWebhook


class DiscordClient:
    def __init__(self, webhook):
        self.webhook = webhook


    def message_handler(self, assets, date):

        self.message = f'''
## Binance Portfolio 💼 : 
    - {date}:
    ```
    USDT: {assets.get('USDT', {'present': 0})['amount']}$
    SHIB: {assets.get('SHIB', {'present': 0})['present']}$
    CAKE: {assets.get('CAKE', {'present': 0})['present']}$
    DOGE: {assets.get('DOGE', {'present': 0})['present']}$
    BNB: {assets.get('BNB', {'present': 0})['present']}$
    ADA: {assets.get('ADA', {'present': 0})['present']}$
    ```
'''


    def send_content(self):
        self.webhook_handler = SyncWebhook.from_url(self.webhook)
        self.webhook_handler.send(self.message)
