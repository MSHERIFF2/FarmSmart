# Import your app and models
from app import db
from app.models import Crop, Livestock, MarketPrice, FarmingTip, WeatherForecast

# Sample data with 20 Nigerian crops and livestock
crops = [
    Crop(name='Maize', description='A staple cereal widely consumed in Nigeria and used for various dishes.'),
    Crop(name='Cassava', description='A root crop used to produce garri, fufu, and other Nigerian staples.'),
    Crop(name='Yam', description='A tuber crop popular in Nigerian cuisine, especially for pounded yam.'),
    Crop(name='Rice', description='Widely consumed in various forms such as jollof rice and fried rice.'),
    Crop(name='Groundnut', description='A legume used in making groundnut oil and snacks like kuli-kuli.'),
    Crop(name='Palm Oil', description='Produced from palm fruit, it is a key ingredient in many Nigerian dishes.'),
    Crop(name='Sorghum', description='A grain used in making traditional dishes and beverages in northern Nigeria.'),
    Crop(name='Millet', description='A cereal crop used in preparing foods like fura and tuwo.'),
    Crop(name='Cocoa', description='Grown in southern Nigeria, it is a major export crop used in chocolate production.'),
    Crop(name='Tomato', description='A versatile crop used in making stews, soups, and sauces across Nigeria.'),
    Crop(name='Pepper', description='Commonly grown for use in spicy Nigerian dishes.'),
    Crop(name='Soybeans', description='Used for food, feed, and oil production, it is an important crop in Nigeria.'),
    Crop(name='Okra', description='A popular vegetable used in soups like ogbono and banga.'),
    Crop(name='Plantain', description='Related to bananas, used in various dishes like dodo and plantain chips.'),
    Crop(name='Cucumber', description='Grown widely and used in salads and as a snack.'),
    Crop(name='Sweet Potato', description='A tuber crop used in various dishes, including porridge and snacks.'),
    Crop(name='Pineapple', description='Grown in tropical regions of Nigeria, used fresh or in juices.'),
    Crop(name='Banana', description='A widely grown fruit in Nigeria, used as a snack and in various dishes.'),
    Crop(name='Onion', description='A staple vegetable in Nigerian cooking, used in almost every dish.'),
    Crop(name='Sugarcane', description='Grown for sugar production and consumed fresh as a snack.')
]

livestock = [
    Livestock(name='Goat', description='Commonly raised for meat, milk, and skin in various regions of Nigeria.'),
    Livestock(name='Cattle', description='Includes breeds like the White Fulani, used for meat, milk, and as draft animals.'),
    Livestock(name='Chicken', description='Raised for eggs and meat, commonly found in rural and urban areas.'),
    Livestock(name='Sheep', description='Kept mainly for meat and sometimes wool, thriving in various parts of Nigeria.'),
    Livestock(name='Pig', description='Raised in many parts of Nigeria for pork, an important source of protein.'),
    Livestock(name='Snail', description='A popular delicacy in Nigeria, especially in the southern regions.'),
    Livestock(name='Fish', description='Catfish, tilapia, and other species are widely farmed and consumed in Nigeria.'),
    Livestock(name='Rabbit', description='Raised for meat, which is considered a healthy alternative to other meats.'),
    Livestock(name='Turkey', description='Grown for meat, particularly popular during festive periods.'),
    Livestock(name='Duck', description='Raised for eggs and meat, common in some rural areas of Nigeria.')
]

market_prices = [
    MarketPrice(item='Maize', price=130, unit='per bag'),
    MarketPrice(item='Cassava', price=50, unit='per bunch'),
    MarketPrice(item='Yam', price=300, unit='per tuber'),
    MarketPrice(item='Rice', price=200, unit='per bag'),
    MarketPrice(item='Groundnut', price=120, unit='per bag'),
    MarketPrice(item='Palm Oil', price=400, unit='per keg'),
    MarketPrice(item='Tomato', price=150, unit='per basket'),
    MarketPrice(item='Pepper', price=100, unit='per basket'),
    MarketPrice(item='Cocoa', price=700, unit='per bag'),
    MarketPrice(item='Onion', price=80, unit='per bag')
]

farming_tips = [
    FarmingTip(title='Timely Weeding', tip='Regular weeding is essential to prevent competition for nutrients between crops and weeds.'),
    FarmingTip(title='Pest Control', tip='Use organic or chemical methods to control pests that can damage crops and reduce yields.'),
    FarmingTip(title='Soil Fertility Management', tip='Incorporate organic matter such as compost or manure to improve soil fertility.'),
    FarmingTip(title='Proper Spacing', tip='Ensure adequate spacing between plants to allow for proper growth and reduce competition.'),
    FarmingTip(title='Water Management', tip='Irrigate crops during dry periods to maintain soil moisture and improve crop yields.')
]

weather_forecasts = [
    WeatherForecast(location='Lagos', forecast='Rainy', date='2024-09-08'),
    WeatherForecast(location='Kano', forecast='Sunny', date='2024-09-08'),
    WeatherForecast(location='Enugu', forecast='Cloudy', date='2024-09-08'),
    WeatherForecast(location='Ibadan', forecast='Thunderstorms', date='2024-09-08'),
    WeatherForecast(location='Abuja', forecast='Partly cloudy', date='2024-09-08')
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
