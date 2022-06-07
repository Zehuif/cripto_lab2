import random

def unicode(largo):
    clave = ""
    for i in range(largo):
        clave += chr(random.randint(0, 1114111))
    return clave

def subScript(largo):
    chars = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₊", "₋", "₌", "₍", "₎", "ₐ", "ₑ", "ₒ", "ₓ", "ₔ", "ₕ", "ₖ", "ₗ", "ₘ", "ₙ", "ₚ", "ₛ", "ₜ", "₝", "₞", "₟", "₠", "₡", "₢", "₣", "₤", "₥", "₦", "₧", "₨", "₩", "₪", "₫", "₭", "₮", "₯", "₰", "₱", "₲", "₳", "₴", "₵", "₶", "₷", "₸", "₹", "₺", "₻", "₼", "₽", "₾", "₿", "⃀", "⃁", "⃂", "⃃", "⃄", "⃅", "⃆", "⃇", "⃈", "⃉", "⃊", "⃋", "⃌", "⃍", "⃎", "⃏", "⃐", "⃑", "⃒", "⃓", "⃔", "⃕", "⃖", "⃗", "⃘", "⃙", "⃚", "⃛", "⃜", "⃝", "⃞", "⃟", "⃠", "⃡", "⃢", "⃣", "⃤"]
    clave = ""
    for i in range(largo):
        clave += random.choice(chars)
    return clave

def superScript(largo):
    chars = ["⁰", "ⁱ", "⁲", "⁳", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "⁺", "⁻", "⁼", "⁽", "⁾", "ⁿ", "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₊", "₋", "₌", "₍", "₎", "ₐ", "ₑ", "ₒ", "ₓ", "ₔ", "ₕ", "ₖ", "ₗ", "ₘ", "ₙ", "ₚ", "ₛ", "ₜ", "₝", "₞", "₟", "₠", "₡", "₢", "₣", "₤", "₥", "₦", "₧", "₨", "₩", "₪", "₫", "₭", "₮", "₯", "₰", "₱", "₲", "₳", "₴", "₵", "₶", "₷", "₸", "₹", "₺", "₻", "₼", "₽", "₾", "₿", "⃀", "⃁", "⃂", "⃃", "⃄", "⃅", "⃆", "⃇", "⃈", "⃉", "⃊", "⃋", "⃌", "⃍", "⃎", "⃏", "⃐", "⃑", "⃒", "⃓", "⃔", "⃕", "⃖", "⃗"]
    clave = ""
    for i in range(largo):
        clave += random.choice(chars)
    return clave

def emoji(largo):
    chars = ["😁", "😂", "😵", "😶", "😷", "😸", "🚎", "🚏", "🚐", "🚑", "🚒", "🚓", "🚔", "🙌","😹", "😺", "😃", "😄", "😅", "😆", "😎", "😍", "😘", "😚", "😋", "😛", "😜", "😝", "😒", "😓", "😔", "😖", "😘", "😽", "😾", "😿", "🙀", "🙅", "🙆", "🙇", "🙈", "🙉", "🙊", "🙋", "🚄", "🚅", "🚆", "🚇", "😜", "😝", "😞", "😟", "😠", "😡", "😢", "😣", "😤", "😥", "😦", "😧", "😨", "😩", "😪", "😫", "😬", "😭", "😮", "😯", "😰", "😱", "😲", "😳", "😴", "😻", "😼", "🚉", "🚊", "🚋", "🚌", "🚍", "🙍", "🙎", "🙏", "🚀", "🚗", "🚘", "🚙", "🚚", "🚛", "🚜", "🚣", "🚤", "🚝", "🚞", "🚟", "🚠", "🚡", "🚢"]
    clave = ""
    for i in range(largo):
        clave += random.choice(chars)
    return clave

def ASCII256(largo):
    clave = ""
    for i in range(largo):
        clave += chr(random.randint(0,255))
    return clave

def base26(largo):
    chars = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    clave = ""
    for i in range(largo):
        clave += random.choice(chars)
    return clave  

def alfabetos(largo):
    chars = ["@","Q","e","i","m","n","«","Έ","Ω","γ","ι","ν","؛","ء","ؤ","ئ","ع","ف","ك","ٌ","َ","ஊ","ன","ௌ","ഃ","ഉ","ഌ","ഏ","ഒ","ച","ാ","ඍ","ඕ","ඛ","ච","ඣ","හ","ේ","ག","ཏ","ན","མ","ཝ","ཾ","ྜ","ྤ","ྵ","መ","ሜ","ሲ","ቀ","ቅ","ቊ","ት","ቺ","ኚ","ኝ","ከ","ኴ","ኻ","ው","ዬ","ዳ","ጕ","ጥ","ጧ","ጨ","ጱ","ឃ","ធ","ឬ","ឱ","ើ","ែ","Ἅ","ἡ","Ἡ","ἰ","ﭻ","ﯩ","ﺚ","ﺢ","ﺤ","ﺨ","ﺲ","ﺵ","ﻀ","ﻄ","ﻆ","ﻈ","ﻙ","ﻢ","ﻦ"]
    clave = ""
    for i in range(largo):
        clave += random.choice(chars)
    return clave

print(unicode(20))
print(subScript(20))
print(superScript(20))
print(emoji(20))
print(ASCII256(20))
print(base26(20))
print(alfabetos(20))
