import unittest
import random
import uuid
from main import *

class TestTicketReservationService(unittest.TestCase):
    def setUp(self) -> None:
        self.ticket_reversation_service = TicketReservationService()
        self.ticket_reversation_service.generate_ticket("Isabelle Boulay", 100)
        self.username = "User-ABC"
    
    def tearDown(self) -> None:
        self.ticket_reversation_service = None

    def test_count_available_ticket(self) -> None:
        self.assertEqual(100, self.ticket_reversation_service.count_available_tickets("Isabelle Boulay"))

    def test_count_available_ticket_not_existant(self):
        self.assertEqual(0, self.ticket_reversation_service.count_available_tickets("Claude Dubois"))

    def test_generate_ticket(self) -> None:
        number = random.randint(1, 100)
        self.ticket_reversation_service.generate_ticket("Paul Piché", number)
        self.assertEqual(number, self.ticket_reversation_service.count_available_tickets("Paul Piché"))
    
    def test_generate_invalid_ticket_number(self) -> None:
        number = random.randint(-100, 0)
        with self.assertRaises(InvalidNumberOfTicketToGenerate):
            self.ticket_reversation_service.generate_ticket("Paul Piché", number)

    def test_reserve_show_not_exist(self) -> None:
        with self.assertRaises(ShowDoesNotExist):
            self.ticket_reversation_service.reserve("Céline Dion", self.username)
    
    def test_reserve_show(self) -> None:
        reserved_ticket = self.ticket_reversation_service.reserve("Isabelle Boulay", self.username)
        self.assertEqual(self.username, reserved_ticket.name)
        self.assertNotEqual(reserved_ticket.unique_id, uuid.UUID(int = 0))

    def test_reserve_show_no_more_ticket(self) -> None:
        with self.assertRaises(NoTicketAvailable):
            for _ in range(0, 101):
                self.ticket_reversation_service.reserve("Isabelle Boulay", "UltraFan!01")