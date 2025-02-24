def get_prompt(product_name):
    """以下にプロンプトを記載する"""
    return f"""
    Amazon.co.jpに存在する怪しい中華メーカーの商品説明文を書いてください。
    箇条書きで10個生成してください。

    以下の特徴を含めてください:
    - 中華フォント風の謎の漢字が混ざる（例:智慧型高科技耳机搭載！最強音效体验可能！）
    - 単語の使い方が不自然（例:高品級音楽体験！耳穴震える驚愕サウンド！）
    - 文の構造がガタガタ（例:このイヤホン、高品級の音楽あなたへ提供！）
    - 誇張表現が多い（例:軍事級強化ボディ！未来技術搭載！）
    - 文章が無駄に長い（例:このイヤホンは、音の宇宙をあなたの耳に届ける驚異の未来製品！）
    - 変なカタカナ＆漢字の誤用（例:最新鋭ブルートゥース耳機格納箱付き！）
    - 助詞の使い方が変（例:耳フィット形状が、快適付け心地！）
    - 英語や中国語が混ざる（例:Powerful Sound！超高科技爆音響！）
    - 感情を煽る（例:あなたの人生が変わる！これは買わないと損！）
    - 妙に詩的・哲学的（例:暗闇を切り裂く、太陽の輝き！）

    上記を踏まえ、{product_name} の説明を中華メーカー風に書いてください。
    """
