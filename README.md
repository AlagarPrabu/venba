# வெண்பா || Venba

Venba is a type or form of the classical tamil poetry. Venba grammer rules and regulations are very structural than the other form of tamil poetry types like "AASIRIYAPPA", "VANJIPPA", "KALIPPA".

Venba rules have been proved to form CFG (Context free Grammer) 

## Prerequisites  
  python should be installed in the system  
  
##### This venba project will helps to find out the error in the literature poem.

**STEP 1:** Type the cheyyul(poem) in the text file and save it.  

**STEP 2:** Open the terminal in the project directory.

**STEP 3:** Type below syntax in the terminal.  

```python
python main.py
```
**STEP 4:** Now type the text file path. (Ex: /home/root/Desktop/test.py)  

**STEP 5:** Type **Y** to proceed.  

Proceed to check (Y/N): Y

**Result**

Now, Termianl will display the text file content and type of venba (Ex: Nerisai Venba).

Incase of error, it will indicate  

Example 1: **ERROR: LINE 1 WORD 3 not following venba asai rule**  - **ASAI_ERROR**

Example 2: **ERROR: LINE 1 WORD 2 not following venba thalai rule** - **THALAI_ERROR**  

Example 3: **ERROR: Venba should have minimum 2 and maximum 12 lines** - **LINE_ERROR**  

Example 4: **ERROR: LINE 4 should have 3 words** - **WORD_ERROR**  

Example 5: **ERROR: LINE 1 should have 4 words** - **WORD_ERROR**
