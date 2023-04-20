import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5938202035:AAF0WsU1V5lv3w1_faMJIACbrp5G5xKWh7c
")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu4jz1t363yjncD2gIpd4fBdkmPurDtMKThN7QtlrepbI-4PUB3fSKsAZLOLuCMbn92HKHDhyK6WwGXweepen0QX0drba0zQjppBeHvP6oZSiNYmXiA7y-fFDbIblFoEBF1XzFmBsIBM_Nh9tzIehN4W40-qJTsD4IMSNiHxRjBIEJzuik9FtYC_tjndpfcfv8vLalTv2yNtCXOwf3O4JxasKJqVThNSz9cUh78s0L-4pk6lymUVHppUoaJ3aPdH4XlXxwBe4KxQlCp6uSfpBtLk9wUdoIpwh6uEUOtMNhpfEd_h_B8sd90WsySsc1QzZaWqQ_FIJSahk6ekxSc30Fac=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
