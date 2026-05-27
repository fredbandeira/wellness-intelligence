#!/usr/bin/env python3
import os, json, shutil, re

PORTAL = "/tmp/wellness-intelligence"
TODAY = "2026-05-27"
TODAY_LABEL = "27 de Maio de 2026"

cards = [
  {
    "modal": 1, "size": "c-hero", "bg": "bg-navy", "category": "mercado",
    "tag": "Mercado &middot; Ozempic Pilula FDA Mai 2026 GLP-1 Oral Semaglutida Generico Brasil",
    "tag_js": "Mercado - Ozempic Pilula FDA Aprovado Mai 2026 GLP-1 Oral Semaglutida Generico Brasil",
    "headline": "Ozempic em pilula aprovado pela FDA em 4 de maio de 2026 — semaglutida oral de 1,5mg a 9mg muda o acesso ao GLP-1 nos EUA e acelera chegada do generico ao Brasil; suplementos de apoio ao usuario tornam-se categoria obrigatoria",
    "sub": "Com a aprovacao da pilula de Ozempic em maio de 2026 e o generico de semaglutida chegando ao Brasil ainda este ano, a base de usuarios de GLP-1 pode quintuplicar. O suplemento de apoio nutricional para usuarios de GLP-1 passa de oportunidade a categoria urgente para marcas de wellness em 2026.",
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐⭐",
    "summary_js": "Em 4 de maio de 2026, a FDA aprovou os comprimidos de Ozempic (semaglutida) nas doses de 1,5mg, 4mg e 9mg para adultos com diabetes tipo 2 nos EUA, tornando-o o unico peptideo GLP-1 oral aprovado pela FDA. A Novo Nordisk protocolou pedido de aprovacao para comprimidos de 25mg, com decisao prevista ate o final de 2026. No Brasil, o generico da semaglutida deve chegar ao mercado em 2026 com a expiracao da patente em marco de 2026, democratizando o acesso. O impacto no mercado de suplementos e direto: o usuario de GLP-1 inicia uma dieta hipocalorica involuntaria - come menos, mas sua necessidade de proteinas, fibras, vitaminas e probioticos permanece ou aumenta. GLP Booster, lancado pela NotCo em 2026, e o primeiro suplemento botanico que estimula a producao natural de GLP-1 sem medicamento. Para a Voce Mais+, a oportunidade e precisa: o usuario de GLP-1 e o consumidor mais consciente de saude do mercado e esta altamente receptivo a protocolos de suporte nutricional.",
    "source_js": "Novo Nordisk FDA Aprovacao Ozempic Comprimidos 4 Mai 2026 / PR Newswire Ozempic Pill FDA-Approved Mai 2026 / FoodBiz GLP-1 Suplementos Reinvencao 2026 / Essential Nutrition GLP-1 Support Brasil / BHB Food Novo Suplemento GLP-1 Perda de Peso",
    "curto": "10", "medio": "9", "longo": "8",
    "idea_js": "Linha GLP-1 Support Voce Mais+: protocolo urgente de 4 SKUs para usuarios de Ozempic e similares. (1) Proteina Dense: proteina isolada com leucina extra para preservar massa muscular; (2) Fibra+Sac: psyllium+glucomanano para saciedade e microbioma; (3) MultiDense: multivitaminico de alta potencia para cobrir deficit da dieta restritiva; (4) ProbioGLP: probiotico com cepas especificas para microbioma em dieta hipocalorica. Lancamento via parceria com nutrologos prescritores de Ozempic. Bundle mensal R$280-380."
  },
  {
    "modal": 2, "size": "c-tall", "bg": "bg-yellow", "category": "tendencias",
    "tag": "Tendencias &middot; GLP Booster NotCo Botanico GLP-1 Endogeno Inovacao 2026",
    "tag_js": "Tendencias - GLP Booster NotCo Botanico Natural GLP-1 Endogeno Inovacao 2026",
    "headline": "NotCo lanca GLP Booster em 2026: po botanico que estimula producao natural de GLP-1 e bloqueia enzimas degradadoras — o primeiro suplemento a imitar o mecanismo do Ozempic sem farmaco",
    "sub": None,
    "stat": "GLP Booster",
    "stat_desc": "primeiro suplemento botanico mundial que estimula GLP-1 endogeno e inibe enzimas DPP-4 degradadoras — mantendo o hormonio da saciedade ativo por mais tempo sem prescricao medica.",
    "stars_html": "&#11088;&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐⭐",
    "summary_js": "A NotCo surpreendeu o mercado em 2026 com o lancamento do GLP Booster, um po botanico que pode ser adicionado a qualquer alimento para ajudar a reduzir o apetite. O mecanismo e distinto dos farmacos GLP-1: o GLP Booster estimula a producao natural do hormonio GLP-1 pelo proprio organismo e bloqueia as enzimas DPP-4 que o degradam rapidamente, mantendo os niveis elevados por mais tempo. O produto capitaliza a onda de interesse em torno dos medicamentos GLP-1 para criar uma alternativa natural sem necessidade de prescricao medica. Para o mercado de suplementos, o GLP Booster representa uma categoria inteiramente nova: modulador natural do eixo metabolico GLP-1. A demanda por alternativas botanicas ao Ozempic, chamadas de faux-zempic, cresceu exponencialmente nas redes sociais em 2025-2026.",
    "source_js": "BHB Food Novo Suplemento Estimula GLP-1 Perda de Peso 2026 / NotCo GLP Booster Lancamento 2026 / FoodBiz GLP-1 Suplementos Nutricionais Reinvencao / Naturaltech Impacto GLP-1 Mercado Bem-Estar",
    "curto": "9", "medio": "10", "longo": "9",
    "idea_js": "Linha Faux-Zempic Natural Voce Mais+: desenvolver suplemento botanico de estimulacao de GLP-1 endogeno com ingredientes regulados pela ANVISA. Candidatos com mecanismo comprovado: Berberina (mimetiza acao GLP-1 no metabolismo da glicose), Psyllium (estimula secrecao de GLP-1 via fibra fermentavel), Gengibre (potencializa resposta GLP-1 pos-prandial). Posicionamento: para quem quer os beneficios do GLP-1 sem prescricao. Ticket estimado R$120-180 por mes."
  },
  {
    "modal": 3, "size": "c-wide", "bg": "bg-black", "category": "tendencias",
    "tag": "Tendencias &middot; Menopausa Economia Climatérica USD 33 Tri Terapias Nao-Hormonais",
    "tag_js": "Tendencias - Menopausa Economia Climatérica USD 33 Tri Saude Feminina Terapias Nao-Hormonais 2026",
    "headline": "Economia climatérica: menopausa impulsiona mercado de USD 33 trilhoes — terapias nao-hormonais crescem de USD 4,5bi para USD 6,5bi ate 2030 e suplementos naturais lideram a preferencia da mulher que rejeita TRH",
    "sub": "O mercado de saude feminina na menopausa e avaliado em USD 33 trilhoes globalmente. As mulheres que nao querem ou nao podem fazer terapia de reposicao hormonal estao migrando massivamente para suplementos naturais, fitoterapicos e nutracosmeticos como primeira linha de autocuidado.",
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐⭐",
    "summary_js": "O estudo Data8 avalia o mercado de medicamentos para a menopausa em USD 33 trilhoes globalmente, e as terapias nao-hormonais sao projetadas para crescer de USD 4,5 bilhoes em 2024 para USD 6,5 bilhoes ate 2030 (CAGR de 7,8%). O motor do crescimento: a mulher que nao quer ou nao pode fazer terapia de reposicao hormonal tem limitada oferta medica e busca alternativas naturais eficazes para ondas de calor, disturbios do sono, alteracoes de humor e ressecamento vaginal. EstroG-100 (extrato fitoterápico patenteado) demonstrou melhora significativa de multiplos sintomas da menopausa em estudos clinicos. Vitex agnus-castus, isoflavonas de soja, oleo de primula, magnesio bisglicinato e maca peruana formam o protocolo mais prescrito por nutricionistas especializadas. Retencao media da consumidora que encontra o produto certo para menopausa: 40% superior ao mercado geral.",
    "source_js": "Meio e Mensagem Economia Climatérica Menopausa Mercado 2026 / Marcas e Mercados Suplementos Femininos Explosao 2026 / Ocean Drop Suplementos Menopausa Opcoes / Bonita Mulher Saude Feminina 2026 / CartaCapital Saude Feminina 2026",
    "curto": "9", "medio": "10", "longo": "10",
    "idea_js": "Linha Transicao Climatérica Voce Mais+ - tres SKUs para a mulher na perimenopausa e menopausa: (1) Equilifem Calm: Vitex 400mg + Isoflavonas 80mg + Magnesio Bisglicinato 200mg + B6 50mg; (2) Equilifem Noite: Valeriana 300mg + Magnesio L-Treonato 1g + Triptofano 500mg + Melatonina 0,5mg; (3) Equilifem Pele: Colageno Verisol 2,5g + Hialuronico 150mg + Oleo de Primula 1000mg + Vitamina C. Canal: parceria com ginecologistas e nutrologas."
  },
  {
    "modal": 4, "size": "c-med", "bg": "bg-gray800", "category": "mercado",
    "tag": "Mercado &middot; Adaptogenicos USD 11.3bi 2024 USD 18.8bi 2032 CAGR 6.56%",
    "tag_js": "Mercado - Adaptogenicos USD 11.3bi 2024 USD 18.8bi 2032 CAGR 6.56% Ashwagandha Reishi Cordyceps",
    "headline": "Mercado de adaptogenicos supera USD 11,3 bilhoes em 2024 e cresce a CAGR de 6,56% ate 2032 — ashwagandha, rhodiola, lion mane e reishi lideram; pos adaptogenicos emergem como formato de maior crescimento",
    "sub": "Stress cronico, burnout corporativo e busca por energia sustentavel sem cafeina impulsionam o mercado. O consumidor de adaptogenicos em 2026 nao e mais niche - e o executivo de 40 anos que nao aguenta mais tomar cafe o dia todo.",
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐",
    "summary_js": "O mercado global de adaptogenicos foi avaliado em USD 11,32 bilhoes em 2024 e projeta-se atingir USD 18,82 bilhoes ate 2032, com CAGR de 6,56% (Verified Market Research). Outros relatorios projetam USD 20,3 bilhoes ate 2031. O crescimento e impulsionado pela demanda por solucoes naturais para estresse e saude mental. Ashwagandha lidera em volume de pesquisa. Rhodiola Rosea se consolida como segunda opcao mais procurada. Cogumelos adaptogenicos (Reishi, Cordyceps, Lion Mane) crescem em segmento premium. O formato em po e o de maior crescimento: facilidade de incorporar em cafes e smoothies. O Brasil tem oportunidade unica: especies adaptogenicas brasileiras como Catuaba e Guarana nao foram exploradas no contexto do marketing moderno de adaptogenicos.",
    "source_js": "Verified Market Research Adaptogens Market 2024-2032 / Food Connection Guia Adaptogenicos Industria / GiftedPicks Best Cortisol Stress Supplements 2026 / CoreStacks Rhodiola Rosea Guide 2026 / Napiers Adaptogens Ashwagandha Rhodiola 2026",
    "curto": "8", "medio": "9", "longo": "9",
    "idea_js": "Stack Anti-Stress Corporativo Voce Mais+: produto para o executivo brasileiro sobrecarregado. Formula: Ashwagandha KSM-66 600mg + Rhodiola Rosea 300mg (3% rosavinas) + Eleuthero 400mg + L-Teanina 200mg. Formato em po solúvel para adesao na rotina corporativa. Parceria com programas de beneficios corporativos como canal B2B. Ticket estimado R$90-140 por mes."
  },
  {
    "modal": 5, "size": "c-sm", "bg": "bg-gray100", "category": "ciencia",
    "tag": "Ciencia &middot; Ashwagandha KSM-66 Cortisol -27.9% RCT 60 Dias 2026",
    "tag_js": "Ciencia - Ashwagandha KSM-66 Cortisol -27.9% RCT 60 Dias Placebo-Controlado 2026",
    "headline": "Ashwagandha KSM-66 reduz cortisol serum em 27,9% em 60 dias no maior RCT duplo-cego — revisao 2026 o confirma como adaptogenico de maior robustez cientifica; efeito aparece a partir de 4 semanas",
    "sub": None,
    "stat": "-27,9%",
    "stat_desc": "reducao media de cortisol serico em RCT duplo-cego com 300mg KSM-66 duas vezes ao dia por 60 dias, versus apenas 7,9% no grupo placebo.",
    "stars_html": "&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐",
    "summary_js": "Estudo randomizado duplo-cego placebo-controlado com adultos em estresse cronico usando 300mg de extrato KSM-66 duas vezes ao dia por 60 dias documentou reducao media de 27,9% nos niveis de cortisol serico, frente a apenas 7,9% no grupo placebo. Resultados positivos sobre estresse, ansiedade, depressao e desejo por comida foram observados em escalas validadas. O efeito aparece consistentemente apos 4 semanas de uso continuo. Mecanismo: os vitanolideos da ashwagandha regulam o eixo HPA (hipotalamo-hipofise-adrenal), reduzindo a sensibilidade ao estresse e a producao cronica de cortisol. A revisao de 2026 consolida ashwagandha como o adaptogenico com maior numero de estudos clinicos em humanos e maior consistencia de resultados.",
    "source_js": "Tua Saude Ashwagandha Cortisol Como Usar Abril 2026 / Academia Central Fitness Ashwagandha Guia 2026 / MSD Manuals Ashwagandha 2026 / UNISC Ashwagandha Cortisol Estudo / NIH ODS Ashwagandha Fact Sheet 2026",
    "curto": "8", "medio": "8", "longo": "8",
    "idea_js": "Ashwagandha Premium Voce Mais+ com diferenciacão de forma: posicionar KSM-66 600mg como evidence-based com laudo de pureza certificado. SKU feminino: Ashwagandha + Maca + Oleo de Primula. SKU masculino: Ashwagandha + Tribulus + L-Carnitina. SKU universal com QR code para o estudo original no PubMed, construindo credibilidade cientifica da marca."
  },
  {
    "modal": 6, "size": "c-third", "bg": "bg-navy", "category": "ciencia",
    "tag": "Ciencia &middot; Magnesio Vitamina D Sinergia Sono Melatonina Dependencia Mutua Abril 2026",
    "tag_js": "Ciencia - Magnesio Vitamina D Sinergia Dependencia Mutua Sono Melatonina Abril 2026",
    "headline": "Magnesio e Vitamina D: evidencia de abril 2026 confirma dependencia mutua — sem Mg, a D3 nao e ativada; combinacao melhora sono profundo e producao de melatonina em adultos deficientes",
    "sub": None,
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐",
    "summary_js": "Artigos publicados em abril de 2026 sistematizaram evidencias da dependencia mutua entre magnesio e vitamina D. O magnesio e cofator essencial para ativacao enzimatica da D3 (de 25-OH para 1,25-OH ativa). Sem magnesio adequado, o corpo nao aproveita a D3 suplementada. Em direcao oposta, vitamina D otimiza a absorcao intestinal de magnesio. Sobre sono: a combinacao Mg+D3 atua na regulacao circadiana e producao de melatonina. O magnesio ativa enzimas de sintese de serotonina (precursora da melatonina), enquanto a D3 regula receptores de melatonina no hipotalamo. Para o mercado brasileiro: 40-60% da populacao tem insuficiencia de vitamina D e 70% tem ingestao inadequada de magnesio - duas deficiencias coexistentes com impacto sinergico negativo no sono.",
    "source_js": "Tua Saude Magnesio Vitamina D Dependencia Mutua Abr 2026 / Tua Saude Vitamina D Magnesio Sono Abr 2026 / Unikka Pharma Magnesio Vitamina D Relacao / MedBR Melhores Suplementos Big 5 / Correio Braziliense Beneficios Magnesio",
    "curto": "8", "medio": "8", "longo": "7",
    "idea_js": "Bundle Noturno D3+K2+Mg Voce Mais+: dose unica noturna. Formula: D3 4000UI + K2 (MK-7) 180mcg + Magnesio Bisglicinato 400mg + Zinco Quelado 15mg. 2 capsulas 30 minutos antes de dormir. Racional: a combinacao que ativa cada nutriente com o proximo. Ticket estimado R$75-95 por mes."
  },
  {
    "modal": 7, "size": "c-third", "bg": "bg-gray100", "category": "tendencias",
    "tag": "Tendencias &middot; Sono US$1.5bi Stacks Multi-Ingrediente L-Teanina Passiflora Inverno 2026",
    "tag_js": "Tendencias - Sono Mercado US$1.5bi Stacks Multi-Ingrediente L-Teanina Passiflora Valeriana Inverno 2026",
    "headline": "Mercado de suplementos para sono ultrapassa US$ 1,5 bilhao global — segunda onda pos-melatonina chega: stacks L-teanina + Magnesio + Passiflora + Glicina superam eficacia da melatonina isolada; inverno amplifica demanda",
    "sub": None,
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐",
    "summary_js": "O mercado global de suplementos para sono ultrapassou US$1,5 bilhao em 2023 com crescimento continuo. No Brasil, suplementos para sono ganharam espaco em adultos 25-45 anos com insonia relacionada ao estresse. A segunda onda vai alem da melatonina: nova geracao combina multiplos ingredientes em vias diferentes do ciclo sono-vigilia. Ingredientes: L-Teanina 400mg (relaxamento sem sedacao), Magnesio Bisglicinato 400mg (ativa sistema GABAergico, reduz cortisol noturno), Passiflora 300mg (ansiolytica natural), Glicina 3g (reduz temperatura corporal central), Inositol 500mg (modulacao serotonina noturna). Busca por qualidade do sono cresceu 45% no Brasil em 2025-2026. Com a chegada do inverno brasileiro (junho-agosto), demanda por sono qualidade aumenta sazonalmente 30-40%.",
    "source_js": "Naturaltech Mercado Sono Suplementos Brasil / Fitobrasil Sonol Plus Melatonina L-Teanina Inositol / Selektz Brasil Melhores Melatoninas 2026 / Docmorris Suplementos Sono Natural / Stasis Melhores Suplementos Sono Atletas",
    "curto": "9", "medio": "8", "longo": "7",
    "idea_js": "Sono Profundo Voce Mais+ - stack premium de segunda geracao. Formula: L-Teanina 400mg + Magnesio Bisglicinato 300mg + Passiflora 300mg + Glicina 2g + Inositol 500mg + Melatonina 0,5mg (dose minima). Diferencial: age em cinco vias diferentes simultaneamente. Lancamento estrategico: pre-inverno (inicio junho). Bundle com D3+K2+Mg para protocolo noturno completo."
  },
  {
    "modal": 8, "size": "c-third", "bg": "bg-white", "category": "ciencia",
    "tag": "Ciencia &middot; Psicobioticos Gut-Brain Parkinson Autismo Ansiedade Cepas Especificas 2026",
    "tag_js": "Ciencia - Psicobioticos Gut-Brain Parkinson Autismo Ansiedade Cepas Especificas Microbioterapia 2026",
    "headline": "Psicobioticos testados para Parkinson, autismo e enxaqueca em 2026 — eixo gut-brain entra na clinica com cepas especificas por indicacao; mercado de psicobioticos avaliado em USD 10,5bi",
    "sub": None,
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐",
    "summary_js": "Psicobioticos sao bacterias vivas que conferem beneficios para saude mental via eixo intestino-cerebro. Em 2026, a pesquisa clinica expandiu para novas indicacoes: estudos investigam o papel do microbioma no autismo, na enxaqueca e no Parkinson. Mecanismo: cepas especificas de Lactobacillus e Bifidobacterium produzem neurotransmissores (GABA, serotonina), acidos graxos de cadeia curta e compostos anti-inflamatorios que atuam no eixo intestino-cerebro. O mercado de psicobioticos foi avaliado em USD 10,5 bilhoes em 2026 com CAGR de 15%. Cepas com maior respaldo clinico: Lactobacillus rhamnosus JB-1, Lactobacillus helveticus R0052 e Bifidobacterium longum R0175.",
    "source_js": "UNESP Cartilha Psicobioticos Saude Mental / ESADI Psicobioticos Bacterias Saude Mental / Revista Contemporanea Psicobioticos 2026 / UFRJ LANUTRI Saude Mental Microbiota / Caderno Pedagogico Modulacao Microbiota 2026",
    "curto": "7", "medio": "9", "longo": "10",
    "idea_js": "Psicobiotico Premium Voce Mais+ com cepas clinicamente validadas. Formula: L. helveticus R0052 3bi UFC + B. longum R0175 1bi UFC + Prebiotico FOS 1g. Posicionamento: o probiotico para o cerebro. QR code com link ao estudo RCT no PubMed. Diferencial impossivel de replicar sem acesso as cepas certificadas. Parceria com psicologos e psiquiatras progressistas como canal de indicacao."
  },
  {
    "modal": 9, "size": "c-wide", "bg": "bg-gray100", "category": "ciencia",
    "tag": "Ciencia &middot; NMN NAD+ Pressao Arterial Cardiovascular Estudo Abril 2026",
    "tag_js": "Ciencia - NMN NAD+ Pressao Arterial Cardiovascular Estudo Abril 2026 Anti-Aging Longevidade",
    "headline": "NMN e pressao arterial: pesquisa de abril 2026 documenta reducao significativa da pressao diastolica em repouso — novo beneficio cardiovascular reposiciona o precursor NAD+ de longevidade para saude do coracao",
    "sub": "O NMN era conhecido como precursor do NAD+ com potencial anti-aging. Em abril de 2026, pesquisa documenta reducao da pressao arterial diastolica, especialmente em pessoas acima de 60 anos, abrindo nova indicacao cardiovascular para a categoria de longevidade.",
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐",
    "summary_js": "Pesquisa publicada em abril de 2026 encontrou que o uso de NMN (mononucleotideo de nicotinamida) foi associado a uma reducao modesta porem significativa da pressao arterial diastolica em repouso, com efeito mais relevante na pressao sistolica de pessoas com 60 anos ou mais. Este e um novo beneficio documentado para o NMN, que era estudado principalmente pela longevidade celular via elevacao dos niveis de NAD+ e ativacao das sirtuinas. Mecanismo: o NMN melhora a funcao endotelial via NAD+, o que pode explicar o efeito vasodilatador. Caveat importante: a maioria dos suplementos de NMN do mercado contem quantidade diferente do anunciado - um estudo mostrou que a maioria dos produtos testados nao correspondeu ao declarado, reforcando a importancia de qualidade e certificacao.",
    "source_js": "Tua Saude NMN Anti-Envelhecimento Pressao Arterial Abr 2026 / A Voz do Idoso NAD+ Suplementos Longevidade / Naturecan NMN Suplementos Longevidade / CRN1 Resveratrol Suplementos Anti-Aging Mai 2026",
    "curto": "6", "medio": "8", "longo": "9",
    "idea_js": "NMN Ultra 500 Voce Mais+ com garantia de pureza: certificacao de laboratorio independente (NSF ou Informed Sport). Mostrar o laudo no produto. Formula: NMN 500mg + Resveratrol 150mg + CoQ10 100mg - sinergia de longevidade com suporte cardiovascular. Comunicacao: o suplemento de longevidade que tambem cuida do coracao. Posicionamento para 45-65 anos com historico familiar cardiovascular. Ticket R$180-250 por mes."
  },
  {
    "modal": 10, "size": "c-med", "bg": "bg-navy", "category": "tendencias",
    "tag": "Tendencias &middot; Creatina Saude Universal Cognicao Cardiovascular Mulheres 50+ Big 5 2026",
    "tag_js": "Tendencias - Creatina Saude Universal Cognicao Cardiovascular Mulheres 50+ Big 5 2026",
    "headline": "Creatina ultrapassa o fitness e vira suplemento de saude universal: evidencias em cognicao, cardiovascular e longevidade muscular elevam o ingrediente mais estudado da historia para mulheres e adultos 50+",
    "sub": "A creatina monohidratada tem mais de 1.000 publicacoes cientificas. Em 2026, sai do nicho de academia e entra no protocolo Big 5 de longevidade como suplemento essencial para todas as idades, especialmente mulheres apos os 40 anos.",
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐",
    "summary_js": "Em 2026, a creatina monohidratada consolida-se como o suplemento com maior base de evidencias cientificas - mais de 1.000 estudos confirmando seguranca e eficacia. Novas evidencias apontam para: cognicao (melhora memoria de trabalho e reduz fadiga mental); saude cardiovascular (melhora funcao endotelial e perfil lipidico); preservacao de massa muscular em 50+ (acao anti-sarcopenica documentada); saude ossea. Para mulheres: o deficit de creatina muscular e 20-30% superior ao masculino, o que explica por que a suplementacao gera beneficios mais rapidos. A creatina entra no protocolo Big 5 de 2026: Creatina Monohidratada, Magnesio, Omega-3, D3+K2 e Probiotico. Buscas para creatina feminina cresceram 45% no Brasil em 2025-2026.",
    "source_js": "MedBR Melhores Suplementos Ciencia 2026 Big 5 / Treinomestre Creatina Melhores Marcas 2026 / ProdutosAnalisados Melhor Creatina 2026 / Food Connection Pilares Mercado Suplementos 2026 / Underlabz Mercado Suplementos 2026",
    "curto": "8", "medio": "8", "longo": "9",
    "idea_js": "Creatina Feminina Premium Voce Mais+: reposicionar creatina como suplemento de longevidade para mulheres 35+. Formula: CreaPure 5g + Magnesio Bisglicinato 200mg + D3 1000UI. Comunicacao: creatina nao e so para academia - e para o seu cerebro, coracao e musculos aos 40, 50, 60 anos. Formato em po com sabores clean. Ticket estimado R$80-110 por mes."
  },
  {
    "modal": 11, "size": "c-sm", "bg": "bg-yellow", "category": "mercado",
    "tag": "Mercado &middot; Nutraceuticos +850% Buscas Brasil 2026 DTC Digital Assinatura Canal",
    "tag_js": "Mercado - Nutraceuticos +850% Buscas Brasil 2026 DTC Digital Assinatura Canal Oportunidade",
    "headline": "Nutraceuticos viram febre online no Brasil: buscas cresceram +850% em 2026 — mercado global beira US$1 trilhao; canal DTC e assinatura superam farmacia fisica como ponto de compra para consumidores abaixo de 45 anos",
    "sub": None,
    "stat": "+850%",
    "stat_desc": "crescimento nas buscas por nutraceuticos no Brasil em 2026. Mercado global projetado em US$1 trilhao. DTC e assinaturas sao os modelos de maior margem e retencao.",
    "stars_html": "&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐",
    "summary_js": "Em 2026, os nutraceuticos viraram febre online no Brasil com buscas crescendo +850%. O mercado global de nutraceuticos ja beira US$1 trilhao. O dado estrategico: o DTC (direct-to-consumer) e o e-commerce de assinatura superaram a farmacia fisica como principal ponto de compra para consumidores abaixo de 45 anos. O dropshipping de nutraceuticos expandiu como modelo de entrada, mas a ameaca e real: produtos importados de qualidade questionavel concorrem com marcas nacionais. A resposta correta nao e mais volume ou mais SKUs, mas diferenciais que o dropshipper nao tem: narrativa de origem, evidencia cientifica, personalizacao e confianca de marca. O consumidor digital de nutraceuticos em 2026 pesquisa antes de comprar: compara ingredientes, le reviews e verifica certificacoes antes de converter.",
    "source_js": "Pro Growth Global Nutraceuticos Dropshipping +850% 2026 / Ekobe Tendencias Suplementos 2026 / Hile Suplementos 2026 / Food Connection Mercado Suplementos 2026 / Underlabz Tendencias Suplementos 2026",
    "curto": "7", "medio": "8", "longo": "8",
    "idea_js": "Estrategia DTC Voce Mais+: fortalecer canal proprio como diferencial competitivo. (1) Site com conteudo cientifico por produto; (2) Programa de assinatura com desconto progressivo (10%/15%/20%); (3) Chatbot nutricionista no WhatsApp para protocolo personalizado; (4) Programa de fidelidade com pontos. O dropshipper vende o produto. A Voce Mais+ vende o resultado."
  },
  {
    "modal": 12, "size": "c-third", "bg": "bg-black", "category": "ciencia",
    "tag": "Ciencia &middot; Resveratrol Revisao 2026 Anti-Aging Hype Realidade Biodisponibilidade",
    "tag_js": "Ciencia - Resveratrol Revisao 2026 Anti-Aging Hype Realidade Limitacoes Biodisponibilidade",
    "headline": "Resveratrol em revisao: CRN1 avalia promessas anti-aging em maio 2026 — beneficios em animais nao replicam em humanos com a mesma magnitude; biodisponibilidade oral baixa e a variavel critica ignorada",
    "sub": None,
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐",
    "summary_js": "O CRN1 publicou em maio de 2026 uma avaliacao critica do resveratrol e outros suplementos anti-aging. Conclusao: resveratrol e precursores de NAD+ tem ressalvas importantes sobre eficacia em humanos. Beneficios robustos em modelos animais nao se replicam de forma consistente em humanos com a mesma magnitude. A variavel critica: biodisponibilidade. O resveratrol oral e metabolizado rapidamente no figado antes de atingir tecidos-alvo. Formulacoes liposomais ou com piperina aumentam a absorcao mas sao raramente usadas. Dado positivo: resveratrol combinado com exercicio fisico mostrou beneficios adicionais na funcao endotelial. Conclusao pratica: posicionar como componente de stack de longevidade, nao como solucao isolada.",
    "source_js": "CRN1 Resveratrol Suplementos Anti-Envelhecimento Ciencia Mai 2026 / A Voz do Idoso NAD+ Resveratrol Longevidade / Naturecan Suplementos Longevidade 2026 / FSL Farma Complexo Longevidade NMN / Naturecan NMN Qualidade",
    "curto": "5", "medio": "7", "longo": "8",
    "idea_js": "Posicionamento responsavel de longevidade Voce Mais+: comunicar suplementos de longevidade com linguagem honesta. Em vez de prometer jovialidade eterna, comunicar: suporte ao metabolismo celular, antioxidante de alta potencia. Usar nivel de evidencia como diferencial: CRN1, ABRAN, PubMed visiveis no site. O consumidor de 2026 pesquisa antes de comprar - a marca que nao exagera e percebida como mais confiavel."
  },
  {
    "modal": 13, "size": "c-full", "bg": "bg-gray100", "category": "tendencias",
    "tag": "Analise de Cruzamento &middot; 27 Maio 2026 &middot; Inverno 2026 Janela de Ouro Wellness",
    "tag_js": "Analise de Cruzamento - 27 Maio 2026 - Inverno 2026 Janela de Ouro Wellness GLP-1 Menopausa Sono",
    "headline": "27 Mai: Ozempic pilula FDA + GLP Booster botanico + menopausa USD 33tri + adaptogenicos USD 18.8bi + ashwagandha -27.9% + Mg+D3 sono + sono stacks inverno + psicobioticos Parkinson + NMN pressao + creatina universal + nutraceuticos +850% + resveratrol realidade = INVERNO 2026 E A JANELA DE OURO PARA LANCAMENTOS URGENTES DE WELLNESS",
    "sub": "O tema unificador de 27 de maio e a convergencia perfeita entre sazonalidade e tendencias estruturais: o inverno que se aproxima amplifica cada uma dessas tendencias. Sono, imunidade, energia e equilibrio hormonal sao as prioridades do consumidor entre junho e agosto. A marca que ativar sua estrategia de inverno agora chega ao ponto de venda com antecedencia de 30-45 dias.",
    "stat": None, "stat_desc": None,
    "stars_html": "&#11088;&#11088;&#11088;&#11088;&#11088;",
    "stars_js": "⭐⭐⭐⭐⭐",
    "summary_js": "O tema unificador de 27 de maio e a convergencia entre sazonalidade e tendencias estruturais: o inverno brasileiro (inicio 21 de junho) amplifica cada tendencia monitorada hoje. Sono e mais urgente: dias mais curtos e noites mais frias elevam a demanda por suplementos de sono em 30-40% entre junho e agosto. Vitamina D e critica: no inverno, producao cutanea de D3 cai drasticamente. Adaptogenicos ganham relevancia: estresse acumulado + frio + menor exposicao solar cria terreno para burnout e ansiedade de inverno. GLP-1 continua urgente: com Ozempic em pilula aprovado em maio e generico chegando ao Brasil, cada semana sem o produto de apoio e posicao cedida ao concorrente. Menopausa e perene mas o inverno amplifica os sintomas. As tres janelas de acao imediata: (1) Bundle Inverno Imunidade Sono, lancamento ate 10 de junho; (2) GLP-1 Support, protocolo urgente; (3) Linha Climatérica Feminina, posicionamento antes do concorrente nacional se consolidar.",
    "source_js": "Sintese das 12 tendencias analisadas em 27 de maio de 2026 / Wellness Intelligence Voce Mais+ / FDA Ozempic Pill Approval Mai 2026 / Data8 Menopausa Mercado USD 33tri / Verified Market Research Adaptogenicos 2032 / Tua Saude Mg D3 Sono Abr 2026 / Naturaltech Mercado Sono",
    "curto": "10", "medio": "10", "longo": "10",
    "idea_js": "Plano de Inverno 2026 Voce Mais+ - quatro movimentos prioritarios: (Semana 1-2) Bundle Inverno Imunidade: D3 4000UI+K2+Mg + Probiotico + Vitamina C Lipossomal - campanha lancada antes de 10 de junho. (Semana 2-4) Bundle Sono Profundo: stack L-Teanina+Mg+Passiflora - timing perfeito com noites de inverno. (Semana 3-6) GLP-1 Support: protocolo urgente em parceria com nutrologos. (Semana 6-12) Linha Climatérica Feminina: 3 SKUs - janela de ser a primeira marca nacional consolidada."
  }
]

