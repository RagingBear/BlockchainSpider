from BlockchainSpider.spiders.blocks.eth import BlocksETHSpider


class BlocksPolygonSpider(BlocksETHSpider):
    name = 'blocks.polygon'
    net = 'polygon'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # load apikey bucket class
        self.apikey_bucket = type(self.apikey_bucket)(net='polygon', kps=5)

        # api url
        self.base_api_url = 'https://api.polygonscan.com/api'
