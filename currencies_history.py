from lackey import *
import glob
import csv
import time
from datetime import date, timedelta
import datetime
from database import *

def clicker (img):

    done = False
    while not done:
        try:
            doubleClick(Pattern("images/" + img).similar(0.99))# .exact())
        except:
            done = False
        else:
            done = True

    wait(2)
    doubleClick("images/" + "1596803866478.png")
    wait(2)
    click("images/" + "1596803878783.png")
    wait(2)
    click("images/" + "1596804549302.png")
    wait(2)
    if exists("images/" + "1596805260576.png", 2):
        click(Pattern("images/" + "1596804650551.png").targetOffset(31, 22))
        click("images/" + "1596804575762.png")
    wait(60)
    if exists("images/" + "1596803894691.png", 2):
        click("images/" + "1596803894691.png")
    elif exists("images/" + "1596803894691_2.png", 2):
        click("images/" + "1596803894691_2.png")
    wait(4)
    click("images/" + "1596803910193.png")
    wait(60)

    done = False
    while not done:
        try:
            doubleClick(Pattern("images/" + img).similar(0.99))  # .exact())
        except:
            done = False
        else:
            done = True

    wait(2)

ordered_forex_dict = {
    "AUDCAD" : "1596803847485.png",
    "AUDNZD" : "1596822694142.png",
    "AUDUSD" : "1596909601505.png",
    "CADCHF" : "1596910399598.png",
    "CADJPY" : "1596910432505.png",
    "CHFJPY" : "1596910556340.png",
    "EURAUD" : "1596910589177.png",
    "EURCAD" : "1596910613147.png",
    "EURCHF" : "1596910642104.png",
    "EURGBP" : "1596910666093.png",
    "EURJPY" : "1596910886577.png",
    "EURNOK" : "1596910909741.png",
    "EURNZD" : "1596910941338.png",
    "EURSEK" : "1596910974217.png",
    "EURUSD" : "1596910996294.png",
    "GBPCAD" : "1596911027133.png",
    "GBPCHF" : "1596911048393.png",
    "GBPJPY" : "1596911072764.png",
    "GBPNZD" : "1596911097003.png",
    "GBPUSD" : "1596911122556.png",
    "NZDCAD" : "1596911160554.png",
    "NZDCHF" : "1596911181148.png",
    "NZDJPY" : "1596911205156.png",
    "NZDUSD" : "1596911231968.png",
    "USDCAD" : "1596911259021.png",
    "USDCNH" : "1596911292350.png",
    "USDJPY" : "1596911314366.png",
    "USDMXN" : "1596911336906.png",
    "USDNOK" : "1596911364070.png",
    "USDSEK" : "1596911384888.png",
    "USDZAR" : "1596911407726.png",
    "ZARJPY" : "1596911436741.png"
}

ordered_cfd_dict = {
    "AUS200" : "1596911464283.png",
    "Bund" : "1596911486079.png",
    "Copper" : "1596911503675.png",
    "ESP35" : "1596911520992.png",
    "EUSTX50" : "1596911536959.png",
    "FRA40" : "1596911553463.png",
    "GER30" : "1596911590958.png",
    "JPN225" : "1596911679384.png",
    "NAS100" : "1596911704281.png",
    "NGAS" : "1596911725623.png",
    "SPX500" : "1596911744201.png",
    "UK100" : "1596911772587.png",
    "UKOil" : "1596911798918.png",
    "US30" : "1596911821523.png",
    "USOilSpot" : "1596911842939.png",
    "XAGUSD" : "1596911866705.png",
    "XAUUSD" : "1596911891335.png"
}

ordered_crypto_dict = {
    "BCHUSD" : "1596911917571.png",
    "BTCUSD" : "1596911943146.png",
    "ETHUSD" : "1596911967374.png",
    "LTCUSD" : "1596911991784.png",
    "XRPUSD" : "1596912013668.png"
}

