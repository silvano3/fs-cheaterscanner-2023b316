"""enrich etapas.json com análise estruturada incluindo paywall completo."""
import json

PATH = "/root/funnel_spy_cheaterscanner/etapas.json"
with open(PATH) as f: bundle = json.load(f)

analises = {
    0: {
        "tipo": "landing",
        "headline": "FIND OUT IF THEY'RE CHEATING",
        "subheadline": "Instantly scan dating apps to discover if your partner is active on Tinder, Bumble, Hinge & more.",
        "cta": "Female / Male (gender cards) — entrada por 'What's their gender?'",
        "mecanismo": "Promessa nua + imperativo + 6 idiomas no header (alcance internacional) + dropdown 'Search By Use Case' segmentando intenção (Deep Person Scan, Bumble/Tinder/Hinge Search, Reverse Phone/Email/Name Lookup) + selo 'AI bots' como autoridade técnica",
        "observacoes": "Hero minimalista (sem ticker, sem logos de mídia ainda — esses chegam no paywall). Aposta na promessa nua + entrada imediata pelo gender card. Footer com info corporativa visível (endereço Delaware, telefone 800) = legitimidade aparente. Multi-idioma sinaliza foco em tráfego pago internacional escalado."
    },
    1: {
        "tipo": "quiz · entrada (idade)",
        "headline": "How old are they?",
        "subheadline": "(input numérico)",
        "cta": "→ (chevron-right minimalista)",
        "mecanismo": "Pergunta única por tela (foco máximo) + dot navigation (5 dots no topo = 5 etapas) = barra de progresso minimalista = sunk-cost suave sem pressão visual",
        "observacoes": "Banner inferior 'Did you know? 43% of people on dating apps are actively in relationships according to the New York Times' = autoridade-emprestada via citação NYT, estatística que normaliza paranoia. Chevrons sem texto (vs 'Continue' grande) reduz peso da decisão a cada step."
    },
    2: {
        "tipo": "quiz · entrada (nome)",
        "headline": "What is their name?",
        "subheadline": "First name (required)",
        "cta": "→",
        "mecanismo": "Compromisso emocional: digitar o nome do alvo concretiza a busca + nome vira variável personalizada ('compiling report for Alex')",
        "observacoes": "Banner inferior MUDA: '99.6% accuracy rate across Tinder, Bumble, and Hinge' + tríade de disclaimers legais (not affiliated / publicly available / no unauthorized scraping). Combina autoridade quantitativa com cover-up legal — discipline copy pra sobreviver a ad-platform audit."
    },
    3: {
        "tipo": "quiz · entrada (localização)",
        "headline": "Add a location where they might be active",
        "subheadline": "Enter address, city, or landmark (com autocomplete + mapa Google embedado)",
        "cta": "→",
        "mecanismo": "Autocomplete + mapa visual ao vivo = sensação de 'sistema profissional integrado a Google Maps' → eleva percepção técnica e justifica preço futuro",
        "observacoes": "O mapa renderiza a área com pinos reais. Cria a ilusão de geolocalização real do alvo (o sistema não localiza nada de verdade, mas o usuário acredita). Menos perguntas que CheaterCatcher (4 vs 18) = aposta em ticket alto + decisão rápida."
    },
    4: {
        "tipo": "quiz · upload opcional + storytelling técnico",
        "headline": "Facial Recognition to Search — Identify Your Partner",
        "subheadline": "We Learn About Your Partner. Our AI securely stores your partner's photo, name, and location to create a detailed profile for scanning.",
        "cta": "Skip / Next >",
        "mecanismo": "Tela de upload posicionada como STORYTELLING do mecanismo (não só pedido). Marca '[ Optional ]' reduz fricção; 'securely stores' tira objeção de privacidade; subtexto cria sensação de pipeline técnico.",
        "observacoes": "Etapa 4 + 5 são as ÚNICAS telas de persuasão pura — funcionam como mini-VSL textual explicando o produto antes do paywall. CheaterCatcher faz isso com 4 telas emocionais; CheaterScanner faz em 2 telas técnicas."
    },
    5: {
        "tipo": "persuasão · mecanismo único em 1 linha",
        "headline": "Scan the Dating Apps — We Scan the Dating Apps",
        "subheadline": "CheaterScanner swipes through Tinder, Bumble, and Hinge profiles in your partner's area, just like a real user would—only faster and smarter.",
        "cta": "Next >",
        "mecanismo": "Metáfora vívida ('swipes like a real user') + comparativo final ('faster and smarter') = mecanismo único memorável em 1 frase. Disclaimer legal triplicado mantido (not affiliated / publicly available / no unauthorized scraping).",
        "observacoes": "Frase do MU é compacta o suficiente pra virar copy de ad. 'Like a real user' = justificativa técnica E cover legal simultânea. CTA mudou de chevron pra 'Next >' com texto = transição pra autoridade maior antes do email gate."
    },
    6: {
        "tipo": "email gate · pre-paywall",
        "headline": "Enter your email to get the report",
        "subheadline": "Important! Enter a real email address to receive the report. Your data is 100% private. We never share or sell data.",
        "cta": "Get Cheating Report",
        "mecanismo": "Email gate como ENTREGA (não como bloqueio): 'to receive the report' implica que o report virá grátis. Checkbox 'Receive emails' pré-marcado pra opt-in marketing.",
        "observacoes": "'Important!' em azul = micro-priming. 'Real email address' filtra fake (preserva valor da lista). CTA com palavra carregada ('Cheating') = última fricção emocional forçando compromisso com framing antes do paywall. Captura lead = retargeting + abandoned cart."
    },
    7: {
        "tipo": "loading theatrical + social proof wall",
        "headline": "Scanning History — Deep searching billions of public records for {nome}",
        "subheadline": "Public Score: 0 (gauge gamificada) · Background Check Complete (8 itens: Dating Profile Verification ✓ · Tinder Scan ✓ · Bumble Activity ✓ · Hinge ⚠ · Social Media ✓ · Relationship History ✓ · Hidden Accounts ⚠ · Location Cross-Reference ⚠)",
        "cta": "SEE FULL REPORT → (leva para /subscription)",
        "mecanismo": "Loading theatrical com 8 categorias (3 com ⚠ = curiosity gap dirigido). Gauge 'Public Score 0' gamifica o output. Abaixo: 16+ depoimentos verificados de múltiplas geografias (US/UK/CA/AU/DE/IE) + 4.75★/816 reviews. Wall MASSIVO de social proof.",
        "observacoes": "Personagens dos depoimentos cobrem 2 cenários: descoberta de traição (maioria) E confirmação clean (Olivia/Marcus/Chris) → neutraliza ambos os medos antes do paywall. 16 depoimentos é anti-padrão (maioria do nicho usa 3-5) = aposta em conversão por sobrecarga de prova social. 'Billions of public records' = autoridade quantitativa + cobertura legal numa frase só."
    },
    8: {
        "tipo": "paywall · subscription completa",
        "headline": "Upgrade to Uncover the Truth — Loyalty or Lies?",
        "subheadline": "We searched for: Unknown, 25 yr old, Unknown location · Potential matches: 15+ Profiles · Oldest profile creation date: 12-05-2025 · Latest profile creation date: 9 days ago",
        "cta": "SEE FULL REPORT (botão vermelho com '30 day money-back guarantee' embaixo, REPETIDO 4x na página)",
        "mecanismo": "PAYWALL 11/12 ELEMENTOS — escassez (Limited Time Offer 9:50 countdown) + resultado parcial revelado (15+ Profiles + datas específicas) + preview censurado (4 fotos borradas no topo) + preço âncora riscado (R$ 198,32 → R$ 99,16 SAVE 50%) + 3 tiers (1/2/3 Searches com selo 'MOST POPULAR' pré-selecionado no 2º) + garantia 30-day money-back (repetida 5x) + bullet do que vem (timelines, scan apps, 99.6%) + selos (Your info safe / Secure checkout SSL / Need help) + autoridade mídia ('AS SEEN IN TIME') + 5 depoimentos curados (incluindo objeção-handler Michael R) + FAQ de 5 perguntas + e-book bonus 'To Catch a Cheater' + Stripe atrás do botão. SÓ FALTA: 1-click Apple Pay visível (provavelmente no checkout Stripe).",
        "observacoes": "💰 PRICING (R$ porque IP detectou Brasil) — SUBSCRIPTION SAAS com desconto 1º mês: 1 Search R$99,16 · 2 Searches R$165,31 (MOST POPULAR pré-selecionado) · 3 Searches R$192,86. 🔁 RECORRÊNCIA DECLARADA: R$ 195,07 cobrado 1º mês = R$ 165,31 (tier MOST POPULAR pré-selecionado) + 18% tax. Renovação mensal R$ 390,14 = R$ 330,61 (preço cheio sem desconto) + 18% tax. Modelo transparente: desconto SAVE 60% só no 1º mês, depois preço cheio mensal. Disclosure cumpre FB/Google/FTC. 🎁 ORDER BUMP NO PAYWALL: 'FREE E-BOOK INCLUDED: To Catch a Cheater' — bonifica conversão E vende identidade. Disclaimer 'unethical tips section (use at your own risk)' é risco de ad-platform mas funciona como hook identitário. 🔁 Botão SEE FULL REPORT repete 4x na página = quanto mais rola, mais convertido."
    },
}

for e in bundle["etapas"]:
    e["analise"] = analises.get(e["numero"], {
        "tipo": "?", "headline": "(não anotado)", "subheadline": "", "cta": "",
        "mecanismo": "", "observacoes": ""
    })

with open(PATH, "w") as f: json.dump(bundle, f, ensure_ascii=False, indent=2)
print(f"[OK] {len(bundle['etapas'])} etapas enriquecidas")
