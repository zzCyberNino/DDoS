
# Denial of Service (DoS) Attack Tool

## Descrizione

Questo script Python implementa uno strumento per eseguire un attacco Denial of Service (DoS) inviando pacchetti UDP al target specificato. L'attacco consiste nell'invio continuo di pacchetti di dimensioni casuali al target, sovraccaricandone la capacità di risposta.

## Requisiti

- Python 3.x
- Modulo `socket` (preinstallato)
- Modulo `random` (preinstallato)

## Uso

Esegui lo script tramite il terminale fornendo l'indirizzo IP del target e la porta desiderata quando richiesto.

```bash
python dos_attack.py
```

## Avvertenze

1. L'uso improprio di questo strumento può violare leggi locali o internazionali.
2. Utilizza questo strumento solo in ambienti di testing o con il consenso esplicito del proprietario del sistema di destinazione.
3. L'autore non è responsabile per eventuali danni derivanti dall'uso di questo software.

## Nota

Il banner di avvio fornisce un riconoscimento visivo del tool all'avvio dello script.

## Disclaimer

Questo strumento è fornito solo a scopo educativo. L'uso improprio è severamente scoraggiato.

```
8888888b.  8888888b.            .d8888b.  
888  "Y88b 888  "Y88b          d88P  Y88b 
888    888 888    888          Y88b.      
888    888 888    888  .d88b.   "Y888b.   
888    888 888    888 d88""88b     "Y88b. 
888    888 888    888 888  888       "888 
888  .d88P 888  .d88P Y88..88P Y88b  d88P 
8888888P"  8888888P"   "Y88P"   "Y8888P"  
                                          
```

# Output (Esempio)

```
Invitati 1 pacchetti all'indirizzo ip : <IP del Target>
Invitati 2 pacchetti all'indirizzo ip : <IP del Target>
...
```

```

---

**Nota:** Si prega di utilizzare questo script in conformità alle leggi locali e solo a scopo educativo. L'autore non è responsabile per un uso improprio o danni causati dall'uso di questo software.
