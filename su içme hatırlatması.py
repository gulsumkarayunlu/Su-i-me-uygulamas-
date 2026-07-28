<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Filiz ile Su Takibi 💧</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #FAF6F0;
    --card: #FFFFFF;
    --text: #5B4A3F;
    --text-light: #A8998C;
    --water: #5AACC7;
    --water-dark: #3A87A3;
    --leaf: #7FAE8C;
    --leaf-dark: #5E8F6E;
    --leaf-light: #A8CBAE;
    --pot: #D89268;
    --pot-dark: #B97748;
    --flower: #FF8FA3;
    --flower-center: #FFC857;
    --pink-blush: #FFB6C1;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    min-height: 100vh;
    background: var(--bg);
    font-family: 'Quicksand', sans-serif;
    color: var(--text);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px 16px;
    position: relative;
    overflow-x: hidden;
  }

  .blobs { position: fixed; inset: 0; z-index: 0; overflow: hidden; pointer-events: none; }
  .blob { position: absolute; border-radius: 50%; filter: blur(55px); opacity: 0.28; }
  .blob1 { width: 260px; height: 260px; background: var(--water); top: -80px; left: -80px; }
  .blob2 { width: 230px; height: 230px; background: var(--flower); bottom: -70px; right: -70px; }

  .card {
    position: relative;
    z-index: 1;
    background: var(--card);
    border-radius: 32px;
    box-shadow: 0 20px 50px rgba(91,74,63,0.10), 0 4px 14px rgba(91,74,63,0.06);
    padding: 30px 24px 28px;
    max-width: 400px;
    width: 100%;
    text-align: center;
  }

  header h1 {
    font-family: 'Baloo 2', sans-serif;
    font-size: 23px;
    margin: 0 0 4px;
    font-weight: 700;
  }
  header .subtitle {
    font-size: 13px;
    color: var(--text-light);
    margin: 0 0 6px;
    font-weight: 600;
  }

  .plant-stage { display: flex; justify-content: center; margin: 6px 0 2px; }
  .plant-stage svg { width: 230px; max-width: 70%; height: auto; animation: float 4.5s ease-in-out infinite; }

  @keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }

  .plant-stage.bounce svg { animation: bounce 0.5s cubic-bezier(0.34,1.56,0.64,1); }
  @keyframes bounce {
    0% { transform: scale(1) translateY(0); }
    30% { transform: scale(1.07) translateY(-5px); }
    60% { transform: scale(0.97) translateY(0); }
    100% { transform: scale(1) translateY(0); }
  }

  #stemGroup { transition: transform 0.6s cubic-bezier(0.34,1.56,0.64,1); }

  .leaf-pair {
    opacity: 0;
    transform: scale(0.3);
    transition: opacity 0.55s cubic-bezier(0.34,1.56,0.64,1), transform 0.55s cubic-bezier(0.34,1.56,0.64,1);
  }
  .leaf-pair.visible { opacity: 1; transform: scale(1); }

  .bloom-state {
    opacity: 0;
    transform: scale(0);
    transition: opacity 0.6s cubic-bezier(0.34,1.56,0.64,1), transform 0.6s cubic-bezier(0.34,1.56,0.64,1);
  }
  .bloom-state.visible { opacity: 1; transform: scale(1); }

  .face-state { opacity: 0; transition: opacity 0.4s ease; }
  .face-state.active { opacity: 1; }

  .sparkles path { animation: twinkle 1.6s ease-in-out infinite; transform-origin: center; }
  .sparkles path:nth-child(2) { animation-delay: 0.4s; }
  .sparkles path:nth-child(3) { animation-delay: 0.8s; }
  @keyframes twinkle {
    0%, 100% { opacity: 0.35; transform: scale(0.8); }
    50% { opacity: 1; transform: scale(1.15); }
  }

  .message {
    font-size: 14.5px;
    font-weight: 700;
    background: rgba(90,172,199,0.12);
    border-radius: 14px;
    padding: 10px 14px;
    margin: 6px 0 18px;
    min-height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    line-height: 1.35;
  }

  .count {
    font-family: 'Baloo 2', sans-serif;
    font-size: 20px;
    margin: 0 0 2px;
    font-weight: 600;
  }
  .count.pop { animation: pop 0.4s ease; }
  @keyframes pop {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); color: var(--water-dark); }
    100% { transform: scale(1); }
  }

  .remaining {
    font-size: 14px;
    font-weight: 700;
    color: var(--water-dark);
    margin: 0 0 14px;
  }

  .progress-track {
    width: 100%;
    height: 14px;
    background: #F0EAE3;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 14px;
  }
  .progress-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--water), var(--water-dark));
    border-radius: 10px;
    transition: width 0.6s cubic-bezier(0.34,1.56,0.64,1);
  }

  .droplets-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 6px;
    margin-bottom: 22px;
  }
  .droplet {
    width: 13px;
    height: 17px;
    background: #DCD3C8;
    opacity: 0.45;
    border-radius: 50% 50% 50% 0;
    transform: rotate(45deg);
    transition: all 0.4s ease;
  }
  .droplet.filled { background: var(--water); opacity: 1; }

  .actions { display: flex; align-items: center; justify-content: center; gap: 12px; }
  .actions button { font-family: 'Baloo 2', sans-serif; border: none; cursor: pointer; -webkit-tap-highlight-color: transparent; user-select: none; }

  #removeBtn {
    width: 46px;
    height: 46px;
    min-width: 46px;
    border-radius: 50%;
    background: #FFFFFF;
    border: 2px solid var(--water);
    color: var(--water-dark);
    font-size: 22px;
    line-height: 1;
    transition: transform 0.15s ease, opacity 0.2s ease;
  }
  #removeBtn:active { transform: scale(0.92); }
  #removeBtn:disabled { opacity: 0.35; cursor: not-allowed; }

  #addBtn {
    flex: 1;
    max-width: 220px;
    padding: 14px 20px;
    border-radius: 30px;
    background: linear-gradient(135deg, var(--water), var(--water-dark));
    color: white;
    font-weight: 700;
    font-size: 15.5px;
    box-shadow: 0 10px 22px rgba(58,135,163,0.35);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  #addBtn:hover { transform: translateY(-2px); box-shadow: 0 14px 26px rgba(58,135,163,0.4); }
  #addBtn:active { transform: translateY(0) scale(0.97); }

  .last-drink { font-size: 12.5px; color: var(--text-light); margin: 16px 0 0; font-weight: 600; }

  .settings { margin-top: 18px; text-align: left; }
  .settings summary {
    cursor: pointer;
    text-align: center;
    color: var(--text-light);
    font-weight: 700;
    font-size: 13px;
    list-style: none;
    padding: 6px;
  }
  .settings summary::-webkit-details-marker { display: none; }
  .settings-body { margin-top: 10px; display: flex; flex-direction: column; gap: 12px; }
  .settings-body label {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    font-size: 13px;
    font-weight: 700;
  }
  .settings-body input {
    width: 64px;
    padding: 6px 8px;
    border-radius: 10px;
    border: 1.5px solid #E5DDD3;
    font-family: 'Quicksand', sans-serif;
    font-size: 14px;
    text-align: center;
    color: var(--text);
  }
  .settings-actions { display: flex; gap: 8px; margin-top: 2px; }
  .settings-actions button {
    flex: 1;
    padding: 9px 6px;
    border-radius: 12px;
    border: 1.5px solid #E5DDD3;
    background: white;
    color: var(--text);
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 12px;
    cursor: pointer;
  }
  .settings-actions button:active { transform: scale(0.96); }

  .toast {
    position: fixed;
    bottom: 22px;
    left: 50%;
    transform: translate(-50%, 160%);
    background: white;
    border-radius: 20px;
    box-shadow: 0 14px 34px rgba(0,0,0,0.16);
    padding: 14px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    max-width: 340px;
    width: calc(100% - 32px);
    transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
    z-index: 1000;
  }
  .toast.show { transform: translate(-50%, 0); }
  .toast-icon { font-size: 26px; flex-shrink: 0; }
  .toast-text { flex: 1; display: flex; flex-direction: column; font-size: 12.5px; }
  .toast-text strong { font-family: 'Baloo 2', sans-serif; font-size: 14.5px; font-weight: 600; }
  .toast button {
    border: none;
    border-radius: 12px;
    font-weight: 700;
    cursor: pointer;
    font-family: 'Quicksand', sans-serif;
    -webkit-tap-highlight-color: transparent;
  }
  #toastDrinkBtn { background: var(--water); color: white; padding: 8px 12px; font-size: 12.5px; white-space: nowrap; }
  #toastCloseBtn { background: transparent; color: var(--text-light); padding: 4px 6px; font-size: 15px; }

  .confetti-piece {
    position: fixed;
    top: 32%;
    width: 8px;
    height: 8px;
    border-radius: 2px;
    animation: confettiFall 1.8s ease-out forwards;
    z-index: 999;
    pointer-events: none;
  }
  @keyframes confettiFall {
    0% { transform: translate(0,0) rotate(0deg); opacity: 1; }
    100% { transform: translate(var(--dx), 280px) rotate(var(--rot)); opacity: 0; }
  }

  button:focus-visible, input:focus-visible, summary:focus-visible {
    outline: 2.5px solid var(--water-dark);
    outline-offset: 2px;
  }

  @media (max-width: 380px) {
    .card { padding: 24px 18px 22px; border-radius: 26px; }
    header h1 { font-size: 21px; }
  }

  @media (prefers-reduced-motion: reduce) {
    * { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; }
  }
