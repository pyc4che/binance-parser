from binance.client import Client


class BinanceClient:
    def __init__(
            self, crypto, 
            api, secret):
        self.crypto = crypto

        self.client = Client(
            api_key=api,
            api_secret=secret,
            testnet=False
        )


    def get_balance(self):
        self.data = self.client.get_account()


    def list_assets(self):
        assets = {

        }

        for asset in self.data['balances']:
            if (asset['asset'] in self.crypto
                and asset['asset'] not in ['USDT', 'USDC']):
                _price = float(self.client.get_ticker(
                    symbol=f'{asset["asset"]}USDT'
                )['lastPrice'])

                _name = str(asset['asset'])

                _amount = float(asset['free'])

                _present = round(
                    float(_amount * _price),
                    3
                )

                assets[_name] = {
                    'amount': _amount,
                    'price': _price,
                    'present': _present
                }

            elif (asset['asset'] in ['USDT', 'USDC']
                and float(asset['free']) != 0.0):
                _name = str(asset['asset'])

                _amount = round(
                    float(asset['free']),
                    3
                )

                assets[_name] = {
                    'amount': _amount
                }

        return assets
