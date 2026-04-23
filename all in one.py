from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

# ---------------- APP ----------------
app = FastAPI(title="Study M - Учебно-исследовательская работа")

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Цветовая схема
COLORS = {
    'primary': '#FFFFFF', 'secondary': '#1B1F26', 'accent1': '#81818B',
    'accent2': '#968AE1', 'accent3': '#FFF854', 'accent4': '#002FE7',
    'accent5': '#FF7641', 'card_bg': '#F5F5F7'
}


# ================ ГЛАВНАЯ СТРАНИЦА ================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Study M - Учебно-исследовательская работа</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: {COLORS['primary']}; color: {COLORS['secondary']}; }}
            .navbar {{ position: fixed; top: 0; left: 0; right: 0; background: {COLORS['primary']}; padding: 15px 40px; display: flex; justify-content: space-between; align-items: center; z-index: 100; border-bottom: 3px solid {COLORS['accent2']}; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }}
            .logo {{ font-size: 28px; font-weight: bold; background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .nav-menu {{ display: flex; gap: 30px; }}
            .nav-menu a {{ text-decoration: none; color: {COLORS['secondary']}; padding: 8px 20px; border-radius: 25px; transition: all 0.3s; font-weight: 500; }}
            .nav-menu a:hover {{ background: {COLORS['accent2']}; color: white; transform: translateY(-2px); }}
            .main-container {{ display: flex; min-height: 100vh; }}
            .animation-sidebar {{ width: 420px; background: {COLORS['card_bg']}; padding: 100px 25px 25px; position: fixed; left: 0; top: 0; bottom: 0; overflow-y: auto; border-right: 1px solid {COLORS['accent1']}; box-shadow: 2px 0 10px rgba(0,0,0,0.05); }}
            .animation-card {{ background: white; border-radius: 20px; padding: 20px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); transition: transform 0.3s; border: 1px solid {COLORS['accent1']}30; }}
            .animation-card:hover {{ transform: translateX(5px); border-color: {COLORS['accent2']}; }}
            .animation-card h3 {{ color: {COLORS['accent4']}; margin-bottom: 12px; font-size: 16px; display: flex; align-items: center; gap: 8px; }}
            .animation-card canvas {{ width: 100%; height: 200px; border-radius: 12px; background: {COLORS['card_bg']}; border: 1px solid {COLORS['accent1']}30; }}
            .content {{ margin-left: 420px; padding: 100px 50px 50px; width: calc(100% - 420px); }}
            .welcome-section {{ text-align: center; margin-bottom: 50px; }}
            .welcome-section h1 {{ font-size: 48px; margin-bottom: 20px; background: linear-gradient(135deg, {COLORS['accent4']}, {COLORS['accent2']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .welcome-text {{ max-width: 800px; margin: 0 auto; line-height: 1.8; font-size: 18px; background: {COLORS['card_bg']}; padding: 30px; border-radius: 20px; border-left: 4px solid {COLORS['accent5']}; }}
            .features-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 50px; }}
            .feature-card {{ background: white; border-radius: 20px; padding: 30px; text-align: center; transition: all 0.3s; border: 1px solid {COLORS['accent1']}30; cursor: pointer; }}
            .feature-card:hover {{ transform: translateY(-10px); border-color: {COLORS['accent2']}; box-shadow: 0 10px 30px rgba(150, 138, 225, 0.2); }}
            .feature-icon {{ font-size: 48px; margin-bottom: 20px; }}
            .feature-card h3 {{ color: {COLORS['accent4']}; margin-bottom: 15px; font-size: 24px; }}
            .feature-card p {{ color: {COLORS['secondary']}; line-height: 1.6; margin-bottom: 20px; }}
            .feature-btn {{ display: inline-block; padding: 10px 30px; background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); color: white; text-decoration: none; border-radius: 25px; font-weight: bold; transition: all 0.3s; }}
            .feature-btn:hover {{ transform: scale(1.05); box-shadow: 0 4px 15px rgba(0, 47, 231, 0.3); }}
            @media (max-width: 768px) {{ .animation-sidebar {{ display: none; }} .content {{ margin-left: 0; width: 100%; }} }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div class="logo">Study M</div>
            <div class="nav-menu">
                <a href="/">Главная</a>
                <a href="/theory">Теория</a>
                <a href="/physics">Обучение</a>
                <a href="/optimization">Попробуй сам</a>
            </div>
        </div>

        <div class="main-container">
            <div class="animation-sidebar">
                <div class="animation-card">
                    <h3>🎯 Движение тела под углом</h3>
                    <canvas id="projectileAnimCanvas" width="370" height="200"></canvas>
                </div>
                <div class="animation-card">
                    <h3>🔧 Реалистичная пружина</h3>
                    <canvas id="springAnimCanvas" width="370" height="200"></canvas>
                </div>
                <div class="animation-card">
                    <h3>💥 Выстрел ядра из пушки</h3>
                    <canvas id="cannonAnimCanvas" width="370" height="200"></canvas>
                </div>
            </div>

            <div class="content">
                <div class="welcome-section">
                    <h1>Добро пожаловать!</h1>
                    <div class="welcome-text">
                        <p>В систему обучения дисциплине <strong>«Учебно-исследовательская работа»</strong> 
                        для бакалавров направления <strong>15.03.03 «Прикладная механика»</strong>.</p>
                        <p style="margin-top: 20px;">Система поможет вам научиться получать <strong>численное решение физических задач</strong>, 
                        поставленных в дифференциальной форме, с использованием языка программирования <strong>Python</strong>.</p>
                    </div>
                </div>

                <div class="features-grid">
                    <div class="feature-card" onclick="location.href='/theory'"><div class="feature-icon">📚</div><h3>Теория</h3><p>Изучите численные методы решения дифференциальных уравнений и оптимизации</p><span class="feature-btn">Изучить →</span></div>
                    <div class="feature-card" onclick="location.href='/physics'"><div class="feature-icon">⚡</div><h3>Обучение</h3><p>Практические примеры из физики и механики с интерактивными расчетами</p><span class="feature-btn">Практиковать →</span></div>
                    <div class="feature-card" onclick="location.href='/optimization'"><div class="feature-icon">🎯</div><h3>Попробуй сам</h3><p>Решите задачи поиска оптимальных параметров в реальном времени</p><span class="feature-btn">Решать →</span></div>
                </div>
            </div>
        </div>

        <script>
            const colors = {{
                accent2: '#968AE1', accent3: '#FFF854', accent4: '#002FE7', accent5: '#FF7641', accent1: '#81818B', card_bg: '#F5F5F7'
            }};

            // ========== 1. АНИМАЦИЯ ДВИЖЕНИЯ ТЕЛА ПОД УГЛОМ ==========
            const projectileCanvas = document.getElementById('projectileAnimCanvas');
            let projectileTime = 0;

            function calcTrajectory(v0, angle, h0) {{
                const g = 9.81;
                const rad = angle * Math.PI / 180;
                const vx = v0 * Math.cos(rad);
                const vy = v0 * Math.sin(rad);
                const tFlight = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g;
                return {{ vx: vx, vy: vy, tFlight: tFlight }};
            }}

            function drawProjectile() {{
                if (!projectileCanvas) return;
                const ctx = projectileCanvas.getContext('2d');
                const w = projectileCanvas.width;
                const h = projectileCanvas.height;
                const traj = calcTrajectory(28, 50, 0);
                const vx = traj.vx;
                const vy = traj.vy;
                const tFlight = traj.tFlight;
                const g = 9.81;

                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);

                let t = projectileTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t;
                const y = 0 + vy * t - 0.5 * g * t * t;
                const maxX = vx * tFlight;
                const maxY = (vy*vy/(2*g) + 0);

                if (maxX > 0 && maxY > 0) {{
                    const x_px = (x / maxX) * (w - 50) + 25;
                    const y_px = h - 30 - (y / maxY) * (h - 55);
                    ctx.beginPath();
                    ctx.arc(x_px, y_px, 7, 0, Math.PI * 2);
                    ctx.fillStyle = colors.accent5;
                    ctx.fill();
                    ctx.beginPath();
                    ctx.arc(x_px, y_px, 3, 0, Math.PI * 2);
                    ctx.fillStyle = 'white';
                    ctx.fill();
                }}

                projectileTime += 0.035;
                if (projectileTime > tFlight) projectileTime = 0;
                requestAnimationFrame(drawProjectile);
            }}

            // ========== 2. РЕАЛИСТИЧНАЯ АНИМАЦИЯ ПРУЖИНЫ ==========
            const springCanvas = document.getElementById('springAnimCanvas');
            let springTime = 0;

            // Параметры физической системы
            const springMass = 0.8;
            const springStiffness = 45;
            const springDamping = 2.5;

            function getSpringDisplacement(t) {{
                const omega0 = Math.sqrt(springStiffness / springMass);
                const zeta = springDamping / (2 * Math.sqrt(springMass * springStiffness));
                const x0 = 30;
                let x;
                if (zeta < 1) {{
                    const omega_d = omega0 * Math.sqrt(1 - zeta*zeta);
                    x = x0 * Math.exp(-zeta * omega0 * t) * Math.cos(omega_d * t);
                }} else {{
                    x = x0 * Math.exp(-zeta * omega0 * t) * (1 + zeta * omega0 * t);
                }}
                return Math.min(Math.max(x, -25), 35);
            }}

            function drawSpring() {{
                if (!springCanvas) return;
                const ctx = springCanvas.getContext('2d');
                const w = springCanvas.width;
                const h = springCanvas.height;

                ctx.clearRect(0, 0, w, h);

                ctx.fillStyle = colors.accent1;
                ctx.fillRect(0, 0, w, 12);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, 12, w, 3);

                const centerX = w / 2;
                const displacement = getSpringDisplacement(springTime);
                const equilibriumY = 140;
                const currentY = equilibriumY + displacement;
                const topY = 15;
                const bottomY = currentY - 12;
                const coils = 18;

                ctx.beginPath();
                for (let i = 0; i <= coils; i++) {{
                    const t = i / coils;
                    const y = topY + (bottomY - topY) * t;
                    const amplitude = 12 * (1 + Math.abs(displacement) / 80);
                    const xOffset = Math.sin(t * Math.PI * 6) * amplitude;
                    if (i === 0) ctx.moveTo(centerX + xOffset, y);
                    else ctx.lineTo(centerX + xOffset, y);
                }}
                ctx.strokeStyle = colors.accent4;
                ctx.lineWidth = 2.5;
                ctx.stroke();

                ctx.fillStyle = colors.accent5;
                ctx.fillRect(centerX - 20, currentY - 12, 40, 24);
                ctx.fillStyle = colors.accent3;
                ctx.fillRect(centerX - 12, currentY - 8, 24, 16);
                ctx.fillStyle = 'white';
                ctx.fillRect(centerX - 6, currentY - 4, 12, 8);

                const forceMagnitude = Math.abs(displacement) / 35;
                const arrowLength = 20 + forceMagnitude * 30;
                const arrowColor = displacement > 0 ? colors.accent5 : colors.accent2;

                ctx.beginPath();
                const arrowStartX = centerX + 35;
                const arrowStartY = currentY;
                const arrowEndY = displacement > 0 ? currentY + arrowLength : currentY - arrowLength;
                ctx.moveTo(arrowStartX, arrowStartY);
                ctx.lineTo(arrowStartX, arrowEndY);
                ctx.strokeStyle = arrowColor;
                ctx.lineWidth = 2 + forceMagnitude * 2;
                ctx.stroke();

                ctx.beginPath();
                if (displacement > 0) {{
                    ctx.moveTo(arrowStartX - 4, arrowEndY + 6);
                    ctx.lineTo(arrowStartX, arrowEndY);
                    ctx.lineTo(arrowStartX + 4, arrowEndY + 6);
                }} else {{
                    ctx.moveTo(arrowStartX - 4, arrowEndY - 6);
                    ctx.lineTo(arrowStartX, arrowEndY);
                    ctx.lineTo(arrowStartX + 4, arrowEndY - 6);
                }}
                ctx.fillStyle = arrowColor;
                ctx.fill();

                ctx.font = 'bold 10px "Segoe UI"';
                ctx.fillStyle = colors.accent2;
                ctx.fillText('F = -k·Δx', arrowStartX + 8, (arrowStartY + arrowEndY)/2);

                ctx.font = '10px "Segoe UI"';
                ctx.fillStyle = colors.accent1;
                ctx.fillText('m = 0.8 кг', 8, 30);
                ctx.fillText('k = 45 Н/м', 8, 45);
                ctx.fillText('ζ = 0.33', 8, 60);

                springTime += 0.04;
                if (springTime > 5) springTime = 0;
                requestAnimationFrame(drawSpring);
            }}

            // ========== 3. АНИМАЦИЯ ВЫСТРЕЛА ЯДРА ==========
            const cannonCanvas = document.getElementById('cannonAnimCanvas');
            let cannonTime = 0;

            function calcCannonTrajectory(v0, angle, h0) {{
                const g = 9.81;
                const rad = angle * Math.PI / 180;
                const vx = v0 * Math.cos(rad);
                const vy = v0 * Math.sin(rad);
                const tFlight = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g;
                return {{ vx: vx, vy: vy, tFlight: tFlight }};
            }}

            function drawCannon() {{
                if (!cannonCanvas) return;
                const ctx = cannonCanvas.getContext('2d');
                const w = cannonCanvas.width;
                const h = cannonCanvas.height;
                const traj = calcCannonTrajectory(35, 42, 25);
                const vx = traj.vx;
                const vy = traj.vy;
                const tFlight = traj.tFlight;
                const g = 9.81;

                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);

                const cannonX = 35;
                const cannonY = h - 35;
                const angleRad = 42 * Math.PI / 180;

                ctx.save();
                ctx.translate(cannonX, cannonY);
                ctx.rotate(-angleRad);
                ctx.fillStyle = colors.accent4;
                ctx.fillRect(0, -6, 35, 12);
                ctx.restore();

                ctx.beginPath();
                ctx.arc(cannonX - 5, cannonY + 5, 7, 0, Math.PI * 2);
                ctx.fillStyle = colors.accent1;
                ctx.fill();
                ctx.beginPath();
                ctx.arc(cannonX + 20, cannonY + 5, 7, 0, Math.PI * 2);
                ctx.fillStyle = colors.accent1;
                ctx.fill();

                let t = cannonTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t;
                const y = 25 + vy * t - 0.5 * g * t * t;
                const maxX = vx * tFlight;
                const maxY = (vy*vy/(2*g) + 25);

                if (maxX > 0 && t < tFlight) {{
                    const x_px = cannonX + 40 + (x / maxX) * (w - cannonX - 60);
                    const y_px = h - 35 - (y / maxY) * (h - 60);
                    ctx.beginPath();
                    ctx.arc(x_px, y_px, 6, 0, Math.PI * 2);
                    ctx.fillStyle = colors.accent5;
                    ctx.fill();
                }}

                cannonTime += 0.04;
                if (cannonTime > tFlight) cannonTime = 0;
                requestAnimationFrame(drawCannon);
            }}

            // ЗАПУСК ВСЕХ АНИМАЦИЙ
            drawProjectile();
            drawSpring();
            drawCannon();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# ================ СТРАНИЦА ТЕОРИИ ================
