from discord_webhooks import DiscordWebhooks


class DiscordClient:
    def __init__(self, webhook):
        self.webhook = webhook


    def message_handler(self, assets, date):
        all_in = float(
            sum(
                asset_data['present'] for asset_data in assets.values()
            )
        )
        
        self.message = f'''
##Binance Profit 💸:
    - {date}:
        ```
        All-in: {all_in}$
        BTC Amount: 70$
        Dad's shares: {(all_in - 70.00) / 2}
        Mine shares: {((all_in - 70.00) / 2)}$ + 70.00$ (BTC Amount)
        ```

##Binance Portfolio 💼: 
    - {date}:
        ```
        All-in: {all_in}$
        USDT: {assets['USDT']['amount']}$
        SHIB: {assets['SHIB']['present']}$
        CAKE: {assets['CAKE']['present']}$
        DOGE: {assets['DOGE']['present']}$
        BNB: {assets['BNB']['present']}$
        ADA: {assets['ADA']['present']}$
        ```
'''


    def send_content(self):
        self.webhook = DiscordWebhooks(
            webhook_url=self.webhook,
            content=self.message
    )
