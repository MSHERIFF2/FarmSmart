from app import app
from flask import render_template, request, redirect, url_for
from app.models import Crop, Livestock, MarketPrice, FarmingTip, WeatherForecast

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crops')
def show_crops():
    crops = Crop.query.all()
    return render_template('crops.html', crops=crops)

@app.route('/livestock')
def show_livestock():
    livestock = Livestock.query.all()
    return render_template('livestock.html', livestock=livestock)

@app.route('/market-prices')
def show_market_prices():
    prices = MarketPrice.query.all()
    return render_template('market_prices.html', prices=prices)

@app.route('/farming-tips')
def show_farming_tips():
    tips = FarmingTip.query.order_by(FarmingTip.date.desc()).all()
    return render_template('farming_tips.html', tips=tips)

@app.route('/weather-forecast')
def show_weather_forecast():
    forecasts = WeatherForecast.query.order_by(WeatherForecast.forecast_date.desc()).all()
    return render_template('weather_forecast.html', forecasts=forecasts)
