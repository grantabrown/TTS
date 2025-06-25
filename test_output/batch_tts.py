# batch_tts.py
from pathlib import Path
from TTS.api import TTS

# 1. Load model once (GPU=True if you have CUDA)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# 2. Configuration
text      = "Hola, cómo estás? Voy a cocinar un cerdo para la cena y llevar la lluvia porque he acabado con todo esto."
language  = "es"
speakers  = {
    "Claribel Dervla": "claribel_test.wav",
    "Daisy Studious": "daisy_test.wav",
    "Gracie Wise": "gracie_test.wav",
    "Tammie Ema": "tammie_test.wav", 
    "Alison Dietlinde": "alison_test.wav",
    "Ana Florence": "ana_test.wav",
    "Annmarie Nele": "annmarie_test.wav",
    "Asya Anara": "asya_test.wav",
    "Brenda Stern": "brenda_test.wav",
    "Gitta Nikolina": "gitta_test.wav",
    "Henriette Usha": "henriette_test.wav",
    "Sofia Hellen": "sofia_test.wav",
    "Tammy Grit": "tammy_test.wav",
    "Tanja Adelina": "tanja_test.wav",
    "Vjollca Johnnie": "vjollca_test.wav",
    "Andrew Chipper": "andrew_test.wav",
    "Badr Odhiambo": "badr_test.wav",
    "Dionisio Schuyler": "dionisio_test.wav",
    "Royston Min": "royston_test.wav",
    "Viktor Eka": "viktor_test.wav",
    "Abrahan Mack": "abrahan_test.wav",
    "Adde Michal": "adde_test.wav",
    "Baldur Sanjin": "baldur_test.wav",
    "Craig Gutsy": "craig_test.wav",
    "Damien Black": "damien_test.wav",
    "Gilberto Mathias": "gilberto_test.wav",
    "Ilkin Urbano": "ilkin_test.wav",
    "Kazuhiko Atallah": "kazuhiko_test.wav",
    "Ludvig Milivoj": "ludvig_test.wav",
    "Suad Qasim": "suad_test.wav",
    "Torcull Diarmuid": "torcull_test.wav",
    "Viktor Menelaos": "viktor_test.wav",
    "Zacharie Aimilios": "zacharie_test.wav",
    "Nova Hogarth": "nova_test.wav",
    "Maja Ruoho": "maja_test.wav",
    "Uta Obando": "uta_test.wav",
    "Lidiya Szekeres": "lidiya_test.wav",
    "Chandra MacFarland": "chandra_test.wav",
    "Szofi Granger": "szofi_test.wav",
    "Camilla Holmström": "camila_test.wav",
    "Lilya Stainthorpe": "lilya_test.wav",
    "Zofija Kendrick": "zofija_test.wav",
    "Narelle Moon": "narelle_test.wav",
    "Barbora MacLean": "barbora_test.wav",
    "Alexandra Hisakawa": "alexandra_test.wav",
    "Alma María": "alma_test.wav",
    "Rosemary Okafor": "rosemary_test.wav",
    "Ige Behringer": "ige_test.wav",
    "Filip Traverse": "filip_test.wav",
    "Damjan Chapman": "damjan_test.wav",
    "Wulf Carlevaro": "wulf_test.wav",
    "Aaron Dreschner": "aaron_test.wav",
    "Kumar Dahl": "kumar_test.wav",
    "Eugenio Mataracı": "eugenio_test.wav",
    "Ferran Simen": "ferran_test.wav",
    "Xavier Hayasaka": "xavier_test.wav",
    "Luis Moray": "luis_test.wav",
    "Marcos Rudaski": "marcos_test.wav"
}

out_dir = Path("test_output")
out_dir.mkdir(exist_ok=True)

# 3. Synthesis loop
for speaker, filename in speakers.items():
    out_path = out_dir / filename
    print(f"🔊  {speaker}  ➜  {out_path}")
    tts.tts_to_file(
        text=text,
        speaker=speaker,
        language=language,
        file_path=out_path
    )
print("✅  Done!")   