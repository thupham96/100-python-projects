# Day 48: 🍪 Cookie Clicker Bot → Auto Upgrade Buyer 🖱️🤖

Turn your browser into a cookie-clicking machine! This Python automation bot plays the [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) game by clicking cookies and purchasing upgrades intelligently to boost performance.

## How It Works

1. **Browser Automation**: Opens Cookie Clicker in Chrome using Selenium.
2. **Cookie Clicking**: Clicks the main cookie repeatedly.
3. **Upgrade Analysis**: Monitors available store upgrades.
4. **Smart Purchasing**: Buys the most expensive item that can be afforded.
5. **Performance Report**: Prints cookies per second after 5 minutes.

## Features

* ⚙️ Automatically clicks the main cookie
* 🏪 Selects and purchases the best upgrades dynamically
* 🧠 Implements logic to only buy affordable items
* ⏱️ Increases upgrade frequency over time
* 📈 Reports cookies per second after timed gameplay

## How to Use

1. Clone the repo and install Selenium:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day48_CookieClickerBot
   pip install selenium
   ```

2. Download and set up [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version, and add it to your PATH.

3. Run the bot:

   ```bash
   python main.py
   ```

## Technologies Used

* Python 3
* `selenium` for browser automation
* Chrome + ChromeDriver

## Example Output

```
Cookies per second: 157.4
```

## What I Learned

* Using Selenium to automate browser interaction
* Extracting and parsing dynamic content with CSS selectors
* Writing smart decision logic for upgrades
* Managing timing and event loops in automation scripts

---

💡 Build your first game bot — let Python click and win cookies for you!