@app.get("/theory", response_class=HTMLResponse)
async def theory_page(request: Request):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Теория - Study M</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: {COLORS['primary']}; color: {COLORS['secondary']}; }}
            .navbar {{ position: fixed; top: 0; left: 0; right: 0; background: {COLORS['primary']}; padding: 15px 40px; display: flex; justify-content: space-between; align-items: center; z-index: 100; border-bottom: 3px solid {COLORS['accent2']}; }}
            .logo {{ font-size: 28px; font-weight: bold; background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .nav-menu {{ display: flex; gap: 30px; }}
            .nav-menu a {{ text-decoration: none; color: {COLORS['secondary']}; padding: 8px 20px; border-radius: 25px; transition: all 0.3s; }}
            .nav-menu a:hover {{ background: {COLORS['accent2']}; color: white; }}
            .animation-sidebar {{ width: 420px; background: {COLORS['card_bg']}; padding: 100px 25px 25px; position: fixed; left: 0; top: 0; bottom: 0; overflow-y: auto; border-right: 1px solid {COLORS['accent1']}; }}
            .animation-card {{ background: white; border-radius: 20px; padding: 20px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid {COLORS['accent1']}30; }}
            .animation-card h3 {{ color: {COLORS['accent4']}; margin-bottom: 12px; font-size: 16px; }}
            .animation-card canvas {{ width: 100%; height: 200px; border-radius: 12px; background: {COLORS['card_bg']}; border: 1px solid {COLORS['accent1']}30; }}
            .theory-content {{ margin-left: 420px; padding: 100px 50px 50px; }}
            .theory-section {{ background: white; border-radius: 20px; padding: 30px; margin-bottom: 30px; border: 1px solid {COLORS['accent1']}30; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
            .theory-section h2 {{ color: {COLORS['accent4']}; margin-bottom: 20px; border-left: 4px solid {COLORS['accent5']}; padding-left: 15px; }}
            .math-block {{ background: {COLORS['card_bg']}; padding: 20px; border-radius: 12px; font-family: monospace; margin: 20px 0; overflow-x: auto; color: {COLORS['accent5']}; border-left: 3px solid {COLORS['accent2']}; }}
            @media (max-width: 768px) {{ .animation-sidebar {{ display: none; }} .theory-content {{ margin-left: 0; }} }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div class="logo">Study M</div>
            <div class="nav-menu">
                <a href="/">Главная</a>
                <a href="/theory">Теория</a>
                <a href="/physics">Обучение</a>
                <a href="/optimization">Попробуй сам</a>
            </div>
        </div>

        <div class="animation-sidebar">
            <div class="animation-card"><h3>🎯 Движение тела под углом</h3><canvas id="projectileAnimCanvas" width="370" height="200"></canvas></div>
            <div class="animation-card"><h3>🔧 Реалистичная пружина</h3><canvas id="springAnimCanvas" width="370" height="200"></canvas></div>
            <div class="animation-card"><h3>💥 Выстрел ядра</h3><canvas id="cannonAnimCanvas" width="370" height="200"></canvas></div>
        </div>

        <div class="theory-content">
            <div class="theory-section">
                <h2>📚 1. Численное решение математических задач</h2>

                <h3 style="color: #968AE1; margin-top: 20px;">1.1. Задача Коши</h3>
                <div class="math-block">dy/dt = f(t, y),  y(t₀) = y₀</div>
                <p>Метод Рунге-Кутты 4-го порядка:</p>
                <div class="math-block">
                    k₁ = f(t_n, y_n)<br>
                    k₂ = f(t_n + h/2, y_n + h·k₁/2)<br>
                    k₃ = f(t_n + h/2, y_n + h·k₂/2)<br>
                    k₄ = f(t_n + h, y_n + h·k₃)<br>
                    y_{{n+1}} = y_n + h·(k₁ + 2k₂ + 2k₃ + k₄)/6
                </div>

                <h3 style="color: #968AE1; margin-top: 20px;">1.2. Сведение ДУ высокого порядка к системе</h3>
                <div class="math-block">
                    y₁' = y₂<br>
                    y₂' = y₃<br>
                    ...<br>
                    yₙ' = f(t, y₁, y₂, ..., yₙ)
                </div>

                <h3 style="color: #968AE1; margin-top: 20px;">1.3. Краевая задача. Метод пристрелки</h3>
                <p>Для уравнения y'' = f(x, y, y') с краевыми условиями y(a) = α, y(b) = β.</p>
                <div class="math-block">
                    Алгоритм:<br>
                    1. Задаем начальный угол наклона s = y'(a)<br>
                    2. Решаем задачу Коши от a до b<br>
                    3. Сравниваем полученное y(b) с β<br>
                    4. Корректируем s методом Ньютона
                </div>

                <h3 style="color: #968AE1; margin-top: 20px;">1.4. Оптимизация. Метод Нелдера-Мида</h3>
                <p>Метод деформируемого симплекса для поиска минимума функции n переменных.</p>
                <div class="math-block">
                    Алгоритм:<br>
                    1. Построение начального симплекса из n+1 точки<br>
                    2. Отражение худшей точки через центр тяжести<br>
                    3. Растяжение или сжатие симплекса
                </div>
            </div>

            <div class="theory-section">
                <h2>⚡ 2. Математические модели в физике</h2>

                <h3 style="color: #968AE1; margin-top: 20px;">2.1. Движение тела под углом к горизонту</h3>
                <div class="math-block">
                    x(t) = v₀·cos(α)·t<br>
                    y(t) = y₀ + v₀·sin(α)·t - g·t²/2
                </div>

                <h3 style="color: #968AE1; margin-top: 20px;">2.2. Колебания пружинного маятника</h3>
                <div class="math-block">
                    m·x'' + γ·x' + k·x = 0<br>
                    ω₀ = √(k/m) — собственная частота<br>
                    ζ = γ/(2√(mk)) — коэффициент затухания
                </div>

                <h3 style="color: #968AE1; margin-top: 20px;">2.3. Другие физические модели</h3>
                <ul style="margin-left: 20px; margin-top: 10px;">
                    <li>Рост популяции (закон Мальтуса): dN/dt = rN</li>
                    <li>Радиоактивный распад: dN/dt = -λN</li>
                    <li>Задачи электродинамики: RC, RL цепи</li>
                </ul>
            </div>

            <div class="theory-section">
                <h2>🎯 3. Задачи поиска параметров модели</h2>
                <p>Оптимизационные задачи для нахождения параметров, обеспечивающих попадание в цель:</p>
                <ul style="margin-left: 30px; margin-top: 15px;">
                    <li>Попадание мяча в корзину</li>
                    <li>Попадание мяча в корзину с отскоком от щитка</li>
                    <li>Стендовая стрельба по тарелкам</li>
                    <li>Сброс груза с движущегося объекта</li>
                    <li>Задача «Теннис»</li>
                </ul>
            </div>
        </div>

        <script>
            const colors = {{ accent2: '#968AE1', accent3: '#FFF854', accent4: '#002FE7', accent5: '#FF7641', accent1: '#81818B', card_bg: '#F5F5F7' }};

            const projectileCanvas = document.getElementById('projectileAnimCanvas');
            let projectileTime = 0;
            function calcTraj(v0, angle, h0) {{ const g = 9.81, rad = angle * Math.PI / 180, vx = v0 * Math.cos(rad), vy = v0 * Math.sin(rad), tFlight = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g; return {{ vx: vx, vy: vy, tFlight: tFlight }}; }}
            function drawProjectile() {{
                if (!projectileCanvas) return;
                const ctx = projectileCanvas.getContext('2d'), w = projectileCanvas.width, h = projectileCanvas.height, traj = calcTraj(28, 50, 0), vx = traj.vx, vy = traj.vy, tFlight = traj.tFlight, g = 9.81;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);
                let t = projectileTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t, y = vy * t - 0.5 * g * t * t, maxX = vx * tFlight, maxY = (vy*vy/(2*g));
                if (maxX > 0) {{ const x_px = (x / maxX) * (w - 50) + 25, y_px = h - 30 - (y / maxY) * (h - 55); ctx.beginPath(); ctx.arc(x_px, y_px, 7, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill(); }}
                projectileTime += 0.035;
                if (projectileTime > tFlight) projectileTime = 0;
                requestAnimationFrame(drawProjectile);
            }}

            const springCanvas = document.getElementById('springAnimCanvas');
            let springTime = 0;
            function getSpringDisplacement(t) {{ const omega0 = Math.sqrt(45 / 0.8), zeta = 2.5 / (2 * Math.sqrt(0.8 * 45)), x0 = 30; if (zeta < 1) {{ const omega_d = omega0 * Math.sqrt(1 - zeta*zeta); return x0 * Math.exp(-zeta * omega0 * t) * Math.cos(omega_d * t); }} return x0 * Math.exp(-zeta * omega0 * t) * (1 + zeta * omega0 * t); }}
            function drawSpring() {{
                if (!springCanvas) return;
                const ctx = springCanvas.getContext('2d'), w = springCanvas.width, h = springCanvas.height;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1;
                ctx.fillRect(0, 0, w, 12);
                const cx = w / 2, displacement = getSpringDisplacement(springTime), currentY = 140 + displacement;
                ctx.beginPath();
                for (let i = 0; i <= 18; i++) {{ const t = i / 18, y = 15 + (currentY - 12 - 15) * t, amp = 12 * (1 + Math.abs(displacement) / 80), xo = Math.sin(t * Math.PI * 6) * amp; if (i === 0) ctx.moveTo(cx + xo, y); else ctx.lineTo(cx + xo, y); }}
                ctx.strokeStyle = colors.accent4;
                ctx.stroke();
                ctx.fillStyle = colors.accent5;
                ctx.fillRect(cx - 20, currentY - 12, 40, 24);
                springTime += 0.04;
                if (springTime > 5) springTime = 0;
                requestAnimationFrame(drawSpring);
            }}

            const cannonCanvas = document.getElementById('cannonAnimCanvas');
            let cannonTime = 0;
            function calcCannon(v0, a, h0) {{ const g = 9.81, r = a * Math.PI / 180, vx = v0 * Math.cos(r), vy = v0 * Math.sin(r), tf = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g; return {{ vx: vx, vy: vy, tFlight: tf }}; }}
            function drawCannon() {{
                if (!cannonCanvas) return;
                const ctx = cannonCanvas.getContext('2d'), w = cannonCanvas.width, h = cannonCanvas.height, traj = calcCannon(35, 42, 25), vx = traj.vx, vy = traj.vy, tFlight = traj.tFlight, g = 9.81;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);
                const cx = 35, cy = h - 35;
                ctx.save();
                ctx.translate(cx, cy);
                ctx.rotate(-42 * Math.PI / 180);
                ctx.fillStyle = colors.accent4;
                ctx.fillRect(0, -6, 35, 12);
                ctx.restore();
                ctx.beginPath();
                ctx.arc(cx - 5, cy + 5, 7, 0, Math.PI * 2);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(cx + 20, cy + 5, 7, 0, Math.PI * 2);
                ctx.fill();
                let t = cannonTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t, y = 25 + vy * t - 0.5 * g * t * t, maxX = vx * tFlight, maxY = (vy*vy/(2*g) + 25);
                if (maxX > 0 && t < tFlight) {{ const x_px = cx + 40 + (x / maxX) * (w - cx - 60), y_px = h - 35 - (y / maxY) * (h - 60); ctx.beginPath(); ctx.arc(x_px, y_px, 6, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill(); }}
                cannonTime += 0.04;
                if (cannonTime > tFlight) cannonTime = 0;
                requestAnimationFrame(drawCannon);
            }}

            drawProjectile();
            drawSpring();
            drawCannon();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# ================ СТРАНИЦА ОБУЧЕНИЯ ================
@app.get("/physics", response_class=HTMLResponse)
async def physics_page(request: Request):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Обучение - Study M</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: {COLORS['primary']}; color: {COLORS['secondary']}; }}
            .navbar {{ position: fixed; top: 0; left: 0; right: 0; background: {COLORS['primary']}; padding: 15px 40px; display: flex; justify-content: space-between; align-items: center; z-index: 100; border-bottom: 3px solid {COLORS['accent2']}; }}
            .logo {{ font-size: 28px; font-weight: bold; background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .nav-menu {{ display: flex; gap: 30px; }}
            .nav-menu a {{ text-decoration: none; color: {COLORS['secondary']}; padding: 8px 20px; border-radius: 25px; transition: all 0.3s; }}
            .nav-menu a:hover {{ background: {COLORS['accent2']}; color: white; }}
            .animation-sidebar {{ width: 420px; background: {COLORS['card_bg']}; padding: 100px 25px 25px; position: fixed; left: 0; top: 0; bottom: 0; overflow-y: auto; border-right: 1px solid {COLORS['accent1']}; }}
            .animation-card {{ background: white; border-radius: 20px; padding: 20px; margin-bottom: 25px; border: 1px solid {COLORS['accent1']}30; }}
            .animation-card h3 {{ color: {COLORS['accent4']}; margin-bottom: 12px; font-size: 16px; }}
            .animation-card canvas {{ width: 100%; height: 200px; border-radius: 12px; background: {COLORS['card_bg']}; }}
            .physics-content {{ margin-left: 420px; padding: 100px 50px 50px; }}
            .physics-section {{ background: white; border-radius: 20px; padding: 30px; margin-bottom: 30px; border: 1px solid {COLORS['accent1']}30; }}
            .physics-section h2 {{ color: {COLORS['accent4']}; margin-bottom: 20px; border-left: 4px solid {COLORS['accent5']}; padding-left: 15px; }}
            .form-group {{ margin: 20px 0; }}
            .form-group label {{ display: inline-block; width: 200px; color: {COLORS['accent2']}; font-weight: 500; }}
            .form-group input {{ background: {COLORS['card_bg']}; border: 1px solid {COLORS['accent1']}; color: {COLORS['secondary']}; padding: 8px 15px; border-radius: 10px; width: 150px; }}
            button {{ background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); color: white; border: none; padding: 12px 30px; border-radius: 25px; cursor: pointer; font-weight: bold; margin-top: 10px; }}
            button:hover {{ transform: translateY(-2px); }}
            .result {{ margin-top: 20px; padding: 20px; background: {COLORS['card_bg']}; border-radius: 12px; display: none; border-left: 3px solid {COLORS['accent3']}; }}
            canvas.plot-canvas {{ margin-top: 20px; max-width: 600px; border-radius: 12px; background: {COLORS['card_bg']}; border: 1px solid {COLORS['accent1']}30; }}
            @media (max-width: 768px) {{ .animation-sidebar {{ display: none; }} .physics-content {{ margin-left: 0; }} }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div class="logo">Study M</div>
            <div class="nav-menu">
                <a href="/">Главная</a>
                <a href="/theory">Теория</a>
                <a href="/physics">Обучение</a>
                <a href="/optimization">Попробуй сам</a>
            </div>
        </div>

        <div class="animation-sidebar">
            <div class="animation-card"><h3>🎯 Движение тела под углом</h3><canvas id="projectileAnimCanvas" width="370" height="200"></canvas></div>
            <div class="animation-card"><h3>🔧 Реалистичная пружина</h3><canvas id="springAnimCanvas" width="370" height="200"></canvas></div>
            <div class="animation-card"><h3>💥 Выстрел ядра</h3><canvas id="cannonAnimCanvas" width="370" height="200"></canvas></div>
        </div>

        <div class="physics-content">
            <div class="physics-section">
                <h2>⚡ Движение тела под углом к горизонту</h2>
                <div class="form-group"><label>Начальная скорость (м/с):</label><input type="number" id="v0" value="20" step="5"></div>
                <div class="form-group"><label>Угол (градусы):</label><input type="number" id="angle" value="45" step="5"></div>
                <div class="form-group"><label>Начальная высота (м):</label><input type="number" id="h0" value="0" step="1"></div>
                <button onclick="solveProjectile()">Рассчитать траекторию</button>
                <canvas id="projectileCanvas" class="plot-canvas" width="600" height="400"></canvas>
                <div id="projectileResult" class="result"></div>
            </div>

            <div class="physics-section">
                <h2>🔧 Колебания пружинного маятника</h2>
                <div class="form-group"><label>Масса (кг):</label><input type="number" id="mass" value="1" step="0.5"></div>
                <div class="form-group"><label>Жесткость (Н/м):</label><input type="number" id="k" value="10" step="5"></div>
                <div class="form-group"><label>Смещение (м):</label><input type="number" id="x0" value="0.1" step="0.05"></div>
                <div class="form-group"><label>Затухание:</label><input type="number" id="damping" value="0" step="0.5"></div>
                <button onclick="solveSpring()">Рассчитать колебания</button>
                <canvas id="springCanvas" class="plot-canvas" width="600" height="400"></canvas>
                <div id="springResult" class="result"></div>
            </div>
        </div>

        <script>
            const colors = {{ accent2: '#968AE1', accent3: '#FFF854', accent4: '#002FE7', accent5: '#FF7641', accent1: '#81818B', card_bg: '#F5F5F7' }};

            // Анимации для сайдбара
            const projectileCanvas = document.getElementById('projectileAnimCanvas');
            let projectileTime = 0;
            function calcTraj(v0, angle, h0) {{ const g = 9.81, rad = angle * Math.PI / 180, vx = v0 * Math.cos(rad), vy = v0 * Math.sin(rad), tFlight = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g; return {{ vx, vy, tFlight }}; }}
            function drawProjectileAnim() {{
                if (!projectileCanvas) return;
                const ctx = projectileCanvas.getContext('2d'), w = projectileCanvas.width, h = projectileCanvas.height, traj = calcTraj(28, 50, 0), vx = traj.vx, vy = traj.vy, tFlight = traj.tFlight, g = 9.81;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);
                let t = projectileTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t, y = vy * t - 0.5 * g * t * t, maxX = vx * tFlight, maxY = (vy*vy/(2*g));
                if (maxX > 0) {{ const x_px = (x / maxX) * (w - 50) + 25, y_px = h - 30 - (y / maxY) * (h - 55); ctx.beginPath(); ctx.arc(x_px, y_px, 7, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill(); }}
                projectileTime += 0.035;
                if (projectileTime > tFlight) projectileTime = 0;
                requestAnimationFrame(drawProjectileAnim);
            }}

            const springCanvasSide = document.getElementById('springAnimCanvas');
            let springTime = 0;
            function getSpringDisp(t) {{ const omega0 = Math.sqrt(45 / 0.8), zeta = 2.5 / (2 * Math.sqrt(0.8 * 45)), x0 = 30; if (zeta < 1) {{ const omega_d = omega0 * Math.sqrt(1 - zeta*zeta); return x0 * Math.exp(-zeta * omega0 * t) * Math.cos(omega_d * t); }} return x0 * Math.exp(-zeta * omega0 * t) * (1 + zeta * omega0 * t); }}
            function drawSpringAnim() {{
                if (!springCanvasSide) return;
                const ctx = springCanvasSide.getContext('2d'), w = springCanvasSide.width, h = springCanvasSide.height;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1;
                ctx.fillRect(0, 0, w, 12);
                const cx = w / 2, displacement = getSpringDisp(springTime), currentY = 140 + displacement;
                ctx.beginPath();
                for (let i = 0; i <= 18; i++) {{ const t = i / 18, y = 15 + (currentY - 12 - 15) * t, amp = 12 * (1 + Math.abs(displacement) / 80), xo = Math.sin(t * Math.PI * 6) * amp; if (i === 0) ctx.moveTo(cx + xo, y); else ctx.lineTo(cx + xo, y); }}
                ctx.strokeStyle = colors.accent4;
                ctx.stroke();
                ctx.fillStyle = colors.accent5;
                ctx.fillRect(cx - 20, currentY - 12, 40, 24);
                springTime += 0.04;
                if (springTime > 5) springTime = 0;
                requestAnimationFrame(drawSpringAnim);
            }}

            const cannonCanvasSide = document.getElementById('cannonAnimCanvas');
            let cannonTime = 0;
            function calcCannon(v0, a, h0) {{ const g = 9.81, r = a * Math.PI / 180, vx = v0 * Math.cos(r), vy = v0 * Math.sin(r), tf = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g; return {{ vx, vy, tFlight: tf }}; }}
            function drawCannonAnim() {{
                if (!cannonCanvasSide) return;
                const ctx = cannonCanvasSide.getContext('2d'), w = cannonCanvasSide.width, h = cannonCanvasSide.height, traj = calcCannon(35, 42, 25), vx = traj.vx, vy = traj.vy, tFlight = traj.tFlight, g = 9.81;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);
                const cx = 35, cy = h - 35;
                ctx.save();
                ctx.translate(cx, cy);
                ctx.rotate(-42 * Math.PI / 180);
                ctx.fillStyle = colors.accent4;
                ctx.fillRect(0, -6, 35, 12);
                ctx.restore();
                ctx.beginPath();
                ctx.arc(cx - 5, cy + 5, 7, 0, Math.PI * 2);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(cx + 20, cy + 5, 7, 0, Math.PI * 2);
                ctx.fill();
                let t = cannonTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t, y = 25 + vy * t - 0.5 * g * t * t, maxX = vx * tFlight, maxY = (vy*vy/(2*g) + 25);
                if (maxX > 0 && t < tFlight) {{ const x_px = cx + 40 + (x / maxX) * (w - cx - 60), y_px = h - 35 - (y / maxY) * (h - 60); ctx.beginPath(); ctx.arc(x_px, y_px, 6, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill(); }}
                cannonTime += 0.04;
                if (cannonTime > tFlight) cannonTime = 0;
                requestAnimationFrame(drawCannonAnim);
            }}

            drawProjectileAnim();
            drawSpringAnim();
            drawCannonAnim();

            function solveProjectile() {{
                const v0 = parseFloat(document.getElementById('v0').value), angle = parseFloat(document.getElementById('angle').value), h0 = parseFloat(document.getElementById('h0').value), g = 9.81, rad = angle * Math.PI / 180, vx = v0 * Math.cos(rad), vy = v0 * Math.sin(rad), tFlight = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g;
                const canvas = document.getElementById('projectileCanvas'), ctx = canvas.getContext('2d'), w = canvas.width, h = canvas.height;
                ctx.clearRect(0, 0, w, h);
                ctx.strokeStyle = colors.accent1;
                for(let i = 0; i <= 10; i++) {{ ctx.beginPath(); ctx.moveTo(i * w/10, 0); ctx.lineTo(i * w/10, h); ctx.stroke(); ctx.beginPath(); ctx.moveTo(0, i * h/10); ctx.lineTo(w, i * h/10); ctx.stroke(); }}
                const points = [];
                for(let t = 0; t <= tFlight; t += tFlight/100) {{ const x = vx * t, y = h0 + vy * t - 0.5 * g * t * t; if(y >= 0) {{ const x_px = (x / (vx * tFlight)) * w, y_px = h - (y / (vy*vy/(2*g) + h0 + 1)) * h; points.push({{x: x_px, y: y_px}}); }} }}
                ctx.beginPath(); ctx.moveTo(points[0].x, points[0].y); for(let i = 1; i < points.length; i++) ctx.lineTo(points[i].x, points[i].y); ctx.strokeStyle = colors.accent2; ctx.lineWidth = 2; ctx.stroke();
                document.getElementById('projectileResult').innerHTML = `<strong>Результаты расчета:</strong><br>Время полета: ${{tFlight.toFixed(2)}} с<br>Дальность полета: ${{(vx * tFlight).toFixed(2)}} м<br>Максимальная высота: ${{(vy*vy/(2*g) + h0).toFixed(2)}} м`;
                document.getElementById('projectileResult').style.display = 'block';
            }}

            function solveSpring() {{
                const mass = parseFloat(document.getElementById('mass').value), k = parseFloat(document.getElementById('k').value), x0 = parseFloat(document.getElementById('x0').value), damping = parseFloat(document.getElementById('damping').value), omega0 = Math.sqrt(k / mass), beta = damping / (2 * mass), period = 2 * Math.PI / omega0;
                const canvas = document.getElementById('springCanvas'), ctx = canvas.getContext('2d'), w = canvas.width, h = canvas.height;
                ctx.clearRect(0, 0, w, h);
                ctx.beginPath(); ctx.moveTo(50, h/2); ctx.lineTo(w-20, h/2); ctx.stroke(); ctx.beginPath(); ctx.moveTo(50, 20); ctx.lineTo(50, h-20); ctx.stroke();
                const points = [];
                for(let t = 0; t <= 5; t += 0.05) {{ let x; if(damping > 0) x = x0 * Math.exp(-beta * t) * Math.cos(omega0 * t); else x = x0 * Math.cos(omega0 * t); const x_px = 50 + (t / 5) * (w - 100), y_px = h/2 - (x / x0) * (h/2 - 50); points.push({{x: x_px, y: y_px}}); }}
                ctx.beginPath(); ctx.moveTo(points[0].x, points[0].y); for(let i = 1; i < points.length; i++) ctx.lineTo(points[i].x, points[i].y); ctx.strokeStyle = colors.accent5; ctx.stroke();
                document.getElementById('springResult').innerHTML = `<strong>Результаты расчета:</strong><br>Собственная частота: ${{(omega0/(2*Math.PI)).toFixed(2)}} Гц<br>Период колебаний: ${{period.toFixed(2)}} с<br>${{damping > 0 ? `Коэффициент затухания: ${{beta.toFixed(2)}}` : 'Колебания незатухающие'}}`;
                document.getElementById('springResult').style.display = 'block';
            }}
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# ================ СТРАНИЦА ОПТИМИЗАЦИИ ================
@app.get("/optimization", response_class=HTMLResponse)
async def optimization_page(request: Request):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Оптимизация - Study M</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: {COLORS['primary']}; color: {COLORS['secondary']}; }}
            .navbar {{ position: fixed; top: 0; left: 0; right: 0; background: {COLORS['primary']}; padding: 15px 40px; display: flex; justify-content: space-between; align-items: center; z-index: 100; border-bottom: 3px solid {COLORS['accent2']}; }}
            .logo {{ font-size: 28px; font-weight: bold; background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .nav-menu {{ display: flex; gap: 30px; }}
            .nav-menu a {{ text-decoration: none; color: {COLORS['secondary']}; padding: 8px 20px; border-radius: 25px; transition: all 0.3s; }}
            .nav-menu a:hover {{ background: {COLORS['accent2']}; color: white; }}
            .animation-sidebar {{ width: 420px; background: {COLORS['card_bg']}; padding: 100px 25px 25px; position: fixed; left: 0; top: 0; bottom: 0; overflow-y: auto; border-right: 1px solid {COLORS['accent1']}; }}
            .animation-card {{ background: white; border-radius: 20px; padding: 20px; margin-bottom: 25px; border: 1px solid {COLORS['accent1']}30; }}
            .animation-card h3 {{ color: {COLORS['accent4']}; margin-bottom: 12px; font-size: 16px; }}
            .animation-card canvas {{ width: 100%; height: 200px; border-radius: 12px; background: {COLORS['card_bg']}; }}
            .optimization-content {{ margin-left: 420px; padding: 100px 50px 50px; }}
            .optimization-section {{ background: white; border-radius: 20px; padding: 30px; margin-bottom: 30px; border: 1px solid {COLORS['accent1']}30; }}
            .optimization-section h2 {{ color: {COLORS['accent4']}; margin-bottom: 20px; border-left: 4px solid {COLORS['accent5']}; padding-left: 15px; }}
            .form-group {{ margin: 20px 0; }}
            .form-group label {{ display: inline-block; width: 200px; color: {COLORS['accent2']}; font-weight: 500; }}
            .form-group input {{ background: {COLORS['card_bg']}; border: 1px solid {COLORS['accent1']}; color: {COLORS['secondary']}; padding: 8px 15px; border-radius: 10px; width: 150px; }}
            button {{ background: linear-gradient(135deg, {COLORS['accent2']}, {COLORS['accent4']}); color: white; border: none; padding: 12px 30px; border-radius: 25px; cursor: pointer; font-weight: bold; margin-top: 10px; }}
            button:hover {{ transform: translateY(-2px); }}
            .result {{ margin-top: 20px; padding: 20px; background: {COLORS['card_bg']}; border-radius: 12px; display: none; border-left: 3px solid {COLORS['accent3']}; }}
            canvas.plot-canvas {{ margin-top: 20px; max-width: 600px; border-radius: 12px; background: {COLORS['card_bg']}; border: 1px solid {COLORS['accent1']}30; }}
            @media (max-width: 768px) {{ .animation-sidebar {{ display: none; }} .optimization-content {{ margin-left: 0; }} }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div class="logo">Study M</div>
            <div class="nav-menu">
                <a href="/">Главная</a>
                <a href="/theory">Теория</a>
                <a href="/physics">Обучение</a>
                <a href="/optimization">Попробуй сам</a>
            </div>
        </div>

        <div class="animation-sidebar">
            <div class="animation-card"><h3>🎯 Движение тела под углом</h3><canvas id="projectileAnimCanvas" width="370" height="200"></canvas></div>
            <div class="animation-card"><h3>🔧 Реалистичная пружина</h3><canvas id="springAnimCanvas" width="370" height="200"></canvas></div>
            <div class="animation-card"><h3>💥 Выстрел ядра</h3><canvas id="cannonAnimCanvas" width="370" height="200"></canvas></div>
        </div>

        <div class="optimization-content">
            <div class="optimization-section">
                <h2>🏀 Попадание мяча в корзину</h2>
                <p>Найдите оптимальную скорость и угол броска, чтобы мяч попал в корзину.</p>
                <div class="form-group"><label>Расстояние до корзины (м):</label><input type="number" id="distance" value="5" step="0.5"></div>
                <div class="form-group"><label>Высота корзины (м):</label><input type="number" id="height" value="3.05" step="0.1"></div>
                <div class="form-group"><label>Мин. скорость (м/с):</label><input type="number" id="vmin" value="5" step="1"></div>
                <div class="form-group"><label>Макс. скорость (м/с):</label><input type="number" id="vmax" value="15" step="1"></div>
                <button onclick="solveBasketball()">Найти оптимальные параметры</button>
                <canvas id="basketballCanvas" class="plot-canvas" width="600" height="400"></canvas>
                <div id="basketballResult" class="result"></div>
            </div>
        </div>

        <script>
            const colors = {{ accent2: '#968AE1', accent3: '#FFF854', accent4: '#002FE7', accent5: '#FF7641', accent1: '#81818B', card_bg: '#F5F5F7' }};

            // Анимации для сайдбара
            const projectileCanvas = document.getElementById('projectileAnimCanvas');
            let projectileTime = 0;
            function calcTraj(v0, angle, h0) {{ const g = 9.81, rad = angle * Math.PI / 180, vx = v0 * Math.cos(rad), vy = v0 * Math.sin(rad), tFlight = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g; return {{ vx, vy, tFlight }}; }}
            function drawProjectileAnim() {{
                if (!projectileCanvas) return;
                const ctx = projectileCanvas.getContext('2d'), w = projectileCanvas.width, h = projectileCanvas.height, traj = calcTraj(28, 50, 0), vx = traj.vx, vy = traj.vy, tFlight = traj.tFlight, g = 9.81;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);
                let t = projectileTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t, y = vy * t - 0.5 * g * t * t, maxX = vx * tFlight, maxY = (vy*vy/(2*g));
                if (maxX > 0) {{ const x_px = (x / maxX) * (w - 50) + 25, y_px = h - 30 - (y / maxY) * (h - 55); ctx.beginPath(); ctx.arc(x_px, y_px, 7, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill(); }}
                projectileTime += 0.035;
                if (projectileTime > tFlight) projectileTime = 0;
                requestAnimationFrame(drawProjectileAnim);
            }}

            const springCanvas = document.getElementById('springAnimCanvas');
            let springTime = 0;
            function getSpringDisp(t) {{ const omega0 = Math.sqrt(45 / 0.8), zeta = 2.5 / (2 * Math.sqrt(0.8 * 45)), x0 = 30; if (zeta < 1) {{ const omega_d = omega0 * Math.sqrt(1 - zeta*zeta); return x0 * Math.exp(-zeta * omega0 * t) * Math.cos(omega_d * t); }} return x0 * Math.exp(-zeta * omega0 * t) * (1 + zeta * omega0 * t); }}
            function drawSpringAnim() {{
                if (!springCanvas) return;
                const ctx = springCanvas.getContext('2d'), w = springCanvas.width, h = springCanvas.height;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1;
                ctx.fillRect(0, 0, w, 12);
                const cx = w / 2, displacement = getSpringDisp(springTime), currentY = 140 + displacement;
                ctx.beginPath();
                for (let i = 0; i <= 18; i++) {{ const t = i / 18, y = 15 + (currentY - 12 - 15) * t, amp = 12 * (1 + Math.abs(displacement) / 80), xo = Math.sin(t * Math.PI * 6) * amp; if (i === 0) ctx.moveTo(cx + xo, y); else ctx.lineTo(cx + xo, y); }}
                ctx.strokeStyle = colors.accent4;
                ctx.stroke();
                ctx.fillStyle = colors.accent5;
                ctx.fillRect(cx - 20, currentY - 12, 40, 24);
                springTime += 0.04;
                if (springTime > 5) springTime = 0;
                requestAnimationFrame(drawSpringAnim);
            }}

            const cannonCanvas = document.getElementById('cannonAnimCanvas');
            let cannonTime = 0;
            function calcCannon(v0, a, h0) {{ const g = 9.81, r = a * Math.PI / 180, vx = v0 * Math.cos(r), vy = v0 * Math.sin(r), tf = (vy + Math.sqrt(vy*vy + 2*g*h0)) / g; return {{ vx, vy, tFlight: tf }}; }}
            function drawCannonAnim() {{
                if (!cannonCanvas) return;
                const ctx = cannonCanvas.getContext('2d'), w = cannonCanvas.width, h = cannonCanvas.height, traj = calcCannon(35, 42, 25), vx = traj.vx, vy = traj.vy, tFlight = traj.tFlight, g = 9.81;
                ctx.clearRect(0, 0, w, h);
                ctx.fillStyle = colors.accent1 + '40';
                ctx.fillRect(0, h - 25, w, 25);
                const cx = 35, cy = h - 35;
                ctx.save();
                ctx.translate(cx, cy);
                ctx.rotate(-42 * Math.PI / 180);
                ctx.fillStyle = colors.accent4;
                ctx.fillRect(0, -6, 35, 12);
                ctx.restore();
                ctx.beginPath();
                ctx.arc(cx - 5, cy + 5, 7, 0, Math.PI * 2);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(cx + 20, cy + 5, 7, 0, Math.PI * 2);
                ctx.fill();
                let t = cannonTime;
                if (t > tFlight) t = tFlight;
                const x = vx * t, y = 25 + vy * t - 0.5 * g * t * t, maxX = vx * tFlight, maxY = (vy*vy/(2*g) + 25);
                if (maxX > 0 && t < tFlight) {{ const x_px = cx + 40 + (x / maxX) * (w - cx - 60), y_px = h - 35 - (y / maxY) * (h - 60); ctx.beginPath(); ctx.arc(x_px, y_px, 6, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill(); }}
                cannonTime += 0.04;
                if (cannonTime > tFlight) cannonTime = 0;
                requestAnimationFrame(drawCannonAnim);
            }}

            drawProjectileAnim();
            drawSpringAnim();
            drawCannonAnim();

            function solveBasketball() {{
                const distance = parseFloat(document.getElementById('distance').value), height = parseFloat(document.getElementById('height').value), vmin = parseFloat(document.getElementById('vmin').value), vmax = parseFloat(document.getElementById('vmax').value), g = 9.81;
                let bestV = vmin, bestAngle = 45, minError = Infinity;
                for(let v = vmin; v <= vmax; v += 0.5) for(let angle = 30; angle <= 60; angle += 1) {{ const rad = angle * Math.PI / 180, t = distance / (v * Math.cos(rad)), y = v * Math.sin(rad) * t - 0.5 * g * t * t, error = Math.abs(y - height); if(error < minError) {{ minError = error; bestV = v; bestAngle = angle; }} }}
                const canvas = document.getElementById('basketballCanvas'), ctx = canvas.getContext('2d'), w = canvas.width, h = canvas.height;
                ctx.clearRect(0, 0, w, h);
                ctx.strokeStyle = colors.accent1;
                for(let i = 0; i <= 10; i++) {{ ctx.beginPath(); ctx.moveTo(i * w/10, 0); ctx.lineTo(i * w/10, h); ctx.stroke(); ctx.beginPath(); ctx.moveTo(0, i * h/10); ctx.lineTo(w, i * h/10); ctx.stroke(); }}
                const rad = bestAngle * Math.PI / 180, vx = bestV * Math.cos(rad), vy = bestV * Math.sin(rad), tFlight = distance / vx;
                const points = [];
                for(let t = 0; t <= tFlight; t += tFlight/100) {{ const x = vx * t, y = vy * t - 0.5 * g * t * t, x_px = (x / distance) * w, y_px = h - (y / (height + 1)) * h; if(x_px >= 0 && x_px <= w && y_px >= 0) points.push({{x: x_px, y: y_px}}); }}
                ctx.beginPath(); ctx.moveTo(points[0].x, points[0].y); for(let i = 1; i < points.length; i++) ctx.lineTo(points[i].x, points[i].y); ctx.strokeStyle = colors.accent2; ctx.stroke();
                ctx.beginPath(); ctx.arc(w, h - (height / (height + 1)) * h, 8, 0, Math.PI * 2); ctx.fillStyle = colors.accent5; ctx.fill();
                document.getElementById('basketballResult').innerHTML = `<strong>Оптимальные параметры броска:</strong><br>Начальная скорость: ${{bestV.toFixed(1)}} м/с<br>Угол броска: ${{bestAngle.toFixed(0)}}°<br>Точность попадания: ${{((1 - minError/height)*100).toFixed(1)}}%`;
                document.getElementById('basketballResult').style.display = 'block';
            }}
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# Запуск
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
