# Vanguard Ticker 📈

Get a push notification containing Vanguard FTSE Global All Cap Index Fund
data whenenver the fund price is updated.

### Prerequisites
* [Python3](https://www.python.org/download/releases/3.0/)
* [pipenv](https://pypi.org/project/pipenv/)

### Setup

1. **Installation**

   Clone this repo and run:
   ```bash
   pipenv sync
   ```
1. **Create the IFTTT applet**

   1. If you don't already have one, sign up for an
      [IFTTT account](https://ifttt.com/) and download and login to the IFTTT
      app on the device you want to receive the push notification on
   1. [Create](https://ifttt.com/create) a new IFTTT applet
   1. For _This_, select the _Webhooks_ service and choose
      _Receive a web request_
   1. Enter `vanguard_ticker` as the Event Name and click _Create Trigger_
   1. For _That_, select the _Notifications_ service and choose
      _Send a rich notification from the IFTTT app_
   1. Change the _Title_ field to `{{Value1}}`
   1. Change the _Message_ field to `{{Value2}}`
   1. Change the _Image URL_ field to `{{Value3}}`
   1. Click _Create Action_ and then _Finish_
1. **Get your IFTTT Webhook API key**
   1. Go to your [Webhook Settings](https://ifttt.com/maker_webhooks/settings)
   1. Copy the API key listed as part of the URL
      (`https://maker.ifttt.com/use/<API-KEY>`) for use below

### Usage

1. Create a `.env` file in the root of the repo containing the IFTTT Webhook API
   key you retrieved above.
   ```bash
   $ cat .env

   IFTTT_API_KEY=...
   ```
1. To get a highlight sent to you via a push notification, run:
   ```bash
   pipenv run python send-ticker.py
   ```


### Getting notifications

To get a notification sent to you whenever the fund price has updated, use
crontab on a device of your choice to periodically fetch the latest fund price.
You will only be notified when the price has changed (the notification will
contain the closing price along with the real and percentage change):
```
*/30 * * * *  cd ~/<path-to-repo>/vanguard-ticker && pipenv run python send-ticker.py
```