</style>
</head>
<body>

<div class="blobs">
  <div class="blob blob1"></div>
  <div class="blob blob2"></div>
</div>

<main class="card">
  <header>
    <h1>🌱 Filiz ile Su Takibi</h1>
    <p class="subtitle">Her yudumda biraz daha büyüyor</p>
  </header>

  <div class="plant-stage">
    <svg id="plantSvg" viewBox="0 0 300 320" role="img" aria-label="Filiz adında büyüyen bitki maskotu" xmlns="http://www.w3.org/2000/svg">
      <g id="pot">
        <path d="M95,235 L205,235 L192,300 L108,300 Z" fill="var(--pot)"/>
        <path d="M100,250 L200,250 L192,300 L108,300 Z" fill="var(--pot-dark)" opacity="0.25"/>
        <ellipse cx="150" cy="235" rx="55" ry="10" fill="var(--pot-dark)"/>
        <ellipse cx="150" cy="236" rx="46" ry="7" fill="#6B4A35"/>
      </g>

      <g class="face-state sleepy">
        <text x="188" y="205" font-family="Baloo 2, sans-serif" font-size="13" fill="var(--text-light)">z</text>
        <text x="198" y="192" font-family="Baloo 2, sans-serif" font-size="9" fill="var(--text-light)">z</text>
      </g>

      <g id="stemGroup" style="transform-origin: 150px 235px;">
        <rect x="144" y="105" width="12" height="130" rx="6" fill="var(--leaf-dark)"/>
      </g>

      <g class="leaf-pair" data-threshold="0.2" style="transform-origin: 150px 215px;">
        <path d="M150,215 C130,208 112,195 108,178 C128,182 148,198 150,215 Z" fill="var(--leaf)"/>
        <path d="M150,215 C170,208 188,195 192,178 C172,182 152,198 150,215 Z" fill="var(--leaf-light)"/>
      </g>
      <g class="leaf-pair" data-threshold="0.45" style="transform-origin: 150px 175px;">
        <path d="M150,175 C132,169 116,156 112,140 C130,144 148,159 150,175 Z" fill="var(--leaf-light)"/>
        <path d="M150,175 C168,169 184,156 188,140 C170,144 152,159 150,175 Z" fill="var(--leaf)"/>
      </g>
      <g class="leaf-pair" data-threshold="0.7" style="transform-origin: 150px 140px;">
        <path d="M150,140 C136,135 124,124 121,111 C135,114 149,127 150,140 Z" fill="var(--leaf)"/>
        <path d="M150,140 C164,135 176,124 179,111 C165,114 151,127 150,140 Z" fill="var(--leaf-light)"/>
      </g>

      <g id="bud" class="bloom-state" style="transform-origin: 150px 118px;">
        <path d="M141,120 L150,110 L159,120 Z" fill="var(--leaf)"/>
        <path d="M141,120 C138,111 140,99 150,94 C160,99 162,111 159,120 Z" fill="var(--flower)"/>
      </g>

      <g id="flower" class="bloom-state" style="transform-origin: 150px 95px;">
        <line x1="150" y1="105" x2="150" y2="95" stroke="var(--leaf)" stroke-width="4" stroke-linecap="round"/>
        <circle cx="150" cy="75" r="11" fill="var(--flower)"/>
        <circle cx="131" cy="88" r="11" fill="var(--flower)"/>
        <circle cx="169" cy="88" r="11" fill="var(--flower)"/>
        <circle cx="138" cy="105" r="11" fill="var(--flower)"/>
        <circle cx="162" cy="105" r="11" fill="var(--flower)"/>
        <circle cx="150" cy="93" r="10" fill="var(--flower-center)"/>
        <g class="sparkles">
          <path d="M108,55 l2.5,7 l7,2.5 l-7,2.5 l-2.5,7 l-2.5,-7 l-7,-2.5 l7,-2.5 Z" fill="var(--flower-center)"/>
          <path d="M195,68 l2,5.5 l5.5,2 l-5.5,2 l-2,5.5 l-2,-5.5 l-5.5,-2 l5.5,-2 Z" fill="var(--water)"/>
          <path d="M150,40 l2,5.5 l5.5,2 l-5.5,2 l-2,5.5 l-2,-5.5 l-5.5,-2 l5.5,-2 Z" fill="var(--flower)"/>
        </g>
      </g>

      <g id="face">
        <g class="face-state sleepy">
          <path d="M120,262 Q128,258 136,262" stroke="var(--text)" stroke-width="3" fill="none" stroke-linecap="round"/>
          <path d="M164,262 Q172,258 180,262" stroke="var(--text)" stroke-width="3" fill="none" stroke-linecap="round"/>
          <path d="M143,280 Q150,283 157,280" stroke="var(--text)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        </g>
        <g class="face-state neutral">
          <circle cx="128" cy="262" r="4.5" fill="var(--text)"/>
          <circle cx="172" cy="262" r="4.5" fill="var(--text)"/>
          <path d="M140,280 Q150,285 160,280" stroke="var(--text)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        </g>
        <g class="face-state happy">
          <circle cx="128" cy="260" r="4.5" fill="var(--text)"/>
          <circle cx="172" cy="260" r="4.5" fill="var(--text)"/>
          <path d="M136,278 Q150,290 164,278" stroke="var(--text)" stroke-width="3" fill="none" stroke-linecap="round"/>
        </g>
        <g class="face-state veryhappy">
          <path d="M120,258 Q128,250 136,258" stroke="var(--text)" stroke-width="3" fill="none" stroke-linecap="round"/>
          <path d="M164,258 Q172,250 180,258" stroke="var(--text)" stroke-width="3" fill="none" stroke-linecap="round"/>
          <path d="M132,276 Q150,296 168,276" stroke="var(--text)" stroke-width="3" fill="none" stroke-linecap="round"/>
        </g>
        <ellipse cx="118" cy="272" rx="9" ry="5.5" fill="var(--pink-blush)" opacity="0.6"/>
        <ellipse cx="182" cy="272" rx="9" ry="5.5" fill="var(--pink-blush)" opacity="0.6"/>
      </g>
    </svg>
  </div>

  <p class="message" id="message"></p>

  <div class="stats">
    <p class="count" id="countText"></p>
    <p class="remaining" id="remainingText"></p>
    <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
    <div class="droplets-row" id="dropletsRow"></div>
  </div>

  <div class="actions">
    <button id="removeBtn" type="button" aria-label="Bir bardak çıkar">−</button>
    <button id="addBtn" type="button">+ Bardak Ekle</button>
  </div>

  <p class="last-drink" id="lastDrink"></p>

  <details class="settings">
    <summary>⚙️ Ayarlar</summary>
    <div class="settings-body">
      <label>Günlük hedef (bardak)
        <input type="number" id="goalInput" min="1" max="20" value="8">
      </label>
      <label>Hatırlatma sıklığı (dk)
        <input type="number" id="reminderInput" min="5" max="240" step="5" value="60">
      </label>
      <div class="settings-actions">
        <button id="testReminderBtn" type="button">🔔 Hatırlatmayı Dene</button>
        <button id="resetBtn" type="button">Günü Sıfırla</button>
      </div>
    </div>
  </details>
