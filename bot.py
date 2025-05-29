import re

class CryptoAdvisor:
    def __init__(self):
        self.name = "EcoCryptoGuide"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            }
        }

    def greet(self):
        return f"Hi! I'm {self.name}, your eco-friendly crypto advisor! 🌱\nHow can I help you today?"

    def get_sustainable_crypto(self):
        return max(self.crypto_db.items(), key=lambda x: x[1]["sustainability_score"])[0]

    def get_trending_crypto(self):
        trending = [name for name, data in self.crypto_db.items() 
                   if data["price_trend"] == "rising"]
        return trending

    def process_query(self, user_input):
        user_input = user_input.lower()
        
        if "sustainable" in user_input or "eco" in user_input:
            coin = self.get_sustainable_crypto()
            return f"🌱 {coin} is your best bet for sustainability with a score of {self.crypto_db[coin]['sustainability_score']*10}/10!"
        
        elif "trending" in user_input or "rising" in user_input:
            trending = self.get_trending_crypto()
            return f"📈 These coins are trending up: {', '.join(trending)}"
        
        elif "help" in user_input:
            return """I can help you with:
            - Finding sustainable cryptocurrencies
            - Checking which coins are trending
            - Getting general crypto advice
            Just ask me anything!"""
        
        else:
            return "I'm not sure about that. Try asking about sustainable coins or trending cryptocurrencies!"

def main():
    bot = CryptoAdvisor()
    print(bot.greet())
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nThanks for chatting! Remember: Always do your own research before investing! 👋")
            break
            
        response = bot.process_query(user_input)
        print(f"\n{bot.name}: {response}")

if __name__ == "__main__":
    main()