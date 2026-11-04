import random
import streamlit as st

st.set_page_config(page_title="Higher or Lower | Trivia Challenge", page_icon="🂡", layout="wide")

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
.stApp {background: radial-gradient(ellipse at 50% -20%, #203451 0%, #101a2b 45%, #09111e 100%); color:#f4f6fb;}
.block-container {max-width:1180px; padding-top:2rem; padding-bottom:3rem;}
h1,h2,h3 {font-family:'Playfair Display',serif !important; color:#fff;}
p,div,span,label {font-family:'DM Sans',sans-serif;}
.hero {text-align:center; padding:1.2rem 0 1.5rem;}
.eyebrow {color:#d7b76b; letter-spacing:.25em; font-size:.72rem; font-weight:800; text-transform:uppercase;}
.hero h1 {font-size:clamp(2.4rem,6vw,4.5rem); line-height:1.05; margin:.25rem 0;}
.subtitle {color:#aebbd0; font-size:1rem;}
.panel {background:linear-gradient(145deg,rgba(30,47,70,.95),rgba(17,29,47,.96)); border:1px solid rgba(181,199,225,.16); border-radius:18px; padding:1.1rem 1.2rem; box-shadow:0 14px 36px rgba(0,0,0,.18); margin-bottom:1rem;}
.player-a {border-top:3px solid #58a6ff;}
.player-b {border-top:3px solid #ff777e;}
.player-name {font-size:1.05rem; font-weight:800; color:#fff;}
.stat {color:#aebbd0; font-size:.78rem; text-transform:uppercase; letter-spacing:.1em;}
.big-stat {font-size:1.65rem; font-weight:800; color:#f2d58b;}
.playing {color:#f2d58b; font-weight:800; font-size:.78rem; letter-spacing:.12em; text-transform:uppercase;}
.cards {display:flex; flex-wrap:wrap; gap:9px; justify-content:center; padding:.8rem 0;}
.playing-card {width:clamp(48px,8vw,82px); height:112px; border-radius:11px; display:flex; flex-direction:column; justify-content:space-between; padding:9px; box-sizing:border-box; box-shadow:0 7px 14px rgba(0,0,0,.25); font-weight:800;}
.card-back {background:repeating-linear-gradient(45deg,#17395c,#17395c 7px,#214d78 7px,#214d78 14px); border:2px solid #b6c7d8; color:#e7eef7; align-items:center; justify-content:center; font-size:1.7rem;}
.card-front {background:linear-gradient(145deg,#fff,#e8edf3); color:#182335; border:2px solid #fff;}
.card-red {color:#c83d52;}
.card-gold {background:linear-gradient(145deg,#fff4ce,#e4c16a); border:2px solid #f7df9c;}
.card-value {font-size:1.55rem; line-height:1;}
.card-suit {font-size:1.1rem; align-self:flex-end;}
.card-index {font-size:.62rem; color:#9ca9b8;}
.event {background:rgba(217,178,91,.1); border:1px solid rgba(217,178,91,.32); border-radius:13px; padding:1rem; color:#f4e4bb;}
.muted {color:#aebbd0;}
div.stButton > button {border-radius:11px; font-weight:800; min-height:2.8rem; border:1px solid rgba(255,255,255,.16);}
div.stButton > button[kind="primary"] {background:linear-gradient(135deg,#d8b66b,#a9823d); color:#172235; border:0;}
div[data-testid="stRadio"] label {color:#e8edf5 !important;}
div[data-testid="stAlert"] {border-radius:12px;}
hr {border-color:rgba(255,255,255,.12);}
</style>
""", unsafe_allow_html=True)

SUITS = ["♠", "♥", "♦", "♣"]
RED_SUITS = {"♥", "♦"}
RANKS = list(range(1, 14))
RANK_LABELS = {1:"A", 11:"J", 12:"Q", 13:"K"}
TRIVIA = [
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Mercury"], "Mars"),
    ("What is the capital city of Canada?", ["Toronto", "Vancouver", "Ottawa", "Montreal"], "Ottawa"),
    ("How many sides does a hexagon have?", ["Five", "Six", "Seven", "Eight"], "Six"),
    ("Which ocean is the largest?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
    ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Mary Shelley", "Emily Brontë", "Charles Dickens"], "Jane Austen"),
    ("What is the chemical symbol for gold?", ["Ag", "Go", "Au", "Gd"], "Au"),
    ("In which country would you find the city of Kyoto?", ["China", "Japan", "Thailand", "South Korea"], "Japan"),
    ("How many players are on the pitch for one football team at kick-off?", ["9", "10", "11", "12"], "11"),
    ("Which animal is the largest mammal?", ["African elephant", "Blue whale", "Giraffe", "Orca"], "Blue whale"),
    ("What is the hardest natural substance?", ["Quartz", "Diamond", "Granite", "Iron"], "Diamond"),
    ("Which language has the most native speakers worldwide?", ["English", "Spanish", "Mandarin Chinese", "Hindi"], "Mandarin Chinese"),
    ("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
    ("Which artist painted the Mona Lisa?", ["Michelangelo", "Raphael", "Leonardo da Vinci", "Van Gogh"], "Leonardo da Vinci"),
    ("How many rings are on the Olympic flag?", ["Four", "Five", "Six", "Seven"], "Five"),
    ("What is the currency of Switzerland?", ["Euro", "Swiss franc", "Krone", "Zloty"], "Swiss franc"),
    ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "Carbon dioxide"),
    ("What is the tallest mountain above sea level?", ["K2", "Kilimanjaro", "Everest", "Denali"], "Everest"),
    ("Which year did the first human land on the Moon?", ["1965", "1969", "1972", "1975"], "1969"),
    ("What is the largest desert on Earth?", ["Sahara", "Gobi", "Arabian", "Antarctic"], "Antarctic"),
    ("Which instrument has 88 keys on a standard version?", ["Violin", "Piano", "Harp", "Accordion"], "Piano"),
]

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
        q = random.choice(TRIVIA)
        g["pending"] = {"type":"trivia", "player":player_index, "question":q, "card":card, "free":free}
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

def answer_trivia(answer, stealing=False):
    g = st.session_state.game
    pending = g["pending"]
    q = pending["question"]
    actor = 1 - pending["player"] if stealing else pending["player"]
    p = g["players"][actor]
    if answer == q[2]:
        if stealing:
            p["free_flips"] += 1
            log(f"{p['name']} stole the trivia question and earned a Free Flip.")
            switch_turn(f"Steal successful! {p['name']} earns a Free Flip and takes the turn.")
        else:
            p["progress"] += 1
            log(f"{p['name']} answered the trivia trap correctly.")
            g["pending"] = None
            g["last_message"] = "Correct answer! The trap is beaten — make your next call."
            win_check(actor)
    else:
        if stealing:
            lose_one(actor)
            log(f"{p['name']} failed the steal and lost one card.")
            switch_turn(f"Failed steal. {p['name']} loses one card, but now takes the turn.")
        else:
            trap_index = p["progress"]
            lose_one(actor)
            # The trap card itself is also replaced face-down.
            p["row"][trap_index] = make_card()
            g["pending"] = {"type":"steal", "player":actor, "question":q}
            log(f"{p['name']} missed the trivia trap and moved back one card.")
            g["last_message"] = f"Wrong answer. {g['players'][1-actor]['name']} can now steal the same question."

# ---------- Setup ----------
if "game" not in st.session_state:
    st.session_state.setup = True
    st.session_state.game = None

st.markdown('<div class="hero"><div class="eyebrow">Two-player card & general knowledge game</div><h1>Higher or Lower</h1><div class="subtitle">The Trivia Challenge · Read the cards. Trust your instincts. Beat the traps.</div></div>', unsafe_allow_html=True)

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
    st.markdown('<div class="panel"><h3>How to play</h3><p>Guess whether the next card is <b>Higher</b> or <b>Lower</b> than the last one. Correct guesses let you continue. A wrong guess resets your row and passes the turn.</p><p><b>Pairs:</b> matching numbers freeze your progress and end your turn. <b>Odd cards (3, 5, 7, 9):</b> trigger a trivia trap. Get it right to continue; get it wrong and lose one card — then your opponent can steal the question.</p><p><b>Aces:</b> pocket them and spend them later to survive a wrong guess, break a Pair freeze, or skip a trivia question. <b>Free Flip:</b> a successful steal earns one automatic advance on your next turn.</p></div>', unsafe_allow_html=True)
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
st.markdown("### The table")
st.caption("The host controls the laptop. Ask the active player for their call, then click the next face-down card to reveal it.")
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
                st.markdown(f'<div class="playing-card card-front {extra}" style="width:100%;height:112px"><span class="card-value">{face}</span><span class="card-index">CARD {j+1}</span></div>', unsafe_allow_html=True)
            else:
                is_target = (i == current and j == p["progress"] and g.get("pending") is None and j < 5)
                can_flip = is_target and (g.get("host_guess") in ("Higher", "Lower") or g.get("host_use_free_flip", False))
                if st.button(f"🂠 CARD {j+1}", key=f"flip_{i}_{j}", disabled=not can_flip, use_container_width=True, type="primary" if can_flip else "secondary"):
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
        q = pending["question"]
        st.markdown("### " + ("🎯 Steal the question" if stealing else "⚡ Trivia trap"))
        st.info(f"**{players[actor]['name']}** — {q[0]}")
        if not stealing and players[actor]["aces"] > 0:
            if st.button(f"🂡 Spend an Ace to skip this question ({players[actor]['aces']} available)", type="secondary"):
                players[actor]["aces"] -= 1
                players[actor]["progress"] += 1
                log(f"{players[actor]['name']} spent an Ace to skip a trivia trap.")
                g["pending"] = None
                g["last_message"] = "Ace spent. Trivia trap skipped — make your next call."
                win_check(actor)
                st.rerun()
        choice = st.radio("Choose your answer", q[1], key=f"answer_{kind}_{len(g['log'])}")
        if st.button("Lock in answer", type="primary", use_container_width=True):
            answer_trivia(choice, stealing=stealing)
            st.rerun()
else:
    st.markdown(f"### {active['name']}, make your call")
    idx = active["progress"]
    if idx < 5:
        previous = active["row"][idx-1]
        prev_label = RANK_LABELS.get(previous["rank"], str(previous["rank"]))
        st.markdown(f'<div class="panel" style="text-align:center"><div class="stat">Your current card</div><div style="font-size:3rem;font-weight:800;color:#f2d58b">{prev_label} {previous["suit"]}</div><div class="muted">Will the next card be higher or lower?</div></div>', unsafe_allow_html=True)
        if active["free_flips"] > 0:
            if st.button(f"✨ Prepare Free Flip ({active['free_flips']}) — then click the card", type="secondary", use_container_width=True):
                g["host_guess"] = None
                g["host_use_free_flip"] = True
                g["last_message"] = "Free Flip ready. Host: click the active player's next face-down card."
                st.rerun()
        c1, c2 = st.columns(2)
        with c1:
            if st.button("⬆️  PLAYER CALLS HIGHER", type="primary" if g.get("host_guess") == "Higher" else "secondary", use_container_width=True):
                g["host_guess"] = "Higher"
                g["host_use_free_flip"] = False
                g["last_message"] = "Higher selected. Host: click the active player's next face-down card to reveal it."
                st.rerun()
        with c2:
            if st.button("⬇️  PLAYER CALLS LOWER", type="primary" if g.get("host_guess") == "Lower" else "secondary", use_container_width=True):
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
