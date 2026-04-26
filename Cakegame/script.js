let score = 0;
const flavours = {
    "Chocolate": "#8B4513",
    "Vanilla": "#F5DEB3", 
    "Strawberry": "#FF69B4",
    "Red Velvet": "#C71585"
};
const shapes = ["Round", "Heart", "Square", "Star"];
const sprinkles = ["Rainbow", "Chocolate", "Silver", "None"];
const creams = ["Whipped", "Buttercream", "Fondant", "Cream Cheese"];

function updateScore() {
    document.getElementById('score').textContent = score;
}

function createSprinkles(count) {
    let html = '';
    for(let i = 0; i < count; i++) {
        html += `<div class="sprinkle" style="
            left: ${Math.random()*80}%;
            animation-delay: ${Math.random()*2}s;
            background: ${Math.random()>0.5 ? '#FFD700' : '#FF69B4'};
        "></div>`;
    }
    return html;
}

function showRealCake(flavour, shape, sprinkle, cream) {
    const cakeColor = flavours[flavour];
    const visual = document.getElementById('cake-visual');
    
    visual.innerHTML = `
        <div class="real-cake">
            <!-- Layer 1 - Base -->
            <div class="cake-base" style="background: linear-gradient(145deg, ${cakeColor}, ${shadeColor(cakeColor, 20)});"></div>
            
            <!-- Layer 2 -->
            <div class="cake-layer1" style="background: linear-gradient(145deg, ${cakeColor}, ${shadeColor(cakeColor, 10)});"></div>
            
            <!-- Layer 3 -->
            <div class="cake-layer2" style="background: ${cakeColor};"></div>
            
            <!-- Whipped Cream -->
            <div class="cream-top"></div>
            
            <!-- Sprinkles -->
            <div class="sprinkles">
                ${sprinkle !== "None" ? createSprinkles(15) : ''}
            </div>
            
            <!-- Cherry -->
            <div class="cherry"></div>
        </div>
        <h3>🍰 ${flavour} ${shape} Cake<br>
            ${cream} Cream + ${sprinkle} Sprinkles</h3>
    `;
}

function shadeColor(color, percent) {
    const num = parseInt(color.replace("#", ""), 16);
    const amt = Math.round(2.55 * percent);
    const R = (num >> 16) + amt;
    const G = (num >> 8 & 0x00FF) + amt;
    const B = (num & 0x0000FF) + amt;
    return "#" + (0x1000000 + (R<255?R<1?0:R:255)*0x10000 +
        (G<255?G<1?0:G:255)*0x100 +
        (B<255?B<1?0:B:255)).toString(16).slice(1);
}

function bakeCake() {
    const flavour = Object.keys(flavours)[Math.floor(Math.random()*4)];
    const shape = shapes[Math.floor(Math.random()*4)];
    const sprinkle = sprinkles[Math.floor(Math.random()*4)];
    const cream = creams[Math.floor(Math.random()*4)];
    
    document.getElementById('game-area').innerHTML = `
        <h2>✅ Perfect Cake Baked!</h2>
        <button onclick="bakeCake()">🔥 Bake Another</button>
    `;
    showRealCake(flavour, shape, sprinkle, cream);
    score += 25;
    updateScore();
}

function guessCake() {
    const judgeCake = {
        flavour: Object.keys(flavours)[Math.floor(Math.random()*4)],
        shape: shapes[Math.floor(Math.random()*4)],
        sprinkle: sprinkles[Math.floor(Math.random()*4)],
        cream: creams[Math.floor(Math.random()*4)]
    };
    
    document.getElementById('game-area').innerHTML = `
        <h2>🎯 Guess Judge's Cake!</h2>
        <div>Hints: F=${judgeCake.flavour[0]} | Shape=${judgeCake.shape.length}L | Sprinkles=${judgeCake.sprinkle=='None'?'No':'Yes'}</div>
        <input type="text" id="guess" class="guess-input" placeholder="Chocolate-Round-Rainbow-Whipped">
        <br><button onclick="checkGuess('${judgeCake.flavour}','${judgeCake.shape}','${judgeCake.sprinkle}','${judgeCake.cream}')">🎲 Guess!</button>
    `;
}

function checkGuess(jFlavour, jShape, jSprinkle, jCream) {
    const guess = document.getElementById('guess').value.split('-');
    let points = 0;
    
    if (guess[0] === jFlavour) points += 50;
    if (guess[1] === jShape) points += 50;
    if (guess[2] === jSprinkle) points += 50;
    if (guess[3] === jCream) points += 50;
    
    score += points;
    updateScore();
    showRealCake(jFlavour, jShape, jSprinkle, jCream);
    
    document.getElementById('game-area').innerHTML = `
        <h2 style="color:${points==200?'#28a745':'#ffc107'}">🎉 ${points}/200 Points!</h2>
        <button onclick="guessCake()">🔄 New Cake</button>
    `;
}