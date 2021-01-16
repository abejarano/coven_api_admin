#!/usr/bin python3
import decimal
import os

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from apps.indicadores.models import ValoresMercado, Commodities
import requests


class Command(BaseCommand):
    help = "Obtiene el valor del cafe"

    def handle(self, *args, **options):
        r = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
        soup = BeautifulSoup(r.content, 'html.parser')
        span = soup.find(class_="priceValue___11gHJ")
        btc = span.get_text().strip().replace(',', '').replace('$', '')

        btc_usd = decimal.Decimal(btc)
        if btc_usd > 0:
            ValoresMercado(
                tipo_mercado='I',
                precio=btc_usd,
                par='USD/BTC',
                mercado=Commodities.objects.get(abreviatura='BTC')
            ).save()

        # buscar el valor del dolar
        bs_usd = ValoresMercado.objects.filter(mercado__abreviatura='USD', par='BS/USD')[:1]

        btc_bs = decimal.Decimal(float(btc) * float(bs_usd[0].precio))
        if btc_bs > 0:
            ValoresMercado(
                tipo_mercado='N',
                precio=btc_bs,
                par='BS/BTC',
                mercado=Commodities.objects.get(abreviatura='BTC')
            ).save()
