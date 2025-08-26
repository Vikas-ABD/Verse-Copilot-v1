## carryable_spawner_device – UEFN Verse Device Documentation

### 🔹 Description
The `carryable_spawner_device` is used to spawn a carryable object into your Fortnite experience. Carryables are interactive objects that players can pick up, carry, throw, drop, or cause to explode.

This device provides fine control over the carryable’s behavior, including damage values, explosion settings, pickup/drop/throw detection, and force-carry functionality. It’s ideal for:
- Delivery objectives
- Interactive game items
- Explosive payloads
- Puzzle mechanics

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

### 🧬 Inheritance Hierarchy
| Class | Description |
|-------|-------------|
| `creative_object` | Base class for creative devices and props |
| `creative_device_base` | Base class for creative devices |
| `carryable_spawner_device` | This class. Used for spawning and managing carryables |

### 🔗 Exposed Interfaces
| Interface | Description |
|-----------|-------------|
| `enableable` | Allows the device to be enabled or disabled dynamically |

### 🧩 Data Members
| Name | Type | Description |
|------|------|-------------|
| `CanTakeDamage` | ?logic | Whether the carryable can take damage and be destroyed |
| `CarryableObjectTransform` | ??transform | Transform of the carryable if currently spawned |
| `CarryingAgent` | ??agent | The agent currently carrying the item (if any) |
| `ExplosionDamage` | ?float | Character damage dealt when it explodes |
| `ExplosionEnvironmentalDamage` | ?float | Environmental damage from explosion |
| `ExplosionImpulse` | ?float | Knockback impulse from explosion |
| `ExplosionRadius` | ?float | Radius of explosion in meters |
| `ImpactDamage` | ?float | Character damage on physical impact (velocity-scaled) |
| `ImpactEnvironmentalDamage` | ?float | Environmental damage on impact (velocity-scaled) |
| `InitialSpawnAngle` | ?float | Cone angle for random spawn direction |
| `InitialSpawnVelocity` | ?float | Initial velocity of the spawned carryable |
| `StartingHealth` | ?float | Health of the carryable when spawned |

### 🔁 Listenable Events
| Event Name | Payload | Description |
|------------|---------|-------------|
| `PickUpEvent` | `agent` | Fired when a player picks it up |
| `DropEvent` | `agent` | Fired when a player drops/is forced to drop it |
| `ThrowEvent` | `agent` | Fired when it is thrown |
| `ReleaseEvent` | `agent` | Fired when carrying ends |
| `SpawnEvent` | `agent` | Fired when carryable is spawned |
| `ExplodeEvent` | `(Instigator: agent, Affected: []agent)` | Fired on explosion, includes instigator and affected agents |

### 🧰 Core Methods
| Method Signature | Description |
|------------------|-------------|
| `Spawn(): void` | Spawns the carryable if it doesn't exist |
| `Despawn(): void` | Removes it if it exists |
| `Explode(): void` | Triggers explosion |
| `Explode(Instigator: agent): void` | Explodes with specific instigator |
| `ForcePlayerToCarry(Player: agent): void` | Forces player to pick it up |
| `Enable(): void` | Enables the spawner |
| `Disable(): void` | Disables the spawner and despawns it |
| `IsEnabled(): logic` | Returns true if device is enabled |
| `IsSpawned(): logic` | Returns true if carryable exists |
| `GetTransform(): transform` | Gets device’s transform (check IsValid()) |
| `MoveTo(Position: vector3, Rotation: rotation, Time: float): void` | Smoothly moves to new position/rotation |
| `MoveTo(TargetTransform: transform, Time: float): void` | Moves to full transform |
| `TeleportTo(Position: vector3, Rotation: rotation): void` | Instantly teleports |
| `TeleportTo(TargetTransform: transform): void` | Instantly moves/rotates using transform |

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }

carryable_controller := class(
    @editable CarryableSpawner: carryable_spawner_device
):

    OnBegin<override>() :=
        CarryableSpawner.Enable()
        CarryableSpawner.Spawn()
        CarryableSpawner.PickUpEvent.Subscribe(OnPickedUp)
        CarryableSpawner.ExplodeEvent.Subscribe(OnExploded)

    OnPickedUp(Player: agent): void =
        Print("Carryable picked up by: {Player}")

    OnExploded(Info: tuple(Instigator: agent, Affected: []agent)): void =
        Print("Carryable exploded by: {Info.Instigator}")
```

### ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong | ✅ Fix |
|-------|----------|--------|
| Spawning twice | `CarryableSpawner.Spawn()` repeatedly | Use `IsSpawned()` before calling `Spawn()` |
| Using transform without check | `CarryableSpawner.GetTransform()` | Use `if (CarryableSpawner.IsValid()):` before calling |
| Exploding without carryable | `CarryableSpawner.Explode()` | Check `IsSpawned()` first |
| Misusing events | `CarryableSpawner.OnPickUp()` | Use `.PickUpEvent.Subscribe()` correctly |

### 🧠 Best Practices
- Use `Enable()`/`Disable()` to manage spawner state.
- Use `ForcePlayerToCarry()` for quest-related logic.
- Combine explosion with gameplay mechanics.
- Track `CarryingAgent` to see who holds the item.
- Adjust explosion values for desired gameplay feel.
- Trigger `ThrowEvent` or `DropEvent` to detect mission completions.

### ✅ Great For:
- Delivery/fetch missions
- Explosive payload objectives
- Puzzle mechanics using throw/drop
- Timed pickup events
- Team-based item games (capture-the-item)

