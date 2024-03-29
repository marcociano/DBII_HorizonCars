import pandas as pd


def load_and_format_csv(file_path, output_path):
    # Funzione per caricare il file CSV, formattarlo e salvarlo
    def capitalize_first_letter_model(name):
        # Funzione per trasformare il nome dell'auto con il modello con la prima lettera in maiuscolo
        parts = name.split(" ", 1)
        if len(parts) > 1:
            # Converte in maiuscolo la prima lettera della seconda parte (il modello)
            model = parts[1].capitalize()  # Cambia solo la prima lettera del modello in maiuscolo
            return parts[0].capitalize() + " " + model
        else:
            # Se c'è solo una parte, significa che il modello non è specificato, quindi converte solo la prima parte
            return parts[0].capitalize()

    try:
        # Caricamento del file CSV
        df = pd.read_csv(file_path, sep=';')

        # Rimozione degli spazi bianchi in eccesso da tutte le stringhe del DataFrame
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        # Trasformazione del nome dell'auto
        df['CarName'] = df['CarName'].apply(capitalize_first_letter_model)

        # Converto la colonna dei prezzi per rimuovere gli zeri non significativi
        if 'price' in df.columns:
            df['price'] = df['price'].apply(pd.to_numeric, errors='coerce')

        # Salvataggio del DataFrame modificato in un nuovo file CSV, usando la virgola come separatore
        df.to_csv(output_path, index=False, sep=',', float_format='%g')

        return "File salvato con successo: " + output_path
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    input_path = 'CarPrice.csv'
    output_path = 'CarPrice_formatted.csv'
    print(load_and_format_csv(input_path, output_path))
