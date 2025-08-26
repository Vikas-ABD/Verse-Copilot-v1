## storm_controller_device – UEFN Verse Device Documentation

### 🔹 Description
The `storm_controller_device` is the **base class** for controlling storms in Fortnite projects. It is not placed directly in the level but serves as the foundation for specific storm devices:

- `basic_storm_controller_device` — for simple, single-phase storms.
- `advanced_storm_controller_device` — for multi-phase, customizable storms with dynamic beacons.

Devices based on this class can:
- Generate, destroy, and move storms
- Control storm position
- Signal storm-cycle events

Common use cases include:
- Battle Royale
- Survival modes
- Shrinking play zones
- Advanced gameplay control

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `storm_controller_device`
  - `basic_storm_controller_device`
  - `advanced_storm_controller_device`

### 🧹 Events (Data Members)
| Name               | Type          | Description                                         |
|--------------------|---------------|-----------------------------------------------------|
| `PhaseEndedEvent` | `listenable()` | Fires every time the storm completes a resizing phase |

### 🛠️ Functions & Methods
| Name                        | Description |
|-----------------------------|-------------|
| `GenerateStorm()`           | Generates and starts the storm. Must set "Generate Storm On Game Start" to `No`. |
| `DestroyStorm()`            | Immediately eliminates the storm from the world. |
| `GetTransform()`            | Returns the current transform (position, rotation, scale). |
| `MoveTo(Position,Rotation,OverTime)` | Moves to new position/rotation over specified seconds. |
| `MoveTo(Transform,OverTime)`| Moves to new transform in specified time. |
| `TeleportTo(Position,Rotation)` | Instantly moves to a new position/rotation. |
| `TeleportTo(Transform)`     | Instantly moves to new transform (position, rotation, scale). |

**Note**: These functions move the storm device itself. New storm phases use the updated center/position.

### 📆 Configuration Options (Details Panel)
*(On the storm controller subclass in the editor)*
| Option Name                  | Description |
|-----------------------------|-------------|
| Generate Storm On Game Start| If `No`, call `GenerateStorm()` from Verse to start the storm |
| Storm Center                | Sets the initial center for the generated storm |
| Phase Count (Advanced only) | Number of phases the storm will use |
| Visual/Audio FX, Damage     | Storm visuals, damage per tick, etc. |

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use storm_controller_device
storm_controller_example := class(creative_device):

    @editable
    StormController : basic_storm_controller_device = basic_storm_controller_device{}

    @editable
    StartButton : button_device = button_device{}

    @editable
    EndButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to storm events
        StormController.PhaseEndedEvent.Subscribe(OnPhaseEnded)

        # Subscribe to control buttons
        StartButton.InteractedWithEvent.Subscribe(OnStartPressed)
        EndButton.InteractedWithEvent.Subscribe(OnEndPressed)

    # Event handlers
    OnPhaseEnded() : void =
        Print("Storm phase ended!")

    # Button control handlers
    OnStartPressed(Agent : agent) : void =
        StormController.GenerateStorm()
        Print("Storm started!")

    OnEndPressed(Agent : agent) : void =
        StormController.DestroyStorm()
        Print("Storm ended!")
```

### How to Use in UEFN
1. **Place a Storm Controller Device**
   - Drag a `basic_storm_controller_device` or `advanced_storm_controller_device` into your level.

2. **Configure Options**
   - In Details: Set storm center, number of phases, generation options, visuals, and "Generate Storm On Game Start".

3. **Add (Optional) Control Buttons**
   - Place two `button_device` objects: one to start the storm, one to end it.

4. **Verse Device Setup**
   - In Verse Explorer, create a new file (e.g., `storm_controller_example.verse`).
   - Paste the sample code and save.
   - Click **Verse > Build Verse Code** (`Ctrl+Shift+B`) until successful.

5. **Device Reference Assignment**
   - Place your Verse device in the level.
   - In Details panel, assign:
     - `StormController` → your storm device
     - `StartButton`, `EndButton` → your placed buttons

6. **Test**
   - Use buttons to generate and destroy the storm.
   - Watch logs for `PhaseEndedEvent` messages.

### 🧠 Tips
- Use `MoveTo` or `TeleportTo` for advanced layouts and storm repositioning.
- React to `PhaseEndedEvent` for scoring, alerts, or phase transitions.

### ❌ Common Issues & Solutions
| Issue                | Possible Reason                         | How To Fix                            |
|----------------------|------------------------------------------|----------------------------------------|
| Storm doesn’t start | "Generate Storm On Game Start" is `Yes` or device not referenced | Set to `No` and use `GenerateStorm()` |
| Storm doesn’t destroy | Wrong device or missing reference        | Assign the correct device              |
| Verse errors         | Incorrect class reference                | Use only supported subclasses          |

### 🔹 Notes
- Use `basic_storm_controller_device` for simple single-phase storms.
- Use `advanced_storm_controller_device` for multi-phase storms with dynamic behavior.
- All runtime control (movement, generation, destruction) is handled via the Verse API.

