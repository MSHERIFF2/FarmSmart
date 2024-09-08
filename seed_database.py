# seed/seed_database.py

from app import app, db
from app.models import Crop, Livestock, MarketPrice, FarmingTip, WeatherForecast
from datetime import date

# Create an application context
with app.app_context():
    # Sample data
    crops = [
        Crop(name='Maize'),
        Crop(name='Cassava'),
        Crop(name='Yam'),
        Crop(name='Rice'),
        Crop(name='Groundnut'),
        Crop(name='Palm Oil'),
        Crop(name='Sorghum'),
        Crop(name='Millet'),
        Crop(name='Cocoa'),
        Crop(name='Tomato'),
        Crop(name='Pepper'),
        Crop(name='Soybeans'),
        Crop(name='Okra'),
        Crop(name='Plantain'),
        Crop(name='Cucumber'),
        Crop(name='Sweet Potato'),
        Crop(name='Pineapple'),
        Crop(name='Banana'),
        Crop(name='Onion'),
        Crop(name='Sugarcane')
    ]

    livestock = [
        Livestock(name='Goat'),
        Livestock(name='Cattle'),
        Livestock(name='Chicken'),
        Livestock(name='Sheep'),
        Livestock(name='Pig'),
        Livestock(name='Snail'),
        Livestock(name='Fish'),
        Livestock(name='Rabbit'),
        Livestock(name='Turkey'),
        Livestock(name='Duck')
    ]

    # Create sample market prices
    market_prices = [
        MarketPrice(crop_id=1, price=130, date=date(2024, 9, 8)),   # Maize
        MarketPrice(crop_id=2, price=50, date=date(2024, 9, 8)),   # Cassava
        MarketPrice(crop_id=3, price=300, date=date(2024, 9, 8)),  # Yam
        MarketPrice(crop_id=4, price=200, date=date(2024, 9, 8)),  # Rice
        MarketPrice(crop_id=5, price=120, date=date(2024, 9, 8)),  # Groundnut
        MarketPrice(crop_id=6, price=400, date=date(2024, 9, 8)),  # Palm Oil
        MarketPrice(crop_id=10, price=150, date=date(2024, 9, 8)), # Tomato
        MarketPrice(crop_id=11, price=100, date=date(2024, 9, 8)), # Pepper
        MarketPrice(crop_id=9, price=700, date=date(2024, 9, 8)),  # Cocoa
        MarketPrice(crop_id=19, price=80, date=date(2024, 9, 8))   # Onion
    ]

    # Create sample farming tips
    farming_tips = [
        FarmingTip(title='Timely Weeding', content='Regular weeding is essential to prevent competition for nutrients between crops and weeds.', date=date(2024, 9, 8)),
        FarmingTip(title='Pest Control', content='Use organic or chemical methods to control pests that can damage crops and reduce yields.', date=date(2024, 9, 8)),
        FarmingTip(title='Soil Fertility Management', content='Incorporate organic matter such as compost or manure to improve soil fertility.', date=date(2024, 9, 8)),
        FarmingTip(title='Proper Spacing', content='Ensure adequate spacing between plants to allow for proper growth and reduce competition.', date=date(2024, 9, 8)),
        FarmingTip(title='Water Management', content='Irrigate crops during dry periods to maintain soil moisture and improve crop yields.', date=date(2024, 9, 8))
    ]

    # Create sample weather forecasts
    weather_forecasts = [
        WeatherForecast(forecast_date=date(2024, 9, 8), temperature=28.5, condition='Rainy'),
        WeatherForecast(forecast_date=date(2024, 9, 8), temperature=34.0, condition='Sunny'),
        WeatherForecast(forecast_date=date(2024, 9, 8), temperature=26.0, condition='Cloudy'),
        WeatherForecast(forecast_date=date(2024, 9, 8), temperature=22.0, condition='Thunderstorms'),
        WeatherForecast(forecast_date=date(2024, 9, 8), temperature=30.0, condition='Partly cloudy')
    ]

    # Add all the sample data to the session
    db.session.add_all(crops + livestock + market_prices + farming_tips + weather_forecasts)

    # Commit the session to save the data to the database
    try:
        db.session.commit()
        print("Database seeded successfully with Nigerian-specific data!")
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")
