import re
from typing import Callable
def generator_numbers(text: str):
    pattern = r'\d+\.\d+'
    text_nums = re.findall(pattern, text)
    if text_nums:
        for nums in text_nums:
            yield float(nums)

def sum_profit(text: str, func: Callable[[float], float]):
    generation = generator_numbers(text)
    total = 0
    for i in generation:
        value = func(i)
        total += value
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
nums_in_text = generator_numbers(text)

total_income = sum_profit(text, lambda x: x)
print(f"Загальний дохід: {total_income}")
