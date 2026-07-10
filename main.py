<!DOCTYPE html>
<html>
<head>
  <base target="_top">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Raised Bed DIY Design Studio</title>
  <style>
    :root{
      --bg:#edf1f3;
      --panel:#ffffff;
      --soft:#f7f9fa;
      --ink:#1f2933;
      --muted:#6b7680;
      --line:#dbe2e8;
      --accent:#4A5D4E;
      --accent-rgb:74,93,78;
      --wood:#B17852;
      --wood-dark:#8F5D3D;
      --soil:#6a4b35;
      --grass:#7e9d62;
      --metal:#7b8791;
      --brick:#a85643;
      --shadow:0 10px 28px rgba(24,34,44,.12);
      --radius:18px;
      --thumb:100px;
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family:Arial,Helvetica,sans-serif;
      background:linear-gradient(135deg,#edf1f3 0%,#e8ecef 100%);
      color:var(--ink);
    }
    button,input,select{font:inherit}
    .app{
      max-width:1540px;
      margin:0 auto;
      padding:22px;
    }
    .topbar{
      display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:16px;
    }
    .brand{display:flex;align-items:center;gap:12px}
    .brand-mark{
      width:48px;height:48px;border-radius:14px;background:var(--accent);display:grid;place-items:center;color:#fff;font-size:24px;box-shadow:var(--shadow)
    }
    .brand strong{display:block;font-size:18px}
    .brand span{display:block;font-size:13px;color:var(--muted)}
    .icon-btn{
      border:1px solid var(--line);background:var(--panel);border-radius:12px;padding:10px 14px;cursor:pointer;font-weight:800;color:var(--ink)
    }
    .hero{
      background:linear-gradient(135deg,rgba(var(--accent-rgb),.12),rgba(var(--accent-rgb),.03)),var(--panel);
      border:1px solid var(--line);border-radius:24px;padding:30px;box-shadow:var(--shadow);margin-bottom:20px;position:relative;overflow:hidden
    }
    .hero:after{
      content:"";position:absolute;right:-70px;top:-80px;width:220px;height:220px;border-radius:50%;background:rgba(var(--accent-rgb),.08)
    }
    .eyebrow{font-size:12px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:8px}
    h1{margin:0 0 10px;font-size:clamp(30px,4vw,56px);line-height:.98}
    .hero p{margin:0;max-width:840px;color:var(--muted);font-size:17px;line-height:1.55}
    .workspace{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(390px,.75fr);gap:22px}
    .panel{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden}
    .panel-header{padding:20px 22px 14px;border-bottom:1px solid var(--line)}
    .panel-header h2{margin:0 0 6px;font-size:22px}
    .panel-header p{margin:0;color:var(--muted);font-size:14px}
    .gallery{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;padding:18px}
    .template-card{
      display:grid;grid-template-columns:var(--thumb) minmax(0,1fr);min-height:var(--thumb);
      border:1px solid var(--line);border-radius:14px;background:linear-gradient(var(--panel),var(--soft));
      overflow:hidden;cursor:pointer;text-align:left;color:var(--ink);padding:0;box-shadow:0 6px 12px rgba(25,35,45,.1);transition:.16s transform,.16s box-shadow,.16s border-color
    }
    .template-card:hover{transform:translateY(-2px);box-shadow:0 10px 18px rgba(25,35,45,.14)}
    .template-card.active{border-color:var(--accent);box-shadow:0 0 0 3px rgba(var(--accent-rgb),.18),0 10px 18px rgba(25,35,45,.14)}
    .thumb{
      min-height:var(--thumb);display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative;
      background:linear-gradient(180deg,rgba(255,255,255,.14),rgba(0,0,0,.08)), var(--accent)
    }
    .thumb svg{width:92%;height:88%}
    .template-copy{padding:14px 16px;display:flex;flex-direction:column;justify-content:center}
    .template-copy strong{font-size:16px;line-height:1.2;margin-bottom:6px}
    .template-copy span{font-size:14px;color:var(--muted);font-weight:800}
    .customizer{position:sticky;top:16px}
    .preview-wrap{padding:18px;background:linear-gradient(145deg,var(--soft),rgba(var(--accent-rgb),.06));border-bottom:1px solid var(--line)}
    .preview-card{
      min-height:320px;background:var(--panel);border:1px solid var(--line);border-radius:18px;overflow:hidden;
      display:flex;align-items:center;justify-content:center;padding:12px;position:relative
    }
    .preview-card svg{width:100%;max-height:320px}
    .form{padding:20px}
    .selected-title{margin:0 0 4px;font-size:24px}
    .selected-size{margin-bottom:18px;color:var(--muted);font-weight:800}
    .field-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}
    .field label,.mini-title{display:block;font-size:12px;font-weight:900;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
    .measurement{display:grid;grid-template-columns:1fr 1fr;gap:6px}
    .measurement span{position:relative}
    .measurement small{position:absolute;right:9px;top:50%;transform:translateY(-50%);color:var(--muted);font-weight:800;pointer-events:none}
    input[type="number"],select{
      width:100%;padding:10px;border:1px solid #cfd7de;border-radius:10px;background:var(--panel);color:var(--ink)
    }
    .measurement input{padding-right:28px}
    .choice-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
    .choice-grid.two{grid-template-columns:repeat(2,1fr)}
    .choice{
      border:1px solid #cfd7de;background:var(--panel);border-radius:10px;padding:10px 8px;cursor:pointer;font-weight:800;text-align:center;color:var(--ink)
    }
    .choice.active{background:var(--accent);border-color:var(--accent);color:#fff}
    .addon-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
    .addon{
      display:flex;gap:8px;align-items:center;border:1px solid #cfd7de;border-radius:10px;padding:10px;background:var(--panel);font-size:14px;font-weight:800
    }
    .preview-controls{
      margin-top:14px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px
    }
    .tiny-choice{
      border:1px solid #cfd7de;background:var(--panel);border-radius:10px;padding:8px 6px;cursor:pointer;font-size:13px;font-weight:800;text-align:center
    }
    .tiny-choice.active{background:rgba(var(--accent-rgb),.11);border-color:var(--accent);color:var(--accent)}
    .action-row{display:grid;grid-template-columns:1fr 1.25fr;gap:10px;margin-top:18px}
    .btn{border:0;border-radius:12px;padding:13px 14px;font-size:15px;font-weight:900;cursor:pointer}
    .btn.secondary{background:rgba(var(--accent-rgb),.1);color:var(--accent);border:1px solid rgba(var(--accent-rgb),.16)}
    .btn.primary{background:var(--accent);color:#fff}
    .summary{margin-top:18px;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--soft)}
    .summary-title{padding:12px 14px;font-weight:900;background:rgba(var(--accent-rgb),.08);border-bottom:1px solid var(--line)}
    .summary-grid{display:grid;grid-template-columns:1fr 1fr}
    .metric{padding:12px 14px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
    .metric:nth-child(even){border-right:0}
    .metric small{display:block;color:var(--muted);margin-bottom:4px}
    .metric strong{font-size:16px}
    .status{display:none;margin-top:14px;border-radius:12px;padding:12px 14px}
    .status.show{display:block}
    .status.ok{background:rgba(47,123,71,.1);border:1px solid rgba(47,123,71,.24)}
    .status.error{background:rgba(177,58,58,.09);border:1px solid rgba(177,58,58,.24)}
    .quick-notes{margin-top:14px;border:1px dashed var(--line);border-radius:12px;padding:12px;background:var(--soft)}
    .quick-notes strong{display:block;margin-bottom:6px}
    .quick-notes ul{margin:0;padding-left:18px;color:var(--muted)}
    .drawer-backdrop,.guide-backdrop{
      position:fixed;inset:0;background:rgba(15,22,29,.48);z-index:40;opacity:0;pointer-events:none;transition:opacity .16s ease
    }
    .drawer-backdrop.open,.guide-backdrop.open{opacity:1;pointer-events:auto}
    .drawer{
      position:fixed;top:0;right:0;bottom:0;width:min(420px,92vw);background:var(--panel);z-index:50;
      transform:translateX(100%);transition:transform .18s ease;box-shadow:-18px 0 50px rgba(0,0,0,.18);overflow:auto
    }
    .drawer.open{transform:translateX(0)}
    .drawer-head{display:flex;justify-content:space-between;align-items:center;padding:18px 20px;border-bottom:1px solid var(--line)}
    .drawer-body{padding:20px}
    .settings-group{margin-bottom:22px}
    .settings-group h3{margin:0 0 10px;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
    .option-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
    .set-btn{border:1px solid var(--line);background:var(--soft);border-radius:10px;padding:11px;cursor:pointer;font-weight:800}
    .set-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
    .swatches{display:flex;gap:10px;flex-wrap:wrap}
    .swatch{width:38px;height:38px;border-radius:50%;border:3px solid var(--panel);box-shadow:0 0 0 1px var(--line);cursor:pointer}
    .guide{
      position:fixed;inset:3vh 2.5vw;background:var(--panel);z-index:60;border-radius:22px;box-shadow:0 26px 80px rgba(15,22,29,.3);
      display:flex;flex-direction:column;opacity:0;transform:translateY(18px) scale(.99);pointer-events:none;transition:opacity .18s ease,transform .18s ease
    }
    .guide.open{opacity:1;transform:none;pointer-events:auto}
    .guide-head{display:flex;justify-content:space-between;align-items:flex-start;gap:14px;padding:18px 20px;border-bottom:1px solid var(--line)}
    .guide-head h2{margin:0 0 4px;font-size:24px}
    .guide-head p{margin:0;color:var(--muted)}
    .guide-actions{display:flex;gap:8px;flex-wrap:wrap}
    .guide-body{display:grid;grid-template-columns:220px minmax(0,1fr);min-height:0;flex:1}
    .guide-nav{border-right:1px solid var(--line);background:var(--soft);padding:14px;overflow:auto}
    .guide-tab{width:100%;border:0;background:transparent;padding:11px 12px;text-align:left;border-radius:10px;cursor:pointer;font-weight:850;color:var(--ink);margin-bottom:5px}
    .guide-tab.active{background:var(--accent);color:#fff}
    .guide-content{overflow:auto;padding:24px}
    .g-section{display:none}
    .g-section.active{display:block}
    .section-title{margin:0 0 6px;font-size:28px}
    .section-lede{margin:0 0 18px;color:var(--muted);line-height:1.55}
    .overview-grid{display:grid;grid-template-columns:minmax(0,1.08fr) minmax(300px,.92fr);gap:18px}
    .card{border:1px solid var(--line);background:var(--soft);border-radius:16px;padding:16px}
    .card h3{margin:0 0 10px}
    .hero-preview{min-height:340px;display:grid;place-items:center;background:radial-gradient(circle at top,rgba(var(--accent-rgb),.12),transparent 55%),var(--soft)}
    .hero-preview svg{width:100%;max-height:340px}
    .facts{display:grid;grid-template-columns:1fr 1fr;gap:10px}
    .fact{padding:12px;border:1px solid var(--line);border-radius:12px;background:var(--panel)}
    .fact small{display:block;color:var(--muted);margin-bottom:4px}
    .fact strong{font-size:17px}
    .materials,.cut-list,.image-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
    .item{border:1px solid var(--line);background:var(--soft);border-radius:14px;padding:14px}
    .item strong{display:block;margin-bottom:4px}
    .item .big{font-size:20px;font-weight:900;color:var(--accent);margin:4px 0 7px}
    .tools{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
    .chip{border:1px solid var(--line);border-radius:999px;padding:8px 11px;background:var(--soft);font-size:13px;font-weight:800}
    .steps{display:grid;gap:16px}
    .step{
      display:grid;grid-template-columns:minmax(280px,42%) minmax(0,1fr);gap:18px;border:1px solid var(--line);
      border-radius:18px;overflow:hidden;background:var(--soft)
    }
    .step-art{min-height:280px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(var(--accent-rgb),.08),var(--panel));border-right:1px solid var(--line);padding:12px}
    .step-art svg{width:100%;max-height:260px}
    .step-copy{padding:18px 18px 18px 0}
    .step-no{color:var(--accent);font-size:12px;font-weight:900;text-transform:uppercase;letter-spacing:.08em}
    .step-copy h3{margin:6px 0 8px;font-size:22px}
    .step-copy p{margin:0 0 10px;color:var(--muted);line-height:1.6}
    .tip{padding:12px;border-radius:12px;background:rgba(var(--accent-rgb),.08);border:1px solid rgba(var(--accent-rgb),.18)}
    .image-card{border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--soft)}
    .image-art{min-height:240px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(var(--accent-rgb),.08),var(--panel));padding:12px}
    .image-art svg{width:100%;max-height:220px}
    .image-copy{padding:12px 14px}
    .image-copy strong{display:block;margin-bottom:4px}
    .image-copy span{color:var(--muted)}
    .dual{display:grid;grid-template-columns:1fr 1fr;gap:18px}
    .cad-links{display:grid;grid-template-columns:1fr 1fr;gap:10px}
    .download{
      display:block;width:100%;border:1px solid var(--line);background:var(--panel);border-radius:12px;padding:14px;text-align:left;
      color:var(--accent);font-weight:900;cursor:pointer
    }
    .download:disabled{opacity:.64;cursor:wait}
    .warn{padding:12px;border-radius:12px;border:1px solid rgba(177,58,58,.24);background:rgba(177,58,58,.08);margin-top:12px}
    @media (max-width:1120px){
      .workspace{grid-template-columns:1fr}
      .customizer{position:static}
      .overview-grid,.dual{grid-template-columns:1fr}
    }
    @media (max-width:860px){
      .guide{inset:0;border-radius:0}
      .guide-body{grid-template-columns:1fr}
      .guide-nav{display:flex;gap:6px;overflow:auto;border-right:0;border-bottom:1px solid var(--line)}
      .guide-tab{white-space:nowrap;width:auto;margin:0}
      .step{grid-template-columns:1fr}
      .step-art{border-right:0;border-bottom:1px solid var(--line)}
      .step-copy{padding:18px}
    }
    @media (max-width:760px){
      .app{padding:12px}
      .gallery,.materials,.cut-list,.image-grid,.field-grid,.choice-grid,.addon-grid,.preview-controls,.action-row,.cad-links{grid-template-columns:1fr}
      .guide-actions{justify-content:flex-end}
      .facts,.summary-grid{grid-template-columns:1fr 1fr}
    }
    @media print{
      body *{visibility:hidden!important}
      .guide,.guide *{visibility:visible!important}
      .guide{position:static;inset:auto;opacity:1;transform:none;box-shadow:none;border-radius:0}
      .guide-nav,.drawer,.drawer-backdrop,.guide-backdrop,.guide-actions{display:none!important}
      .guide-body{display:block}
      .g-section{display:block!important;page-break-before:always}
      .g-section:first-child{page-break-before:auto}
    }
  </style>
</head>
<body>
  <div class="app">
    <div class="topbar">
      <div class="brand">
        <div class="brand-mark">🌱</div>
        <div>
          <strong>Raised Bed DIY Studio</strong>
          <span>Realistic wood-first builder • gallery first • DIY ready</span>
        </div>
      </div>
      <button class="icon-btn" onclick="openSettings()">⚙ Settings</button>
    </div>

    <section class="hero">
      <div class="eyebrow">Phase 1 • realistic wood builder</div>
      <h1>Pick a proven bed. Preview it like a real build.</h1>
      <p>
        This version starts with a more realistic wood-first experience. The preview now shows individual boards,
        corner posts, screws, top rails, soil, base layers, trellis options, and multiple views. The project guide
        is also more detailed for real DIY use.
      </p>
    </section>

    <main class="workspace">
      <section class="panel">
        <div class="panel-header">
          <h2>Choose a template</h2>
          <p>Every design loads instantly with a built-in visual thumbnail.</p>
        </div>
        <div id="gallery" class="gallery"></div>
      </section>

      <aside class="panel customizer">
        <div class="panel-header">
          <h2>Customize your design</h2>
          <p>Realistic wood preview first. Standard U.S. measurements only.</p>
        </div>

        <div class="preview-wrap">
          <div id="previewCard" class="preview-card"></div>
        </div>

        <div class="form">
          <h3 id="selectedTitle" class="selected-title"></h3>
          <div id="selectedSize" class="selected-size"></div>

          <div class="field-grid">
            <div class="field">
              <label>Length</label>
              <div class="measurement">
                <span><input id="lengthFeet" type="number" min="0" step="1"><small>ft</small></span>
                <span><input id="lengthInches" type="number" min="0" step="0.125"><small>in</small></span>
              </div>
            </div>
            <div class="field">
              <label>Width</label>
              <div class="measurement">
                <span><input id="widthFeet" type="number" min="0" step="1"><small>ft</small></span>
                <span><input id="widthInches" type="number" min="0" step="0.125"><small>in</small></span>
              </div>
            </div>
            <div class="field">
              <label>Height</label>
              <div class="measurement">
                <span><input id="heightFeet" type="number" min="0" step="1"><small>ft</small></span>
                <span><input id="heightInches" type="number" min="0" step="0.125"><small>in</small></span>
              </div>
            </div>
          </div>

          <div class="mini-title">Construction material</div>
          <div id="materialChoices" class="choice-grid">
            <button class="choice active" data-value="wood">Wood</button>
            <button class="choice" data-value="metal">Metal</button>
            <button class="choice" data-value="brick">Brick</button>
          </div>

          <div class="mini-title" style="margin-top:16px;">Construction style</div>
          <div id="constructionChoices" class="choice-grid two">
            <button class="choice active" data-value="standard">Standard Hardware</button>
            <button class="choice" data-value="nailless">Nailless Interlocking</button>
          </div>

          <div class="mini-title" style="margin-top:16px;">Add-ons & realism</div>
          <div class="addon-grid">
            <label class="addon"><input type="checkbox" id="topRail" checked> Top rails</label>
            <label class="addon"><input type="checkbox" id="trellis"> Trellis</label>
            <label class="addon"><input type="checkbox" id="hardwareCloth"> Hardware cloth</label>
            <label class="addon"><input type="checkbox" id="drainageCloth"> Drainage cloth</label>
            <label class="addon"><input type="checkbox" id="perimeterEdging"> Perimeter edging</label>
            <label class="addon"><input type="checkbox" id="showSoil" checked> Filled with soil</label>
          </div>

          <div class="mini-title" style="margin-top:16px;">Preview mode</div>
          <div id="previewControls" class="preview-controls">
            <button class="tiny-choice active" data-value="assembled">Assembled</button>
            <button class="tiny-choice" data-value="exploded">Exploded</button>
            <button class="tiny-choice" data-value="top">Top</button>
            <button class="tiny-choice" data-value="front">Front</button>
          </div>

          <div class="action-row">
            <button class="btn secondary" onclick="updatePreview()">Update Preview</button>
            <button class="btn primary" onclick="generateProject()">Generate Project Guide</button>
          </div>

          <div class="summary">
            <div class="summary-title">Live project summary</div>
            <div class="summary-grid">
              <div class="metric"><small>Soil volume</small><strong id="soilVolume">—</strong></div>
              <div class="metric"><small>1.5 cu ft bags</small><strong id="soilBags">—</strong></div>
              <div class="metric"><small>Base area</small><strong id="baseArea">—</strong></div>
              <div class="metric"><small>Perimeter</small><strong id="perimeter">—</strong></div>
              <div class="metric"><small>Dry soil weight</small><strong id="soilWeightDry">—</strong></div>
              <div class="metric"><small>Wet soil weight</small><strong id="soilWeightWet">—</strong></div>
            </div>
          </div>

          <div class="quick-notes">
            <strong>What changed in this visual upgrade</strong>
            <ul>
              <li>Wood previews show individual wall boards, corner posts, screws, soil, and rails.</li>
              <li>Exploded view helps users understand how the bed goes together.</li>
              <li>The guide adds helpers, safety gear, wet-soil weight, lifespan, and beginner mistakes.</li>
            </ul>
          </div>

          <div id="status" class="status"></div>
        </div>
      </aside>
    </main>
  </div>

  <div id="drawerBackdrop" class="drawer-backdrop" onclick="closeSettings()"></div>
  <aside id="settingsDrawer" class="drawer" aria-hidden="true">
    <div class="drawer-head">
      <h2>Settings</h2>
      <button class="icon-btn" onclick="closeSettings()">✕</button>
    </div>
    <div class="drawer-body">
      <div class="settings-group">
        <h3>Gallery layout</h3>
        <div class="option-grid">
          <button class="set-btn" data-setting="layout" data-value="grid">Grid</button>
          <button class="set-btn" data-setting="layout" data-value="compact">Compact</button>
          <button class="set-btn" data-setting="layout" data-value="list">List</button>
        </div>
      </div>
      <div class="settings-group">
        <h3>Theme</h3>
        <div class="option-grid">
          <button class="set-btn" data-setting="theme" data-value="light">Light</button>
          <button class="set-btn" data-setting="theme" data-value="garden">Garden</button>
          <button class="set-btn" data-setting="theme" data-value="workshop">Workshop</button>
          <button class="set-btn" data-setting="theme" data-value="dark">Dark</button>
        </div>
      </div>
      <div class="settings-group">
        <h3>Accent color</h3>
        <div class="swatches">
          <button class="swatch" style="background:#4A5D4E" data-color="#4A5D4E"></button>
          <button class="swatch" style="background:#B17852" data-color="#B17852"></button>
          <button class="swatch" style="background:#246BCE" data-color="#246BCE"></button>
          <button class="swatch" style="background:#7B3FB6" data-color="#7B3FB6"></button>
          <button class="swatch" style="background:#C04763" data-color="#C04763"></button>
        </div>
        <div style="display:grid;grid-template-columns:1fr 78px;gap:8px;margin-top:10px;">
          <div class="item" style="padding:10px;background:var(--soft);"><strong style="margin:0;">Custom accent</strong></div>
          <input id="customColor" type="color" value="#4A5D4E">
        </div>
      </div>
      <div class="settings-group">
        <h3>Thumbnail size</h3>
        <div class="option-grid">
          <button class="set-btn" data-setting="thumb" data-value="small">Small</button>
          <button class="set-btn" data-setting="thumb" data-value="medium">Medium</button>
          <button class="set-btn" data-setting="thumb" data-value="large">Large</button>
        </div>
      </div>
    </div>
  </aside>

  <div id="guideBackdrop" class="guide-backdrop" onclick="closeGuide()"></div>
  <section id="guide" class="guide" aria-hidden="true">
    <header class="guide-head">
      <div>
        <h2 id="guideTitle">Project Guide</h2>
        <p id="guideSubtitle"></p>
      </div>
      <div class="guide-actions">
        <button class="icon-btn" onclick="window.print()">🖨 Print</button>
        <button class="icon-btn" onclick="closeGuide()">✕ Close</button>
      </div>
    </header>
    <div class="guide-body">
      <nav class="guide-nav">
        <button class="guide-tab active" data-tab="overview">Overview</button>
        <button class="guide-tab" data-tab="materials">Materials</button>
        <button class="guide-tab" data-tab="cuts">Cut List</button>
        <button class="guide-tab" data-tab="instructions">Instructions</button>
        <button class="guide-tab" data-tab="images">Images</button>
        <button class="guide-tab" data-tab="garden">Garden Setup</button>
        <button class="guide-tab" data-tab="cad">CAD Files</button>
      </nav>
      <div class="guide-content">
        <section id="g-overview" class="g-section active"></section>
        <section id="g-materials" class="g-section"></section>
        <section id="g-cuts" class="g-section"></section>
        <section id="g-instructions" class="g-section"></section>
        <section id="g-images" class="g-section"></section>
        <section id="g-garden" class="g-section"></section>
        <section id="g-cad" class="g-section"></section>
      </div>
    </div>
  </section>

  <script>
    const TEMPLATES = [
      { id:"compact-patio", name:"Compact Patio Bed", size:"2' × 4' × 1'", length_ft:4, width_ft:2, height_ft:1, accent:"#D94747" },
      { id:"narrow-pathway", name:"Narrow Pathway Border", size:"2' × 6' × 1'", length_ft:6, width_ft:2, height_ft:1, accent:"#F26A21" },
      { id:"classic-fence", name:"Classic Fence-Line Bed", size:"2' × 8' × 1'", length_ft:8, width_ft:2, height_ft:1, accent:"#F2B134" },
      { id:"square-foot", name:"Square Foot Grid Box", size:"3' × 3' × 1'", length_ft:3, width_ft:3, height_ft:1, accent:"#6FBF3D" },
      { id:"grid-standard", name:"The Grid Standard", size:"4' × 4' × 1'", length_ft:4, width_ft:4, height_ft:1, accent:"#27A6A6" },
      { id:"family-box", name:"Mid-Size Family Box", size:"4' × 6' × 1'", length_ft:6, width_ft:4, height_ft:1, accent:"#1598D4" },
      { id:"gold-standard", name:"The Gold Standard", size:"4' × 8' × 1'", length_ft:8, width_ft:4, height_ft:1, accent:"#3746A6" },
      { id:"extra-deep", name:"Extra-Deep Root Bed", size:"4' × 8' × 2'", length_ft:8, width_ft:4, height_ft:2, accent:"#6D2C91" },
      { id:"waist-height", name:"Elevated Waist-Height Planter", size:"3.5' × 4' × 2.5'", length_ft:4, width_ft:3.5, height_ft:2.5, accent:"#C21874" }
    ];

    const DEFAULT_SETTINGS = {
      layout:"grid",
      theme:"light",
      accent:"#4A5D4E",
      thumb:"medium"
    };

    let settings = {...DEFAULT_SETTINGS};
    let selectedTemplate = TEMPLATES[6];
    let selectedMaterial = "wood";
    let selectedConstruction = "standard";
    let previewMode = "assembled";
    let currentProject = null;
    let currentCadResult = null;

    document.addEventListener("DOMContentLoaded", () => {
      loadSettings();
      renderGallery();
      applySettings();
      wireBaseEvents();
      wireGuideTabs();
      selectTemplate(selectedTemplate.id);
    });

    function wireBaseEvents(){
      document.querySelectorAll("#materialChoices .choice").forEach(btn => {
        btn.addEventListener("click", () => {
          selectedMaterial = btn.dataset.value;
          document.querySelectorAll("#materialChoices .choice").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          if (selectedMaterial !== "wood" && selectedConstruction === "nailless") {
            selectedConstruction = "standard";
            document.querySelectorAll("#constructionChoices .choice").forEach(b => {
              b.classList.toggle("active", b.dataset.value === "standard");
            });
          }
          updatePreview();
        });
      });

      document.querySelectorAll("#constructionChoices .choice").forEach(btn => {
        btn.addEventListener("click", () => {
          if (selectedMaterial !== "wood" && btn.dataset.value === "nailless") {
            showStatus("Nailless interlocking is visualized for wood in this version. Metal and brick stay on standard assembly.", true);
            return;
          }
          selectedConstruction = btn.dataset.value;
          document.querySelectorAll("#constructionChoices .choice").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          updatePreview();
        });
      });

      document.querySelectorAll("#previewControls .tiny-choice").forEach(btn => {
        btn.addEventListener("click", () => {
          previewMode = btn.dataset.value;
          document.querySelectorAll("#previewControls .tiny-choice").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          updatePreview();
        });
      });

      [
        "lengthFeet","lengthInches","widthFeet","widthInches","heightFeet","heightInches",
        "topRail","trellis","hardwareCloth","drainageCloth","perimeterEdging","showSoil"
      ].forEach(id => {
        document.getElementById(id).addEventListener("input", updatePreview);
        document.getElementById(id).addEventListener("change", updatePreview);
      });

      document.querySelectorAll(".set-btn").forEach(btn => {
        btn.addEventListener("click", () => {
          settings[btn.dataset.setting] = btn.dataset.value;
          applySettings();
          saveSettings();
        });
      });

      document.querySelectorAll(".swatch").forEach(btn => {
        btn.addEventListener("click", () => {
          settings.accent = btn.dataset.color;
          document.getElementById("customColor").value = settings.accent;
          applySettings();
          saveSettings();
        });
      });

      document.getElementById("customColor").addEventListener("input", e => {
        settings.accent = e.target.value;
        applySettings();
        saveSettings();
      });
    }

    function renderGallery(){
      const gallery = document.getElementById("gallery");
      gallery.innerHTML = TEMPLATES.map(t => `
        <button class="template-card" id="template-${t.id}" onclick="selectTemplate('${t.id}')">
          <div class="thumb" style="background:${t.accent}">
            ${thumbnailSvg(t)}
          </div>
          <div class="template-copy">
            <strong>${t.name}</strong>
            <span>${t.size}</span>
          </div>
        </button>
      `).join("");
    }

    function selectTemplate(id){
      selectedTemplate = TEMPLATES.find(t => t.id === id) || TEMPLATES[0];
      document.querySelectorAll(".template-card").forEach(el => {
        el.classList.toggle("active", el.id === "template-" + id);
      });
      setMeasurement("length", selectedTemplate.length_ft);
      setMeasurement("width", selectedTemplate.width_ft);
      setMeasurement("height", selectedTemplate.height_ft);
      document.getElementById("selectedTitle").textContent = selectedTemplate.name;
      updatePreview();
    }

    function setMeasurement(prefix, totalFeet){
      const ft = Math.floor(totalFeet);
      const inches = Math.round((totalFeet - ft) * 12 * 8) / 8;
      document.getElementById(prefix + "Feet").value = ft;
      document.getElementById(prefix + "Inches").value = inches;
    }

    function getMeasurement(prefix){
      const ft = Number(document.getElementById(prefix + "Feet").value || 0);
      const inch = Number(document.getElementById(prefix + "Inches").value || 0);
      return ft + (inch / 12);
    }

    function currentParams(){
      return {
        template_id: selectedTemplate.id,
        template_name: selectedTemplate.name,
        length_ft: getMeasurement("length"),
        width_ft: getMeasurement("width"),
        height_ft: getMeasurement("height"),
        material: selectedMaterial,
        construction_style: selectedConstruction,
        addons: {
          top_rail: document.getElementById("topRail").checked,
          trellis: document.getElementById("trellis").checked,
          hardware_cloth: document.getElementById("hardwareCloth").checked,
          drainage_cloth: document.getElementById("drainageCloth").checked,
          border_trim: document.getElementById("perimeterEdging").checked,
          show_soil: document.getElementById("showSoil").checked
        }
      };
    }

    function updatePreview(){
      const p = currentParams();
      document.getElementById("selectedSize").textContent =
        `${formatFeetInches(p.width_ft)} × ${formatFeetInches(p.length_ft)} × ${formatFeetInches(p.height_ft)}`;
      document.getElementById("previewCard").innerHTML = realisticPreviewSvg(p, previewMode);
      updateSummary(p);
      clearStatus();
    }

    function updateSummary(p){
      const volume = p.length_ft * p.width_ft * p.height_ft;
      const area = p.length_ft * p.width_ft;
      const per = 2 * (p.length_ft + p.width_ft);
      const dry = volume * 40;
      const wet = volume * 75;
      document.getElementById("soilVolume").textContent = volume.toFixed(1) + " cu ft";
      document.getElementById("soilBags").textContent = Math.ceil(volume / 1.5) + " bags";
      document.getElementById("baseArea").textContent = area.toFixed(1) + " sq ft";
      document.getElementById("perimeter").textContent = per.toFixed(1) + " linear ft";
      document.getElementById("soilWeightDry").textContent = Math.round(dry) + " lb";
      document.getElementById("soilWeightWet").textContent = Math.round(wet) + " lb";
    }

    function formatFeetInches(totalFeet){
      let ft = Math.floor(totalFeet);
      let inches = Math.round((totalFeet - ft) * 12 * 8) / 8;
      if (inches >= 12) { ft += 1; inches = 0; }
      return `${ft}'${inches ? ` ${inches}"` : ""}`;
    }

    function formatInchesOnly(totalFeet){
      return `${Math.round(totalFeet * 12 * 8) / 8}"`;
    }

    function realisticPreviewSvg(p, mode){
      if (p.material === "wood") return realisticWoodSvg(p, mode);
      if (p.material === "metal") return realisticMetalSvg(p, mode);
      return realisticBrickSvg(p, mode);
    }

    function woodCourses(heightFt){
      return Math.max(1, Math.ceil((heightFt * 12) / 12));
    }

    function realisticWoodSvg(p, mode){
      const courses = woodCourses(p.height_ft);
      const showTopRail = p.addons.top_rail;
      const showSoil = p.addons.show_soil;
      const showTrellis = p.addons.trellis;
      const showHardware = p.addons.hardware_cloth;
      const showDrainage = p.addons.drainage_cloth;
      const showEdging = p.addons.border_trim;
      const exploded = mode === "exploded";

      const lenScale = Math.min(210, 80 + p.length_ft * 18);
      const widScale = Math.min(115, 45 + p.width_ft * 14);
      const heightScale = Math.min(140, 32 + p.height_ft * 52);
      const x = 95;
      const y = mode === "top" ? 168 : 188;
      const slant = widScale * .5;
      const boardH = heightScale / courses;
      const offset = exploded ? 16 : 0;
      const longFaceX = x + (exploded ? 12 : 0);
      const shortSideShift = exploded ? 14 : 0;
      const topLift = exploded ? 14 : 0;

      const topA = `${x},${y}`;
      const topB = `${x + lenScale},${y}`;
      const topC = `${x + lenScale + widScale},${y - slant}`;
      const topD = `${x + widScale},${y - slant}`;
      const frontBaseY = y + heightScale;
      const rightX = x + lenScale;
      const post = 16;

      const screwsFront = [];
      const screwsRight = [];
      for (let c = 0; c < courses; c++){
        const cy = y + (c * boardH) + boardH / 2;
        screwsFront.push(`<circle cx="${x + 18}" cy="${cy}" r="2.3" fill="#d9dfe5"/><circle cx="${x + lenScale - 18}" cy="${cy}" r="2.3" fill="#d9dfe5"/>`);
        screwsRight.push(`<circle cx="${rightX + 10}" cy="${cy - slant + 8}" r="2.3" fill="#d9dfe5"/><circle cx="${rightX + widScale - 10}" cy="${cy - slant + 8}" r="2.3" fill="#d9dfe5"/>`);
      }

      const boardLinesFront = Array.from({length: courses - 1}, (_, i) => {
        const ly = y + boardH * (i + 1);
        return `<line x1="${x}" y1="${ly}" x2="${x + lenScale}" y2="${ly}" stroke="#7a4d31" stroke-width="2"/>`;
      }).join("");

      const boardLinesRight = Array.from({length: courses - 1}, (_, i) => {
        const ly1 = y - slant + boardH * (i + 1);
        const ly2 = y + boardH * (i + 1);
        return `<line x1="${rightX}" y1="${ly2}" x2="${rightX + widScale}" y2="${ly1}" stroke="#7a4d31" stroke-width="2"/>`;
      }).join("");

      const frontY = y + offset;
      const rightYOffset = exploded ? -2 : 0;
      const topYOffset = exploded ? -topLift : 0;

      if (mode === "front"){
        return `
          <svg viewBox="0 0 640 340" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect width="640" height="340" fill="url(#sky)"/>
            <rect y="250" width="640" height="90" fill="url(#ground)"/>
            ${showEdging ? `<rect x="98" y="255" width="${lenScale + 22}" height="6" fill="#56605f"/>` : ""}
            <rect x="120" y="120" width="${lenScale}" height="${heightScale}" fill="url(#woodFront)" stroke="#6d442b" stroke-width="2"/>
            ${Array.from({length:courses - 1}, (_, i) => `<line x1="120" y1="${120 + boardH * (i + 1)}" x2="${120 + lenScale}" y2="${120 + boardH * (i + 1)}" stroke="#7a4d31" stroke-width="2"/>`).join("")}
            <rect x="120" y="120" width="${post}" height="${heightScale}" fill="url(#postFill)" stroke="#6d442b"/>
            <rect x="${120 + lenScale - post}" y="120" width="${post}" height="${heightScale}" fill="url(#postFill)" stroke="#6d442b"/>
            ${Array.from({length:courses}, (_, i) => {
              const cy = 120 + i * boardH + boardH/2;
              return `<circle cx="${120 + 18}" cy="${cy}" r="2.2" fill="#d7dce1"/><circle cx="${120 + lenScale - 18}" cy="${cy}" r="2.2" fill="#d7dce1"/>`;
            }).join("")}
            ${showTopRail ? `<rect x="114" y="111" width="${lenScale + 12}" height="10" rx="2" fill="#8c5c3e" stroke="#6d442b"/>` : ""}
            ${showSoil ? `<rect x="135" y="132" width="${lenScale - 30}" height="${Math.max(18, heightScale * .62)}" fill="url(#soilFill)" opacity=".95"/>` : ""}
            ${showTrellis ? `
              <g>
                <rect x="${120 + lenScale - 26}" y="30" width="6" height="95" fill="#55616b"/>
                <rect x="${120 + lenScale - 6}" y="30" width="6" height="95" fill="#55616b"/>
                ${Array.from({length:4}, (_, i) => `<line x1="${120 + lenScale - 26}" y1="${40 + i * 20}" x2="${120 + lenScale}" y2="${40 + i * 20}" stroke="#7c8791" stroke-width="2"/>`).join("")}
              </g>
            ` : ""}
            <text x="120" y="38" font-size="16" font-weight="800" fill="#344049">Front view • realistic wood elevation</text>
            <text x="120" y="62" font-size="13" fill="#65717c">${formatFeetInches(p.length_ft)} long • ${formatFeetInches(p.height_ft)} high</text>
          </svg>
        `;
      }

      if (mode === "top"){
        return `
          <svg viewBox="0 0 640 340" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect width="640" height="340" fill="url(#sky)"/>
            <rect y="248" width="640" height="92" fill="url(#ground)"/>
            <rect x="120" y="72" width="${lenScale + widScale}" height="${lenScale * 0 + widScale + 70}" opacity="0"/>
            ${showEdging ? `<rect x="106" y="224" width="${lenScale + 30}" height="5" fill="#56605f"/><rect x="104" y="95" width="5" height="${widScale + 65}" fill="#56605f"/>` : ""}
            <polygon points="${topA} ${topB} ${topC} ${topD}" fill="url(#woodTop)" stroke="#6d442b" stroke-width="2"/>
            <polygon points="${x + 16},${y - 10} ${x + lenScale - 16},${y - 10} ${x + lenScale + widScale - 16},${y - slant + 16} ${x + widScale + 16},${y - slant + 16}" fill="${showSoil ? 'url(#soilFill)' : '#d7c2a8'}" stroke="#6d442b" stroke-width="1.6"/>
            <rect x="${x + 6}" y="${y + 12}" width="${lenScale - 12}" height="8" fill="#8c5c3e" opacity="${showTopRail ? '1' : '0'}"/>
            ${showHardware ? `<text x="98" y="56" font-size="12" fill="#65717c">Hardware cloth under base</text>` : ""}
            ${showDrainage ? `<text x="98" y="72" font-size="12" fill="#65717c">Drainage cloth above hardware layer</text>` : ""}
            ${showTrellis ? `
              <g>
                <line x1="${x + lenScale}" y1="${y}" x2="${x + lenScale + 18}" y2="${y - 88}" stroke="#55616b" stroke-width="6"/>
                <line x1="${x + lenScale + widScale}" y1="${y - slant}" x2="${x + lenScale + widScale + 18}" y2="${y - slant - 88}" stroke="#55616b" stroke-width="6"/>
                ${Array.from({length:5}, (_, i) => `<line x1="${x + lenScale + 4}" y1="${y - 14 - i * 17}" x2="${x + lenScale + widScale + 12}" y2="${y - slant - 14 - i * 17}" stroke="#7c8791" stroke-width="2"/>`).join("")}
              </g>
            ` : ""}
            <text x="96" y="38" font-size="16" font-weight="800" fill="#344049">Top view • structure footprint</text>
            <text x="96" y="58" font-size="13" fill="#65717c">${formatFeetInches(p.width_ft)} wide • ${formatFeetInches(p.length_ft)} long</text>
          </svg>
        `;
      }

      return `
        <svg viewBox="0 0 640 340" xmlns="http://www.w3.org/2000/svg">
          ${sceneDefs()}
          <rect width="640" height="340" fill="url(#sky)"/>
          <ellipse cx="220" cy="268" rx="190" ry="22" fill="rgba(0,0,0,.08)"/>
          <ellipse cx="394" cy="258" rx="110" ry="16" fill="rgba(0,0,0,.05)"/>
          <path d="M0 252 C120 228, 260 235, 640 250 L640 340 L0 340 Z" fill="url(#ground)"/>
          ${showEdging ? `<path d="M82 254 L${x + lenScale + 24} 254 L${x + lenScale + widScale + 26} ${254 - slant * .24}" stroke="#56605f" stroke-width="5" fill="none"/>` : ""}
          ${showHardware ? `<polygon points="${x + 22},${frontBaseY - 4} ${x + lenScale - 18},${frontBaseY - 4} ${x + lenScale + widScale - 18},${frontBaseY - slant} ${x + widScale + 18},${frontBaseY - slant}" fill="none" stroke="#8f989e" stroke-width="1.5" stroke-dasharray="4 4"/>` : ""}
          ${showDrainage ? `<polygon points="${x + 16},${frontBaseY - 11} ${x + lenScale - 12},${frontBaseY - 11} ${x + lenScale + widScale - 12},${frontBaseY - slant - 7} ${x + widScale + 12},${frontBaseY - slant - 7}" fill="rgba(220,226,230,.35)" stroke="#c4ccd2" stroke-width="1"/>` : ""}

          <!-- left/front wall -->
          <rect x="${x + (exploded ? -offset : 0)}" y="${frontY}" width="${lenScale}" height="${heightScale}" fill="url(#woodFront)" stroke="#6d442b" stroke-width="2"/>
          ${boardLinesFront}
          <rect x="${x - (exploded ? offset : 0)}" y="${frontY}" width="${post}" height="${heightScale}" fill="url(#postFill)" stroke="#6d442b"/>
          <rect x="${x + lenScale - post + (exploded ? offset : 0)}" y="${frontY}" width="${post}" height="${heightScale}" fill="url(#postFill)" stroke="#6d442b"/>
          ${screwsFront.join("")}

          <!-- right wall -->
          <polygon points="
            ${rightX + shortSideShift},${y + rightYOffset}
            ${rightX + widScale + shortSideShift},${y - slant + rightYOffset}
            ${rightX + widScale + shortSideShift},${frontBaseY - slant + rightYOffset}
            ${rightX + shortSideShift},${frontBaseY + rightYOffset}
          " fill="url(#woodSide)" stroke="#6d442b" stroke-width="2"/>
          ${boardLinesRight}
          <polygon points="
            ${rightX + shortSideShift},${y + rightYOffset}
            ${rightX + shortSideShift + post},${y + rightYOffset - 8}
            ${rightX + shortSideShift + post},${frontBaseY + rightYOffset - 8}
            ${rightX + shortSideShift},${frontBaseY + rightYOffset}
          " fill="url(#postFill)" stroke="#6d442b"/>
          <polygon points="
            ${rightX + widScale + shortSideShift - post},${y - slant + rightYOffset + 8}
            ${rightX + widScale + shortSideShift},${y - slant + rightYOffset}
            ${rightX + widScale + shortSideShift},${frontBaseY - slant + rightYOffset}
            ${rightX + widScale + shortSideShift - post},${frontBaseY - slant + rightYOffset + 8}
          " fill="url(#postFill)" stroke="#6d442b"/>
          ${screwsRight.join("")}

          <!-- top rim -->
          <polygon points="
            ${x},${y + topYOffset}
            ${x + lenScale},${y + topYOffset}
            ${x + lenScale + widScale},${y - slant + topYOffset}
            ${x + widScale},${y - slant + topYOffset}
          " fill="url(#woodTop)" stroke="#6d442b" stroke-width="2"/>

          ${showSoil ? `
            <polygon points="
              ${x + 18},${y + 8 + topYOffset}
              ${x + lenScale - 18},${y + 8 + topYOffset}
              ${x + lenScale + widScale - 18},${y - slant + 20 + topYOffset}
              ${x + widScale + 18},${y - slant + 20 + topYOffset}
            " fill="url(#soilFill)" stroke="#523726" stroke-width="1.5"/>
          ` : ""}

          ${showTopRail ? `
            <polygon points="
              ${x - 6},${y - 8 + topYOffset}
              ${x + lenScale + 8},${y - 8 + topYOffset}
              ${x + lenScale + widScale + 8},${y - slant + topYOffset - 8}
              ${x + widScale - 6},${y - slant + topYOffset - 8}
            " fill="#8d5c3e" stroke="#6d442b" stroke-width="1.6"/>
          ` : ""}

          ${selectedConstruction === "nailless" ? `
            <rect x="${x + lenScale - 18}" y="${frontY}" width="18" height="${boardH}" fill="rgba(255,255,255,.16)" stroke="#6d442b" stroke-width="1"/>
            <rect x="${x}" y="${frontY + boardH}" width="18" height="${boardH}" fill="rgba(255,255,255,.16)" stroke="#6d442b" stroke-width="1"/>
            <text x="96" y="42" font-size="13" fill="#65717c">Nailless visual detail: overlap/notch hints shown at corners.</text>
          ` : ""}

          ${showTrellis ? `
            <g>
              <line x1="${rightX + widScale - 8}" y1="${y - slant}" x2="${rightX + widScale - 8}" y2="${y - slant - 102}" stroke="#59656f" stroke-width="6"/>
              <line x1="${rightX + 10}" y1="${y}" x2="${rightX + 10}" y2="${y - 102}" stroke="#59656f" stroke-width="6"/>
              ${Array.from({length:5}, (_, i) => `<line x1="${rightX + 10}" y1="${y - 14 - i * 18}" x2="${rightX + widScale - 8}" y2="${y - slant - 14 - i * 18}" stroke="#7d8790" stroke-width="2"/>`).join("")}
            </g>
          ` : ""}

          <text x="88" y="38" font-size="16" font-weight="800" fill="#344049">
            ${mode === "exploded" ? "Exploded assembly view" : "Assembled realistic wood preview"}
          </text>
          <text x="88" y="59" font-size="13" fill="#65717c">
            ${formatFeetInches(p.width_ft)} × ${formatFeetInches(p.length_ft)} × ${formatFeetInches(p.height_ft)} • ${courses} wall course${courses > 1 ? "s" : ""}
          </text>
        </svg>
      `;
    }

    function realisticMetalSvg(p, mode){
      const len = Math.min(210, 80 + p.length_ft * 18);
      const wid = Math.min(112, 45 + p.width_ft * 14);
      const height = Math.min(140, 30 + p.height_ft * 52);
      const x = 108, y = 188, sl = wid * .5;
      return `
        <svg viewBox="0 0 640 340" xmlns="http://www.w3.org/2000/svg">
          ${sceneDefs()}
          <rect width="640" height="340" fill="url(#sky)"/>
          <path d="M0 252 C120 228, 260 235, 640 250 L640 340 L0 340 Z" fill="url(#ground)"/>
          <rect x="${x}" y="${y}" width="${len}" height="${height}" fill="url(#metalFront)" stroke="#55616b" stroke-width="2"/>
          ${Array.from({length:10}, (_,i)=>`<path d="M${x + 12 + i * 18} ${y} Q${x + 20 + i * 18} ${y + height/2} ${x + 12 + i * 18} ${y + height}" stroke="#b8c0c7" stroke-width="3" fill="none"/>`).join("")}
          <polygon points="${x + len},${y} ${x + len + wid},${y - sl} ${x + len + wid},${y + height - sl} ${x + len},${y + height}" fill="url(#metalSide)" stroke="#55616b" stroke-width="2"/>
          <polygon points="${x},${y} ${x + len},${y} ${x + len + wid},${y - sl} ${x + wid},${y - sl}" fill="#72808c" stroke="#55616b" stroke-width="2"/>
          <text x="88" y="38" font-size="16" font-weight="800" fill="#344049">Enhanced metal preview</text>
          <text x="88" y="59" font-size="13" fill="#65717c">Corrugated panel styling with corner angles and hardware hints</text>
        </svg>
      `;
    }

    function realisticBrickSvg(p, mode){
      const len = Math.min(212, 80 + p.length_ft * 18);
      const wid = Math.min(112, 45 + p.width_ft * 14);
      const height = Math.min(132, 28 + p.height_ft * 48);
      const x = 100, y = 190, sl = wid * .5;
      const courseH = 24;
      const courses = Math.max(1, Math.round(height / courseH));
      return `
        <svg viewBox="0 0 640 340" xmlns="http://www.w3.org/2000/svg">
          ${sceneDefs()}
          <rect width="640" height="340" fill="url(#sky)"/>
          <path d="M0 252 C120 228, 260 235, 640 250 L640 340 L0 340 Z" fill="url(#ground)"/>
          <rect x="${x}" y="${y}" width="${len}" height="${height}" fill="#b56752" stroke="#7b392d" stroke-width="2"/>
          ${Array.from({length:courses-1},(_,i)=>`<line x1="${x}" y1="${y + (i+1)*(height/courses)}" x2="${x + len}" y2="${y + (i+1)*(height/courses)}" stroke="#874333" stroke-width="2"/>`).join("")}
          <polygon points="${x + len},${y} ${x + len + wid},${y - sl} ${x + len + wid},${y + height - sl} ${x + len},${y + height}" fill="#a85643" stroke="#7b392d" stroke-width="2"/>
          <polygon points="${x},${y} ${x + len},${y} ${x + len + wid},${y - sl} ${x + wid},${y - sl}" fill="#c67a63" stroke="#7b392d" stroke-width="2"/>
          <text x="88" y="38" font-size="16" font-weight="800" fill="#344049">Enhanced brick / block preview</text>
          <text x="88" y="59" font-size="13" fill="#65717c">Block-course styling with cap and massing hints</text>
        </svg>
      `;
    }

    function thumbnailSvg(t){
      return realisticWoodThumb(t);
    }

    function realisticWoodThumb(t){
      const len = 95 + t.length_ft * 7;
      const wid = 40 + t.width_ft * 8;
      const height = 26 + t.height_ft * 18;
      const x = 26;
      const y = 80;
      const sl = wid * .45;
      return `
        <svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="thumbWood" x1="0" x2="1">
              <stop offset="0%" stop-color="#D29B72"/>
              <stop offset="100%" stop-color="#A56D49"/>
            </linearGradient>
          </defs>
          <rect width="320" height="180" fill="rgba(255,255,255,.06)"/>
          <ellipse cx="140" cy="152" rx="112" ry="12" fill="rgba(0,0,0,.14)"/>
          <rect x="${x}" y="${y}" width="${len}" height="${height}" fill="url(#thumbWood)" stroke="#6d442b" stroke-width="2"/>
          <polygon points="${x + len},${y} ${x + len + wid},${y - sl} ${x + len + wid},${y + height - sl} ${x + len},${y + height}" fill="#b67c56" stroke="#6d442b" stroke-width="2"/>
          <polygon points="${x},${y} ${x + len},${y} ${x + len + wid},${y - sl} ${x + wid},${y - sl}" fill="#8e5b3d" stroke="#6d442b" stroke-width="2"/>
          <polygon points="${x + 10},${y + 7} ${x + len - 10},${y + 7} ${x + len + wid - 10},${y - sl + 14} ${x + wid + 10},${y - sl + 14}" fill="#5f412c"/>
        </svg>
      `;
    }

    function sceneDefs(){
      return `
        <defs>
          <linearGradient id="sky" x1="0" x2="0" y1="0" y2="1">
            <stop offset="0%" stop-color="#eef5fb"/>
            <stop offset="100%" stop-color="#fafcfd"/>
          </linearGradient>
          <linearGradient id="ground" x1="0" x2="0" y1="0" y2="1">
            <stop offset="0%" stop-color="#91b071"/>
            <stop offset="100%" stop-color="#738f59"/>
          </linearGradient>
          <linearGradient id="woodFront" x1="0" x2="1">
            <stop offset="0%" stop-color="#d39b72"/>
            <stop offset="50%" stop-color="#b67c56"/>
            <stop offset="100%" stop-color="#9d6a49"/>
          </linearGradient>
          <linearGradient id="woodSide" x1="0" x2="1">
            <stop offset="0%" stop-color="#c48a62"/>
            <stop offset="100%" stop-color="#8e5c3d"/>
          </linearGradient>
          <linearGradient id="woodTop" x1="0" x2="1">
            <stop offset="0%" stop-color="#9d6945"/>
            <stop offset="100%" stop-color="#784c31"/>
          </linearGradient>
          <linearGradient id="postFill" x1="0" x2="1">
            <stop offset="0%" stop-color="#a86f49"/>
            <stop offset="100%" stop-color="#7d5136"/>
          </linearGradient>
          <linearGradient id="soilFill" x1="0" x2="1">
            <stop offset="0%" stop-color="#6d4a34"/>
            <stop offset="100%" stop-color="#4f3325"/>
          </linearGradient>
          <linearGradient id="metalFront" x1="0" x2="1">
            <stop offset="0%" stop-color="#9da9b3"/>
            <stop offset="100%" stop-color="#6f7d89"/>
          </linearGradient>
          <linearGradient id="metalSide" x1="0" x2="1">
            <stop offset="0%" stop-color="#88939d"/>
            <stop offset="100%" stop-color="#64717c"/>
          </linearGradient>
        </defs>
      `;
    }

    function generateProject(){
      const p = currentParams();
      if (p.length_ft <= 0 || p.width_ft <= 0 || p.height_ft <= 0) {
        showStatus("Enter dimensions greater than zero.", true);
        return;
      }
      currentProject = buildProject(p);
      currentCadResult = null;
      renderGuide(currentProject);
      renderCadPending();
      openGuide();

      if (google && google.script && google.script.run) {
        google.script.run
          .withSuccessHandler(result => {
            currentCadResult = result;
            renderCadResult(result);
          })
          .withFailureHandler(error => {
            renderCadResult({
              success:false,
              error:error && error.message ? error.message : String(error)
            });
          })
          .generateRaisedBedFromParameters(p);
      } else {
        renderCadResult({
          success:false,
          error:"google.script.run is unavailable in this preview environment."
        });
      }
    }

    function buildProject(p){
      const volume = p.length_ft * p.width_ft * p.height_ft;
      const area = p.length_ft * p.width_ft;
      const per = 2 * (p.length_ft + p.width_ft);
      const dryWeight = volume * 40;
      const wetWeight = volume * 75;
      const helpers = wetWeight > 1800 || p.material === "brick" ? 2 : 1;
      const complexity =
        p.material === "brick" ? "Moderate to advanced" :
        p.construction_style === "nailless" ? "Moderate" :
        p.length_ft >= 8 || p.height_ft > 1 ? "Beginner to moderate" : "Beginner-friendly";
      const buildTime =
        p.material === "brick" ? "4–8 hours" :
        p.construction_style === "nailless" ? "4–6 hours" :
        p.length_ft >= 8 || p.height_ft > 1 ? "3–5 hours" : "2–4 hours";
      return {
        params:p,
        volume, area, per, dryWeight, wetWeight, helpers, complexity, buildTime,
        materials: buildMaterials(p),
        cuts: buildCuts(p),
        tools: buildTools(p),
        steps: buildSteps(p),
        images: buildImages(p)
      };
    }

    function buildMaterials(p){
      const out = [];
      const courses = woodCourses(p.height_ft);
      const baseArea = p.length_ft * p.width_ft;
      const volume = baseArea * p.height_ft;

      if (p.material === "wood") {
        out.push(
          {name:`2" × 12" long-side boards`, qty:`${2 * courses} pieces`, note:`Cut to ${formatFeetInches(p.length_ft)}${p.construction_style === "nailless" ? ' plus overlap allowance' : ''}.`},
          {name:`2" × 12" end boards`, qty:`${2 * courses} pieces`, note:`Cut to ${formatFeetInches(p.width_ft)}${p.construction_style === "nailless" ? ' plus overlap allowance' : ''}.`},
          {name:`4" × 4" corner posts`, qty:`4 pieces`, note:`Cut to about ${formatFeetInches(p.height_ft)}.`}
        );
        if (p.construction_style === "standard") {
          out.push({name:`3" exterior deck screws`, qty:`${Math.max(32, courses * 16)} screws`, note:`For wall fastening to corner posts.`});
        } else {
          out.push({name:`Interlocking notch allowance`, qty:`8 board ends`, note:`Cut matching saddle / lap style notches using actual board thickness.`});
        }
        if (p.addons.top_rail) out.push({name:`1" × 4" top rails`, qty:`4 pieces`, note:`Two long and two short for finished top trim.`});
      } else if (p.material === "metal") {
        out.push(
          {name:`Corrugated wall panels`, qty:`${Math.ceil((2 * (p.length_ft + p.width_ft) * p.height_ft))} sq ft minimum`, note:`Allow extra material for overlap and waste.`},
          {name:`Corner angle brackets`, qty:`4 pieces`, note:`Full wall height.`},
          {name:`Self-tapping roofing screws`, qty:`40–60 screws`, note:`Use sealing washers.`}
        );
      } else {
        const blocksPerCourse = Math.ceil((2 * (p.length_ft + p.width_ft) * 12) / 16);
        const coursesB = Math.max(1, Math.ceil((p.height_ft * 12) / 8));
        out.push(
          {name:`8" × 8" × 16" concrete blocks`, qty:`${blocksPerCourse * coursesB} blocks`, note:`${blocksPerCourse} blocks per course × ${coursesB} courses.`},
          {name:`Top caps`, qty:`${blocksPerCourse} caps`, note:`Finish the perimeter cleanly.`},
          {name:`Optional rebar`, qty:`4–12 stakes`, note:`Useful for added stabilization.`}
        );
      }

      if (p.addons.hardware_cloth) out.push({name:`Hardware cloth`, qty:`${Math.ceil(baseArea)} sq ft`, note:`Cover the entire base to deter burrowing pests.`});
      if (p.addons.drainage_cloth) out.push({name:`Drainage cloth / geotextile`, qty:`${Math.ceil(baseArea)} sq ft`, note:`Place above the base layer where appropriate.`});
      if (p.addons.border_trim) out.push({name:`Perimeter edging`, qty:`${Math.ceil(2 * (p.length_ft + p.width_ft))} linear ft`, note:`For a clean outside edge.`});
      if (p.addons.trellis) out.push({name:`Trellis assembly`, qty:`1 assembly`, note:`Mount to the selected wall before full planting load.`});

      out.push({name:`Raised-bed growing mix`, qty:`${volume.toFixed(1)} cu ft`, note:`About ${Math.ceil(volume / 1.5)} bags at 1.5 cu ft each for a full fill.`});
      return out;
    }

    function buildCuts(p){
      const out = [];
      if (p.material === "wood") {
        const allowance = p.construction_style === "nailless" ? (4 / 12) : 0;
        const courses = woodCourses(p.height_ft);
        out.push(
          {name:"Long-side wall boards", qty:`${2 * courses} pieces`, length:formatFeetInches(p.length_ft + allowance), note:p.construction_style === "nailless" ? "Includes overlap allowance for corner joinery." : "Finished cut length."},
          {name:"Short-end wall boards", qty:`${2 * courses} pieces`, length:formatFeetInches(p.width_ft + allowance), note:p.construction_style === "nailless" ? "Includes overlap allowance for corner joinery." : "Finished cut length."},
          {name:"Corner posts", qty:"4 pieces", length:formatFeetInches(p.height_ft), note:"Use 4×4 stock."}
        );
        if (p.addons.top_rail) {
          out.push(
            {name:"Top rails", qty:"2 long + 2 short", length:`${formatFeetInches(p.length_ft)} and ${formatFeetInches(p.width_ft)}`, note:"Miter or butt-join corners."}
          );
        }
        if (p.construction_style === "nailless") {
          out.push({
            name:"Notch dimensions",
            qty:"8 board ends",
            length:`1½" wide × about 5⅝" deep on actual 2×12 stock`,
            note:"Measure actual board size before cutting."
          });
        }
      } else if (p.material === "metal") {
        out.push(
          {name:"Long-side panels", qty:"2 panels", length:`${formatFeetInches(p.length_ft)} × ${formatFeetInches(p.height_ft)}`, note:"Cut from corrugated sheet stock."},
          {name:"Short-end panels", qty:"2 panels", length:`${formatFeetInches(p.width_ft)} × ${formatFeetInches(p.height_ft)}`, note:"Deburr cut edges."}
        );
      } else {
        out.push({
          name:"Block layout",
          qty:`${Math.ceil((2 * (p.length_ft + p.width_ft) * 12) / 16)} blocks per course`,
          length:"No planned cutting",
          note:"Dry-stack and adjust corner orientation as needed."
        });
      }
      return out;
    }

    function buildTools(p){
      const tools = ["Tape measure","Level","Square","Work gloves","Shovel or rake"];
      if (p.material === "wood") {
        tools.push("Circular saw or miter saw","Drill/driver");
        if (p.construction_style === "nailless") tools.push("Chisel","Hammer","Clamps");
      }
      if (p.material === "metal") tools.push("Metal snips","Driver bits","Safety glasses");
      if (p.material === "brick") tools.push("Rubber mallet","Mason's line","Hand tamper");
      if (p.addons.hardware_cloth) tools.push("Wire cutters");
      return [...new Set(tools)];
    }

    function buildSteps(p){
      const courses = woodCourses(p.height_ft);
      const steps = [
        {
          title:"Prepare and level the site",
          body:`Mark a ${formatFeetInches(p.width_ft)} × ${formatFeetInches(p.length_ft)} footprint. Remove weeds, rocks, and high spots. Check both directions with a level before you build.`,
          tip:"The flatter the base, the easier the rest of the assembly will be.",
          art:"site"
        },
        {
          title:"Measure, label, and cut the parts",
          body:`Cut the wall boards, posts, and optional rails to the required lengths. Label each part before assembly so the long and short walls do not get mixed up.`,
          tip:"Measure the actual lumber width and thickness before cutting special joinery.",
          art:"measure"
        }
      ];

      if (p.material === "wood" && p.construction_style === "nailless") {
        steps.push({
          title:"Cut the interlocking corner joints",
          body:`Mark each notch using the actual board thickness. Cut matching overlap notches so opposing boards lock together at the corners without screws in the wall joint itself.`,
          tip:"Test-fit one full corner before cutting the rest of the set.",
          art:"joint"
        });
      }

      if (p.material === "wood" && p.construction_style === "standard") {
        steps.push({
          title:"Assemble the wall frame",
          body:`Stand the long walls and short walls around the footprint. Fasten the boards to the corner posts with exterior-rated screws. For a ${courses}-course build, keep every course flush and level as you go.`,
          tip:"Check both diagonals to confirm the rectangle is square.",
          art:"assemble"
        });
      }

      if (p.material === "metal") {
        steps.push({
          title:"Build the metal shell",
          body:`Fasten the corrugated panels to the corner angles. Keep ridges aligned and verify the shell stays square while you tighten the screws.`,
          tip:"Wear gloves. Fresh-cut metal edges are very sharp.",
          art:"metal"
        });
      }

      if (p.material === "brick") {
        steps.push({
          title:"Dry-stack the block courses",
          body:`Lay the first course as accurately as possible. Then stack the remaining courses while keeping the walls level and aligned.`,
          tip:"If the first course is off, the whole build will show it.",
          art:"brick"
        });
      }

      if (p.addons.hardware_cloth || p.addons.drainage_cloth) {
        steps.push({
          title:"Install the base layers",
          body:`${p.addons.hardware_cloth ? "Place hardware cloth across the full base. " : ""}${p.addons.drainage_cloth ? "Add drainage cloth above the base layer where needed. " : ""}Trim neatly at the edges before adding soil.`,
          tip:"Do not use an impermeable plastic sheet in a ground-contact bed unless you intentionally want a planter-style barrier.",
          art:"base"
        });
      }

      steps.push({
        title:"Add top rails and supports",
        body:`${p.addons.top_rail ? "Install the top rails after the shell is square. " : ""}${p.addons.trellis ? "Mount the trellis before the bed is planted and fully loaded. " : ""}Make sure every optional part is secure before the fill stage.`,
        tip:"It is easier to attach structural accessories before the bed is filled.",
        art:"addons"
      });

      steps.push({
        title:"Fill the bed and finish the garden side",
        body:`Add about ${(p.length_ft * p.width_ft * p.height_ft).toFixed(1)} cubic feet of growing medium if filling to near full depth. Leave a little freeboard at the top so water and mulch do not spill over.`,
        tip:"Water lightly in layers to settle the mix without compacting it too hard.",
        art:"soil"
      });

      steps.push({
        title:"Inspect and plant",
        body:`Check for twist, looseness, fastener issues, and level one more time. Then plant, mulch, and monitor after the first full watering.`,
        tip:"The first week after filling tells you a lot about any needed adjustments.",
        art:"finish"
      });

      return steps;
    }

    function buildImages(p){
      const images = [
        {title:"Realistic assembled preview", caption:"How the bed looks when built with the chosen options.", art:"finished"},
        {title:"Footprint plan", caption:"Top-down look at the selected width and length.", art:"plan"},
        {title:"Site prep concept", caption:"Leveling and marking the footprint before assembly.", art:"site"}
      ];
      if (p.material === "wood" && p.construction_style === "nailless") {
        images.push({title:"Nailless corner concept", caption:"Interlocking overlap style for a screw-light corner connection.", art:"joint"});
      }
      if (p.addons.hardware_cloth || p.addons.drainage_cloth) {
        images.push({title:"Base layer setup", caption:"Hardware cloth and drainage fabric at the bed base.", art:"base"});
      }
      if (p.addons.trellis) {
        images.push({title:"Trellis placement", caption:"A typical trellis attached to one wall.", art:"addons"});
      }
      return images;
    }

    function renderGuide(project){
      const p = project.params;
      document.getElementById("guideTitle").textContent = p.template_name;
      document.getElementById("guideSubtitle").textContent =
        `${formatFeetInches(p.width_ft)} × ${formatFeetInches(p.length_ft)} × ${formatFeetInches(p.height_ft)} • ${capitalize(p.material)} • ${p.construction_style === "nailless" ? "Nailless interlocking" : "Standard hardware"}`;

      document.getElementById("g-overview").innerHTML = `
        <h2 class="section-title">Project overview</h2>
        <p class="section-lede">A more realistic DIY summary of the selected build, including weight, helpers, build time, and practical considerations.</p>
        <div class="overview-grid">
          <div class="card hero-preview">
            ${realisticPreviewSvg(p, "assembled")}
          </div>
          <div class="card">
            <h3>Project facts</h3>
            <div class="facts">
              <div class="fact"><small>Difficulty</small><strong>${project.complexity}</strong></div>
              <div class="fact"><small>Build time</small><strong>${project.buildTime}</strong></div>
              <div class="fact"><small>Helpers suggested</small><strong>${project.helpers}</strong></div>
              <div class="fact"><small>Wall material</small><strong>${capitalize(p.material)}</strong></div>
              <div class="fact"><small>Soil volume</small><strong>${project.volume.toFixed(1)} cu ft</strong></div>
              <div class="fact"><small>1.5 cu ft bags</small><strong>${Math.ceil(project.volume / 1.5)}</strong></div>
              <div class="fact"><small>Estimated dry soil weight</small><strong>${Math.round(project.dryWeight)} lb</strong></div>
              <div class="fact"><small>Estimated wet soil weight</small><strong>${Math.round(project.wetWeight)} lb</strong></div>
              <div class="fact"><small>Base area</small><strong>${project.area.toFixed(1)} sq ft</strong></div>
              <div class="fact"><small>Perimeter</small><strong>${project.per.toFixed(1)} linear ft</strong></div>
            </div>
            <div class="warn">
              <strong>Practical note:</strong> Wet soil is extremely heavy. Confirm the site is stable and the selected construction method is appropriate for the size you are building.
            </div>
          </div>
        </div>
      `;

      document.getElementById("g-materials").innerHTML = `
        <h2 class="section-title">Materials & tools</h2>
        <p class="section-lede">This list is driven by the chosen dimensions, material, construction style, and add-ons.</p>
        <div class="materials">
          ${project.materials.map(m => `
            <div class="item">
              <strong>${esc(m.name)}</strong>
              <div class="big">${esc(m.qty)}</div>
              <div style="color:var(--muted);line-height:1.5;">${esc(m.note)}</div>
            </div>
          `).join("")}
        </div>
        <h3 style="margin-top:24px;">Recommended tools & safety</h3>
        <div class="tools">
          ${project.tools.map(t => `<span class="chip">${esc(t)}</span>`).join("")}
          <span class="chip">Safety glasses</span>
          <span class="chip">Hearing protection</span>
        </div>
      `;

      document.getElementById("g-cuts").innerHTML = `
        <h2 class="section-title">Cut list</h2>
        <p class="section-lede">Board-by-board or panel-by-panel cut guidance for the selected design.</p>
        <div class="cut-list">
          ${project.cuts.map(c => `
            <div class="item">
              <strong>${esc(c.name)}</strong>
              <div class="big">${esc(c.qty)} • ${esc(c.length)}</div>
              <div style="color:var(--muted);line-height:1.5;">${esc(c.note)}</div>
            </div>
          `).join("")}
        </div>
        ${p.material === "wood" ? `
          <div class="warn">
            <strong>Wood note:</strong> For dimensional lumber, always verify actual stock width and thickness before making final joinery cuts.
          </div>
        ` : ""}
      `;

      document.getElementById("g-instructions").innerHTML = `
        <h2 class="section-title">Step-by-step instructions</h2>
        <p class="section-lede">Illustrated build steps aimed at real DIY use, not just abstract geometry.</p>
        <div class="steps">
          ${project.steps.map((s,i) => `
            <article class="step">
              <div class="step-art">${guideArt(s.art, project)}</div>
              <div class="step-copy">
                <div class="step-no">Step ${i+1} of ${project.steps.length}</div>
                <h3>${esc(s.title)}</h3>
                <p>${esc(s.body)}</p>
                <div class="tip"><strong>Beginner tip:</strong> ${esc(s.tip)}</div>
              </div>
            </article>
          `).join("")}
        </div>
      `;

      document.getElementById("g-images").innerHTML = `
        <h2 class="section-title">Visual guide</h2>
        <p class="section-lede">Built-in diagrams help the user understand assembly, footprint, joints, and garden setup.</p>
        <div class="image-grid">
          ${project.images.map(img => `
            <article class="image-card">
              <div class="image-art">${guideArt(img.art, project)}</div>
              <div class="image-copy">
                <strong>${esc(img.title)}</strong>
                <span>${esc(img.caption)}</span>
              </div>
            </article>
          `).join("")}
        </div>
      `;

      document.getElementById("g-garden").innerHTML = `
        <h2 class="section-title">Garden setup</h2>
        <p class="section-lede">This section bridges the build side and the planting side of the project.</p>
        <div class="dual">
          <div class="card">
            <h3>Fill strategy</h3>
            <div class="facts">
              <div class="fact"><small>Total volume</small><strong>${project.volume.toFixed(1)} cu ft</strong></div>
              <div class="fact"><small>Bag count</small><strong>${Math.ceil(project.volume / 1.5)} bags</strong></div>
              <div class="fact"><small>Dry soil weight</small><strong>${Math.round(project.dryWeight)} lb</strong></div>
              <div class="fact"><small>Wet soil weight</small><strong>${Math.round(project.wetWeight)} lb</strong></div>
            </div>
            <div style="margin-top:12px;color:var(--muted);line-height:1.6;">
              A simple profile is: drainage support at the base if needed, quality soil and compost blend through the main root zone,
              and a small freeboard left at the top edge.
            </div>
          </div>
          <div class="card">
            <h3>Good practical reminders</h3>
            <ul style="margin:0;padding-left:18px;color:var(--muted);line-height:1.75;">
              <li>Confirm water access before placing the bed.</li>
              <li>Do not overfill; leave a little top margin.</li>
              <li>Use mulch after planting to help with moisture retention.</li>
              <li>Recheck fasteners or joints after the first deep watering.</li>
              <li>Expected lifespan is usually longest with brick, then metal, then untreated wood.</li>
            </ul>
          </div>
        </div>
      `;
      switchTab("overview");
    }

    function renderCadPending(){
      document.getElementById("g-cad").innerHTML = `
        <h2 class="section-title">CAD files</h2>
        <p class="section-lede">Your CAD files are being generated now.</p>
        <div class="card">⏳ Generating STEP and STL files...</div>
      `;
    }

    function renderCadResult(result){
      const host = document.getElementById("g-cad");
      if (!result || !result.success) {
        host.innerHTML = `
          <h2 class="section-title">CAD files</h2>
          <p class="section-lede">The project guide is ready, but CAD generation did not complete.</p>
          <div class="warn"><strong>CAD generation error:</strong> ${esc(result && result.error ? result.error : "Unknown error")}</div>
        `;
        return;
      }
      host.innerHTML = `
        <h2 class="section-title">CAD files</h2>
        <p class="section-lede">Download the fabrication-ready files generated for this project.</p>
        <div class="card">
          <div style="margin-bottom:14px;color:var(--muted);line-height:1.6;">
            ✅ CAD generation complete.<br>
            STEP: ${esc(result.step_filename || "raised_bed.step")}<br>
            STL: ${esc(result.stl_filename || "raised_bed.stl")}
          </div>
          <div class="cad-links">
            <button class="download" onclick="downloadCad('${esc(result.download_token || "")}','step',this)">Download STEP file</button>
            <button class="download" onclick="downloadCad('${esc(result.download_token || "")}','stl',this)">Download STL file</button>
          </div>
          ${result.project_folder ? `<div style="margin-top:12px;"><a href="${result.project_folder}" target="_blank" style="font-weight:900;color:var(--accent);">Open saved project folder</a></div>` : ""}
        </div>
      `;
    }

    function downloadCad(token, type, button){
      if (!token) {
        alert("No download token was returned by the backend.");
        return;
      }
      const original = button.textContent;
      button.disabled = true;
      button.textContent = "Preparing download...";
      google.script.run
        .withSuccessHandler(payload => {
          button.disabled = false;
          button.textContent = original;
          if (!payload || !payload.success || !payload.base64) {
            alert("The CAD file could not be prepared.");
            return;
          }
          const blob = base64ToBlob(payload.base64, payload.mime_type || "application/octet-stream");
          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = url;
          a.download = payload.filename || (type === "step" ? "project.step" : "project.stl");
          document.body.appendChild(a);
          a.click();
          a.remove();
          setTimeout(() => URL.revokeObjectURL(url), 5000);
        })
        .withFailureHandler(error => {
          button.disabled = false;
          button.textContent = original;
          alert(error && error.message ? error.message : String(error));
        })
        .getCadDownloadPayload(token, type);
    }

    function guideArt(type, project){
      const p = project.params;
      if (type === "finished") return realisticPreviewSvg(p, "assembled");
      if (type === "plan") return realisticPreviewSvg({...p, addons:{...p.addons, show_soil:false}}, "top");
      if (type === "site") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect width="520" height="300" fill="url(#sky)"/>
            <rect y="194" width="520" height="106" fill="url(#ground)"/>
            <rect x="100" y="94" width="260" height="106" rx="10" fill="none" stroke="#4A5D4E" stroke-width="4" stroke-dasharray="12 8"/>
            <path d="M390 72 L430 182" stroke="#5B6570" stroke-width="8"/>
            <path d="M368 82 L418 64 L432 94 Z" fill="#7C8894"/>
            <rect x="130" y="62" width="165" height="18" rx="9" fill="#D9DEE5" stroke="#8A949F"/>
            <circle cx="214" cy="71" r="7" fill="#4A5D4E"/>
            <text x="100" y="40" font-size="18" font-weight="800" fill="#344049">Mark the footprint and level the site</text>
          </svg>
        `;
      }
      if (type === "measure") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect width="520" height="300" fill="#fbfcfd"/>
            <rect x="70" y="118" width="360" height="66" rx="6" fill="url(#woodFront)" stroke="#6d442b"/>
            <line x1="90" y1="210" x2="410" y2="210" stroke="#4A5D4E" stroke-width="3"/>
            <polygon points="90,210 105,203 105,217" fill="#4A5D4E"/>
            <polygon points="410,210 395,203 395,217" fill="#4A5D4E"/>
            <text x="250" y="240" text-anchor="middle" font-size="20" font-weight="800" fill="#344049">${formatFeetInches(project.params.length_ft)}</text>
            <rect x="315" y="60" width="120" height="24" fill="#ead16d" stroke="#8b7c36"/>
            <text x="70" y="44" font-size="18" font-weight="800" fill="#344049">Measure twice, cut once</text>
          </svg>
        `;
      }
      if (type === "joint") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect x="72" y="118" width="260" height="70" fill="url(#woodFront)" stroke="#6d442b"/>
            <rect x="240" y="54" width="76" height="190" fill="url(#woodSide)" stroke="#6d442b"/>
            <rect x="240" y="118" width="76" height="35" fill="#f7f0e8"/>
            <rect x="278" y="118" width="54" height="35" fill="#f7f0e8"/>
            <text x="260" y="38" text-anchor="middle" font-size="18" font-weight="800" fill="#344049">Nailless interlocking corner concept</text>
            <text x="260" y="272" text-anchor="middle" font-size="16" fill="#65717c">Use actual board dimensions before cutting</text>
          </svg>
        `;
      }
      if (type === "assemble") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect x="126" y="100" width="260" height="92" fill="none" stroke="#B17852" stroke-width="16"/>
            <rect x="108" y="84" width="20" height="140" fill="url(#postFill)" stroke="#6d442b"/>
            <rect x="386" y="84" width="20" height="140" fill="url(#postFill)" stroke="#6d442b"/>
            <circle cx="150" cy="128" r="5" fill="#d9dfe5"/><circle cx="150" cy="164" r="5" fill="#d9dfe5"/>
            <circle cx="362" cy="128" r="5" fill="#d9dfe5"/><circle cx="362" cy="164" r="5" fill="#d9dfe5"/>
            <text x="260" y="40" text-anchor="middle" font-size="18" font-weight="800" fill="#344049">Fasten walls to corner posts and keep it square</text>
          </svg>
        `;
      }
      if (type === "metal") return realisticMetalSvg(p, "assembled");
      if (type === "brick") return realisticBrickSvg(p, "assembled");
      if (type === "base") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            <rect x="76" y="72" width="366" height="156" rx="12" fill="#dfe4e8" stroke="#8a959e" stroke-width="3"/>
            ${Array.from({length:12},(_,i)=>`<line x1="${88 + i * 28}" y1="74" x2="${88 + i * 28}" y2="226" stroke="#9da6ad" stroke-width="1"/>`).join("")}
            ${Array.from({length:6},(_,i)=>`<line x1="78" y1="${86 + i * 24}" x2="440" y2="${86 + i * 24}" stroke="#9da6ad" stroke-width="1"/>`).join("")}
            <path d="M105 98 H415 V201 H105 Z" fill="none" stroke="#4A5D4E" stroke-width="8" stroke-dasharray="14 8"/>
            <text x="260" y="42" text-anchor="middle" font-size="18" font-weight="800" fill="#344049">Base protection layers</text>
          </svg>
        `;
      }
      if (type === "addons") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect x="110" y="148" width="300" height="82" rx="5" fill="url(#woodFront)" stroke="#6d442b"/>
            <path d="M150 148 V56 H370 V148" fill="none" stroke="#55616b" stroke-width="8"/>
            ${Array.from({length:5},(_,i)=>`<line x1="${190 + i * 36}" y1="56" x2="${190 + i * 36}" y2="148" stroke="#7c8791" stroke-width="2"/>`).join("")}
            ${Array.from({length:3},(_,i)=>`<line x1="150" y1="${84 + i * 24}" x2="370" y2="${84 + i * 24}" stroke="#7c8791" stroke-width="2"/>`).join("")}
            <text x="260" y="40" text-anchor="middle" font-size="18" font-weight="800" fill="#344049">Trellis and accessories</text>
          </svg>
        `;
      }
      if (type === "soil" || type === "finish") {
        return `
          <svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
            ${sceneDefs()}
            <rect x="92" y="84" width="336" height="154" fill="none" stroke="#9a6b49" stroke-width="14"/>
            <rect x="105" y="178" width="310" height="44" fill="#5c4433"/>
            <rect x="105" y="136" width="310" height="42" fill="#6b7c49"/>
            <rect x="105" y="104" width="310" height="32" fill="#8a5d3c"/>
            <text x="260" y="42" text-anchor="middle" font-size="18" font-weight="800" fill="#344049">${type === "soil" ? "Fill in layers and water lightly" : "Final check, then plant"}</text>
          </svg>
        `;
      }
      return realisticPreviewSvg(p, "assembled");
    }

    function wireGuideTabs(){
      document.querySelectorAll(".guide-tab").forEach(btn => {
        btn.addEventListener("click", () => switchTab(btn.dataset.tab));
      });
    }

    function switchTab(tab){
      document.querySelectorAll(".guide-tab").forEach(btn => btn.classList.toggle("active", btn.dataset.tab === tab));
      document.querySelectorAll(".g-section").forEach(sec => sec.classList.toggle("active", sec.id === "g-" + tab));
    }

    function openGuide(){
      document.getElementById("guideBackdrop").classList.add("open");
      document.getElementById("guide").classList.add("open");
      document.getElementById("guide").setAttribute("aria-hidden","false");
      document.body.style.overflow = "hidden";
    }
    function closeGuide(){
      document.getElementById("guideBackdrop").classList.remove("open");
      document.getElementById("guide").classList.remove("open");
      document.getElementById("guide").setAttribute("aria-hidden","true");
      document.body.style.overflow = "";
    }
    function openSettings(){
      document.getElementById("drawerBackdrop").classList.add("open");
      document.getElementById("settingsDrawer").classList.add("open");
    }
    function closeSettings(){
      document.getElementById("drawerBackdrop").classList.remove("open");
      document.getElementById("settingsDrawer").classList.remove("open");
    }

    function loadSettings(){
      try {
        const raw = localStorage.getItem("raisedBedStudioSettingsRealistic");
        if (raw) settings = {...DEFAULT_SETTINGS, ...JSON.parse(raw)};
      } catch (e) {}
    }
    function saveSettings(){
      localStorage.setItem("raisedBedStudioSettingsRealistic", JSON.stringify(settings));
    }
    function applySettings(){
      const gallery = document.getElementById("gallery");
      gallery.style.gridTemplateColumns =
        settings.layout === "list" ? "1fr" :
        settings.layout === "compact" ? "repeat(3,minmax(0,1fr))" :
        "repeat(2,minmax(0,1fr))";

      if (settings.layout === "list") {
        document.querySelectorAll(".template-card").forEach(el => {
          el.style.gridTemplateColumns = "160px minmax(0,1fr)";
          el.style.minHeight = "114px";
        });
      } else if (settings.layout === "compact") {
        document.querySelectorAll(".template-card").forEach(el => {
          el.style.gridTemplateColumns = "1fr";
          el.style.minHeight = "0";
        });
      } else {
        document.querySelectorAll(".template-card").forEach(el => {
          el.style.gridTemplateColumns = "var(--thumb) minmax(0,1fr)";
          el.style.minHeight = "var(--thumb)";
        });
      }

      document.documentElement.style.setProperty("--accent", settings.accent);
      document.documentElement.style.setProperty("--accent-rgb", hexToRgb(settings.accent));

      const thumbMap = {small:"78px", medium:"100px", large:"124px"};
      document.documentElement.style.setProperty("--thumb", thumbMap[settings.thumb] || "100px");

      const body = document.body;
      body.style.background = "linear-gradient(135deg,#edf1f3 0%,#e8ecef 100%)";
      body.style.color = "var(--ink)";
      document.documentElement.style.setProperty("--bg","#edf1f3");
      document.documentElement.style.setProperty("--panel","#ffffff");
      document.documentElement.style.setProperty("--soft","#f7f9fa");
      document.documentElement.style.setProperty("--ink","#1f2933");
      document.documentElement.style.setProperty("--muted","#6b7680");
      document.documentElement.style.setProperty("--line","#dbe2e8");

      if (settings.theme === "dark") {
        document.documentElement.style.setProperty("--bg","#11161b");
        document.documentElement.style.setProperty("--panel","#1b2229");
        document.documentElement.style.setProperty("--soft","#242d35");
        document.documentElement.style.setProperty("--ink","#f1f5f7");
        document.documentElement.style.setProperty("--muted","#aeb7bf");
        document.documentElement.style.setProperty("--line","#36414b");
        body.style.background = "linear-gradient(135deg,#11161b 0%,#151b20 100%)";
      } else if (settings.theme === "garden") {
        document.documentElement.style.setProperty("--bg","#e7efe5");
        document.documentElement.style.setProperty("--panel","#fffdf7");
        document.documentElement.style.setProperty("--soft","#f0f5eb");
        document.documentElement.style.setProperty("--ink","#273126");
        document.documentElement.style.setProperty("--muted","#667164");
        document.documentElement.style.setProperty("--line","#d7dfd3");
        body.style.background = "linear-gradient(135deg,#e7efe5 0%,#edf3ea 100%)";
      } else if (settings.theme === "workshop") {
        document.documentElement.style.setProperty("--bg","#eceeed");
        document.documentElement.style.setProperty("--panel","#fafaf8");
        document.documentElement.style.setProperty("--soft","#efefeb");
        document.documentElement.style.setProperty("--ink","#2a2a2a");
        document.documentElement.style.setProperty("--muted","#6c6c6c");
        document.documentElement.style.setProperty("--line","#d2d2cd");
        body.style.background = "linear-gradient(135deg,#eceeed 0%,#f2f3f0 100%)";
      }

      document.querySelectorAll(".set-btn").forEach(btn => {
        btn.classList.toggle("active", settings[btn.dataset.setting] === btn.dataset.value);
      });
      document.getElementById("customColor").value = settings.accent;
      updatePreview();
    }

    function hexToRgb(hex){
      const clean = hex.replace("#","");
      const value = parseInt(clean,16);
      return `${(value>>16)&255}, ${(value>>8)&255}, ${value&255}`;
    }

    function showStatus(message, isError){
      const el = document.getElementById("status");
      el.innerHTML = message;
      el.className = "status show " + (isError ? "error" : "ok");
    }
    function clearStatus(){
      const el = document.getElementById("status");
      el.className = "status";
      el.innerHTML = "";
    }

    function base64ToBlob(base64Data, mimeType){
      const byteChars = atob(base64Data);
      const sliceSize = 1024;
      const byteArrays = [];
      for (let offset = 0; offset < byteChars.length; offset += sliceSize){
        const slice = byteChars.slice(offset, offset + sliceSize);
        const nums = new Array(slice.length);
        for (let i = 0; i < slice.length; i++) nums[i] = slice.charCodeAt(i);
        byteArrays.push(new Uint8Array(nums));
      }
      return new Blob(byteArrays, {type: mimeType || "application/octet-stream"});
    }

    function capitalize(v){ return String(v).charAt(0).toUpperCase() + String(v).slice(1); }
    function esc(v){
      return String(v)
        .replaceAll("&","&amp;")
        .replaceAll("<","&lt;")
        .replaceAll(">","&gt;")
        .replaceAll('"',"&quot;")
        .replaceAll("'","&#039;");
    }
  </script>
</body>
</html>
