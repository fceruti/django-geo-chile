from decimal import Decimal as D
import json

from django.core.management.base import BaseCommand
import requests

from geo_chile.models import Commune, Province, Region


class Command(BaseCommand):
    help = "Download and populate chilean administrative data"

    def handle(self, *args, **options):
        self.load_communes(self.load_provinces(self.load_regions()))
        print("Drink Wine :)")

        Region.objects.filter(code="16").update(lat=D("-36.6191"), lng=D("-72.0182"))

    def load_regions(self):
        print("Fetching regions ...")
        response = requests.get(
            "https://apis.digital.gob.cl/dpa/regiones/",
            headers={"User-agent": "Mozilla/5.0"},
        )

        regions_cache = {}
        for row in json.loads(response.content):
            code = row["codigo"]
            region, _ = Region.objects.update_or_create(
                code=code,
                defaults={
                    "name": row["nombre"],
                    "lat": D(row["lat"]),
                    "lng": D(row["lng"]),
                },
            )
            regions_cache[code] = region

        return regions_cache

    def load_provinces(self, regions_cache):
        print("Fetching provinces ...")
        response = requests.get(
            "https://apis.digital.gob.cl/dpa/provincias/",
            headers={"User-agent": "Mozilla/5.0"},
        )

        provinces_cache = {}
        for row in json.loads(response.content):
            code = row["codigo"]
            region, _ = Province.objects.update_or_create(
                code=code,
                region=regions_cache[row["codigo_padre"]],
                defaults={
                    "name": row["nombre"],
                    "lat": D(row["lat"]),
                    "lng": D(row["lng"]),
                },
            )
            provinces_cache[code] = region
        return provinces_cache

    def load_communes(self, provinces_cache):
        print("Fetching communes ...")
        response = requests.get(
            "https://apis.digital.gob.cl/dpa/comunas/",
            headers={"User-agent": "Mozilla/5.0"},
        )

        for row in json.loads(response.content):
            code = row["codigo"]
            province = provinces_cache[row["codigo_padre"]]
            Commune.objects.update_or_create(
                code=code,
                province=province,
                region=province.region,
                defaults={
                    "name": row["nombre"],
                    "lat": D(row["lat"]),
                    "lng": D(row["lng"]),
                },
            )
