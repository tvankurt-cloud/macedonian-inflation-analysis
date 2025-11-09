# Macedonian Inflation Forecast (2016–2026)

![Run Inflation Analysis](https://github.com/tvankurt-cloud/macedonian-inflation-forecast/actions/workflows/run-analysis.yml/badge.svg)

# Macedonian Inflation Forecast (2016–2026)

This project analyzes and forecasts the inflation rate in North Macedonia from 2016 to 2026 using historical data and predictive modeling. It incorporates insights from the [IMF Selected Issues Paper (2025)](https://www.imf.org/en/Publications/selected-issues-papers/Issues/2025/05/22/Impact-of-International-Shocks-on-North-Macedonia-and-the-Western-Balkans-Republic-of-North-567136).

## 📊 Features

- Historical inflation data visualization (2016–2020)
- Projected inflation rates (2021–2026)
- Linear regression model for forecasting
- Interactive plots and summary statistics

## 📁 Project Structure

- `inflation_analysis.py`: Main script for data analysis and visualization
- `data/inflation_macedonia_2016_2026.csv`: Source data
- `plots/inflation_trend.png`: Output graph
- `requirements.txt`: Python dependencies

## 📈 Sample Output

![Inflation Trend](plots/inflation_trend.png)

## 📚 Data Source

- IMF Selected Issues Paper (2025): [Impact of International Shocks on North Macedonia](https://www.imf.org/en/Publications/selected-issues-papers/Issues/2025/05/22/Impact-of-International-Shocks-on-North-Macedonia-and-the-Western-Balkans-Republic-of-North-567136)

## 🛠 Installation

```bash
git clone https://github.com/tvankurt-cloud/macedonian-inflation-forecast.git
cd macedonian-inflation-forecast
pip install -r requirements.txt
python inflation_analysis.py
