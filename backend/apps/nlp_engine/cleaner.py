def clean_cv_text(text):
    unwanted_phrases = [
        "Icônes pour CV à copier-coller",
        "Un modèle Word, c’est bien.",
        "Rendez-vous sur app.modeles-de-cv.com",
        "Générateur de CV en ligne avec IA",
        "Test ATS",
    ]

    cleaned = text
    for phrase in unwanted_phrases:
        cleaned = cleaned.replace(phrase, "")

    return cleaned.strip()