# Archive existing index as 2026-05-26
shutil.copy(f"{PORTAL}/index.html", f"{PORTAL}/edicoes/2026-05-26.html")

# Read old archive HTML for rich cards
with open(f"{PORTAL}/index.html", "r") as f:
    old_html = f.read()
archive_match = re.search(r'<div class="archive-grid">(.*?)</div>\s*</div>\s*</section>', old_html, re.DOTALL)
if archive_match:
    old_archive_inner = archive_match.group(1).strip()
    new_today_card = '      <a class="archive-card" href="edicoes/2026-05-26.html"><div class="archive-date">26 de Maio de 2026</div><div class="archive-hl">Ozempic pilula GLP-1 + longevidade USD 219bi + ANVISA fitoterapicos + feminino +67% + Lion Mane BDNF + omega-3 deficit + magnesio Big 5 + clean label 3.0 + biohacking DNA + colageno K-beauty + plant-based</div><div class="archive-tags"><span>glp-1</span><span>longevidade</span><span>anvisa</span></div></a>'
    archive_content = new_today_card + "\n" + old_archive_inner
else:
    archive_content = '      <a class="archive-card" href="edicoes/2026-05-26.html"><div class="archive-date">26 de Maio de 2026</div></a>'

def card_html(c):
    accent = '<span class="accent-bar"></span>' if c["modal"] in [1, 2] else ''
    tag_sec = f'<div class="tag"><div class="tag-dot"></div>{c["tag"]}</div>'
    if c.get("stat"):
        inner = f'<div>{accent}{tag_sec}<div class="headline">{c["headline"]}</div><div class="stat-num">{c["stat"]}</div><div class="stat-desc">{c["stat_desc"]}</div></div>'
    elif c.get("sub"):
        inner = f'<div>{accent}{tag_sec}<div class="headline">{c["headline"]}</div><p class="sub">{c["sub"]}</p></div>'
    else:
        inner = f'<div>{accent}{tag_sec}<div class="headline">{c["headline"]}</div></div>'
    return f'    <div class="card {c["size"]} {c["bg"]}" data-modal="{c["modal"]}">\n      {inner}\n      <div class="card-foot"><span class="cta-label">Ler analise completa</span><div class="arrow-btn">&#8594;</div></div>\n    </div>'

