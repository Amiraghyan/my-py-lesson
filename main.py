import ctypes
import os

# Գտնում ենք մեր գրադարանի ճանապարհը
# os.getcwd() -> ստանում է ընթացիկ թղթապանակի ճանապարհը
lib_path = os.path.join(os.getcwd(), "adder.dll")

# 1. Բեռնում ենք C գրադարանը Python-ի հիշողության մեջ
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Չհաջողվեց բեռնել գրադարանը: {e}")
    exit()

# 2. Python-ին բացատրում ենք, թե ինչ տեսք ունի մեր C ֆունկցիան
#    Որպեսզի Python-ը իմանա, թե ինչ տիպի արգումենտներ ուղարկի
#    և ինչ տիպի պատասխան սպասի։
# c_lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]  # Սպասում է 2 հատ C integer
# c_lib.add_numbers.restype = ctypes.c_int  # Վերադարձնում է C integer

# 3. ԿԱՆՉՈՒՄ ԵՆՔ C ՖՈՒՆԿՑԻԱՆ PYTHON-ԻՑ!
result = c_lib.add_numbers(
    1,
    2,
    3,
    4,
    5,
)

print(f"Python-ը կանչեց C ֆունկցիան, արդյունքը՝ {result}")
print(f"Արդյունքի տիպը Python-ում՝ {type(result)}")
