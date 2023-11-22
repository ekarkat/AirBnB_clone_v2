from models import place
from models import review
from models import city
from models import user
from models import state



sta = state.State()

sta.id = "292be8d1-ec58-4b10-abd9-23b7f5fb0e96"

print(sta.id)

cit1 = city.City()

cit1.state_id = "292be8d1-ec58-4b10-abd9-23b7f5fb0e96"

pla = place.Place()

pla.id = "8e1cb78f-49f7-4344-b941-4923255dabc1"

print(pla.reviews)