grid_html = "\n".join(card_html(c) for c in cards)

def js_str(s):
    s = s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    return f"`{s}`"

modals_entries = []
for c in cards:
    entry = (f"  {c['modal']}: {{\n"
             f"    tag: {js_str(c['tag_js'])},\n"
             f"    headline: {js_str(c['headline'])},\n"
             f"    stars: {js_str(c['stars_js'])},\n"
             f"    summary: {js_str(c['summary_js'])},\n"
             f"    source: {js_str(c['source_js'])},\n"
             f"    curto: `{c['curto']}`, medio: `{c['medio']}`, longo: `{c['longo']}`,\n"
             f"    idea: {js_str(c['idea_js'])}\n"
             f"  }}")
    modals_entries.append(entry)
modals_js = "const MODALS = {\n" + ",\n".join(modals_entries) + "\n};"

TODAY = "2026-05-27"
TODAY_LABEL = "27 de Maio de 2026"
alert_text = "<strong>Ozempic em pilula aprovado pela FDA em 4 de maio de 2026 e generico chega ao Brasil</strong> &mdash; GLP Booster (NotCo) estimula GLP-1 natural sem farmaco; menopausa vale USD 33 trilhoes; INVERNO 2026 amplifica demanda por sono, imunidade e energia sustentavel."

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Wellness Intelligence | voce-mais+</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{ --navy:#00276e;--yellow:#feda14;--black:#1d1d1b;--white:#ffffff;--gray-50:#f7f7f7;--gray-100:#efefef;--gray-200:#e0e0e0;--gray-400:#adadad;--gray-600:#6b6b6b;--gray-800:#2e2e2e;--border:rgba(0,0,0,0.09); }}
    body{{font-family:'Inter',sans-serif;background:var(--white);color:var(--black);-webkit-font-smoothing:antialiased;}}
    header{{background:var(--white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;}}
    .header-inner{{max-width:1280px;margin:0 auto;padding:0 40px;height:64px;display:flex;align-items:center;justify-content:space-between;}}
    .logo-wrap{{display:flex;align-items:center;gap:16px;text-decoration:none;}}
    .logo-img{{height:22px;width:auto;}}
    .logo-divider{{width:1px;height:20px;background:var(--gray-200);}}
    .logo-sub{{font-size:10px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--gray-400);}}
    nav{{display:flex;gap:2px;}}
    nav a{{font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:var(--gray-600);text-decoration:none;padding:6px 14px;border-radius:100px;transition:all .15s;}}
    nav a:hover{{color:var(--navy);background:var(--gray-50);}}
    nav a.active{{color:var(--navy);background:var(--yellow);}}
    .header-date{{font-size:11px;font-weight:500;color:var(--gray-400);}}
    .alert-strip{{background:var(--navy);color:var(--white);padding:11px 40px;display:flex;align-items:center;justify-content:center;gap:20px;}}
    .alert-badge{{font-size:9px;font-weight:800;letter-spacing:0.14em;text-transform:uppercase;background:var(--yellow);color:var(--navy);padding:4px 10px;border-radius:100px;white-space:nowrap;}}
    .alert-text{{font-size:12.5px;opacity:.9;}}
    .alert-text strong{{font-weight:700;}}
    main{{max-width:1280px;margin:0 auto;padding:48px 40px 80px;}}
    .edition-bar{{display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;padding-bottom:20px;border-bottom:1px solid var(--border);}}
    .edition-live{{display:flex;align-items:center;gap:10px;}}
    .live-dot{{width:7px;height:7px;background:var(--navy);border-radius:50%;animation:blink 1.8s infinite;}}
    @keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
    .edition-label{{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--navy);}}
    .edition-meta{{font-size:11px;color:var(--gray-400);}}
    .grid{{display:grid;grid-template-columns:repeat(12,1fr);grid-auto-rows:76px;gap:14px;}}
    .card{{border-radius:14px;padding:26px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:space-between;transition:transform .18s,box-shadow .18s;cursor:pointer;}}
    .card:hover{{transform:translateY(-3px);box-shadow:0 14px 36px rgba(0,0,0,.10);}}
    .c-hero{{grid-column:span 7;grid-row:span 5;}}
    .c-tall{{grid-column:span 5;grid-row:span 5;}}
    .c-wide{{grid-column:span 8;grid-row:span 4;}}
    .c-med{{grid-column:span 4;grid-row:span 4;}}
    .c-sm{{grid-column:span 4;grid-row:span 4;}}
    .c-third{{grid-column:span 4;grid-row:span 3;}}
    .c-full{{grid-column:span 12;grid-row:span 3;}}
    .bg-navy{{background:var(--navy);color:var(--white);}}
    .bg-yellow{{background:var(--yellow);color:var(--navy);}}
    .bg-black{{background:var(--black);color:var(--white);}}
    .bg-gray800{{background:var(--gray-800);color:var(--white);}}
    .bg-gray100{{background:var(--gray-100);color:var(--black);}}
    .bg-white{{background:var(--white);color:var(--black);border:1px solid var(--border);}}
    .tag{{display:inline-flex;align-items:center;gap:5px;font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:4px 10px;border-radius:100px;width:fit-content;}}
    .bg-navy .tag,.bg-black .tag,.bg-gray800 .tag{{background:rgba(255,255,255,.15);color:var(--white);}}
    .bg-yellow .tag{{background:rgba(0,39,110,.12);color:var(--navy);}}
    .bg-gray100 .tag,.bg-white .tag{{background:var(--navy);color:var(--white);}}
    .tag-dot{{width:4px;height:4px;border-radius:50%;background:currentColor;opacity:.6;}}
    .headline{{font-size:clamp(15px,2vw,24px);font-weight:800;line-height:1.15;letter-spacing:-.025em;margin-top:10px;}}
    .c-hero .headline{{font-size:clamp(22px,2.8vw,36px);}}
    .c-full .headline{{font-size:clamp(16px,2vw,26px);max-width:900px;}}
    .sub{{font-size:12px;line-height:1.55;margin-top:8px;opacity:.72;}}
    .stat-num{{font-size:clamp(36px,5vw,60px);font-weight:900;letter-spacing:-.04em;line-height:1;margin:10px 0 4px;}}
    .stat-desc{{font-size:11px;font-weight:500;line-height:1.45;opacity:.70;}}
    .card-foot{{display:flex;align-items:center;justify-content:space-between;margin-top:14px;}}
    .cta-label{{font-size:9.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;opacity:.50;}}
    .arrow-btn{{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;}}
    .bg-navy .arrow-btn,.bg-black .arrow-btn,.bg-gray800 .arrow-btn{{background:rgba(255,255,255,.15);}}
    .bg-yellow .arrow-btn{{background:rgba(0,39,110,.12);}}
    .bg-gray100 .arrow-btn,.bg-white .arrow-btn{{background:var(--navy);color:var(--white);}}
    .accent-bar{{display:block;width:28px;height:3px;background:var(--yellow);border-radius:2px;margin-bottom:12px;}}
    .bg-yellow .accent-bar{{background:var(--navy);}}
    .modal-overlay{{position:fixed;inset:0;z-index:500;background:rgba(0,20,55,.55);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;padding:24px;opacity:0;pointer-events:none;transition:opacity .22s;}}
    .modal-overlay.open{{opacity:1;pointer-events:all;}}
    .modal{{background:var(--white);border-radius:20px;width:100%;max-width:640px;max-height:88vh;overflow-y:auto;box-shadow:0 32px 80px rgba(0,0,0,.22);transform:translateY(20px);transition:transform .25s;position:relative;}}
    .modal-overlay.open .modal{{transform:translateY(0);}}
    .modal-header{{background:var(--navy);border-radius:20px 20px 0 0;padding:28px 32px 24px;position:relative;}}
    .modal-tag{{display:inline-flex;align-items:center;gap:5px;font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:4px 10px;border-radius:100px;background:rgba(255,255,255,.15);color:var(--white);margin-bottom:12px;}}
    .modal-headline{{font-size:22px;font-weight:800;line-height:1.2;letter-spacing:-.02em;color:var(--white);}}
    .modal-stars{{font-size:16px;margin-top:8px;}}
    .modal-close{{position:absolute;top:20px;right:20px;width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.15);border:none;color:var(--white);font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .15s;}}
    .modal-close:hover{{background:rgba(255,255,255,.28);}}
    .modal-body{{padding:28px 32px 32px;}}
    .modal-section{{margin-bottom:24px;}}
    .modal-section-title{{font-size:9px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--gray-400);margin-bottom:10px;}}
    .modal-summary{{font-size:14px;line-height:1.7;color:var(--black);}}
    .modal-source{{font-size:11px;color:var(--gray-600);font-style:italic;margin-top:6px;}}
    .scores{{display:flex;gap:12px;margin-top:14px;}}
    .score-box{{flex:1;background:var(--gray-50);border-radius:10px;padding:12px;text-align:center;}}
    .score-label{{font-size:8.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gray-400);display:block;margin-bottom:4px;}}
    .score-val{{font-size:22px;font-weight:900;color:var(--navy);}}
    .idea-box{{background:var(--navy);border-radius:12px;padding:18px 20px;color:var(--white);}}
    .idea-label{{font-size:8.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--yellow);display:block;margin-bottom:8px;}}
    .idea-text{{font-size:13px;line-height:1.65;opacity:.9;}}
    .archive{{background:var(--gray-50);border-top:1px solid var(--border);padding:56px 40px;}}
    .archive-inner{{max-width:1280px;margin:0 auto;}}
    .archive-hd{{display:flex;align-items:center;gap:16px;margin-bottom:28px;}}
    .archive-title{{font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--gray-400);white-space:nowrap;}}
    .archive-line{{flex:1;height:1px;background:var(--border);}}
    .archive-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;}}
    .archive-card{{display:block;text-decoration:none;color:var(--black);background:var(--white);padding:18px 20px;border-radius:10px;border:1px solid var(--border);transition:all .15s;}}
    .archive-card:hover{{border-color:var(--navy);box-shadow:0 4px 16px rgba(0,39,110,.09);transform:translateY(-2px);}}
    .archive-date{{font-size:9px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--white);background:var(--navy);display:inline-block;padding:3px 8px;border-radius:4px;margin-bottom:9px;}}
    .archive-hl{{font-size:12px;font-weight:600;line-height:1.4;margin-bottom:9px;}}
    .archive-tags{{display:flex;flex-wrap:wrap;gap:4px;}}
    .archive-tags span{{font-size:8.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:3px 7px;border-radius:100px;background:var(--gray-100);color:var(--gray-600);}}
    footer{{background:var(--navy);padding:28px 40px;}}
    .footer-inner{{max-width:1280px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;}}
    .footer-brand{{display:flex;align-items:center;gap:14px;}}
    .footer-sep{{width:1px;height:16px;background:rgba(255,255,255,.2);}}
    .footer-tagline{{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.4);}}
    .footer-note{{font-size:10px;opacity:.3;color:var(--white);}}
    @media(max-width:768px){{
      .header-inner{{padding:0 20px;}}.alert-strip{{flex-direction:column;gap:6px;padding:12px 20px;text-align:center;}}
      main{{padding:32px 16px 60px;}}.grid{{grid-template-columns:1fr;grid-auto-rows:auto;}}
      .c-hero,.c-tall,.c-wide,.c-med,.c-sm,.c-third,.c-full{{grid-column:span 1;grid-row:span 1;min-height:180px;}}
      .archive{{padding:40px 16px;}}.footer-inner{{flex-direction:column;gap:10px;text-align:center;}}
      .modal-body{{padding:20px 20px 24px;}}.modal-header{{padding:22px 22px 18px;}}
    }}
  </style>
