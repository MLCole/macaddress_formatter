# MAC Address Normalizer & List Formatter
> A clipboard-driven tool for standardizing MAC address formats.

This script processes single MAC addresses or lists of MAC addresses, normalizes them into a consistent uppercase format, and copies a clean, paste-ready result back to your system clipboard.

It is designed around a simple workflow:
  #️⃣ Copy text ➡️ Press Enter ➡️ Get a cleaned list on your clipboard ➡️ Paste cleaned data

This solves the common problem where multi-line input gets truncated by the terminal `input()`.
By reading exclusively from the clipboard, the script processes lists reliably every time.

✨ Features
  ✔️ Reads entire lists directly from clipboard (multi-line, comma-separated, or space-separated)
  
  ✔️ Detects list delimiters automatically
  
  ✔️ Normalizes MACs by:
  
      - Removing colons 
      
          OR
          
      - Adding colons every two characters
      
  ✔️ Converts all output to uppercase
  
  ✔️ Copies final result to clipboard in one operation
  
  ✔️ Handles malformed or empty entries safely
  
  ✔️ Runs continuously until you press Ctrl+C
  

# ▶️ How to Use
1. Copy one of the following to your clipboard:
   
  - A single MAC
  
  - A newline-separated list
  
  - A comma-separated list
  
  - A space-separated list

2. Return to the script window.

3. Press Enter to process the clipboard contents.

4. Paste the cleaned output wherever you need it.

The script repeats this loop indefinitely, allowing multiple sets to be processed quickly.

# ❌ Invalid Input Handling

If a MAC without colons has an odd number of characters:

  `abc1234`
  
  The script prints:
  
    `Please try again. An even number of characters is required.`
  
  And clipboard output is not overwritten.

# 🛠 Requirements
Install pyperclip:

  `pip install pyperclip`

Run the script:

  `python mac_formatter.py`
