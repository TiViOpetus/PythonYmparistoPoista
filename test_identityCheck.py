# YKSIKKÖTESTIT MODUULILLE identityCheck.py

import identityCheck

# Viiden numeron opiskelijanumero on oikein
def test_opiskelijanumeroOk_5():
    assert identityCheck.opiskelijanumeroOk('12345') == True

# Kuuden numeron opiskelijanumero on oikein
def test_opiskelijanumeroOk_6():
    assert identityCheck.opiskelijanumeroOk('123456') == True

# Neljä numeroa -> väärin
def test_opiskelijanumeroOk_4():
    assert identityCheck.opiskelijanumeroOk('1234') == False

# Seitsemän numeroa  -> väärin
def test_opiskelijanumeroOk_7():
    assert identityCheck.opiskelijanumeroOk('1234567') == False

# Joukossa kirjain -> väärin
def test_opiskelijanumeroOk_kirjain():
    assert identityCheck.opiskelijanumeroOk('12A45') == False

# Joukossa desimaalipiste
def test_opiskelijanumeroOk_desimaali1():
    assert identityCheck.opiskelijanumeroOk('12.45') == False

# Joukossa desimaalipilkku
def test_opiskelijanumeroOk_desimaali2():
    assert identityCheck.opiskelijanumeroOk('12,45') == False