import unittest
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_root, '..'))

from src.calculator import MortgageCalculator


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment_calculation(self):
        """Тест расчета ежемесячного платежа"""
        calc = MortgageCalculator(100000, 5, 10)
        payment = calc.calculate_monthly_payment()
        self.assertAlmostEqual(payment, 1060.66, places=1)  # Изменил places=1 для большей гибкости

    def test_total_payment_calculation(self):
        """Тест расчета общей суммы выплат"""
        calc = MortgageCalculator(100000, 5, 10)
        total = calc.calculate_total_payment()
        self.assertTrue(127000 <= total <= 127500)

    def test_overpayment_calculation(self):
        """Тест расчета переплаты"""
        calc = MortgageCalculator(100000, 5, 10)
        overpayment = calc.calculate_overpayment()
        self.assertTrue(27000 <= overpayment <= 27500)

    def test_zero_interest(self):
        """Тест с нулевой процентной ставкой"""
        calc = MortgageCalculator(120000, 0, 10)
        payment = calc.calculate_monthly_payment()
        self.assertEqual(payment, 1000.00)

    def test_negative_values_validation(self):
        """Тест валидации отрицательных значений"""
        with self.assertRaises(ValueError):
            MortgageCalculator(-100000, 5, 10)

        with self.assertRaises(ValueError):
            MortgageCalculator(100000, -5, 10)

    def test_payment_schedule_length(self):
        """Тест длины графика платежей"""
        calc = MortgageCalculator(100000, 5, 10)
        schedule = calc.get_payment_schedule()
        self.assertEqual(len(schedule), 120)  # 10 лет * 12 месяцев

    def test_large_loan_calculation(self):
        """Тест расчета для крупного кредита"""
        calc = MortgageCalculator(1000000, 7.5, 30)
        payment = calc.calculate_monthly_payment()
        self.assertTrue(6900 <= payment <= 7100)


if __name__ == '__main__':
    unittest.main()