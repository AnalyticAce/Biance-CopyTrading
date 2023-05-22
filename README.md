# Bot Telegram Binance
***
Un bot Telegram qui suit les traders les plus performants et envoie des notifications lorsqu'ils effectuent un nouveau trade ou ferment une position.

## Technologies Utilisées
***
- Python 3.8.5
- Python-telegram-bot 13.6
- Python-binance 1.0.12

## Installation
***
1. Cloner le dépôt
```bash
git clone git@github.com:AnalyticAce/Biance-CopyTrading.git
```

2. Installer les packages requis
```bash
pip install -r requirements.txt
```
3. Exécuter du script
```bash
python3 script.py
```

## Utilisation
***
- Ajoutez le bot à votre groupe Telegram.
- Le bot suit automatiquement les traders les plus performants spécifiés dans la liste traders_to_follow.
- Lorsqu'un trader effectue un nouveau trade, le bot envoie une notification avec les détails du trade.
- Lorsqu'un trader ferme une position, le bot envoie une notification avec les détails de la position fermée.
