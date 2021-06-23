# வெண்பா || Venba

Venba is a type or form of the classical tamil poetry. Venba grammer rules and regulations are very structural than the other form of tamil poetry types like "AASIRIYAPPA", "VANJIPPA", "KALIPPA".

This project will helps to find the error also give the type of venba of the poetry belongs too.  

## Prerequisites  
  python should be installed in the system  
  
## Usage
**STEP 1:** Download the source file and extract.  

**STEP 2:** Change the path to src directory.

**STEP 3:** Type the cheyyul(poem) in the text file and save it.  

**STEP 4:** Open the terminal in the project directory.

**STEP 5:** Type below syntax in the terminal.  

```python
python main.py
```
**STEP 6:** Now type the text file path. (Ex: /home/root/Desktop/test.py)  

**STEP 7:** Type **Y** to proceed.  

Proceed to check (Y/N): Y

**Result**

Now, Termianl will display the text file content and type of venba (Ex: Nerisai Venba).

Incase of error, it will indicate  

Example 1: **ERROR: LINE 1 WORD 3 not following venba asai rule**  - **ASAI_ERROR**

Example 2: **ERROR: LINE 1 WORD 2 not following venba thalai rule** - **THALAI_ERROR**  

Example 3: **ERROR: Venba should have minimum 2 and maximum 12 lines** - **LINE_ERROR**  

Example 4: **ERROR: LINE 4 should have 3 words** - **WORD_ERROR**  

Example 5: **ERROR: LINE 1 should have 4 words** - **WORD_ERROR**
