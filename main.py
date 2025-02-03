class City:
    def __init__(self, city, region, country, citizens, zip, area):
        self.city = city
        self.region = region
        self.country = country
        self.citizens = citizens
        self.zip = zip
        self.area = area

    def adresa(self):
        print(f"Kompletná adresa je: {self.city}, {self.region}, {self.country}, {self.zip}, {self.area}. Mesto má {self.citizens} obyvateľov.")


bratislava = City(city="Bratislava", region="Bratislavský kraj", country="Slovensko", zip="83102", area="123456", citizens="478 040")

bratislava.adresa()