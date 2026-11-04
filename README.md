# Higher or Lower: The Trivia Challenge

A two-player, pass-and-play card game built with Streamlit.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Visit https://share.streamlit.io/.
2. Choose **Create app** and connect this GitHub repository.
3. Select branch `main` and main file path `app.py`.
4. Select **Deploy**.

## How to play

- Each player starts with five cards. The first card in each row is face-up.
- Guess whether the next card is higher or lower. A correct guess advances your run.
- A wrong guess resets your row and passes the turn.
- A matching rank (a Pair) preserves your progress but ends your turn. Spend an Ace to break the freeze and continue.
- Odd cards (3, 5, 7 and 9) trigger a trivia question. A wrong answer costs one card and lets the opponent try to steal the same question.
- A successful steal earns a Free Flip token, which can be used on a future turn to advance without a Higher/Lower guess.
- Pocketed Aces can protect against a wrong guess, break a Pair freeze, or skip a trivia trap.
- First player to clear all five cards wins.

This is designed for two people sharing one browser session.