ordered_forex_1_dict = {
    "AUDCHF" : "1596912046798.png",
    "AUDJPY" : "1596912077989.png",
    "GBPAUD" : "1596912106030.png",
    "USDCHF" : "1596912136153.png"
}

def currencies_history(DB):
    # start
    click(Pattern("1596803376084.png").targetOffset(1,-12))
    type(Key.F2)
    #doubleClick(Pattern("1596803847485.png").similar(0.99))

    for key, value in ordered_forex_dict.items():
        clicker(value)

    #open CFD
    doubleClick(Pattern("1596824964488.png").similar(0.99))
    wait(1)

    for key, value in ordered_cfd_dict.items():
        clicker(value)

    #open CRYPTO
    doubleClick(Pattern("1596825203354.png").similar(0.99))
    wait(1)

    for key, value in ordered_crypto_dict.items():
        clicker(value)

    #open FOREX 1
    doubleClick(Pattern("1596825296805.png").similar(0.99))
    wait(1)

    for key, value in ordered_forex_1_dict.items():
        clicker(value)
    ------------------------------
    count = 0
    first = True
    for key, value in ordered_forex_dict.items():
        click(Pattern(value).similar(0.99))
        count = count + 1
        if (first and count == 9) or (not first and divmod(count, 3)[1] == 0):
            wheel(0, 1)
            first = False

    #open CFD
    wheel(0, 1)
    doubleClick(Pattern("1596824964488.png").similar(0.99))
    wait(1)

    count = 0
    for key, value in ordered_cfd_dict.items():
        click(Pattern(value).similar(0.99))
        count = count + 1
        if divmod(count, 3)[1] == 0:
            wheel(0, 1)

    #open CRYPTO
    wheel(0, 1)
    doubleClick(Pattern("1596825203354.png").similar(0.99))
    wait(1)

    count = 0
    for key, value in ordered_crypto_dict.items():
        click(Pattern(value).similar(0.99))
        count = count + 1
        if divmod(count, 3)[1] == 0:
            wheel(0, 1)

    #open FOREX 1
    wheel(0, 1)
    doubleClick(Pattern("1596825296805.png").similar(0.99))
    wait(1)

    count = 0
    for key, value in ordered_forex_1_dict.items():
        click(Pattern(value).similar(0.99))
        count = count + 1
        if divmod(count, 3)[1] == 0:
            wheel(0, 1)

    path = "history\\"

    files = glob.glob(path + '*.csv')
    print(files)

    for i in range(0,len(files)):
        with open(files[i]) as csv_file:

            p = files[i].split("\\")
            p = p[1].split(".csv")
            currency_pair_name = p[0][0:-1]
            print(currency_pair_name)
            create_currency_table = f"""
                                CREATE TABLE IF NOT EXISTS '{currency_pair_name}' (
                                  time DATETIME PRIMARY KEY,
                                  open_bid DOUBLE NOT NULL,
                                  high_bid DOUBLE NOT NULL,
                                  low_bid DOUBLE NOT NULL,
                                  close_bid DOUBLE NOT NULL,
                                  volume DOUBLE NOT NULL
                                );
                                """
            execute_query(DB, create_currency_table)
            HEADER = f"""BEGIN TRANSACTION;"""
            CONTENT = ""
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                trade_time = datetime.datetime(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10]), int(row[1][0:2]),
                                               int(row[1][3:5]), 00)
                open_bid = row[2]
                high_bid = row[3]
                low_bid = row[4]
                close_bid = row[5]
                volume = row[6]
                CONTENT = CONTENT + f""" INSERT or IGNORE INTO '{currency_pair_name}' VALUES ('{trade_time}','{open_bid}','{high_bid}','{low_bid}','{close_bid}','{volume}');"""
            FOOTER = f""" COMMIT;"""
            QUERY = HEADER + CONTENT + FOOTER
            execute_multiple_queries(DB, QUERY)
