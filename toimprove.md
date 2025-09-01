# **TO FIX:**
1. faulty handling of Qri and Ktiv- now the source text includes ktiv followed by qri rendering results around those words probably wrong. The Qri is specially tagged in Mechon-Mamre's html, but unmarked when the rendered page is copied and pasted. The fix could either erase every instance of ktiv (or Qri). For the scope of Roshei Tevot, in many cases, the first letter of the Qri and Ktiv is the same. For cases where it is not the same, Perhaps Ideally, (but harder to program,) we would test both versions for a match and record if the match is according to the Qri or Ktiv.

# **TO IMPROVE:**
1. 

# **POSSIBLE EXPANSIONS OF THIS PROJECT**
1. option for user typing w/out hebrew keyboard
2. option of searching entire tanach, or select books of tanach.
    -- given current last-3-letter test to find book name, the following ambiguities result:
        מלכים א/ב ודברי הימים א/ב.
        מיכה ואיכה.
        ישעיהו וירמיהו.
        דברים ושיר השירים.
    -- adopt MM 'full' spelling of Yehoshua to avoid its ambiguity with Hoshea
    -- Ezra/Nechemia needs special handling
3. option for user to alter searched file/filepath.
4. search for RT out of order ?optionally?.
5. search for other remazim - consecutive letters in or out of sequence, sofei tevot...
6. test compatibilty with other command line programs other than cmd.exe