import pyperclip

def list_sorter(listOfMACs, delimiter):
    results = []
    print(f"List Detected: '{listOfMACs}'")
    print(f"Delimiter detected: '{delimiter}'")
    print("Processing List...")
    listOfMACs = listOfMACs.strip()
    listOfMACs = listOfMACs.split(delimiter)
    mac: str
    for mac in listOfMACs:
        mac = mac.strip()
        if not mac:
            continue
        processedMAC = processor(mac)
        uppercaseMAC = processedMAC.upper()
        results.append(uppercaseMAC)
    if delimiter == ",":
        joiner = delimiter + ' '
        joined = joiner.join(results)
    else:
        joined = delimiter.join(results)
    print(f"New List Created: {joined}")
    pyperclip.copy(joined)
    return results

def processor(mac_address):
    if ':' in mac_address:
        processedMAC = colon_stripper(mac_address)
        return processedMAC

    else:
        if len(mac_address) % 2 == 0:
            processedMAC = coloner(mac_address)
            return processedMAC
        else:
            print("Please try again. An even number of characters is required.")
            return None

def colon_stripper(mac_address):
    target_stripped = mac_address.replace(":", "")
    processedMAC = target_stripped
    return processedMAC

def coloner(mac_address):
    target_coloned = ':'.join(mac_address[char:char+2] for char in range(0, len(mac_address), 2))
    processedMAC = target_coloned
    return processedMAC


while True:
    print("Please copy the MAC addresses you'd like processed to system clipboard.")
    input("Press <Enter> key to process clipboard (or 'Ctrl+C' to quit): ")
    # Detect & Capture what is in clipboard
    target = pyperclip.paste()
    # Search for List Delimiters & send to sorter for list formatting
    elif '\n' in target:
        list_sorter(target, delimiter='\n')
    elif ',' in target:
        list_sorter(target, delimiter=',')
    elif ' ' in target:
        list_sorter(target, delimiter=' ')
    # Process Individual MAC addresses
    else:
        processedMAC = processor(target)
        print(f"{processedMAC} added to user clipboard.")
        pyperclip.copy(processedMAC)
