from datetime import date, timedelta

RENTAL_PERIOD_DAYS = 7


class Rental:
    def __init__(self, id, equipment_id, renter_id, due_date, rental_date=None, return_date=None):
        self.id = id
        self.equipment_id = equipment_id
        self.renter_id = renter_id
        self.rental_date = rental_date or date.today()
        self.due_date = due_date
        self.return_date = return_date

    def to_dict(self):
        return {
            "id": self.id,
            "equipment_id": self.equipment_id,
            "renter_id": self.renter_id,
            "rental_date": self.rental_date.isoformat(),
            "due_date": self.due_date.isoformat(),
            "return_date": self.return_date.isoformat() if self.return_date else None,
        }

    @staticmethod
    def default_due_date():
        return date.today() + timedelta(days=RENTAL_PERIOD_DAYS)
