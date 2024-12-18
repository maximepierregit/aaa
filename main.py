import uuid


class ShowDoesNotExist(Exception):
    """This exception is raised when the show is not present in the available list of shows."""
    pass

class NoTicketAvailable(Exception):
    """This exception is raised when no more ticket are available."""
    pass

class InvalidNumberOfTicketToGenerate(Exception):
    """This exception is raised when an invalid number of ticket is provided. For example, providing zero tickets or a negative number."""
    pass

class Ticket:
    """Represent a single ticket that a user can obtain for a given show."""
    def __init__(self, artist) -> None:
        """Constructor that initialize every variable to a default value and generated a unique ID"""
        self.unique_id = uuid.uuid4()
        self.name = ""
        self.is_taken = False
        self.artist = artist
    
    def print_info(self) -> None:
        """Print information about the ticket holder, show and unique ID"""
        print(f"Ticket reserved by {self.name} for {self.artist} with unique ID {self.unique_id}")

class TicketReservationService:
    """This is the reservation web service API. Manage the ticketing system and reservation.""" 
    def __init__(self) -> None:
        """Constructor. Initialize the ticket to an empty dictionnary."""
        self.tickets = {}

    def count_available_tickets(self, artist) -> None:
        """Count the available ticket for a given artist show."""
        if not artist in self.tickets:
            return 0
    
        number = 0
        for ticket in self.tickets[artist]:
            if not ticket.is_taken:
                number = +1
        
        return number
    
    def generate_ticket(self, artist, number) -> None:
        """Generate new ticks for an artist with the provided number in argument. Must be a positive number"""
        if number <= 0:
            raise InvalidNumberOfTicketToGenerate(f"Generate at least 1 ticket for the artist. Provided {number} tickets.")

        generated_ticket = []
        for _ in range(0, number):
            new_ticket = Ticket(artist)
            generated_ticket.append(new_ticket)
        
        if artist in self.tickets:
            for value in self.tickets[artist]:
                generated_ticket.append(value)
        
        self.tickets[artist] = generated_ticket
    
    def reserve(self, artist, username) -> Ticket:
        """Allow a user to reserve one ticket for a show if it exists. Can raise ShowDoesNotExist or NoTicketAvailable exception."""
        if not artist in self.tickets:
            raise ShowDoesNotExist("This show does not exists")

        available_ticket = self.tickets[artist]
        for ticket in available_ticket:
            if not ticket.is_taken:
                ticket.name = username
                ticket.is_taken = True
                return ticket

        raise NoTicketAvailable("No more ticket available")