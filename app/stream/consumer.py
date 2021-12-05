from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
import  pyspark.sql.functions as F

spark = (SparkSession
         .builder
         .appName('finance-changes-event-consumer')
         .getOrCreate())
sc = spark.sparkContext

df = (spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092") # kafka server
  .option("subscribe", "finance") # topic
  .option("startingOffsets", "earliest") # start from beginning 
  .load())

# Convert binary to string key and value
df1 = (df
    .withColumn("key", df["key"].cast(StringType()))
    .withColumn("value", df["value"].cast(StringType())))

schema = spark.read.option("multiline", "true").json("/raw-data/sample_schema.json").schema

df_finance = (df1
           # Sets schema for event data
           .withColumn("value", F.from_json("value", schema))
           .select(
              F.col("value.sector").alias("sector"),
              F.col("value.fullTimeEmployees").alias("fullTimeEmployees"),
              F.col("value.city").alias("city"),
              F.col("value.phone").alias("phone"),
              F.col("value.state").alias("state"),
              F.col("value.country").alias("country"),
              F.col("value.address1").alias("address1"),
              F.col("value.industry").alias("industry"),
              F.col("value.ebitdaMargins").alias("ebitdaMargins"),
              F.col("value.profitMargins").alias("profitMargins"),
              F.col("value.grossMargins").alias("grossMargins"),
              F.col("value.operatingCashflow").alias("operatingCashflow"),
              F.col("value.revenueGrowth").alias("revenueGrowth"),
              F.col("value.operatingMargins").alias("operatingMargins"),
              F.col("value.ebitda").alias("ebitda"),
              F.col("value.targetLowPrice").alias("targetLowPrice"),
              F.col("value.recommendationKey").alias("recommendationKey"),
              F.col("value.grossProfits").alias("grossProfits"),
              F.col("value.freeCashflow").alias("freeCashflow"),
              F.col("value.targetMedianPrice").alias("targetMedianPrice"),
              F.col("value.currentPrice").alias("currentPrice"),
              F.col("value.earningsGrowth").alias("earningsGrowth"),
              F.col("value.currentRatio").alias("currentRatio"),
              F.col("value.returnOnAssets").alias("returnOnAssets"),
              F.col("value.targetMeanPrice").alias("targetMeanPrice"),
              F.col("value.debtToEquity").alias("debtToEquity"),
              F.col("value.returnOnEquity").alias("returnOnEquity"),
              F.col("value.targetHighPrice").alias("targetHighPrice"),
              F.col("value.totalCash").alias("totalCash"),
              F.col("value.totalDebt").alias("totalDebt"),
              F.col("value.totalRevenue").alias("totalRevenue"),
              F.col("value.totalCashPerShare").alias("totalCashPerShare"),
              F.col("value.financialCurrency").alias("financialCurrency"),
              F.col("value.revenuePerShare").alias("revenuePerShare"),
              F.col("value.quickRatio").alias("quickRatio"),
              F.col("value.recommendationMean").alias("recommendationMean"),
              F.col("value.exchange").alias("exchange"),
              F.col("value.shortName").alias("shortName"),
              F.col("value.longName").alias("longName"),
              F.col("value.exchangeTimezoneName").alias("exchangeTimezoneName"),
              F.col("value.exchangeTimezoneShortName").alias("exchangeTimezoneShortName"),
              F.col("value.isEsgPopulated").alias("isEsgPopulated"),
              F.col("value.gmtOffSetMilliseconds").alias("gmtOffSetMilliseconds"),
              F.col("value.underlyingSymbol").alias("underlyingSymbol"),
              F.col("value.quoteType").alias("quoteType"),
              F.col("value.symbol").alias("symbol"),
              F.col("value.underlyingExchangeSymbol").alias("underlyingExchangeSymbol"),
              F.col("value.headSymbol").alias("headSymbol"),
              F.col("value.messageBoardId").alias("messageBoardId"),
              F.col("value.uuid").alias("uuid"),
              F.col("value.market").alias("market"),
              F.col("value.annualHoldingsTurnover").alias("annualHoldingsTurnover"),
              F.col("value.enterpriseToRevenue").alias("enterpriseToRevenue"),
              F.col("value.beta3Year").alias("beta3Year"),
              F.col("value.enterpriseToEbitda").alias("enterpriseToEbitda"),
              F.col("value.52WeekChange").alias("52WeekChange"),
              F.col("value.morningStarRiskRating").alias("morningStarRiskRating"),
              F.col("value.forwardEps").alias("forwardEps"),
              F.col("value.revenueQuarterlyGrowth").alias("revenueQuarterlyGrowth"),
              F.col("value.sharesOutstanding").alias("sharesOutstanding"),
              F.col("value.fundInceptionDate").alias("fundInceptionDate"),
              F.col("value.annualReportExpenseRatio").alias("annualReportExpenseRatio"),
              F.col("value.totalAssets").alias("totalAssets"),
              F.col("value.bookValue").alias("bookValue"),
              F.col("value.sharesShort").alias("sharesShort"),
              F.col("value.sharesPercentSharesOut").alias("sharesPercentSharesOut"),
              F.col("value.fundFamily").alias("fundFamily"),
              F.col("value.lastFiscalYearEnd").alias("lastFiscalYearEnd"),
              F.col("value.heldPercentInstitutions").alias("heldPercentInstitutions"),
              F.col("value.netIncomeToCommon").alias("netIncomeToCommon"),
              F.col("value.trailingEps").alias("trailingEps"),
              F.col("value.lastDividendValue").alias("lastDividendValue"),
              F.col("value.SandP52WeekChange").alias("SandP52WeekChange"),
              F.col("value.priceToBook").alias("priceToBook"),
              F.col("value.heldPercentInsiders").alias("heldPercentInsiders"),
              F.col("value.nextFiscalYearEnd").alias("nextFiscalYearEnd"),
              F.col("value.yield").alias("yield"),
              F.col("value.mostRecentQuarter").alias("mostRecentQuarter"),
              F.col("value.shortRatio").alias("shortRatio"),
              F.col("value.sharesShortPreviousMonthDate").alias("sharesShortPreviousMonthDate"),
              F.col("value.floatShares").alias("floatShares"),
              F.col("value.beta").alias("beta"),
              F.col("value.enterpriseValue").alias("enterpriseValue"),
              F.col("value.priceHint").alias("priceHint"),
              F.col("value.threeYearAverageReturn").alias("threeYearAverageReturn"),
              F.col("value.lastSplitDate").alias("lastSplitDate"),
              F.col("value.lastSplitFactor").alias("lastSplitFactor"),
              F.col("value.legalType").alias("legalType"),
              F.col("value.morningStarOverallRating").alias("morningStarOverallRating"),
              F.col("value.earningsQuarterlyGrowth").alias("earningsQuarterlyGrowth"),
              F.col("value.priceToSalesTrailing12Months").alias("priceToSalesTrailing12Months"),
              F.col("value.dateShortInterest").alias("dateShortInterest"),
              F.col("value.pegRatio").alias("pegRatio"),
              F.col("value.ytdReturn").alias("ytdReturn"),
              F.col("value.forwardPE").alias("forwardPE"),
              F.col("value.lastCapGain").alias("lastCapGain"),
              F.col("value.shortPercentOfFloat").alias("shortPercentOfFloat"),
              F.col("value.sharesShortPriorMonth").alias("sharesShortPriorMonth"),
              F.col("value.category").alias("category"),
              F.col("value.fiveYearAverageReturn").alias("fiveYearAverageReturn"),
              F.col("value.previousClose").alias("previousClose"),
              F.col("value.regularMarketOpen").alias("regularMarketOpen"),
              F.col("value.twoHundredDayAverage").alias("twoHundredDayAverage"),
              F.col("value.trailingAnnualDividendYield").alias("trailingAnnualDividendYield"),
              F.col("value.payoutRatio").alias("payoutRatio"),
              F.col("value.volume24Hr").alias("volume24Hr"),
              F.col("value.regularMarketDayHigh").alias("regularMarketDayHigh"),
              F.col("value.navPrice").alias("navPrice"),
              F.col("value.averageDailyVolume10Day").alias("averageDailyVolume10Day"),
              F.col("value.regularMarketPreviousClose").alias("regularMarketPreviousClose"),
              F.col("value.fiftyDayAverage").alias("fiftyDayAverage"),
              F.col("value.trailingAnnualDividendRate").alias("trailingAnnualDividendRate"),
              F.col("value.open").alias("open"),
              F.col("value.averageVolume10days").alias("averageVolume10days"),
              F.col("value.expireDate").alias("expireDate"),
              F.col("value.algorithm").alias("algorithm"),
              F.col("value.dividendRate").alias("dividendRate"),
              F.col("value.exDividendDate").alias("exDividendDate"),
              F.col("value.circulatingSupply").alias("circulatingSupply"),
              F.col("value.startDate").alias("startDate"),
              F.col("value.regularMarketDayLow").alias("regularMarketDayLow"),
              F.col("value.currency").alias("currency"),
              F.col("value.trailingPE").alias("trailingPE"),
              F.col("value.regularMarketVolume").alias("regularMarketVolume"),
              F.col("value.lastMarket").alias("lastMarket"),
              F.col("value.maxSupply").alias("maxSupply"),
              F.col("value.openInterest").alias("openInterest"),
              F.col("value.marketCap").alias("marketCap"),
              F.col("value.volumeAllCurrencies").alias("volumeAllCurrencies"),
              F.col("value.strikePrice").alias("strikePrice"),
              F.col("value.averageVolume").alias("averageVolume"),
              F.col("value.dayLow").alias("dayLow"),
              F.col("value.ask").alias("ask"),
              F.col("value.askSize").alias("askSize"),
              F.col("value.volume").alias("volume"),
              F.col("value.fiftyTwoWeekHigh").alias("fiftyTwoWeekHigh"),
              F.col("value.fromCurrency").alias("fromCurrency"),
              F.col("value.fiveYearAvgDividendYield").alias("fiveYearAvgDividendYield"),
              F.col("value.fiftyTwoWeekLow").alias("fiftyTwoWeekLow"),
              F.col("value.bid").alias("bid"),
              F.col("value.tradeable").alias("tradeable"),
              F.col("value.dividendYield").alias("dividendYield"),
              F.col("value.bidSize").alias("bidSize"),
              F.col("value.dayHigh").alias("dayHigh"),
              F.col("value.regularMarketPrice").alias("regularMarketPrice"),
              F.col("value.preMarketPrice").alias("preMarketPrice"),
              F.col("value.change_date").alias("change_date"),
           )
          )

# Start query stream over stream dataframe
raw_path = "/raw-data/finance-changes"
checkpoint_path = "/raw-data/finance-changes-checkpoint"

queryStream =(
    df_finance
    .writeStream
    .format("parquet")
    .queryName("finance_changes_ingestion")
    .option("checkpointLocation", checkpoint_path)
    .option("path", raw_path)
    .outputMode("append")
    .partitionBy("change_date")
    .start())

queryStream.awaitTermination(100)