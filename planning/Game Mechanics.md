# Game Mechanics

## Contents

- [Character System](#character-system)
- [How This Affects Game Design](#how-this-affects-game-design)
- [Abbot Trait System](#abbot-trait-system)
- [Abbot Governance Mechanics](#abbot-governance-mechanics)

## Character System

The monastery is not "the player" - the abbot is.
Abbey management is influenced by the abbot's traits, decisions, and tenure.
The abbot it mortal - new abbots may succeed previous ones, potentially changing monastery policies or goals.

## How This Affects Game Design

### Character System for Abbots
- Each abbot could have traits (e.g., Charitable, Strict, Scholarly).
- Traits affect decisions and how monks respond to leadership.
- Abbots could have skill levels (e.g., Administration, Theology).
- Aging and passing leadership to a successor creates long-term strategy.

### Abbey Politics & Decisions
- Players may need to balance relationships with monks, bishops, or secular rulers.
- Decisions could involve church doctrines, monastery expansions, or diplomacy.
- Some abbots may be more spiritual, others more pragmatic.

### Historical/Realism Considerations
- Does the game have historical inspirations (e.g., Benedictine rule)?
- Will there be interaction with the wider Church or rulers?
- Can abbots be removed by external forces (e.g., corruption, papal intervention)?

[🔼 Back to top](#game-mechanics)
## Abbot Trait System

Every abbot will have traits that influence gameplay, much like CK2. These traits can be:

#### Example Traits

|Trait     |Effect on Monastery                                     |Example Consequences|
|----------|--------------------------------------------------------|--------------------
|Charitable|Monks are happier; recruits join faster                 |+10% monk happiness, +5% donations       
|Scholarly |Faster book production and knowledge spread             |+15% learning spread, increased influence in Church
|Strict    |Increases monastery discipline but lowers monk happiness|+10% resource efficiency, -5% monk morale
|Greedy    |Higher wealth but lower reputation with Church          |+20% gold from donations, higher chance of conflict
|Zealous   |Boosts faith but may cause doctrinal disputes           |+10% faith influence, increased risk of heresy
|Diplomatic|Better relations with nobles and Church                 |+10% favour from Church and local lords
|Sickly    |Shorter lifespan                                        |Abbot may die younger, leading to more succession crises
|Visionary |Encourages innovation and new monastery policies        |Unlocks special monastery reforms


#### How Are Traits Assigned?

- Random at start of tenure (with some weighted by previous abbot’s rule).
- Some may develop over time based on decisions.
- Events can add or remove traits (e.g., "A monk accuses the abbot of greed" → Gain Greedy trait?).

[🔼 Back to top](#game-mechanics)
## Abbot Governance Mechanics

### Election or Appointment System
- Is the abbot elected by monks or appointed by a bishop/pope?
- Elections could have different candidates with varied skills.
- Political intrigue: Nobles and church officials might interfere.

### Monastery Rules & Policies
Abbots can set policies affecting how the monastery runs:

|Policy|Effect|
|------|------|
|Strict Silence Rule|Monks work harder but happiness drops|
|Open Doors to Pilgrims|Increases income but brings more outside influence|
|Scribe Focus|More books copied, boosting monastery renown|
|Self-Sufficiency Mandate|Less reliance on outside donations, but slower growth|

## Event Mechanics for Abbots

#### Dynamic Events Based on Traits & Policies

- If Zealous, the abbot might get a papal request to fight heresy.
- If Greedy, monks might accuse the abbot of hoarding wealth.
- If Diplomatic, nobles might seek the abbot's advice.

#### Event Frequency & Impact

- Some events are small daily choices (e.g., "A noble offers a donation with strings attached").
- Others could be major crises (e.g., "The local bishop wants to replace you!").

[🔼 Back to top](#game-mechanics)

## Models

### Basic Abbot Model

```python
from django.db import models
from django.contrib.auth.models import User
import random

class Abbot(models.Model):
    name = models.CharField(max_length=100)
    monastery = models.ForeignKey('Monastery', on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # If the player controls this abbot
    age = models.IntegerField(default=30)
    piety = models.IntegerField(default=50)  # Represents faith and reputation in the Church
    governance = models.IntegerField(default=50)  # How skilled the abbot is at ruling
    learning = models.IntegerField(default=50)  # How much knowledge this abbot has
    diplomacy = models.IntegerField(default=50)  # Relations with nobles and church officials
    health = models.IntegerField(default=100)  # Determines when the abbot might die
    is_active = models.BooleanField(default=True)  # Whether this abbot is alive and leading

    def __str__(self):
        return f"{self.name} (Abbot of {self.monastery.name})"

    def age_up(self):
        """Aging system: Abbots age and may die."""
        self.age += 1
        self.health -= random.randint(1, 10)  # Simulate natural health decline
        if self.health <= 0:
            self.is_active = False  # Abbot dies
        self.save()

    def assign_random_traits(self):
        """Assigns 1-3 random traits when an abbot is created."""
        traits = Trait.objects.order_by('?')[:random.randint(1, 3)]
        self.traits.add(*traits)
```

#### Trait Model for Personalities

```python
class Trait(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    effect = models.JSONField(default=dict)  # Example: {"piety": 10, "governance": -5}

    def __str__(self):
        return self.name
```

#### Election Model (For Selecting New Abbots)

```python
class Election(models.Model):
    monastery = models.ForeignKey('Monastery', on_delete=models.CASCADE)
    candidates = models.ManyToManyField(Abbot, related_name="election_candidates")
    winner = models.ForeignKey(Abbot, on_delete=models.SET_NULL, null=True, blank=True, related_name="elected_abbot")
    date_held = models.DateField(auto_now_add=True)

    def elect_new_abbot(self):
        """Randomly select a new abbot (later add voting logic)."""
        self.winner = self.candidates.order_by('?').first()
        self.winner.is_active = True
        self.winner.save()
        self.save()
```

#### Monastery
```python
class Monastery(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField(auto_now_add=True)
    abbots = models.ManyToManyField(Abbot, related_name="past_abbots")  # Track past abbots
    current_abbot = models.ForeignKey(Abbot, on_delete=models.SET_NULL, null=True, blank=True, related_name="leading_monastery")

    def new_election(self):
        """Triggers an election when the abbot dies."""
        if not self.current_abbot.is_active:
            candidates = Abbot.objects.filter(monastery=self, is_active=False)[:3]  # Pick 3 random monks
            election = Election.objects.create(monastery=self)
            election.candidates.set(candidates)
            election.elect_new_abbot()
            self.current_abbot = election.winner
            self.save()
```