import random
import streamlit as st

st.set_page_config(page_title="Higher or Lower | Trivia Challenge", page_icon="🂡", layout="wide")

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stMainBlockContainer"], .stApp, section.main {background:radial-gradient(ellipse at 50% 0%,#632044 0%,#29132f 42%,#111426 82%,#080b16 100%) !important;color:#fff5df !important;}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], footer {background:transparent !important;}
[data-testid="stHeader"] {height:0;visibility:hidden;}
.block-container {max-width:1320px;padding-top:1.1rem;padding-bottom:3rem;background:transparent !important;}
.stApp, .stApp * {color-scheme:dark;}
[data-testid="stVerticalBlock"] {background:transparent;}
h1,h2,h3 {font-family:'Playfair Display',serif !important;color:#fff3d1;}
p,div,span,label {font-family:'DM Sans',sans-serif;}
.hero {text-align:center;padding:1.1rem 1rem 1.5rem;border:3px solid #d9b65e;border-radius:22px;background:linear-gradient(110deg,rgba(100,18,47,.94),rgba(29,24,58,.96),rgba(100,18,47,.94));box-shadow:0 0 0 5px rgba(217,182,94,.12),0 0 35px rgba(241,187,77,.22);margin-bottom:1.2rem;}
.eyebrow {color:#ffe29a;letter-spacing:.3em;font-size:.72rem;font-weight:800;text-transform:uppercase;}
.hero h1 {font-size:clamp(2.5rem,6vw,5rem);line-height:1.02;margin:.25rem 0;text-transform:uppercase;text-shadow:0 4px 0 #702342,0 7px 18px #000;}
.subtitle {color:#ffe9bd;font-size:1rem;letter-spacing:.04em;}
.panel {background:linear-gradient(145deg,rgba(74,24,54,.97),rgba(24,29,58,.98));border:2px solid rgba(231,192,103,.65);border-radius:16px;padding:1.1rem 1.2rem;box-shadow:0 10px 28px rgba(0,0,0,.3),inset 0 0 22px rgba(255,255,255,.025);margin-bottom:1rem;}
.player-a {border-top:5px solid #4bb9ef;}.player-b {border-top:5px solid #f16d75;}
.player-name {font-size:1.1rem;font-weight:800;color:#fff;}
.stat {color:#f1d8a4;font-size:.74rem;text-transform:uppercase;letter-spacing:.1em;}
.big-stat {font-size:1.65rem;font-weight:800;color:#ffdc82;text-shadow:0 2px 8px #000;}
.playing {color:#ffe08b;font-weight:800;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;}
.playing-card {position:relative;box-sizing:border-box;display:block;padding:0;border-radius:11px;overflow:hidden;font-family:Georgia,serif;isolation:isolate;}
.card-front {background:linear-gradient(145deg,#fffefa 0%,#f7f0e2 68%,#e9dfcc 100%);color:#171522;border:3px solid #d9b967;box-shadow:inset 0 0 0 2px #fff,inset 0 0 18px rgba(91,62,27,.08),0 5px 12px rgba(0,0,0,.3);}
.card-front:before {content:"";position:absolute;inset:5px;border:1px solid rgba(150,117,65,.4);border-radius:6px;pointer-events:none;z-index:0;}
.card-corner {position:absolute;z-index:2;display:flex;flex-direction:column;align-items:center;gap:1px;font-size:1.18rem;font-weight:900;line-height:.9;min-width:22px;}
.card-corner small {font-size:.9rem;line-height:1;}
.card-top {top:10px;left:12px;}
.card-bottom {right:12px;bottom:10px;transform:rotate(180deg);}
.card-pip {position:absolute;inset:0;display:grid;place-items:center;font-size:3.25rem;line-height:1;z-index:1;text-shadow:0 1px 0 rgba(0,0,0,.08);}
.card-red {color:#bd263f;}
.card-gold {background:linear-gradient(145deg,#fff7d8,#f0d38a 72%,#dfbb68);border-color:#f2d991;}
.active-turn-card {height:164px !important;transform:scale(1.035);z-index:3;box-shadow:0 0 0 3px rgba(255,224,138,.28),0 0 24px rgba(255,204,94,.42),inset 0 0 0 2px #fff !important;animation:activeCardExpand .55s cubic-bezier(.2,.85,.25,1) both;transform-origin:center center;}
.pip-field {position:absolute;inset:17px 30px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(5,1fr);align-items:center;justify-items:center;z-index:1;}
.pip {font-size:1.28rem;line-height:1;text-shadow:0 1px 0 rgba(0,0,0,.08);}
.pip-0{grid-column:1;grid-row:1}.pip-1{grid-column:2;grid-row:1}.pip-2{grid-column:1;grid-row:2}.pip-3{grid-column:2;grid-row:2}.pip-4{grid-column:1 / span 2;grid-row:3}.pip-5{grid-column:1 / span 2;grid-row:3}.pip-6{grid-column:1;grid-row:4}.pip-7{grid-column:2;grid-row:4}.pip-8{grid-column:1;grid-row:5}.pip-9{grid-column:2;grid-row:5}
.pip-4:nth-of-type(10){grid-column:2;grid-row:3}
.court-mark {position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:10px;font-family:Georgia,serif;font-size:3.6rem;font-weight:900;color:inherit;text-shadow:0 2px 0 rgba(0,0,0,.08);}
.court-mark span {font-size:3.2rem;}
@keyframes activeCardExpand {0%{height:116px;transform:scale(.94);filter:brightness(1.25)}65%{height:172px;transform:scale(1.055)}100%{height:164px;transform:scale(1.035);filter:brightness(1)}}
@media(max-height:700px){.active-turn-card{height:142px !important}.pip-field{inset:15px 24px}.pip{font-size:1.05rem}}
.scoreboard {display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin:.25rem 0 .8rem;}
.score-card {position:relative;overflow:hidden;background:linear-gradient(145deg,rgba(53,24,62,.98),rgba(22,29,57,.98));border:2px solid #c7a65d;border-radius:15px;padding:.8rem 1rem;box-shadow:0 7px 18px rgba(0,0,0,.28);}
.score-card.player-a {border-top:5px solid #4bb9ef;}.score-card.player-b {border-top:5px solid #f16d75;}
.score-top {display:flex;justify-content:space-between;align-items:center;gap:10px;}
.score-name {font-size:1.05rem;font-weight:900;color:#fff7e5;}
.score-bank {font-size:2rem;line-height:1.1;font-weight:900;color:#ffdf8c;text-shadow:0 2px 10px rgba(0,0,0,.65);}
.score-label {font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:#e8d3a5;font-weight:800;}
.score-meta {display:flex;gap:1rem;align-items:center;color:#eadbc4;font-size:.78rem;margin-top:.45rem;}
.ladder {display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-top:.65rem;}
.ladder-step {height:7px;border-radius:8px;background:rgba(255,255,255,.13);border:1px solid rgba(255,226,154,.2);}
.ladder-step.done {background:linear-gradient(90deg,#f3c45d,#fff0ad);box-shadow:0 0 9px rgba(255,210,105,.35);}
.score-active {font-size:.65rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:#ffe08b;}
.card-reveal {animation:cardReveal .62s cubic-bezier(.2,.8,.2,1) both;transform-origin:center;}
@keyframes cardReveal {0%{opacity:.15;transform:rotateY(88deg) scale(.88);filter:brightness(1.8);}55%{opacity:1;transform:rotateY(-9deg) scale(1.04);filter:brightness(1.3);}100%{transform:rotateY(0) scale(1);filter:brightness(1);}}
.winner-stage {position:relative;overflow:hidden;text-align:center;padding:2.3rem 1rem 2rem;border:3px solid #ffe29a;border-radius:22px;background:radial-gradient(ellipse at 50% 0%,#9a3158 0%,#4c1a45 42%,#171a39 100%);box-shadow:0 0 0 7px rgba(255,220,130,.12),0 0 55px rgba(255,196,79,.3);animation:winnerPop .8s cubic-bezier(.18,.85,.3,1.2) both;}
.winner-stage:before,.winner-stage:after {content:"✦  ✧  ★  ✧  ✦";position:absolute;left:0;right:0;color:#ffe7a1;letter-spacing:1.2rem;font-size:1.2rem;opacity:.8;animation:sparkle 2s ease-in-out infinite alternate;}
.winner-stage:before {top:12px;}.winner-stage:after {bottom:12px;}
.winner-kicker {font-size:.8rem;letter-spacing:.28em;font-weight:900;color:#ffe7a1;text-transform:uppercase;}
.winner-name {font-family:'Playfair Display',serif;font-size:clamp(2.3rem,6vw,4.6rem);font-weight:900;color:#fff4d4;text-shadow:0 4px 0 #78294a,0 8px 22px #000;margin:.4rem 0;}
.winner-prize {font-size:clamp(3rem,8vw,5.8rem);font-weight:1000;line-height:1;color:#ffe08a;text-shadow:0 4px 0 #875c28,0 0 30px rgba(255,220,130,.5);margin:.7rem 0;}
.winner-sub {color:#fff0ce;font-size:1rem;font-weight:700;}
@keyframes winnerPop {0%{opacity:0;transform:scale(.82) translateY(18px);}100%{opacity:1;transform:scale(1) translateY(0);}}
@keyframes sparkle {from{opacity:.35;transform:translateY(-3px);}to{opacity:1;transform:translateY(3px);}}
@media(max-width:650px){.scoreboard{grid-template-columns:1fr;}.score-bank{font-size:1.7rem;}.winner-stage{padding:2rem .5rem;}}
.event {background:linear-gradient(100deg,rgba(116,27,54,.92),rgba(52,31,65,.95));border:2px solid #d9b65e;border-radius:13px;padding:1rem;color:#fff0c7;box-shadow:0 7px 20px rgba(0,0,0,.2);}
.muted {color:#d8c5bd;}
div.stButton > button {border-radius:12px;font-weight:900;min-height:2.8rem;border:2px solid #d8b86b;letter-spacing:.025em;transition:transform .12s ease,filter .12s ease;}
div.stButton > button:hover {transform:translateY(-2px);filter:brightness(1.12);border-color:#fff0b4;}
div.stButton > button[kind="primary"] {background:linear-gradient(180deg,#ffe6a0,#d5a843);color:#35152e;border:2px solid #fff0b4;box-shadow:0 4px 0 #875c28;}
div[class*="st-key-flip_"] button {position:relative;height:116px;min-height:116px;width:100%;border-radius:11px;background:radial-gradient(ellipse at center,#792944 0%,#4b1832 78%) !important;color:transparent!important;border:3px solid #d9b967!important;box-shadow:inset 0 0 0 3px #351226,inset 0 0 0 5px #e4c575,0 5px 12px rgba(0,0,0,.32)!important;font-family:Georgia,serif;font-size:0!important;white-space:pre-wrap;overflow:hidden;}
div[class*="st-key-flip_"] button:before {content:"";position:absolute;inset:8px;border:1px solid rgba(255,224,157,.75);border-radius:5px;background:repeating-linear-gradient(45deg,transparent 0 11px,rgba(255,220,145,.09) 11px 13px),repeating-linear-gradient(-45deg,transparent 0 11px,rgba(255,220,145,.09) 11px 13px);}
div[class*="st-key-flip_"] button:after {content:"✦";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:42px;height:42px;display:grid;place-items:center;border:1px solid #e6c778;border-radius:50%;background:radial-gradient(circle,#8c3550,#511b36);color:#ffe5a0;font-size:1.45rem;text-shadow:0 2px 5px #250d1d;box-shadow:0 0 0 4px rgba(228,197,117,.12);}
div[class*="st-key-flip_"] button:disabled {opacity:.86;filter:saturate(.85);}
div[data-testid="stRadio"] label {color:#fff0d0!important;}
div[data-testid="stAlert"] {border-radius:12px;}hr {border-color:rgba(231,192,103,.35);}
/* Compact desktop layout to minimise scrolling on standard laptop screens. */
.block-container {max-width:1600px;padding:.45rem 1.4rem .7rem !important;background:transparent !important;}
[data-testid="stMainBlockContainer"] [data-testid="stVerticalBlock"] {gap:.48rem !important;}
[data-testid="stMarkdownContainer"] p {margin-bottom:.2rem;}
[data-testid="stMarkdownContainer"] h2 {font-size:1.15rem;margin:.15rem 0;}
[data-testid="stMarkdownContainer"] h3 {font-size:1.05rem;margin:.15rem 0;}
[data-testid="stHorizontalBlock"] {gap:.5rem !important;}
.hero {padding:.45rem .8rem .55rem !important;margin-bottom:.35rem !important;border-width:2px !important;}
.hero h1 {font-size:clamp(2rem,4vw,3.2rem) !important;margin:.05rem 0 !important;}
.eyebrow {font-size:.58rem !important;letter-spacing:.2em !important;}
.subtitle {font-size:.78rem !important;}
.panel {padding:.55rem .8rem !important;margin-bottom:.25rem !important;border-radius:12px !important;}
.player-name {font-size:.95rem !important;}
.big-stat {font-size:1.2rem !important;}
.stat {font-size:.62rem !important;}
.event {padding:.45rem .7rem !important;margin:.1rem 0 !important;}
div.stButton > button {min-height:2.45rem !important;padding:.35rem .65rem !important;background:linear-gradient(180deg,#6e2447,#42172f) !important;color:#fff1d1 !important;border:2px solid #bd9650 !important;box-shadow:0 3px 0 #241020 !important;}
div.stButton > button[kind="primary"] {background:linear-gradient(180deg,#ffe6a0,#d5a843) !important;color:#35152e !important;border:2px solid #fff0b4 !important;box-shadow:0 3px 0 #875c28 !important;}
div.stButton > button:disabled {opacity:.55 !important;color:#cbbca9 !important;}
div[class*="st-key-flip_"] button {height:116px !important;min-height:116px !important;font-size:0 !important;}
@media (max-height:700px) {
 .hero {padding:.25rem .6rem !important;}
 .hero h1 {font-size:2rem !important;}
 .panel {padding:.35rem .55rem !important;}
 div[class*="st-key-flip_"] button {height:96px !important;min-height:96px !important;}
 .card-pip {font-size:2rem !important;}
}
</style>
""", unsafe_allow_html=True)

SUITS = ["♠", "♥", "♦", "♣"]
RED_SUITS = {"♥", "♦"}
RANKS = list(range(1, 14))
RANK_LABELS = {1:"A", 11:"J", 12:"Q", 13:"K"}
# Trivia questions are supplied verbally by the host; none are built into the app.

def make_card():
    return {"rank": random.choice(RANKS), "suit": random.choice(SUITS)}

PIP_POSITIONS = {
    1: [4],
    2: [0, 9],
    3: [0, 4, 9],
    4: [0, 1, 8, 9],
    5: [0, 1, 4, 8, 9],
    6: [0, 1, 2, 7, 8, 9],
    7: [0, 1, 2, 4, 7, 8, 9],
    8: [0, 1, 2, 3, 6, 7, 8, 9],
    9: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    10: [0, 1, 2, 3, 6, 7, 8, 9, 4, 5],
}

def card_pip_pattern(rank, suit):
    positions = PIP_POSITIONS.get(rank)
    if not positions:
        return f'<div class="court-mark">{RANK_LABELS.get(rank, str(rank))}<span>{suit}</span></div>'
    return '<div class="pip-field">' + ''.join(f'<span class="pip pip-{pos}">{suit}</span>' for pos in positions) + '</div>'

def card_text(card):
    return RANK_LABELS.get(card["rank"], str(card["rank"]))

PRIZE_LADDER = {1: 0, 2: 100, 3: 250, 4: 500, 5: 1000}

def prize_money(progress):
    return PRIZE_LADDER.get(min(5, max(1, progress)), 0)

def new_row():
    return [make_card() for _ in range(5)]

def fresh_game(names):
    players = []
    for name in names:
        players.append({"name": name, "row": new_row(), "progress": 1, "aces": 0, "free_flips": 0})
    return {"players": players, "current": 0, "pending": None, "winner": None,
            "log": [f"{names[0]} starts the challenge."], "last_message": "Host: ask the player for Higher or Lower, then click their next face-down card.", "host_guess": None, "host_use_free_flip": False, "last_reveal": None}

def log(message):
    st.session_state.game["log"].insert(0, message)
    st.session_state.game["log"] = st.session_state.game["log"][:12]

def switch_turn(message):
    g = st.session_state.game
    g["current"] = 1 - g["current"]
    g["pending"] = None
    g["host_guess"] = None
    g["host_use_free_flip"] = False
    g["last_message"] = message
    p = g["players"][g["current"]]
    if p["progress"] == 0:
        p["row"][0] = make_card()
        p["progress"] = 1
        log(f"{p['name']} turns over a fresh starting card.")
    st.rerun()

def win_check(player_index):
    g = st.session_state.game
    p = g["players"][player_index]
    if p["progress"] >= 5:
        g["winner"] = player_index
        g["pending"] = None
        log(f"{p['name']} completed all five cards and won!")
        st.rerun()

def lose_one(player_index):
    p = st.session_state.game["players"][player_index]
    p["progress"] = max(0, p["progress"] - 1)
    # The highest completed card is turned face down.
    if p["progress"] < 5:
        p["row"][p["progress"]] = make_card()

def reset_row(player_index):
    p = st.session_state.game["players"][player_index]
    p["row"] = new_row()
    p["progress"] = 1

def resolve_reveal(player_index, free=False, guess=None):
    g = st.session_state.game
    p = g["players"][player_index]
    idx = p["progress"]
    if idx >= 5:
        win_check(player_index)
        return
    previous = p["row"][idx - 1]
    card = p["row"][idx]
    p["revealed"] = idx
    g["last_reveal"] = {"player": player_index, "index": idx}
    rank = card["rank"]

    if rank == 1:
        p["aces"] += 1
        p["row"][idx] = make_card()
        log(f"{p['name']} found an Ace and pocketed it.")
        g["last_message"] = f"{p['name']} found an Ace! It has been added to their reserve."
        return

    if rank == previous["rank"]:
        g["pending"] = {"type":"pair", "player":player_index, "card":card}
        if p["aces"] == 0:
            p["progress"] += 1
            log(f"{p['name']} hit a Pair. Progress is safe, but the turn ends.")
            win_check(player_index)
            switch_turn(f"Pair! {p['name']}'s progress is safe. {g['players'][1-player_index]['name']} is up next.")
        else:
            g["last_message"] = f"Pair! Spend an Ace to break the freeze and keep playing, or let the turn pass."
        return

    if rank in (3, 5, 7, 9):
        g["pending"] = {"type":"trivia", "player":player_index, "card":card, "free":free}
        g["last_message"] = f"Trivia trap! {p['name']} must answer correctly to keep the run alive."
        return

    if not free and guess == "Higher" and rank <= previous["rank"]:
        g["pending"] = {"type":"wrong", "player":player_index, "card":card, "guess":guess}
        g["last_message"] = "Not higher! You can spend an Ace to avoid the full reset, or take the reset."
        return
    if not free and guess == "Lower" and rank >= previous["rank"]:
        g["pending"] = {"type":"wrong", "player":player_index, "card":card, "guess":guess}
        g["last_message"] = "Not lower! You can spend an Ace to avoid the full reset, or take the reset."
        return

    p["progress"] += 1
    log(f"{p['name']} advanced to card {p['progress']}." + (" with a Free Flip." if free else ""))
    g["last_message"] = f"Correct! {p['name']} can make another call."
    win_check(player_index)

def answer_trivia(correct, stealing=False):
    g = st.session_state.game
    pending = g["pending"]
    original_player = pending["player"]
    actor = 1 - original_player if stealing else original_player
    p = g["players"][actor]

    if correct:
        p["progress"] += 1
        log(f"{p['name']} answered the host's trivia question correctly and moved forward one card.")
        g["pending"] = None
        g["host_guess"] = None
        g["host_use_free_flip"] = False
        g["current"] = actor
        g["last_message"] = (
            f"Correct! {p['name']} steals the question, moves forward one card and keeps the turn. "
            "Make the next Higher or Lower call."
            if stealing else
            f"Correct! {p['name']} beats the trivia trap and can make the next call."
        )
        win_check(actor)
    else:
        lose_one(actor)
        log(f"{p['name']} answered the trivia question incorrectly and moved back one card.")
        g["pending"] = None
        g["host_guess"] = None
        g["host_use_free_flip"] = False
        if stealing:
            # A failed steal sends play back to the player who originally hit the trap.
            g["current"] = original_player
            g["last_message"] = (
                f"Wrong answer! {p['name']} moves back one card. "
                f"{g['players'][original_player]['name']} gets the turn back."
            )
        else:
            g["pending"] = {"type":"steal", "player":original_player}
            g["last_message"] = (
                f"Wrong answer! {p['name']} moves back one card. "
                f"{g['players'][1-actor]['name']} can now answer the same question to steal."
            )

# ---------- Setup ----------
if "game" not in st.session_state:
    st.session_state.setup = True
    st.session_state.game = None

st.markdown('<div class="hero"><div class="eyebrow">Ladies and gentlemen · Your Saturday night game show</div><h1>Higher or Lower!</h1><div class="subtitle">THE TRIVIA CHALLENGE · BIG CARDS · BIG CALLS · BIG DRAMA</div></div>', unsafe_allow_html=True)

if st.session_state.get("setup", True):
    st.markdown('<div class="panel"><h3 style="text-align:center">Set up the table</h3><p class="muted" style="text-align:center">Two players. Five cards each. Clear the cards, climb the prize ladder and win the £1,000 jackpot.</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        name1 = st.text_input("Player 1", value="Player 1", max_chars=18)
    with c2:
        name2 = st.text_input("Player 2", value="Player 2", max_chars=18)
    if st.button("🂡  Deal the cards", type="primary", use_container_width=True):
        names = [name1.strip() or "Player 1", name2.strip() or "Player 2"]
        if names[0].casefold() == names[1].casefold():
            st.warning("Please choose two different player names.")
        else:
            st.session_state.game = fresh_game(names)
            st.session_state.setup = False
            st.rerun()
    st.markdown('<div class="panel"><h3>Prize ladder</h3><p><b>2 cards:</b> £100 &nbsp; · &nbsp; <b>3 cards:</b> £250 &nbsp; · &nbsp; <b>4 cards:</b> £500 &nbsp; · &nbsp; <b>5 cards:</b> £1,000 JACKPOT</p><p class="muted">Your prize bank follows your progress. Lose a card and your bank drops to the previous prize level.</p></div><div class="panel"><h3>How to play</h3><p>Guess whether the next card is <b>Higher</b> or <b>Lower</b> than the last one. Correct guesses let you continue. A wrong guess resets your row and passes the turn.</p><p><b>Pairs:</b> matching numbers freeze your progress and end your turn. <b>Odd cards (3, 5, 7, 9):</b> trigger a trivia trap. The host asks a question from their own collection and records whether the answer is right or wrong. If wrong, the opponent can steal.</p><p><b>Aces:</b> pocket them and spend them later to survive a wrong guess, break a Pair freeze, or skip a trivia question. <b>Prize money:</b> your bank rises as you clear cards, but drops if you lose progress. First to five cards wins the £1,000 jackpot.</p></div>', unsafe_allow_html=True)
    st.stop()

g = st.session_state.game
players = g["players"]
current = g["current"]
active = players[current]

# ---------- Game-show scoreboard ----------
st.markdown('<div class="eyebrow" style="text-align:center;margin:.25rem 0">THE CASH DASH · LIVE SCOREBOARD</div>', unsafe_allow_html=True)
score_html = ['<div class="scoreboard">']
for i, p in enumerate(players):
    cls = "player-a" if i == 0 else "player-b"
    status = '<span class="score-active">● Playing now</span>' if i == current and g["winner"] is None else '<span class="muted">Waiting</span>'
    steps = ''.join(f'<span class="ladder-step {"done" if n <= p["progress"] else ""}"></span>' for n in range(1, 6))
    score_html.append(f'<div class="score-card {cls}"><div class="score-top"><div><div class="score-name">{p["name"]}</div>{status}</div><div style="text-align:right"><div class="score-label">Prize bank</div><div class="score-bank">£{prize_money(p["progress"]):,}</div></div></div><div class="score-meta"><span>🂡 {p["aces"]} Aces</span><span>✨ {p["free_flips"]} Free flips</span><span>{p["progress"]}/5 cards</span></div><div class="ladder">{steps}</div></div>')
score_html.append('</div>')
st.markdown(''.join(score_html), unsafe_allow_html=True)

# ---------- Card rows: host clicks to reveal ----------
st.markdown("### THE PLAYING TABLE")
st.caption("HOST CONTROL: record the call, then select the active player’s next card to reveal it.")
for i, p in enumerate(players):
    st.markdown(f"**{p['name']}'s row**")
    card_cols = st.columns(5, gap="small")
    for j, (card, card_col) in enumerate(zip(p["row"], card_cols)):
        revealed = j < p["progress"]
        if i == current and g.get("pending") and g["pending"].get("player") == i and g["pending"]["type"] in ("wrong", "trivia", "pair") and j == p["progress"]:
            revealed = True
        with card_col:
            if revealed:
                rank = card["rank"]
                label = RANK_LABELS.get(rank, str(rank))
                suit = card["suit"]
                face = f"{label}{suit}"
                extra = "card-gold" if rank == 1 else ("card-red" if suit in RED_SUITS else "")
                reveal_class = " card-reveal" if g.get("last_reveal") == {"player": i, "index": j} else ""
                is_turn_card = i == current and g["winner"] is None and p["progress"] > 0 and j == p["progress"] - 1
                turn_class = " active-turn-card" if is_turn_card else ""
                face_pattern = card_pip_pattern(rank, suit) if is_turn_card else f'<div class="card-pip">{suit}</div>'
                card_height = 164 if is_turn_card else 116
                st.markdown(f'<div class="playing-card card-front {extra}{reveal_class}{turn_class}" style="width:100%;height:{card_height}px"><div class="card-corner card-top">{label}<small>{suit}</small></div>{face_pattern}<div class="card-corner card-bottom">{label}<small>{suit}</small></div></div>', unsafe_allow_html=True)
            else:
                is_target = (i == current and j == p["progress"] and g.get("pending") is None and j < 5)
                can_flip = is_target and (g.get("host_guess") in ("Higher", "Lower") or g.get("host_use_free_flip", False))
                if st.button(" ", key=f"flip_{i}_{j}", disabled=not can_flip, use_container_width=True, type="primary" if can_flip else "secondary"):
                    use_free = bool(g.get("host_use_free_flip"))
                    chosen_guess = g.get("host_guess")
                    if use_free and p["free_flips"] > 0:
                        p["free_flips"] -= 1
                    g["host_guess"] = None
                    g["host_use_free_flip"] = False
                    resolve_reveal(current, free=use_free, guess=chosen_guess)
                    st.rerun()
                if is_target and not can_flip:
                    st.caption("Waiting for call")

st.markdown(f'<div class="event"><b>TURN UPDATE</b><br>{g["last_message"]}</div>', unsafe_allow_html=True)

# ---------- Winner ----------
if g["winner"] is not None:
    winner = players[g["winner"]]["name"]
    st.balloons()
    st.markdown(f'<div class="winner-stage"><div class="winner-kicker">Ladies and gentlemen · We have a champion!</div><div class="winner-name">🏆 {winner.upper()}! 🏆</div><div class="winner-sub">HAS CLEARED ALL FIVE CARDS</div><div class="winner-prize">£{prize_money(players[g["winner"]]["progress"]):,}</div><div class="winner-sub">THE £1,000 GRAND JACKPOT WINNER!</div></div>', unsafe_allow_html=True)
    if st.button("Play another game", type="primary", use_container_width=True):
        st.session_state.setup = True
        st.session_state.game = None
        st.rerun()
    st.stop()

pending = g["pending"]
if pending:
    kind = pending["type"]
    actor = pending["player"]
    if kind == "wrong":
        st.markdown("### The guess was wrong")
        st.warning(f"{players[actor]['name']}, spend an Ace to survive this guess, or accept a complete row reset.")
        a, b = st.columns(2)
        with a:
            if st.button(f"🂡 Spend an Ace ({players[actor]['aces']})", disabled=players[actor]["aces"] < 1, type="primary", use_container_width=True):
                players[actor]["aces"] -= 1
                players[actor]["progress"] += 1
                log(f"{players[actor]['name']} spent an Ace to survive a wrong guess.")
                g["pending"] = None
                g["last_message"] = "Ace protection used! The wrong card is survived — keep going."
                win_check(actor)
                st.rerun()
        with b:
            if st.button("Accept reset", use_container_width=True):
                reset_row(actor)
                log(f"{players[actor]['name']}'s row was reset after a wrong guess.")
                switch_turn(f"{players[actor]['name']} reset to card one. {players[1-actor]['name']} takes over.")
    elif kind == "pair":
        st.markdown("### 🃏 Pair — progress frozen")
        st.info("The matching card is safe. Spend an Ace to break the freeze and keep your turn, or pass play to your opponent.")
        a, b = st.columns(2)
        with a:
            if st.button("Spend an Ace & continue", type="primary", disabled=players[actor]["aces"] < 1, use_container_width=True):
                players[actor]["aces"] -= 1
                players[actor]["progress"] += 1
                log(f"{players[actor]['name']} spent an Ace to break a Pair freeze.")
                g["pending"] = None
                g["last_message"] = "Ace spent! The Pair freeze is broken — carry on."
                win_check(actor)
                st.rerun()
        with b:
            if st.button("Pass the turn", use_container_width=True):
                players[actor]["progress"] += 1
                log(f"{players[actor]['name']} accepted the Pair freeze and passed play.")
                win_check(actor)
                switch_turn(f"Progress preserved after the Pair. {players[1-actor]['name']} is now playing.")
    elif kind in ("trivia", "steal"):
        stealing = kind == "steal"
        actor = 1 - pending["player"] if stealing else pending["player"]
        st.markdown("### " + ("🎯 STEAL THE QUESTION!" if stealing else "⚡ TRIVIA TRAP!"))
        st.info(f"**Host:** Ask {players[actor]['name']} one of your own trivia questions. When they answer, record the result below.")
        if not stealing and players[actor]["aces"] > 0:
            if st.button(f"🂡 Spend an Ace to skip the question ({players[actor]['aces']} available)", type="secondary"):
                players[actor]["aces"] -= 1
                players[actor]["progress"] += 1
                log(f"{players[actor]['name']} spent an Ace to skip the host's trivia question.")
                g["pending"] = None
                g["last_message"] = "Ace spent. Trivia trap skipped — make your next call."
                win_check(actor)
                st.rerun()
        st.caption("The host decides whether the answer is correct. No trivia questions or answers are shown on screen.")
        a, b = st.columns(2)
        with a:
            if st.button("✓ Correct answer", type="primary", use_container_width=True):
                answer_trivia(True, stealing=stealing)
                st.rerun()
        with b:
            if st.button("✕ Wrong answer", type="secondary", use_container_width=True):
                answer_trivia(False, stealing=stealing)
                st.rerun()

else:
    st.markdown(f"### {active['name']}, make your call")
    idx = active["progress"]
    if idx < 5:
        # The current card is already visible in the player's row above.
        # Keep the call buttons directly below the playing table without a duplicate card panel.
        if active["free_flips"] > 0:
            if st.button(f"✨ Prepare Free Flip ({active['free_flips']}) — then click the card", type="secondary", use_container_width=True):
                g["host_guess"] = None
                g["host_use_free_flip"] = True
                g["last_message"] = "Free Flip ready. Host: click the active player's next face-down card."
                st.rerun()
        c1, c2 = st.columns(2)
        with c1:
            if st.button("⬆️  HIGHER", type="primary", use_container_width=True):
                g["host_guess"] = "Higher"
                g["host_use_free_flip"] = False
                g["last_message"] = "Higher selected. Host: click the active player's next face-down card to reveal it."
                st.rerun()
        with c2:
            if st.button("⬇️  LOWER", type="primary", use_container_width=True):
                g["host_guess"] = "Lower"
                g["host_use_free_flip"] = False
                g["last_message"] = "Lower selected. Host: click the active player's next face-down card to reveal it."
                st.rerun()
        if g.get("host_guess"):
            st.info(f"Call recorded: **{g['host_guess']}**. Now click the next face-down card in {active['name']}'s row.")

# ---------- Activity & controls ----------
with st.expander("📜 Game history", expanded=False):
    for item in g["log"]:
        st.write("• " + item)

st.divider()
left, right = st.columns([3,1])
with left:
    st.caption("Aces are wild protection cards. A Free Flip bypasses the Higher/Lower guess, but special cards can still trigger.")
with right:
    if st.button("New game", use_container_width=True):
        st.session_state.setup = True
        st.session_state.game = None
        st.rerun()
