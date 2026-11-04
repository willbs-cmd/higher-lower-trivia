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

def card_text(card):
    return RANK_LABELS.get(card["rank"], str(card["rank"]))

def new_row():
    return [make_card() for _ in range(5)]

def fresh_game(names):
    players = []
    for name in names:
        players.append({"name": name, "row": new_row(), "progress": 1, "aces": 0, "free_flips": 0})
    return {"players": players, "current": 0, "pending": None, "winner": None,
            "log": [f"{names[0]} starts the challenge."], "last_message": "Host: ask the player for Higher or Lower, then click their next face-down card.", "host_guess": None, "host_use_free_flip": False}

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
    st.markdown('<div class="panel"><h3 style="text-align:center">Set up the table</h3><p class="muted" style="text-align:center">Two players. Five cards each. First to turn over all five wins.</p></div>', unsafe_allow_html=True)
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
    st.markdown('<div class="panel"><h3>How to play</h3><p>Guess whether the next card is <b>Higher</b> or <b>Lower</b> than the last one. Correct guesses let you continue. A wrong guess resets your row and passes the turn.</p><p><b>Pairs:</b> matching numbers freeze your progress and end your turn. <b>Odd cards (3, 5, 7, 9):</b> trigger a trivia trap. The host asks a question from their own collection and records whether the answer is right or wrong. If wrong, the opponent can steal.</p><p><b>Aces:</b> pocket them and spend them later to survive a wrong guess, break a Pair freeze, or skip a trivia question. <b>Free Flip:</b> a successful steal earns one automatic advance on your next turn.</p></div>', unsafe_allow_html=True)
    st.stop()

g = st.session_state.game
players = g["players"]
current = g["current"]
active = players[current]

# ---------- Scoreboard ----------
cols = st.columns(2)
for i, col in enumerate(cols):
    p = players[i]
    with col:
        cls = "player-a" if i == 0 else "player-b"
        active_label = '<div class="playing">● Playing now</div>' if i == current and not g["winner"] else '<div class="muted">Waiting</div>'
        st.markdown(f'<div class="panel {cls}"><div class="player-name">{p["name"]}</div>{active_label}<div style="display:flex;justify-content:space-between;margin-top:14px"><div><div class="stat">Cards cleared</div><div class="big-stat">{p["progress"]}/5</div></div><div><div class="stat">Aces</div><div class="big-stat">🂡 {p["aces"]}</div></div><div><div class="stat">Free flips</div><div class="big-stat">✨ {p["free_flips"]}</div></div></div></div>', unsafe_allow_html=True)

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
                st.markdown(f'<div class="playing-card card-front {extra}" style="width:100%;height:116px"><div class="card-corner card-top">{label}<small>{suit}</small></div><div class="card-pip">{suit}</div><div class="card-corner card-bottom">{label}<small>{suit}</small></div></div>', unsafe_allow_html=True)
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
    st.markdown(f'<div class="panel" style="text-align:center;padding:2rem"><div class="eyebrow">Challenge complete</div><h1>🏆 {winner} wins!</h1><p class="muted">All five cards successfully revealed. A brilliant run.</p></div>', unsafe_allow_html=True)
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