</main>

<div class="toast" id="reminderToast" role="alert">
  <span class="toast-icon">💧</span>
  <div class="toast-text">
    <strong>Su içme vakti!</strong>
    <span>Bir bardak su içmeye ne dersin?</span>
  </div>
  <button id="toastDrinkBtn" type="button">İçtim ✓</button>
  <button id="toastCloseBtn" type="button" aria-label="Kapat">✕</button>
</div>

<script>
(function () {
  var state = {
    count: 0,
    goal: 8,
    reminderMinutes: 60,
    lastDrinkTime: null
  };
  var reminderTimerId = null;
  var toastHideTimeout = null;
  var bounceTimeout = null;
  var resetConfirming = false;

  var messages = {
    zero: ['Filiz toprakta uyukluyor, onu ilk bardağınla uyandır! 🌱'],
    low: ['Filiz filizlendi, güzel gidiyorsun! 🌱', 'Küçük bir başlangıç, devam et! 💧', 'Filiz seni izliyor, bir bardak daha!'],
    mid: ['Filiz yapraklanıyor, yarı yoldasın! 🌿', 'Harika gidiyorsun, az kaldı!', 'Filiz büyümeye devam ediyor, sen de devam et!'],
    goal: ['Filiz çiçek açtı! Hedefine ulaştın, tebrikler! 🎉🌸'],
    over: ['Filiz mutluluktan parlıyor, sen bir şampiyonsun! 💪💧', 'Hedefini aştın, Filiz seninle gurur duyuyor! 🌸']
  };

  function el(id) { return document.getElementById(id); }
  function pick(arr) { return arr[state.count % arr.length]; }

  function updateMessage(pct) {
    var msg;
    if (state.count === 0) msg = pick(messages.zero);
    else if (pct < 0.5) msg = pick(messages.low);
    else if (pct < 1) msg = pick(messages.mid);
    else if (state.count === state.goal) msg = pick(messages.goal);
    else msg = pick(messages.over);
    el('message').textContent = msg;
  }

  function renderDroplets() {
    var row = el('dropletsRow');
    row.innerHTML = '';
    var frag = document.createDocumentFragment();
    for (var i = 0; i < state.goal; i++) {
      var d = document.createElement('div');
      d.className = 'droplet' + (i < state.count ? ' filled' : '');
      frag.appendChild(d);
    }
    row.appendChild(frag);
  }

  function updateRemainingText() {
    var remEl = el('remainingText');
    if (state.count < state.goal) {
      remEl.textContent = (state.goal - state.count) + ' bardak kaldı 💧';
    } else if (state.count === state.goal) {
      remEl.textContent = 'Hedefine ulaştın! 🎉';
    } else {
      remEl.textContent = 'Hedefini ' + (state.count - state.goal) + ' bardak aştın! 💪';
    }
  }

  function updateUI() {
    var pct = Math.min(state.count / state.goal, 1);
    el('countText').textContent = state.count + ' / ' + state.goal + ' bardak içildi';
    updateRemainingText();
    el('progressFill').style.width = (pct * 100) + '%';
    renderDroplets();

    var stemScale = 0.08 + 0.92 * pct;
    el('stemGroup').style.transform = 'scaleY(' + stemScale + ')';

    var leafPairs = document.querySelectorAll('.leaf-pair');
    for (var i = 0; i < leafPairs.length; i++) {
      var th = parseFloat(leafPairs[i].dataset.threshold);
      leafPairs[i].classList.toggle('visible', pct >= th);
    }

    el('bud').classList.toggle('visible', pct >= 0.85 && pct < 1);
    el('flower').classList.toggle('visible', pct >= 1);

    var mood = 'sleepy';
    if (pct >= 1) mood = 'veryhappy';
    else if (pct >= 0.5) mood = 'happy';
    else if (pct > 0) mood = 'neutral';
    var faceStates = document.querySelectorAll('.face-state');
    for (var j = 0; j < faceStates.length; j++) {
      faceStates[j].classList.toggle('active', faceStates[j].classList.contains(mood));
    }

    updateMessage(pct);
    el('removeBtn').disabled = state.count <= 0;
  }

  function popCount() {
    var c = el('countText');
    c.classList.remove('pop');
    void c.offsetWidth;
    c.classList.add('pop');
  }

  function splashEffect() {
    var stage = document.querySelector('.plant-stage');
    stage.classList.remove('bounce');
    void stage.offsetWidth;
    stage.classList.add('bounce');
    clearTimeout(bounceTimeout);
    bounceTimeout = setTimeout(function () { stage.classList.remove('bounce'); }, 500);
  }

  function celebrate() {
    var colors = ['#FF8FA3', '#5AACC7', '#7FAE8C', '#FFC857'];
    for (var i = 0; i < 22; i++) {
      var p = document.createElement('div');
      p.className = 'confetti-piece';
      p.style.left = (42 + Math.random() * 16) + '%';
      p.style.setProperty('--dx', (Math.random() * 220 - 110) + 'px');
      p.style.setProperty('--rot', (Math.random() * 360) + 'deg');
      p.style.background = colors[i % colors.length];
      p.style.animationDelay = (Math.random() * 0.25) + 's';
      document.body.appendChild(p);
      (function (piece) { setTimeout(function () { piece.remove(); }, 1900); })(p);
    }
  }

  function updateLastDrinkDisplay() {
    var lEl = el('lastDrink');
    if (!state.lastDrinkTime) {
      lEl.textContent = 'Henüz bugün su içmedin, hadi başlayalım! 💧';
      return;
    }
    var diffMs = Date.now() - state.lastDrinkTime;
    var mins = Math.floor(diffMs / 60000);
    if (mins < 1) lEl.textContent = 'Az önce bir bardak içtin, aferin! 👍';
    else if (mins < 60) lEl.textContent = 'Son bardaktan bu yana ' + mins + ' dakika geçti';
    else {
      var h = Math.floor(mins / 60), m = mins % 60;
      lEl.textContent = 'Son bardaktan bu yana ' + h + ' saat ' + m + ' dakika geçti';
    }
  }

  function addGlass() {
    if (state.count >= 30) return;
    var willReachGoalNow = state.count < state.goal;
    state.count++;
    state.lastDrinkTime = Date.now();
    updateUI();
    updateLastDrinkDisplay();
    popCount();
    splashEffect();
    if (willReachGoalNow && state.count >= state.goal) celebrate();
  }

  function removeGlass() {
    if (state.count <= 0) return;
    state.count--;
    updateUI();
  }

  function showReminderToast() {
    var toast = el('reminderToast');
    toast.classList.add('show');
    clearTimeout(toastHideTimeout);
    toastHideTimeout = setTimeout(hideReminderToast, 10000);
  }
  function hideReminderToast() {
    el('reminderToast').classList.remove('show');
  }

  function scheduleReminder() {
    clearTimeout(reminderTimerId);
    var ms = state.reminderMinutes * 60 * 1000;
    reminderTimerId = setTimeout(function () {
      showReminderToast();
      scheduleReminder();
    }, ms);
  }

  function init() {
    updateUI();
    updateLastDrinkDisplay();
    scheduleReminder();
    setInterval(updateLastDrinkDisplay, 30000);

    el('addBtn').addEventListener('click', addGlass);
    el('removeBtn').addEventListener('click', removeGlass);

    el('goalInput').addEventListener('change', function (e) {
      var v = parseInt(e.target.value, 10);
      if (isNaN(v) || v < 1) v = 1;
      if (v > 20) v = 20;
      state.goal = v;
      e.target.value = v;
      updateUI();
    });

    el('reminderInput').addEventListener('change', function (e) {
      var v = parseInt(e.target.value, 10);
      if (isNaN(v) || v < 5) v = 5;
      if (v > 240) v = 240;
      state.reminderMinutes = v;
      e.target.value = v;
      scheduleReminder();
    });

    el('testReminderBtn').addEventListener('click', showReminderToast);

    el('resetBtn').addEventListener('click', function () {
      var btn = el('resetBtn');
      if (!resetConfirming) {
        resetConfirming = true;
        btn.textContent = 'Emin misin? Tekrar tıkla ✓';
        setTimeout(function () {
          resetConfirming = false;
          btn.textContent = 'Günü Sıfırla';
        }, 3000);
      } else {
        state.count = 0;
        state.lastDrinkTime = null;
        resetConfirming = false;
        btn.textContent = 'Günü Sıfırla';
        updateUI();
        updateLastDrinkDisplay();
      }
    });

    el('toastCloseBtn').addEventListener('click', hideReminderToast);
    el('toastDrinkBtn').addEventListener('click', function () {
      addGlass();
      hideReminderToast();
    });
  }

  document.addEventListener('DOMContentLoaded', init);
})();
</script>

</body>
</html>