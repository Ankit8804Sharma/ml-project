<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ethereum Fraud Detection — README</title>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #0f1117;
      --bg2: #161b25;
      --bg3: #1c2333;
      --card: #1a2030;
      --border: rgba(120, 160, 220, 0.12);
      --border2: rgba(120, 160, 220, 0.25);
      --blue: #7eb8f7;
      --teal: #56d4bc;
      --red: #f87171;
      --yellow: #fbbf5a;
      --green: #6ee7b7;
      --text: #dde3ee;
      --text2: #8a97b0;
      --text3: #4e5d75;
      --mono: 'IBM Plex Mono', monospace;
      --sans: 'IBM Plex Sans', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--sans);
      font-size: 14px;
      line-height: 1.7;
    }

    /* subtle dot grid */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image: radial-gradient(circle, rgba(120,160,220,0.04) 1px, transparent 1px);
      background-size: 28px 28px;
      pointer-events: none;
      z-index: 0;
    }

    .page {
      position: relative;
      z-index: 1;
      max-width: 900px;
      margin: 0 auto;
      padding: 3rem 2rem 4rem;
    }

    /* ── HEADER ── */
    .header {
      border-bottom: 1px solid var(--border2);
      padding-bottom: 2rem;
      margin-bottom: 2.5rem;
    }

    .tag-row {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 1.2rem;
    }

    .tag {
      font-family: var(--mono);
      font-size: 10px;
      letter-spacing: 1.2px;
      padding: 3px 10px;
      border-radius: 4px;
      border: 1px solid;
    }

    .tag-blue  { color: var(--blue);  border-color: rgba(126,184,247,0.3); background: rgba(126,184,247,0.05); }
    .tag-teal  { color: var(--teal);  border-color: rgba(86,212,188,0.3);  background: rgba(86,212,188,0.05); }
    .tag-yellow{ color: var(--yellow);border-color: rgba(251,191,90,0.3);  background: rgba(251,191,90,0.05); }

    h1 {
      font-family: var(--mono);
      font-size: 1.9rem;
      font-weight: 600;
      color: #eef2ff;
      letter-spacing: -0.5px;
      margin-bottom: 0.6rem;
    }

    h1 span { color: var(--blue); }

    .subtitle {
      color: var(--text2);
      font-size: 14px;
      font-weight: 300;
      max-width: 600px;
    }

    /* ── SECTIONS ── */
    section { margin-bottom: 2.5rem; }

    h2 {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: var(--blue);
      margin-bottom: 1.2rem;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    h2::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border);
    }

    /* ── PIPELINE ── */
    .pipeline {
      display: flex;
      align-items: center;
      gap: 0;
      overflow-x: auto;
      padding: 1.25rem 1.5rem;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 0.75rem;
    }

    .pipe-step {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
      flex-shrink: 0;
    }

    .pipe-num {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--text3);
    }

    .pipe-box {
      background: var(--bg3);
      border: 1px solid var(--border2);
      border-radius: 7px;
      padding: 7px 14px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text);
      white-space: nowrap;
    }

    .pipe-box.highlight {
      border-color: rgba(126,184,247,0.4);
      color: var(--blue);
      background: rgba(126,184,247,0.05);
    }

    .pipe-arrow {
      font-size: 12px;
      color: var(--text3);
      margin: 0 8px;
      margin-top: 22px;
      flex-shrink: 0;
    }

    .pipe-note {
      font-size: 10px;
      font-family: var(--mono);
      color: var(--text3);
      text-align: center;
      max-width: 80px;
      line-height: 1.3;
    }

    /* ── FILE TREE ── */
    .file-tree {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      font-family: var(--mono);
      font-size: 12.5px;
      line-height: 2;
    }

    .tree-line { display: flex; align-items: center; gap: 0; }
    .tree-indent { display: inline-block; width: 20px; color: var(--border2); font-size: 11px; }
    .tree-folder { color: var(--yellow); }
    .tree-file   { color: var(--text2); }
    .tree-key    { color: var(--blue); }
    .tree-comment{ color: var(--text3); font-size: 11px; margin-left: 12px; }

    /* ── FEATURE TABLE ── */
    .feat-table {
      width: 100%;
      border-collapse: collapse;
    }

    .feat-table th {
      text-align: left;
      font-family: var(--mono);
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--text3);
      padding: 8px 14px;
      border-bottom: 1px solid var(--border2);
    }

    .feat-table td {
      padding: 9px 14px;
      border-bottom: 1px solid var(--border);
      font-size: 13px;
      vertical-align: top;
    }

    .feat-table tr:last-child td { border-bottom: none; }

    .feat-table tbody tr:hover td { background: rgba(126,184,247,0.03); }

    .code { font-family: var(--mono); font-size: 11.5px; color: var(--blue); }
    .formula { font-family: var(--mono); font-size: 11px; color: var(--teal); }

    /* ── MODEL CARDS ── */
    .model-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 12px;
    }

    .model-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.1rem 1.25rem;
    }

    .model-card-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.7rem;
    }

    .model-name {
      font-family: var(--mono);
      font-size: 12px;
      font-weight: 600;
      color: var(--text);
    }

    .model-badge {
      font-family: var(--mono);
      font-size: 9px;
      padding: 2px 7px;
      border-radius: 3px;
      letter-spacing: 0.5px;
    }

    .badge-supervised { background: rgba(86,212,188,0.1); color: var(--teal); border: 1px solid rgba(86,212,188,0.2); }
    .badge-unsupervised{ background: rgba(251,191,90,0.1); color: var(--yellow); border: 1px solid rgba(251,191,90,0.2); }

    .model-detail {
      font-size: 12px;
      color: var(--text2);
      line-height: 1.6;
    }

    .model-detail .kv {
      display: flex;
      justify-content: space-between;
      padding: 2px 0;
      border-bottom: 1px solid var(--border);
    }

    .model-detail .kv:last-child { border-bottom: none; }
    .model-detail .kv .k { color: var(--text3); font-size: 11px; font-family: var(--mono); }
    .model-detail .kv .v { font-family: var(--mono); font-size: 11px; color: var(--text); }

    /* ── SCORING BLOCK ── */
    .score-breakdown {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
    }

    .score-row {
      display: grid;
      grid-template-columns: 110px 1fr;
      border-bottom: 1px solid var(--border);
    }

    .score-row:last-child { border-bottom: none; }

    .score-key {
      padding: 11px 16px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--blue);
      background: rgba(126,184,247,0.04);
      border-right: 1px solid var(--border);
      display: flex;
      align-items: center;
    }

    .score-val {
      padding: 11px 16px;
      font-family: var(--mono);
      font-size: 11.5px;
      color: var(--text2);
    }

    .score-val .weight { color: var(--yellow); }
    .score-val .op     { color: var(--text3); }

    /* ── INSTALL BLOCK ── */
    .code-block {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.1rem 1.5rem;
      font-family: var(--mono);
      font-size: 12.5px;
      line-height: 2;
      overflow-x: auto;
    }

    .code-block .prompt { color: var(--text3); user-select: none; }
    .code-block .cmd    { color: var(--teal); }
    .code-block .comment{ color: var(--text3); font-size: 11px; }

    /* ── API TABLE ── */
    .api-block {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
    }

    .api-header {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 16px;
      border-bottom: 1px solid var(--border);
      background: var(--bg3);
    }

    .method {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      padding: 2px 9px;
      border-radius: 4px;
      background: rgba(86,212,188,0.12);
      color: var(--teal);
      border: 1px solid rgba(86,212,188,0.25);
    }

    .endpoint {
      font-family: var(--mono);
      font-size: 12px;
      color: var(--text);
    }

    .api-body { padding: 1rem 1.25rem; }

    .field-row {
      display: grid;
      grid-template-columns: 130px 80px 1fr;
      gap: 12px;
      padding: 7px 0;
      border-bottom: 1px solid var(--border);
      font-size: 12px;
    }

    .field-row:last-child { border-bottom: none; }
    .field-name  { font-family: var(--mono); color: var(--blue); }
    .field-type  { font-family: var(--mono); color: var(--text3); font-size: 11px; }
    .field-desc  { color: var(--text2); }

    /* ── FOOTER ── */
    footer {
      margin-top: 3rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    footer p {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text3);
    }

    .acc-row { display: flex; gap: 8px; flex-wrap: wrap; }
    .acc-chip {
      font-family: var(--mono);
      font-size: 11px;
      padding: 3px 9px;
      border-radius: 4px;
      background: rgba(86,212,188,0.07);
      color: var(--teal);
      border: 1px solid rgba(86,212,188,0.15);
    }

    @media(max-width:600px) {
      .pipeline { flex-direction: column; align-items: flex-start; gap: 6px; }
      .pipe-arrow { transform: rotate(90deg); margin: 0 0 0 30px; }
      .model-grid { grid-template-columns: 1fr; }
      .field-row { grid-template-columns: 1fr 1fr; }
      .field-type { display: none; }
    }
  </style>
