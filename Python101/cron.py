import requests
import time

from firewatcher import create_app, db
from firewatcher.models import Cities, WildFires

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    while True:
        current_time = int(time.time())
        fire_response = requests.get(
            f'https://ormanyanginlari.ogm.gov.tr/Home/GetOrmanYanginlari?_={current_time}').json().get("data")
        print(type(fire_response))
        with app.app_context():
            for item in fire_response:
                city = Cities(name=item.get("IlAdi"))
                if db.session.query(db.session.query(Cities).filter_by(name=city.name).exists()).scalar():
                    city = db.session.query(Cities).filter_by(name=city.name).one()
                else:
                    db.session.add(city)
                    db.session.commit()
                fire = WildFires(
                    status=item.get("YanginDurumu"),
                    risk_level=item.get("RiskDurumu"),
                    type=item.get("YanginTuru"),
                    cause=item.get("YanginNedeni"),
                    locationx= item.get("XKoordinati"),
                    locationy= item.get("YKoordinati"),
                    time=item.get("YanginBaslamaSaati"),
                    district=item.get("IlceAdi"),
                    city=city.id
                )
                if db.session.query(db.session.query(WildFires).filter_by(
                        locationx=item.get("XKoordinati"),
                        locationy=item.get("YKoordinati"),
                        time=item.get("YanginBaslamaSaati"),
                        district=item.get("IlceAdi"),
                        city=city.id
                ).exists()).scalar():
                    fire = db.session.query(WildFires).filter_by(
                        locationx=item.get("XKoordinati"),
                        locationy=item.get("YKoordinati"),
                        time=item.get("YanginBaslamaSaati"),
                        district=item.get("IlceAdi"),
                        city=city.id
                    ).one()
                    fire.status = item.get("YanginDurumu")
                    fire.risk_level = item.get("RiskDurumu")
                    db.session.add(fire)
                else:
                    db.session.add(fire)
            db.session.commit()
        print("CHECK")
        time.sleep(600)

