from datetime import date

from shared.config import Config

from discord_api.client import DiscordClient
from binance_api.client import BinanceClient




def main():
    _config = Config(
        'your_path_to_config'
    ).read()

    _date = date.today()

    _binance_client = BinanceClient(
        _config['client']['tokens'],
        _config['binance']['api_key'],
        _config['binance']['secret_key']
    )

    _discord_client = DiscordClient(
        _config['discord']['webhook_url']
    )

    _binance_client.get_balance()
    _assets = _binance_client.list_assets()

    print(_assets)

    _discord_client.message_handler(
        _assets, _date
    )

    print(_discord_client.message)

    _discord_client.send_content()


if __name__ == '__main__':
    main()
