"""
Mortgage Calculator CI/CD Demo
Automated testing and deployment
"""

class MortgageCalculator:
    def __init__(self, principal, annual_rate, years):
        """
        Инициализация калькулятора ипотеки

        Args:
            principal (float): Сумма кредита
            annual_rate (float): Годовая процентная ставка (%)
            years (int): Срок кредита в годах
        """
        if principal <= 0 or annual_rate < 0 or years <= 0:
            raise ValueError("Все значения должны быть положительными")

        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.monthly_rate = annual_rate / 100 / 12
        self.months = years * 12

    def calculate_monthly_payment(self):
        """Рассчитать ежемесячный платеж по формуле аннуитета"""
        if self.monthly_rate == 0:
            return round(self.principal / self.months, 2)

        rate_factor = (1 + self.monthly_rate) ** self.months
        monthly_payment = self.principal * (self.monthly_rate * rate_factor) / (rate_factor - 1)
        return round(monthly_payment, 2)

    def calculate_total_payment(self):
        """Рассчитать общую сумму выплат за весь срок"""
        monthly = self.calculate_monthly_payment()
        return round(monthly * self.months, 2)

    def calculate_overpayment(self):
        """Рассчитать переплату (проценты)"""
        total = self.calculate_total_payment()
        return round(total - self.principal, 2)

    def get_payment_schedule(self):
        """Вернуть график платежей (упрощенный)"""
        monthly_payment = self.calculate_monthly_payment()
        schedule = []
        balance = self.principal

        for month in range(1, self.months + 1):
            interest_payment = balance * self.monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            schedule.append({
                'month': month,
                'payment': round(monthly_payment, 2),
                'principal': round(principal_payment, 2),
                'interest': round(interest_payment, 2),
                'balance': round(max(balance, 0), 2)  #баланс не может быть отрицательным
            })

        return schedule