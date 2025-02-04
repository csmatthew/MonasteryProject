# Contents

## Game Mechanics

### Core Game Mechanics:
    - Players manage a monastery as an abbot (build, expand, sustain).
    - Resources like food, materials, monks, and books must be managed.
    - Events happen that affect monastery growth.
[▶️ go to more on Game Mechanics](Game%20Mechanics.md)

### User System (If Needed):
    - Do players log in and save progress?
    - Should users have profiles?

### Gameplay Interactions:
    - Do players interact via forms, buttons, or animations?
    - Is the game turn-based or real-time?
    - How does the game update the monastery state?

### Front-End Considerations:
    - Will it run mostly in a browser with Django templates?
    - Will it use JavaScript (maybe a JS framework)?

## Game Flow
    - Player creates a new monastery
    - Resources start at a base level
    - Player constructs buildings (which consume resources)
    - Buildings generate more resources over time
    - Random events affect the monastery's progress.

[🔼 Back to top](#Contents)

## Planning the Database Structure

### Key Database Questions
#### What data needs to be stored?
    Example: Monastery resources, monks, building progress, events.
#### What relationships exist between data?
    Example: One monastery has many buildings, monks, and resources.

### Example Database Models

#### Monastery Model
```python
class Monastery(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # If users manage monasteries
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Building Model
```python
class Building(models.Model):
    monastery = models.ForeignKey(Monastery, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    construction_time = models.IntegerField()  # Time required to build
```

#### Resource Model
```python
class Resource(models.Model):
    monastery = models.ForeignKey(Monastery, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # Example: "Food", "Wood"
    amount = models.IntegerField(default=0)
```
[🔼 Back to top](#Contents)

# Twizzle