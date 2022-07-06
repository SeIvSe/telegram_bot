import requests
import json
from conf import vales

class ConExp(Exception):
    pass

class ConErr:
    @staticmethod
    def convert(quote:str, base:str, amount:str):

        quote_tic, base_tic = vales[quote], vales[base]
        if quote == base:
            raise ConExp('Указана одна и таже валюта, правильнее писать например "биткоин доллар 1"')

        try:
            quote_tic = vales[quote]
        except KeyError:
            raise ConExp(f'Нет такой валюты, как {quote}')

        try:
            base_tic = vales[base]
        except KeyError:
            raise ConExp(f'Нет такой валюты, как {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConExp(f'Количество валюты указано не верно')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tic}&tsyms={base_tic}')
        t_base = json.loads(r.content)[vales[base]]

        return t_base