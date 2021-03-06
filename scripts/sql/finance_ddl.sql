CREATE DATABASE IF NOT EXISTS finance;

CREATE EXTERNAL TABLE IF NOT EXISTS finance.market (
sector string,
fullTimeEmployees string,
city string,
phone string,
`state` string,
country string,
address1 string,
industry string,
ebitdaMargins string,
profitMargins string,
grossMargins string,
operatingCashflow string,
revenueGrowth string,
operatingMargins string,
ebitda string,
targetLowPrice string,
recommendationKey string,
grossProfits string,
freeCashflow string,
targetMedianPrice string,
currentPrice string,
earningsGrowth string,
currentRatio string,
returnOnAssets string,
targetMeanPrice string,
debtToEquity string,
returnOnEquity string,
targetHighPrice string,
totalCash string,
totalDebt string,
totalRevenue string,
totalCashPerShare string,
financialCurrency string,
revenuePerShare string,
quickRatio string,
recommendationMean string,
`exchange` string,
shortName string,
longName string,
exchangeTimezoneName string,
exchangeTimezoneShortName string,
isEsgPopulated string,
gmtOffSetMilliseconds string,
underlyingSymbol string,
quoteType string,
symbol string,
underlyingExchangeSymbol string,
headSymbol string,
messageBoardId string,
uuid string,
market string,
annualHoldingsTurnover string,
enterpriseToRevenue string,
beta3Year string,
enterpriseToEbitda string,
52WeekChange string,
morningStarRiskRating string,
forwardEps string,
revenueQuarterlyGrowth string,
sharesOutstanding string,
fundInceptionDate string,
annualReportExpenseRatio string,
totalAssets string,
bookValue string,
sharesShort string,
sharesPercentSharesOut string,
fundFamily string,
lastFiscalYearEnd string,
heldPercentInstitutions string,
netIncomeToCommon string,
trailingEps string,
lastDividendValue string,
SandP52WeekChange string,
priceToBook string,
heldPercentInsiders string,
nextFiscalYearEnd string,
yield string,
mostRecentQuarter string,
shortRatio string,
sharesShortPreviousMonthDate string,
floatShares string,
beta string,
enterpriseValue string,
priceHint string,
threeYearAverageReturn string,
lastSplitDate string,
lastSplitFactor string,
legalType string,
morningStarOverallRating string,
earningsQuarterlyGrowth string,
priceToSalesTrailing12Months string,
dateShortInterest string,
pegRatio string,
ytdReturn string,
forwardPE string,
lastCapGain string,
shortPercentOfFloat string,
sharesShortPriorMonth string,
category string,
fiveYearAverageReturn string,
previousClose string,
regularMarketOpen string,
twoHundredDayAverage string,
trailingAnnualDividendYield string,
payoutRatio string,
volume24Hr string,
regularMarketDayHigh string,
navPrice string,
averageDailyVolume10Day string,
regularMarketPreviousClose string,
fiftyDayAverage string,
trailingAnnualDividendRate string,
`open` string,
averageVolume10days string,
`expireDate` string,
`algorithm` string,
dividendRate string,
exDividendDate string,
circulatingSupply string,
startDate string,
regularMarketDayLow string,
currency string,
trailingPE string,
regularMarketVolume string,
lastMarket string,
maxSupply string,
openInterest string,
marketCap string,
volumeAllCurrencies string,
strikePrice string,
averageVolume string,
dayLow string,
ask string,
askSize string,
volume string,
fiftyTwoWeekHigh string,
fromCurrency string,
fiveYearAvgDividendYield string,
fiftyTwoWeekLow string,
bid string,
tradeable string,
dividendYield string,
bidSize string,
dayHigh string,
regularMarketPrice string,
preMarketPrice string
)
COMMENT 'Table to store market information'
PARTITIONED BY (change_date string)
STORED AS PARQUET
LOCATION '/raw-data/finance-changes';