</head>
<body>
<div class="page">

  <!-- HEADER -->
  <header class="header">
    <div class="tag-row">
      <span class="tag tag-blue">PYTHON 3.13</span>
      <span class="tag tag-teal">SCIKIT-LEARN</span>
      <span class="tag tag-yellow">FLASK API</span>
      <span class="tag tag-blue">SMOTE</span>
    </div>
    <h1>Ethereum <span>Fraud Detection</span></h1>
    <p class="subtitle">
      Unsupervised anomaly scoring (Isolation Forest + MF-UFS) used to auto-label
      Ethereum transactions, followed by supervised classifier training via
      Logistic Regression, SVM, KNN, Decision Tree, and Random Forest.
    </p>
  </header>

  <!-- PIPELINE -->
  <section>
    <h2>Pipeline</h2>
    <div class="pipeline">
      <div class="pipe-step">
        <div class="pipe-num">01</div>
        <div class="pipe-box highlight">Feature Engineering</div>
        <div class="pipe-note">feature_engineering.py</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-num">02</div>
        <div class="pipe-box">Isolation Forest</div>
        <div class="pipe-note">isolation_forest.py</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-num">03</div>
        <div class="pipe-box">MF-UFS Scoring</div>
        <div class="pipe-note">mfufs.py</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-num">04</div>
        <div class="pipe-box">Label Creation</div>
        <div class="pipe-note">create_labels.py</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-num">05–09</div>
        <div class="pipe-box highlight">Supervised Models</div>
        <div class="pipe-note">5 classifiers via main.py</div>
      </div>
    </div>
  </section>

  <!-- REPO STRUCTURE -->
  <section>
    <h2>Repository Structure</h2>
    <div class="file-tree">
      <div class="tree-line"><span class="tree-folder">ml-project-main/</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-key">main.py</span><span class="tree-comment">— full pipeline runner (steps 1–9)</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-key">app_backend.py</span><span class="tree-comment">— Flask REST API (port 5000)</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-key">app.html</span><span class="tree-comment">— browser UI for live predictions</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-file">eda.py</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-file">Requirements.txt</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-folder">Data/</span></div>
      <div class="tree-line"><span class="tree-indent">│  ├─</span><span class="tree-folder">new dataset/</span><span class="tree-comment">— primary data used by pipeline</span></div>
      <div class="tree-line"><span class="tree-indent">│  │  ├─</span><span class="tree-file">Dataset.csv</span><span class="tree-comment">— raw input</span></div>
      <div class="tree-line"><span class="tree-indent">│  │  ├─</span><span class="tree-file">processed_data.csv</span><span class="tree-comment">— after step 1</span></div>
      <div class="tree-line"><span class="tree-indent">│  │  ├─</span><span class="tree-file">if_scored.csv</span><span class="tree-comment">— after step 2</span></div>
      <div class="tree-line"><span class="tree-indent">│  │  ├─</span><span class="tree-file">final_output.csv</span><span class="tree-comment">— after step 3</span></div>
      <div class="tree-line"><span class="tree-indent">│  │  └─</span><span class="tree-file">labeled_data.csv</span><span class="tree-comment">— after step 4 (model input)</span></div>
      <div class="tree-line"><span class="tree-indent">│  └─</span><span class="tree-folder">old dataset/</span><span class="tree-comment">— ethereum.csv + intermediates</span></div>
      <div class="tree-line"><span class="tree-indent">├─</span><span class="tree-folder">Models/</span></div>
      <div class="tree-line"><span class="tree-indent">│  ├─</span><span class="tree-file">random_forest.pkl</span><span class="tree-comment">— &nbsp;decision_tree.pkl &nbsp;logistic.pkl</span></div>
      <div class="tree-line"><span class="tree-indent">│  ├─</span><span class="tree-file">svm.pkl &nbsp;knn.pkl</span><span class="tree-comment">— + matching _scaler.pkl files</span></div>
      <div class="tree-line"><span class="tree-indent">│  └─</span><span class="tree-file">decision_tree_plot.png</span></div>
      <div class="tree-line"><span class="tree-indent">└─</span><span class="tree-folder">src/</span></div>
      <div class="tree-line"><span class="tree-indent">   ├─</span><span class="tree-folder">preprocessing/</span><span class="tree-file">&nbsp;feature_engineering.py</span></div>
      <div class="tree-line"><span class="tree-indent">   ├─</span><span class="tree-folder">models/</span><span class="tree-file">&nbsp;isolation_forest.py &nbsp;mfufs.py &nbsp;logistic_model.py &nbsp;svm_model.py &nbsp;knn_model.py &nbsp;decision_tree_model.py &nbsp;random_forest.py</span></div>
      <div class="tree-line"><span class="tree-indent">   └─</span><span class="tree-folder">evaluation/</span><span class="tree-file">&nbsp;create_labels.py</span></div>
    </div>
  </section>

  <!-- FEATURES -->
  <section>
    <h2>Feature Engineering</h2>
    <p style="color:var(--text2);font-size:13px;margin-bottom:1rem;">
      Derived from raw columns <code class="code">value, gas, gas_price, receipt_gas_used, block_timestamp, block_number</code>.
      All five features are z-score normalised before use.
    </p>
    <table class="feat-table">
      <thead>
        <tr>
          <th>Feature (z-score)</th>
          <th>Derived From</th>
          <th>Formula</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="code">Value_z</span></td>
          <td style="color:var(--text2)">value column</td>
          <td><span class="formula">value</span></td>
        </tr>
        <tr>
          <td><span class="code">GasCost_z</span></td>
          <td style="color:var(--text2)">gas × gas_price</td>
          <td><span class="formula">gas * gas_price</span></td>
        </tr>
        <tr>
          <td><span class="code">GasEfficiency_z</span></td>
          <td style="color:var(--text2)">receipt_gas_used / gas</td>
          <td><span class="formula">receipt_gas_used / (gas + ε)</span></td>
        </tr>
        <tr>
          <td><span class="code">TimeGap_z</span></td>
          <td style="color:var(--text2)">block_timestamp diff</td>
          <td><span class="formula">diff(block_timestamp).total_seconds()</span></td>
        </tr>
        <tr>
          <td><span class="code">BlockGap_z</span></td>
          <td style="color:var(--text2)">block_number diff</td>
          <td><span class="formula">diff(block_number)</span></td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- LABELING -->
  <section>
    <h2>Unsupervised Labeling (MF-UFS)</h2>
    <p style="color:var(--text2);font-size:13px;margin-bottom:1rem;">
      Because no ground-truth labels exist in the dataset, fraud labels are generated
      automatically by combining three anomaly scores, then thresholding at the top 15%.
    </p>
    <div class="score-breakdown">
      <div class="score-row">
        <div class="score-key">IF_Score</div>
        <div class="score-val">Isolation Forest (200 trees, contamination=0.15) — normalised decision function score</div>
      </div>
      <div class="score-row">
        <div class="score-key">StatScore</div>
        <div class="score-val">|Value_z| + |GasEfficiency_z| + |TimeGap_z| + |GasCost_z| — normalised</div>
      </div>
      <div class="score-row">
        <div class="score-key">TempScore</div>
        <div class="score-val">|Value_z − rolling_mean(20)| / rolling_mean — normalised temporal deviation</div>
      </div>
      <div class="score-row">
        <div class="score-key">FinalScore</div>
        <div class="score-val">
          <span class="weight">0.3</span> <span class="op">×</span> IF_Score &nbsp;
          <span class="op">+</span> <span class="weight">0.4</span> <span class="op">×</span> StatScore &nbsp;
          <span class="op">+</span> <span class="weight">0.3</span> <span class="op">×</span> TempScore
        </div>
      </div>
      <div class="score-row">
        <div class="score-key">FraudFlag</div>
        <div class="score-val">1 if FinalScore &gt; 85th percentile, else 0 &nbsp;(≈15% fraud rate)</div>
      </div>
    </div>
  </section>

  <!-- MODELS -->
  <section>
    <h2>Models</h2>
    <div class="model-grid">

      <div class="model-card">
        <div class="model-card-head">
          <div class="model-name">Isolation Forest</div>
          <div class="model-badge badge-unsupervised">UNSUPERVISED</div>
        </div>
        <div class="model-detail">
          <div class="kv"><span class="k">n_estimators</span><span class="v">200</span></div>
          <div class="kv"><span class="k">contamination</span><span class="v">0.15</span></div>
          <div class="kv"><span class="k">random_state</span><span class="v">42</span></div>
          <div class="kv"><span class="k">saved</span><span class="v">—&nbsp;(used for scoring only)</span></div>
        </div>
      </div>

      <div class="model-card">
        <div class="model-card-head">
          <div class="model-name">Logistic Regression</div>
          <div class="model-badge badge-supervised">SUPERVISED</div>
        </div>
        <div class="model-detail">
          <div class="kv"><span class="k">max_iter</span><span class="v">1000</span></div>
          <div class="kv"><span class="k">scaler</span><span class="v">StandardScaler</span></div>
          <div class="kv"><span class="k">SMOTE strategy</span><span class="v">auto (balanced)</span></div>
          <div class="kv"><span class="k">saved</span><span class="v">logistic.pkl + scaler</span></div>
        </div>
      </div>

      <div class="model-card">
        <div class="model-card-head">
          <div class="model-name">SVM</div>
          <div class="model-badge badge-supervised">SUPERVISED</div>
        </div>
        <div class="model-detail">
          <div class="kv"><span class="k">kernel</span><span class="v">rbf</span></div>
          <div class="kv"><span class="k">C</span><span class="v">2</span></div>
          <div class="kv"><span class="k">threshold</span><span class="v">0.45 (predict_proba)</span></div>
          <div class="kv"><span class="k">SMOTE strategy</span><span class="v">0.5</span></div>
        </div>
      </div>

      <div class="model-card">
        <div class="model-card-head">
          <div class="model-name">KNN</div>
          <div class="model-badge badge-supervised">SUPERVISED</div>
        </div>
        <div class="model-detail">
          <div class="kv"><span class="k">n_neighbors</span><span class="v">5</span></div>
          <div class="kv"><span class="k">weights</span><span class="v">distance</span></div>
          <div class="kv"><span class="k">scaler</span><span class="v">StandardScaler</span></div>
          <div class="kv"><span class="k">SMOTE strategy</span><span class="v">0.5</span></div>
        </div>
      </div>

      <div class="model-card">
        <div class="model-card-head">
          <div class="model-name">Decision Tree</div>
          <div class="model-badge badge-supervised">SUPERVISED</div>
        </div>
        <div class="model-detail">
          <div class="kv"><span class="k">max_depth</span><span class="v">8</span></div>
          <div class="kv"><span class="k">min_samples_split</span><span class="v">10</span></div>
          <div class="kv"><span class="k">min_samples_leaf</span><span class="v">5</span></div>
          <div class="kv"><span class="k">plot saved</span><span class="v">decision_tree_plot.png</span></div>
        </div>
      </div>

      <div class="model-card">
        <div class="model-card-head">
          <div class="model-name">Random Forest</div>
          <div class="model-badge badge-supervised">SUPERVISED</div>
        </div>
        <div class="model-detail">
          <div class="kv"><span class="k">n_estimators</span><span class="v">300</span></div>
          <div class="kv"><span class="k">max_depth</span><span class="v">12</span></div>
          <div class="kv"><span class="k">min_samples_split</span><span class="v">10</span></div>
          <div class="kv"><span class="k">SMOTE strategy</span><span class="v">0.5</span></div>
        </div>
      </div>

    </div>
    <p style="margin-top:0.9rem;font-size:12px;color:var(--text3);font-family:var(--mono);">
      All supervised models: 80/20 train-test split · stratified · random_state=42 · SMOTE on training set only.
      SVM and KNN not served via the API (only DT, RF, LR are loaded in app_backend.py).
    </p>
  </section>

  <!-- API -->
  <section>
    <h2>Flask API — app_backend.py</h2>
    <div class="api-block">
      <div class="api-header">
        <span class="method">POST</span>
        <span class="endpoint">http://127.0.0.1:5000/predict</span>
      </div>
      <div class="api-body">
        <p style="font-size:12px;color:var(--text3);font-family:var(--mono);margin-bottom:0.8rem;">REQUEST BODY (JSON)</p>
        <div class="field-row">
          <span class="field-name">val_in</span>
          <span class="field-type">float</span>
          <span class="field-desc">ETH received by address</span>
        </div>
        <div class="field-row">
          <span class="field-name">val_out</span>
          <span class="field-type">float</span>
          <span class="field-desc">ETH sent from address</span>
        </div>
        <div class="field-row">
          <span class="field-name">fee</span>
          <span class="field-type">float</span>
          <span class="field-desc">Transaction fee (ETH) — used as GasCost</span>
        </div>
        <div class="field-row">
          <span class="field-name">gas</span>
          <span class="field-type">int</span>
          <span class="field-desc">Gas limit</span>
        </div>
        <div class="field-row">
          <span class="field-name">gas_used</span>
          <span class="field-type">int</span>
          <span class="field-desc">Actual gas used — GasEfficiency = gas_used / gas</span>
        </div>
        <div class="field-row">
          <span class="field-name">time_gap</span>
          <span class="field-type">float</span>
          <span class="field-desc">Seconds since previous transaction</span>
        </div>
        <div class="field-row">
          <span class="field-name">block_gap</span>
          <span class="field-type">int</span>
          <span class="field-desc">Block number difference from previous transaction</span>
        </div>
      </div>
    </div>
    <p style="margin-top:0.8rem;font-size:12px;color:var(--text3);font-family:var(--mono);">
      Response includes: <span style="color:var(--blue)">modelProbs</span> {Decision Tree, Random Forest, Logistic} ·
      <span style="color:var(--blue)">FinalScore</span> (mean of three) ·
      <span style="color:var(--blue)">IF_Score · StatScore · TempScore</span> ·
      <span style="color:var(--blue)">zscores</span> · <span style="color:var(--blue)">derivedFeatures</span>
    </p>
  </section>

  <!-- INSTALL -->
  <section>
    <h2>Setup &amp; Run</h2>
    <div class="code-block">
      <div><span class="prompt"># 1. Install dependencies</span></div>
      <div><span class="prompt">$ </span><span class="cmd">pip install -r Requirements.txt</span></div>
      <div>&nbsp;</div>
      <div><span class="prompt"># 2. Run the full pipeline (feature eng → labeling → train all models)</span></div>
      <div><span class="prompt">$ </span><span class="cmd">python main.py</span></div>
      <div>&nbsp;</div>
      <div><span class="prompt"># 3. Start the Flask API</span></div>
      <div><span class="prompt">$ </span><span class="cmd">python app_backend.py</span></div>
      <div>&nbsp;</div>
      <div><span class="prompt"># 4. Open app.html in a browser and use the UI</span></div>
      <div><span class="comment">#    Make sure the backend is running on localhost:5000</span></div>
    </div>

    <div style="margin-top:1rem;background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1rem 1.25rem;">
      <p style="font-size:12px;font-family:var(--mono);color:var(--text3);margin-bottom:0.5rem;">REQUIREMENTS.TXT</p>
      <p style="font-family:var(--mono);font-size:12px;color:var(--text2);line-height:2;">
        pandas≥2.0 &nbsp;·&nbsp; numpy≥1.24 &nbsp;·&nbsp; scikit-learn≥1.3 &nbsp;·&nbsp; matplotlib≥3.7
        &nbsp;·&nbsp; seaborn≥0.12 &nbsp;·&nbsp; openpyxl≥3.1 &nbsp;·&nbsp; imbalanced-learn≥0.11
        &nbsp;·&nbsp; streamlit≥1.30 &nbsp;·&nbsp; joblib≥1.3
      </p>
    </div>
  </section>

  <footer>
    <p>Ethereum Fraud Detection · MF-UFS Pipeline · CS1138</p>
    <div class="acc-row">
      <span class="acc-chip">DT ~93%</span>
      <span class="acc-chip">RF ~95%</span>
      <span class="acc-chip">LR ~88%</span>
    </div>
  </footer>

</div>
</body>
</html>
