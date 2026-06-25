# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: BookingOps
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Dict, List, Optional
import random

@dataclass
class Resource:
    id: str
    name: str
    capacity: int = 10
    
@dataclass 
class Customer:
    id: str
    name: str
    email: str

@dataclass
class Reservation:
    id: str
    resource_id: str
    customer_id: str
    start_date: date
    end_date: date
    confirmed: bool = True
    
def init_demo_data() -> Dict[str, object]:
    resources = [Resource(f"R-{i}", f"Room {i}") for i in range(1, 6)]
    customers = [Customer(f"C-{i}", f"Client {i}", f"user{i}@example.com") for i in range(1, 21)]
    
    today = date.today()
    reservations: List[Reservation] = []
    for _ in range(50):
        r = random.choice(resources)
        c = random.choice(customers)
        start = today + timedelta(days=random.randint(1, 30))
        end = start + timedelta(hours=random.randint(2, 8))
        reservations.append(Reservation(f"RES-{len(reservations)+1:04d}", r.id, c.id, start, end))
        
    return {"resources": resources, "customers": customers, "reservations": reservations}
