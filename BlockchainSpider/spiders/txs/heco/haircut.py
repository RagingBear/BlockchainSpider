from BlockchainSpider.spiders.txs.eth.haircut import TxsETHHaircutSpider
from BlockchainSpider.utils.apikey import JsonAPIKeyBucket


class TxsHecoHaircutSpider(TxsETHHaircutSpider):
    name = 'txs.heco.haircut'
    TXS_API_URL = 'https://api.hecoinfo.com/api'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.apikey_bucket = JsonAPIKeyBucket('heco')
