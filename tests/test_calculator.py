import sys
import os
from unittest.mock import MagicMock

# Додаємо шлях до src директорії
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Створюємо повний мок для tkinter
mock_tk = MagicMock()
mock_tk.Tk = MagicMock()
mock_tk.Entry = MagicMock()
mock_tk.StringVar = MagicMock()
mock_tk.Button = MagicMock()

# Мокаємо всі можливі імпорти tkinter
sys.modules['tkinter'] = mock_tk
sys.modules['tkinter.Tk'] = mock_tk
sys.modules['tkinter.Entry'] = mock_tk
sys.modules['tkinter.StringVar'] = mock_tk
sys.modules['tkinter.Button'] = mock_tk.Button

# Імпортуємо Calculator
from src.Tkinter_Calculator import button_equal, button_click, button_clear_all

# Тести для математичних операцій
def test_addition():
    button_clear_all()
    button_click('2')
    button_click('+')
    button_click('2')
    result = button_equal()
    assert result == '4'

def test_subtraction():
    button_clear_all()
    button_click('5')
    button_click('-')
    button_click('3')
    result = button_equal()
    assert result == '2'

def test_multiplication():
    button_clear_all()
    button_click('6')
    button_click('*')
    button_click('8')
    result = button_equal()
    assert result == '48'

def test_division():
    button_clear_all()
    button_click('15')
    button_click('/')
    button_click('3')
    result = button_equal()
    assert result == '5.0'

def test_division_by_zero():
    button_clear_all()
    button_click('10')
    button_click('/')
    button_click('0')
    result = button_equal()
    assert result == 'Error'

def test_decimal_operation():
    button_clear_all()
    button_click('2.5')
    button_click('+')
    button_click('2.5')
    result = button_equal()
    assert result == '5.0'

def test_clear():
    button_clear_all()
    button_click('123')
    button_clear_all()
    result = button_equal()
    assert result == ''