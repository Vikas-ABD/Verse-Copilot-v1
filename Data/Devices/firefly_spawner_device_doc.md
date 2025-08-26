# Firefly Spawner Device – UEFN Verse Device Documentation

## 🔹 Description
The `firefly_spawner_device` places collectible fireflies in your Fortnite island. These fireflies circle the spawner until collected by an agent, after which they are stored as firefly jars in the player's equipment bar (usable in stacks of six). Firefly jars can be thrown to set terrain, structures, or players on fire, dealing damage and creating ongoing hazards.

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

## 🔗 Inheritance Hierarchy
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for `creative_device`.
- `firefly_spawner_device`

## 🔁 Listenable Events
| Event Name             | Type           | Description                                                         |
|------------------------|----------------|---------------------------------------------------------------------|
| `OnFirefliesCollected` | listenable(agent) | Fires when an agent collects the spawned fireflies. Useful for triggering other systems (e.g., unlocking doors, scoring, tracking). |

## 🤩 Core Members & Methods
| Name / Function         | Type / Signature        | Description                                                     |
|-------------------------|--------------------------|-----------------------------------------------------------------|
| `OnFirefliesCollected`  | listenable(agent)        | Event: fires when an agent collects spawned fireflies.         |
| `Enable()`              | void                     | Enables the spawner.                                            |
| `Disable()`             | void                     | Disables the spawner.                                           |
| `Respawn()`             | void                     | Destroys/respawns all fireflies; replaces any that were collected. |
| `ResetRespawnCount()`   | void                     | Resets internal respawn count.                                  |
| `GetTransform()`        | transform                | Returns spawner transform; check `IsValid` before use.         |
| `MoveTo()` / `TeleportTo()` | creative_object standard | Move or teleport spawner in the world.                          |

## 🎛 Configuration Options (Details Panel)
| Option                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Enabled At Game Start    | Whether the spawner is active at match start                                |
| Spawn Timer              | Time between spawning fireflies                                              |
| Activating Team          | Teams eligible to collect or trigger spawning                               |
| Allowed Class            | What class can collect (Any, No Class, Pick a class)                         |
| Total Spawn Limit        | Max number of fireflies that can be spawned (or infinite)                    |
| Time to Collect          | Delay required to collect a firefly                                          |
| On Fireflies Collected   | Transmits a signal when fireflies are collected                              |
| Enable/Disable/Respawn   | Bind this device’s actions to receive triggers from other devices            |

## 🛠️ Usage Example 1
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Device to manage firefly spawner and demonstrate its functionality
firefly_spawner_example := class(creative_device):

    @editable
    FireflySpawner : firefly_spawner_device = firefly_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnEnablePressed(Agent : agent) : void =
        FireflySpawner.Enable()
        Print("Firefly spawner enabled")

    OnDisablePressed(Agent : agent) : void =
        FireflySpawner.Disable()
        Print("Firefly spawner disabled")

    OnRespawnPressed(Agent : agent) : void =
        FireflySpawner.Respawn()
        Print("Fireflies respawned")
```

## 🔹 Usage Example 2
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

firefly_manager := class(creative_device):

    @editable
    FireflySpawner: firefly_spawner_device

    OnBegin<override>()<suspends>: void =
        FireflySpawner.Enable()
        FireflySpawner.OnFirefliesCollected.Subscribe(OnFireflyCollected)

    OnFireflyCollected(Player: agent): void =
        Print("Player collected fireflies: {Player}")
```

## 🧠 Explanation
- Place a `firefly_spawner_device` and link control buttons as needed in your island.
- Assign each device (spawner and buttons) to their `@editable` slots in the Details panel.
- The example demonstrates enabling, disabling, and respawning fireflies via button inputs.
- It also shows how to subscribe to the `OnFirefliesCollected` event for further gameplay logic.

## 🤔 Best Practices
- Configure the device’s spawn timing, spawn limit, allowed team/class, and collect timing for your desired gameplay pattern.
- Use the `OnFirefliesCollected` event to trigger custom actions (objectives, score, unlocking areas, etc.).
- Place firefly spawners where fire/hazard gameplay or resource gathering is desired.
- Avoid placing where accidental mass fire damage could disrupt gameplay.
- Use triggering and transmission options to coordinate with other creative devices (e.g., counters, item granters).

## ❌ Incorrect Usage Examples and How to Fix
| Issue                      | ❌ Wrong Example                 | ✅ Correct Example              | Explanation                                                  |
|---------------------------|-------------------------------------|-----------------------------------|--------------------------------------------------------------|
| Not assigning device ref  | Calling methods without setting @editable ref | Always assign in Details panel     | Prevents access errors                                       |
| Enabling while enabled    | Repeatedly calling `Enable()`        | Check device state or use minimally | Redundant but not harmful                                    |
| Wrong team/class settings | Picking a team/class that cannot collect | Use correct Activating Team/Class  | Ensures fair collection conditions                           |

## 🔎 Additional Notes
- Collected fireflies become "firefly jars" (stackable and throwable).
- Firefly jars ignite terrain, structures, or players if fire is enabled in My Island settings.
- Combine with `elimination_feed_device` or `analytics_device` for tracking or feedback on collectibles.