</head>
<body>
<div class="modal-overlay" id="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-tag" id="m-tag"></div>
      <div class="modal-headline" id="m-headline"></div>
      <div class="modal-stars" id="m-stars"></div>
      <button class="modal-close" id="modal-close">&#10005;</button>
    </div>
    <div class="modal-body">
      <div class="modal-section">
        <div class="modal-section-title">Analise Completa</div>
        <div class="modal-summary" id="m-summary"></div>
        <div class="modal-source" id="m-source"></div>
      </div>
      <div class="scores">
        <div class="score-box"><span class="score-label">Curto Prazo</span><span class="score-val" id="m-curto"></span></div>
        <div class="score-box"><span class="score-label">Medio Prazo</span><span class="score-val" id="m-medio"></span></div>
        <div class="score-box"><span class="score-label">Longo Prazo</span><span class="score-val" id="m-longo"></span></div>
      </div>
      <div class="idea-box" style="margin-top:20px;">
        <span class="idea-label">Ideia para Voce Mais+</span>
        <div class="idea-text" id="m-idea"></div>
      </div>
    </div>
  </div>
</div>
<header>
  <div class="header-inner">
    <a class="logo-wrap" href="#"><img src="logo-positiva.png" alt="voce-mais+" class="logo-img" /><div class="logo-divider"></div><span class="logo-sub">Wellness Intelligence</span></a>
    <nav><a href="#" class="active">Hoje</a><a href="#" onclick="document.querySelector('.archive').scrollIntoView({{behavior:'smooth'}});return false;">Arquivo</a></nav>
    <span class="header-date">{TODAY_LABEL}</span>
  </div>
