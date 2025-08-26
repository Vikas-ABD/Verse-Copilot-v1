# 📘 physics_tree_device – UEFN Verse Device Documentation

## 🔹 Description
The `physics_tree_device` is a physics-based, interactive tree designed for Unreal Editor for Fortnite (UEFN) experiences. It can be chopped down by players, falling and transforming into a log that interacts with the world using physics. Both the log and stump can be destroyed, and all parts can deal configurable damage to players, vehicles, creatures, and structures on impact. This tree is ideal for dynamic hazards, puzzles, and creative interactive environments.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- prop_spawner_base_device
- physics_object_base_device
- physics_tree_device

## 🛠️ Functions & Methods
| Method                  | Description                                                        |
|------------------------|--------------------------------------------------------------------|
| `Enable()`             | Enables the device—can be chopped, interacted with, etc.           |
| `Disable()`            | Disables the device; optionally destroys all spawned tree parts.   |
| `SpawnObject()`        | Spawns the tree if not present.                                    |
| `DestroyAllSpawnedObjects()` | Destroys all currently spawned tree objects (trunk, log, stump). |
| `ReleaseLog()`         | Releases/drops the current log part from the tree.                 |
| `DestroyLog()`         | Destroys only the fallen log.                                      |
| `DestroyStump()`       | Destroys only the stump (if present).                              |
| `GetTransform()`       | Returns the device’s current transform.                            |
| `MoveTo()/TeleportTo()`| Move or teleport the device in-world (setup only).                |

## 🥉 Events (Data Members)
| Name                 | Type                  | Fires When...                     |
|----------------------|------------------------|-----------------------------------|
| `TreeSpawnedEvent`   | `listenable(tuple())`  | The tree is spawned or respawns.  |
| `TreeKnockedDownEvent` | `listenable(tuple())`| The standing tree is chopped down/falls. |
| `LogDestroyedEvent`  | `listenable(tuple())`  | The fallen log is destroyed.      |
| `StumpDestroyedEvent`| `listenable(tuple())`  | The stump is destroyed.           |

## 🎛 Configuration Options (Details Panel)
| Option                  | Description                                                   |
|------------------------|---------------------------------------------------------------|
| Damage to Players      | Max damage from the log to players (scaled by impact).        |
| Damage to Vehicles     | Max damage to vehicles from impact.                           |
| Damage to Creatures    | Max damage to creatures.                                      |
| Damage to Environment  | Max damage to structures/environment per hit.                |
| Timed Tree Respawn     | Time before tree respawns after being chopped down.           |
| Spawn When Enabled     | Whether a tree spawns automatically when device is enabled.   |
| Destroy When Disabled  | Automatically destroy tree/log/stump on device being disabled.|
| Health                 | Amount of damage tree can take before falling.                |
| Leave Stump            | Whether the stump remains after chopping down tree.           |
| Stump Health           | Health for stump, if left.                                     |
| Log Health             | Health for log, if left.                                       |

## 🧠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

physics_tree_example := class(creative_device):

    @editable
    Tree : physics_tree_device = physics_tree_device{}

    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}
    @editable
    SpawnButton : button_device = button_device{}
    @editable
    DestroyButton : button_device = button_device{}
    @editable
    ReleaseLogButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Tree.TreeKnockedDownEvent.Subscribe(OnTreeKnockedDown)
        Tree.LogDestroyedEvent.Subscribe(OnLogDestroyed)
        Tree.StumpDestroyedEvent.Subscribe(OnStumpDestroyed)
        Tree.TreeSpawnedEvent.Subscribe(OnTreeSpawned)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)
        ReleaseLogButton.InteractedWithEvent.Subscribe(OnReleaseLogPressed)

    OnTreeKnockedDown() : void =
        Print("Tree was knocked down!")

    OnLogDestroyed() : void =
        Print("Fallen log was destroyed!")

    OnStumpDestroyed() : void =
        Print("Tree stump was destroyed!")

    OnTreeSpawned() : void =
        Print("Tree respawned!")

    OnEnablePressed(Agent : agent) : void =
        Tree.Enable()
        Print("Tree device enabled!")

    OnDisablePressed(Agent : agent) : void =
        Tree.Disable()
        Print("Tree device disabled!")

    OnSpawnPressed(Agent : agent) : void =
        Tree.SpawnObject()
        Print("Tree spawned!")

    OnDestroyPressed(Agent : agent) : void =
        Tree.DestroyAllSpawnedObjects()
        Print("All spawned tree objects destroyed!")

    OnReleaseLogPressed(Agent : agent) : void =
        Tree.ReleaseLog()
        Print("Log released from tree!")
```

## 🔧 How to Set Up in UEFN
1. **Place Devices in Your Level**
   - Drag one `physics_tree_device` and five `button_device`s into your world.
2. **Configure Tree/Buttons**
   - Adjust tree damage, health, respawn, and spawn options in the Details panel.
   - Label buttons appropriately: Enable, Disable, Spawn, DestroyAll, ReleaseLog.
3. **Create and Add Verse Script**
   - In Verse Explorer, right-click a folder → *Create New Verse File*.
   - Paste the example code and save.
   - Press Ctrl+Shift+B to Build Verse Code.
   - Drag the Verse device into the world.
4. **Assign @editable References**
   - Link Tree and each Button to their respective placed devices.
5. **Test In-Game**
   - Launch a session and test tree interaction via buttons and event logs.

## 🧠 Best Practices
- Use event subscriptions to react dynamically (score, elimination, puzzle progress).
- Use `DestroyAllSpawnedObjects()` for resets.
- Use `ReleaseLog()` for puzzle logic or triggered hazards.
- Adjust damage/health settings for gameplay balance.

## ❌ Common Issues & Fixes
| Issue                            | ❌ Problem                  | ✅ Solution                              | Explanation                                      |
|----------------------------------|-------------------------------|---------------------------------------------|--------------------------------------------------|
| Tree/log does not spawn/respawn | Wrong Details config          | Set respawn timers, health, enable spawn    | Tree must be enabled and configured to spawn     |
| Log/tree/stump indestructible   | Health set to Indestructible | Lower health in Details panel               | Set destructible values for interaction          |
| Events don’t fire in Verse       | No event subscription         | Add event subscriptions in `OnBegin()`      | Required for reactive logic                      |
| Reference error in Verse        | @editable not assigned        | Assign in Details panel                     | Devices must be linked to Verse via @editable    |

> **Note:** Damage scales with physics impact. All parts are indestructible by default. Change this in the Details panel.

---
Use `physics_tree_device` to create immersive, interactive environments in your Fortnite island!

