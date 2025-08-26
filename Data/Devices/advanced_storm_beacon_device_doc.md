# Advanced Storm Beacon Device – UEFN Verse Device Documentation

## 🔹 Description
The `advanced_storm_beacon_device` allows developers to customize individual phases of a multi-phase storm system in Fortnite UEFN. When paired with an `advanced_storm_controller_device`, this setup enables detailed configuration of each storm phase, including zone size, timing, damage, and movement behavior. This system supports the creation of complex, Battle Royale-style dynamic storms.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `advanced_storm_beacon_device`

## 🧉 Functions & Methods
| Name | Description |
|------|-------------|
| `GetTransform()` | Gets the device’s world position, rotation, and scale. |
| `MoveTo(Position, Rotation, Time)` | Moves the device to a new location and rotation over the specified time (in seconds). |
| `TeleportTo(Position, Rotation)` | Instantly moves the device to a new position and orientation. Useful for next generated storm phase. |

## 🧹 Events
- The `advanced_storm_beacon_device` **does not** expose Verse events. Storm logic is managed through configuration and the storm controller.

## 🏠 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Phase | Defines which phase (1–50) this beacon customizes. |
| Storm Radius | Size of the storm circle at this phase (not used for phase 1). |
| Wait Time | Delay before progressing to the next phase (not used in final phase). |
| Resize Time | Duration the storm takes to shrink or move to target radius/position. |
| Damage Level | Amount of damage inflicted during this phase; can be lethal. |
| Movement Behavior | Either Move to beacon (exact) or Move randomly (within range). |
| Move Distance Min/Max | For random movement: defines minimum and maximum range. |

## 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }

storm_beacon_example := class(creative_device):

    @editable
    StormController : advanced_storm_controller_device = advanced_storm_controller_device{}

    @editable
    StormBeacons : []advanced_storm_beacon_device = array{}

    @editable
    StartButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        StormController.PhaseEndedEvent.Subscribe(OnPhaseEnded)
        StartButton.InteractedWithEvent.Subscribe(OnStartPressed)

    OnPhaseEnded(PhaseIndex : int) : void =
        Print("Storm phase {PhaseIndex} ended.")

    OnStartPressed(Agent : agent) : void =
        StormController.GenerateStorm()
        Print("Storm started with {StormBeacons.Length} beacons.")

    MoveBeaconToIndex(BeaconIndex : int, NewPosition : vector3, NewRotation : rotation)<suspends> : void =
        if (Beacon := StormBeacons[BeaconIndex]):
            Beacon.MoveTo(NewPosition, NewRotation, 1.0)
            Print("Moved beacon {BeaconIndex} to new position.")
```

## ⚖️ How It Works in UEFN
### 1. Place Devices in Level
- Add an `advanced_storm_controller_device`.
- Place one `advanced_storm_beacon_device` per custom storm phase.

### 2. Configure Devices (Details Panel)
- Set `Use Custom Storm Phases = Yes` on the controller.
- For each beacon:
  - Assign a unique `Phase` (1–50).
  - Configure `Storm Radius`, `Wait Time`, `Resize Time`, `Damage Level`, and `Movement Behavior`.

### 3. Create & Build Verse Script
- Open Verse Explorer, create a new file (e.g., `storm_beacon_example.verse`).
- Paste the example code and build it.

### 4. Place, Reference, Connect Devices
- Drag the Verse device into your map.
- Assign `StormController`, `StormBeacons`, and optionally a `StartButton` in the Details panel.

### 5. Test & Iterate
- Playtest the map.
- Trigger storm generation via button or custom logic.
- Observe storm behavior per phase.

## 🧠 Best Practices
- Label beacons clearly (e.g., "Phase 1", "Phase 2").
- Use `MoveTo`/`TeleportTo` to reset or reposition beacons dynamically.
- Align movement, damage, and timing across phases for balanced gameplay.

## ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|------------|---------------|-------------|
| Not setting phase numbers | All beacons set to Phase 1 | Assign unique phase numbers to each beacon | Controller uses these to sequence the storm |
| Using controller without beacons | Custom storm mode active but no beacons | Place and assign beacons for each phase | No beacons = no storm customization |
| Missing assignments | Verse device fields not assigned | Fill `StormController` and `StormBeacons` in Details | Required for Verse device to function |
| Expecting beacon events | Subscribed to beacon events | Subscribe to controller events | Beacons do not emit Verse events |
| Trying to change radius via Verse | `Beacon.SetStormRadius(400)` | Set via Details panel or move/teleport | Radius is a static config option, not modifiable in Verse |

## 📅 Notes
- Beacons do **not** emit events; all logic is coordinated via the controller.
- Use for multi-phase storms only; simpler alternatives exist for single-phase storms.
- Always call `GenerateStorm()` to initiate beacon logic.