</header>
<div class="alert-strip">
  <span class="alert-badge">Urgente &middot; Hoje</span>
  <span class="alert-text">{alert_text}</span>
</div>
<main>
  <div class="edition-bar">
    <div class="edition-live"><div class="live-dot"></div><span class="edition-label">Edicao de hoje &mdash; {TODAY_LABEL}</span></div>
    <span class="edition-meta">13 tendencias analisadas &middot; Wellness Intelligence Voce Mais+</span>
  </div>
  <div class="grid">
{grid_html}
  </div>
</main>
<section class="archive">
  <div class="archive-inner">
    <div class="archive-hd"><div class="archive-title">Edicoes Anteriores</div><div class="archive-line"></div></div>
    <div class="archive-grid">
{archive_content}
    </div>
  </div>
</section>
<footer>
  <div class="footer-inner">
    <div class="footer-brand"><img src="logo-branca.png" alt="voce-mais+" style="height:20px;width:auto;" /><div class="footer-sep"></div><span class="footer-tagline">Wellness Intelligence</span></div>
    <span class="footer-note">Gerado automaticamente &middot; {TODAY_LABEL}</span>
  </div>
</footer>
<script>
{modals_js}
document.querySelectorAll('.card[data-modal]').forEach(card => {{
  card.addEventListener('click', () => {{
    const id = card.getAttribute('data-modal');
    const d = MODALS[id];
    if (!d) return;
    document.getElementById('m-tag').textContent = d.tag;
    document.getElementById('m-headline').textContent = d.headline;
    document.getElementById('m-stars').textContent = d.stars;
    document.getElementById('m-summary').textContent = d.summary;
    document.getElementById('m-source').textContent = 'Fonte: ' + d.source;
    document.getElementById('m-curto').textContent = d.curto + '/10';
    document.getElementById('m-medio').textContent = d.medio + '/10';
    document.getElementById('m-longo').textContent = d.longo + '/10';
    document.getElementById('m-idea').textContent = d.idea;
    document.getElementById('modal-overlay').classList.add('open');
  }});
}});
document.getElementById('modal-close').addEventListener('click', () => {{
  document.getElementById('modal-overlay').classList.remove('open');
}});
document.getElementById('modal-overlay').addEventListener('click', (e) => {{
  if (e.target === document.getElementById('modal-overlay')) {{
    document.getElementById('modal-overlay').classList.remove('open');
  }}
}});
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') document.getElementById('modal-overlay').classList.remove('open');
}});
</script>
</body>
</html>"""

with open(f"{PORTAL}/index.html", "w") as f:
    f.write(html)
print(f"index.html written: {len(html)} chars")

# UPDATE data.json
with open(f"{PORTAL}/data.json", "r") as f:
    data = json.load(f)

cat_map = {1:"mercado",2:"tendencias",3:"tendencias",4:"mercado",5:"ciencia",6:"ciencia",7:"tendencias",8:"ciencia",9:"ciencia",10:"tendencias",11:"mercado",12:"ciencia"}
new_ed = {"date": TODAY, "dateLabel": TODAY_LABEL, "cards": []}
for c in cards:
    if c["modal"] == 13:
        continue
    new_ed["cards"].append({
        "category": cat_map.get(c["modal"], "tendencias"),
        "tag": c["tag_js"],
        "stars": c["stars_js"],
        "headline": c["headline"],
        "summary": c["summary_js"],
        "source": c["source_js"],
        "curto": c["curto"], "medio": c["medio"], "longo": c["longo"],
        "idea": c["idea_js"]
    })
data["editions"].insert(0, new_ed)
with open(f"{PORTAL}/data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"data.json updated: {len(data['editions'])} editions")
print("ALL DONE")
