# montecarlo

Monte Carlo simulations are a powerful in numerous fields, including operations research, game theory, physics, mathematics, actuarial sciences, finance, among others. It is a technique used to measure risk and uncertainty when making a decision. To put it simple: a Monte Carlo simulation runs an enormous number of statistical experiments with random numbers generated from an underlying distribution based on a given time series. Brownian motion, or random walk, is the main driver for forecasting the future price.
On this README file, I will present some results for Bitcoin close price prediction one week from now, including convergence tests for the number of simulations as well as sensitivity analysis for the historical data sample range.

## Method
The method consist in obtaining a mean and standard deviation from a given sample data (time series), on this particular case the close price data of Bitcoin from a certain time range.

## Usage

Clone repo and install dependencies:

`
git clone https://github.com/cryptohariseldon/Modelling-zbtc.git
`

`
cd Modelling-zbtc
`

`
pip3 install -r requirements.txt
`

Run a single random simulation with a two year time frame, and produce graph of output projections including SMA:

`
python3 montecarlo_single.py
`

Run a 1000 montecarlo simulations with a two year time frame, and output frequency and likelhood of the SMA ending up in different price bands :

`
python3 montecarlo_multi.py
`
