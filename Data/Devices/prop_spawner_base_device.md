# prop_spawner_base_device – UEFN Verse Device Documentation

## 🔍 Description
The `prop_spawner_base_device` is an abstract base class for devices that can spawn prop objects in your Fortnite island. This class is extended by concrete devices that allow you to spawn, move, and destroy props programmatically or via triggers, buttons, and Verse logic. Spawning props can be used for dynamic obstacles, puzzle elements, destructibles, or gameplay rewards.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `prop_spawner_base_device`

## 🛠️ Functions & Methods
| Name                     | Description                                                |
|--------------------------|------------------------------------------------------------|
| `Enable()`               | Enables the device for spawning props.                    |
| `Disable()`              | Disables the device.                                      |
| `SpawnObject()`          | Spawns the configured prop.                               |
| `DestroyAllSpawnedObjects()` | Destroys all props spawned by this device.           |
| `GetTransform()`         | Gets the device’s world transform.                         |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the spawner and/or prop in world.  |

## 🎛 Configuration Options (Details Panel)
| Option                  | Description                                                                |
|-------------------------|----------------------------------------------------------------------------|
| Prop Asset              | Select which prop object to be spawned by this spawner.                    |
| Spawn Location & Rotation | Where and how the prop will spawn in the world.                          |
| Collision Settings      | Affect how props interact with environment/players.                        |
| Max Spawned Count       | Limit how many props can exist at once from this device.                   |
| Spawn on Game Start     | If checked, prop will spawn as soon as game begins.                        |
| Destructible            | Can enable, set health, or destruction options for spawned prop.           |

## 🧹 Events
This base class **does not expose custom Verse events** for spawned/destroyed, but all core functions can be controlled via Verse or device wiring.

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example showing how to use prop mover device functionality
prop_mover_example := class(creative_device):

    @editable
    PropMover : prop_mover_device = prop_mover_device{}

    @editable
    MoveButton : button_device = button_device{}

    @editable
    DestroyButton : button_device = button_device{}

    var SpawnedProp : ?creative_prop = false

    OnBegin<override>()<suspends> : void =
        PropMover.Enable()
        MoveButton.InteractedWithEvent.Subscribe(OnMovePressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)

    OnMovePressed(Agent : agent) : void =
        if (Prop := SpawnedProp?):
            CurrentTransform := Prop.GetTransform()
            NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 200.0}
            if (Prop.TeleportTo[NewLocation, CurrentTransform.Rotation]):
                Print("Prop moved up")
            else:
                Print("Failed to move prop")

    OnDestroyPressed(Agent : agent) : void =
        if (Prop := SpawnedProp?):
            Prop.Dispose()
            set SpawnedProp = false
            Print("Prop destroyed")
        else:
            Print("No prop to destroy")
```

### Explanation:
- Reference the `prop_mover_device` and three control `button_device` components.
- Use `.Enable()` in `OnBegin` to activate spawner.
- Handle prop movement using `.TeleportTo()`.
- Destroy props using `.Dispose()`.

## ✨ How to Use in UEFN
1. **Place a Prop-Spawner Device**  
   Drag a concrete prop spawner device (e.g., Prop Mover) into your level.

2. **Configure the Spawner Device**  
   Set the prop asset, collision, destruction, location/rotation, and spawn count.

3. **Add Button Devices for Player Control (Optional)**  
   Use buttons for triggering spawn, move, or destroy.

4. **Create a Verse Device**  
   Create a Verse file (e.g., `prop_spawner_example.verse`), paste code, and build.

5. **Assign Device References**  
   In the level, assign prop spawner/mover and control buttons in the Verse device settings.

6. **Test in Session**  
   Play the map and interact with buttons to dynamically control props.

## 🧠 Best Practices
- Use `.Enable()`/`.Disable()` to control spawn behavior.
- Combine with triggers or eliminations for dynamic gameplay.
- Adjust destruction parameters and spawn count as per game mechanics.
- Subclass for specialized logic if needed.

## ❌ Common Issues & Fixes
| Issue                  | Cause                          | Solution                                            |
|------------------------|--------------------------------|-----------------------------------------------------|
| Prop doesn’t spawn     | Did not call `.SpawnObject()`  | Trigger spawn in Verse, via button, or game start.  |
| Too many props         | Max count not set              | Set "Max Spawned Count" in device Details panel.    |
| Verse not working      | References unassigned          | Set Verse references for all used devices.          |

### Note:
All prop spawner devices in UEFN derive from this base class. Use a **concrete spawner** (like Prop Mover) for actual spawning in your game. Props can be made destructible and configured fully through Verse logic and UEFN GUI.

