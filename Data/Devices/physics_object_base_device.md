# 📘 physics_object_base_device – UEFN Verse Device Documentation

## 🔊 Description
The `physics_object_base_device` is the **base class** for a family of physics-based gameplay devices, including boulders and trees in Unreal Editor for Fortnite (UEFN). It provides fundamental methods for spawning, moving, enabling/disabling, and destroying physics props. Specialized events or actions are available in derived classes such as `physics_tree_device` and `physics_boulder_device`. Use this class to script generic behaviors for all such physical objects.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `prop_spawner_base_device`
- `physics_object_base_device`
  - *(See: `physics_boulder_device`, `physics_tree_device`, etc.)*

## 🛠️ Functions & Methods
| Name                        | Description                                              |
|-----------------------------|----------------------------------------------------------|
| `Enable()`                  | Enables the device to allow spawning/respawning props.   |
| `Disable()`                 | Disables the device.                                     |
| `DestroyAllSpawnedObjects()`| Destroys all props currently spawned by this device.     |
| `SpawnObject()`            | Spawns the associated prop.                              |
| `GetTransform()`           | Returns the device's current transform.                  |
| `MoveTo()` / `TeleportTo()`| Moves or instantly teleports the device.                 |

## 🧹 Events (Data Members)
- *(No custom events in base class; use derived classes for event handling.)*

## 🎛 Configuration Options (Details Panel)
| Option                 | Description                                                       |
|------------------------|-------------------------------------------------------------------|
| Prop to Spawn          | Select the model/asset to spawn (set in derived class only)       |
| Enable at Game Start   | Whether the device is enabled at round start                      |
| Initial Transform      | Placement, rotation, and scale in the world                       |
| Respawn Handling       | Timer, event, or manual respawn (available in derived classes)    |

## 🛠️ Verse Usage Example
Use this script to control a `physics_object_base_device` or subclass (e.g., boulder/tree):

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

physics_object_base_example := class(creative_device):

    @editable
    PhysicsObject : physics_object_base_device = physics_object_base_device{}

    @editable
    SpawnButton : button_device = button_device{}
    @editable
    DestroyButton : button_device = button_device{}
    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnSpawnPressed(Agent : agent) : void =
        PhysicsObject.SpawnObject()
        Print("Physics prop spawned!")

    OnDestroyPressed(Agent : agent) : void =
        PhysicsObject.DestroyAllSpawnedObjects()
        Print("All physics props destroyed!")

    OnEnablePressed(Agent : agent) : void =
        PhysicsObject.Enable()
        Print("Physics device enabled!")

    OnDisablePressed(Agent : agent) : void =
        PhysicsObject.Disable()
        Print("Physics device disabled!")
```

### Explanation
- Reference your placed `physics_object_base_device` (or subclass) and four `button_device`s.
- Each button invokes a method to spawn, destroy, enable, or disable the prop.
- This allows dynamic in-game interaction with physics objects.

## 📌 How to Use in UEFN
### 1. Place Devices in Level
- Drag a `physics_object_base_device` (or subclass) and four `button_device`s into the world.

### 2. Configure Details Panel
- Set the prop model, enable state, and respawn/transform options.

### 3. Create & Connect Verse Device
- In **Verse Explorer**, create a new Verse file (e.g., `physics_object_base_example.verse`).
- Paste the script above and save.
- Build with `Ctrl + Shift + B` until you see "Build Succeeded."
- Place your Verse device in the level.

### 4. Assign @editable References
- In the Verse device's Details panel:
  - Set `PhysicsObject` → to your physics object device.
  - Set `SpawnButton`, `DestroyButton`, `EnableButton`, `DisableButton` → to your button devices.

### 5. Test
- Enter Play mode and interact with the buttons to control the physics prop live.

## 🧠 Best Practices
- Use this class for abstract/generic scripting of physical props.
- Use `.Enable()` / `.Disable()` for managing round or phase logic.
- Use `.DestroyAllSpawnedObjects()` to reset the level or clean up props.
- For complex behaviors like falling/rolling or reactions to environment, use `physics_boulder_device` or `physics_tree_device`.

## ❌ Common Issues & Fixes
| Issue                        | ❌ Common Problem             | ✅ Solution                                       | Explanation                                                  |
|-----------------------------|----------------------------------|------------------------------------------------------|--------------------------------------------------------------|
| No prop spawns              | Device is disabled               | Call `.Enable()` or enable in Details panel          | Must be enabled to function                                  |
| Can't destroy or respawn   | Not calling Destroy/SpawnObject  | Add button or method call to perform actions         | Manual control required                                      |
| Nothing happens on event   | Missing Verse wiring or handlers | Ensure buttons are wired and Verse logic is present  | Base class has no events—derive and subscribe as needed     |

## 🔹 Note
- For custom events like elimination, destruction, or pickup, use a **derived device** such as `physics_boulder_device` or `physics_tree_device`.
- This base class gives a stable API for implementing gameplay using physics-driven objects in UEFN.

