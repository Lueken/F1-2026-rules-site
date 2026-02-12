import re

files = ['index3.html', 'index4.html', 'index5.html', 'index6.html', 'index7.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add missing IDs (if not already present)
    if 'id="basic-terms"' not in content:
        # Basic Terms
        content = re.sub(
            r'(<div class="feature-panel">\s*<h3>Basic F1 Terms)',
            r'<div class="feature-panel" id="basic-terms">\n            <h3>Basic F1 Terms',
            content
        )
        content = re.sub(
            r'(<div class="neon-panel">\s*<h3>Basic F1 Terms)',
            r'<div class="neon-panel" id="basic-terms">\n            <h3>Basic F1 Terms',
            content
        )
        content = re.sub(
            r'(<div class="alert-panel">\s*<h3>BASIC)',
            r'<div class="alert-panel" id="basic-terms">\n            <h3>BASIC',
            content
        )
        content = re.sub(
            r'(<div class="speech-panel">\s*<h3>Basic F1 Terms!)',
            r'<div class="speech-panel" id="basic-terms">\n            <h3>Basic F1 Terms!',
            content
        )

    if 'id="new-terminology"' not in content:
        # New Terminology
        content = re.sub(
            r'(<section class="section">\s*<h2 class="section-title">New 2026 Terminology)',
            r'<section class="section" id="new-terminology">\n            <h2 class="section-title">New 2026 Terminology',
            content
        )
        content = re.sub(
            r'(<section class="section">\s*<div class="section-header">\s*<h2 class="section-title">New 2026 Terminology)',
            r'<section class="section" id="new-terminology">\n            <div class="section-header">\n                <h2 class="section-title">New 2026 Terminology',
            content
        )
        content = re.sub(
            r'(<section class="section">\s*<div class="section-label">GRID\.02</div>\s*<h2 class="section-title">NEW 2026)',
            r'<section class="section" id="new-terminology">\n            <div class="section-label">GRID.02</div>\n            <h2 class="section-title">NEW 2026',
            content
        )

    if 'id="whats-different"' not in content:
        # What's Different
        patterns = [
            (r'(<section class="section">\s*<h2 class="section-title">What\'s Different in 2026)',
             r'<section class="section" id="whats-different">\n            <h2 class="section-title">What\'s Different in 2026'),
            (r'(<section class="section">\s*<div class="section-header">\s*<h2 class="section-title">What\'s Different in 2026)',
             r'<section class="section" id="whats-different">\n            <div class="section-header">\n                <h2 class="section-title">What\'s Different in 2026'),
            (r'(<section class="section">\s*<div class="section-label">GRID\.03</div>\s*<h2 class="section-title">WHAT\'S)',
             r'<section class="section" id="whats-different">\n            <div class="section-label">GRID.03</div>\n            <h2 class="section-title">WHAT\'S'),
        ]
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)

    if 'id="australian-gp"' not in content:
        # Australian GP
        patterns = [
            (r'(<div class="gp-highlight">\s*<div class="gp-highlight-inner">\s*<h3>Australian Grand Prix)',
             r'<div class="gp-highlight" id="australian-gp">\n            <div class="gp-highlight-inner">\n                <h3>Australian Grand Prix'),
            (r'(<div class="gp-showcase">\s*<h3>Australian Grand Prix)',
             r'<div class="gp-showcase" id="australian-gp">\n            <h3>Australian Grand Prix'),
            (r'(<div class="gp-module">\s*<h3>AUSTRALIAN)',
             r'<div class="gp-module" id="australian-gp">\n            <h3>AUSTRALIAN'),
            (r'(<div class="gp-panel">\s*<h3>AUSTRALIAN GRAND PRIX!)',
             r'<div class="gp-panel" id="australian-gp">\n            <h3>AUSTRALIAN GRAND PRIX!'),
        ]
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Added section IDs to {filename}')

print('Done adding IDs')
