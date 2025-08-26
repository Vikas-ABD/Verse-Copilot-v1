## UEFN Creature Manager Device Documentation

### 📙 Device Description

The `creature_manager_device` is used to manage one type of creature in your island. It enables control over creature behavior, monitoring of eliminations, and triggering of custom logic in Verse when creatures are defeated. For managing multiple types of creatures, use multiple instances of this device.

This device is particularly useful for:

- Creating wave systems
- Tracking creature eliminations
- Spawning rewards based on combat outcomes
- PvE mission scripting and tower defense mechanics

---

### 🧱 Required Imports

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Simulation/Tags }
using { /UnrealEngine.com/Temporary/Diagnostics }
```

---

### ♻ Main Event

**Event:** `MatchingCreatureTypeEliminatedEvent`

- **Description:** Fires when a creature of the selected type is eliminated.
- **Handler Signature:**

```verse
OnCreatureEliminated(Eliminator: agent): void
```

- **Subscription Example:**

```verse
MyCreatureManager.MatchingCreatureTypeEliminatedEvent.Subscribe(OnCreatureEliminated)
```

---

### 🛠️ Core Methods

| Method Signature                                                   | Description                                                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `Enable(): void`                                                   | Enables the device to manage and respond to creature events.                                      |
| `Disable(): void`                                                  | Disables the device, halting creature management.                                                 |
| `GetTransform(): transform`                                        | Returns the device's transform (position, rotation, scale). Use `IsValid()` check before calling. |
| `MoveTo(Position: vector3, Rotation: rotation, Time: float): void` | Smoothly moves device to a new position/rotation over time.                                       |
| `MoveTo(TargetTransform: transform, Time: float): void`            | Moves device to a target transform over time.                                                     |
| `TeleportTo(Position: vector3, Rotation: rotation): void`          | Instantly teleports the device to a new location.                                                 |
| `TeleportTo(TargetTransform: transform): void`                     | Instantly teleports the device to a full transform.                                               |

---

### ⎦ Device Usage Example

```verse
using { /Fortnite.com/Devices }

creature_manager_demo := class(my_creature_manager: creature_manager_device):

    OnBegin<override>() :=
        my_creature_manager.Enable()
        my_creature_manager.MatchingCreatureTypeEliminatedEvent.Subscribe(OnCreatureEliminated)

    OnCreatureEliminated(Eliminator: agent): void =
        Print("Creature eliminated by: {Eliminator}")
```

---

### 🥐 Extended Device Example with Editable Tag

```verse
creature_manager_example_device := class(creative_device):
    @editable
    CreatureManager : creature_manager_device = creature_manager_device{}

    OnBegin<override>()<suspends> : void =
        CreatureManager.MatchingCreatureTypeEliminatedEvent.Subscribe(OnCreatureEliminated)
        CreatureManager.Enable()

    OnCreatureEliminated(Agent : agent) : void =
        Print("A creature was eliminated!")

    EnableCreatures() : void =
        CreatureManager.Enable()

    DisableCreatures() : void =
        CreatureManager.Disable()
```

---

### ❌ Incorrect Usage Examples and Fixes

| Issue                              | ❌ Wrong                        | ✅ Fix                                                                 |
| ---------------------------------- | ------------------------------ | --------------------------------------------------------------------- |
| Incorrect handler signature        | `OnCreatureEliminated(): void` | Must include `agent` param: `OnCreatureEliminated(Eliminator: agent)` |
| Not enabling the device            | Just subscribing to event      | Call `Enable()` before subscribing                                    |
| Using event before device is valid | Call `GetTransform()` directly | Check `IsValid()` before calling methods                              |

---

### 🧠 Best Practices

- Always call `Enable()` in `OnBegin()` to activate the device.
- Use `@editable` to expose devices in the Verse editor for easier configuration.
- Track eliminations for scoring, spawning items, or custom logic.
- Use `Disable()` during pauses or resets to avoid triggering logic.
- Pair with spawn devices or timers to create dynamic wave systems.

---

### 🚀 Great For:

- Tower defense mechanics
- Wave-based survival modes
- Boss encounters and special rewards
- PvE mission scripting
- Progress tracking via combat

---

This documentation provides a full overview of how to use the `creature_manager_device` in your UEFN projects using Verse scripting.

