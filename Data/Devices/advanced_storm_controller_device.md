# Advanced Storm Controller Device – UEFN Verse Device Documentation

## 📙 Description

The `advanced_storm_controller_device` allows creators to build and manage a Battle Royale-style storm system with up to 50 customizable phases. Unlike the `basic_storm_controller_device`, it supports dynamic, multi-phase storms, with each phase configurable through `advanced_storm_beacon_devices`. This enables detailed control over storm timing, size, movement, and damage. The device supports event triggering, storm manipulation, and integration with Verse logic for custom game modes.

## 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `storm_controller_device`
- `advanced_storm_controller_device`

## 🥩 Data Members (Events)

| Name            | Type                | Description                               |
| --------------- | ------------------- | ----------------------------------------- |
| PhaseEndedEvent | listenable(payload) | Signals when a storm resizing phase ends. |

## 🛠️ Functions & Methods

| Name                             | Description                                                             |
| -------------------------------- | ----------------------------------------------------------------------- |
| GenerateStorm()                  | Begins storm generation using current configuration.                    |
| DestroyStorm()                   | Instantly stops and removes the storm.                                  |
| GetTransform()                   | Retrieves the storm controller's current position, rotation, and scale. |
| MoveTo(Position, Rotation, Time) | Moves the controller to a new location for the next storm.              |
| TeleportTo(Position, Rotation)   | Instantly teleports controller; applies to next storm only.             |

## 🎮 Configuration Options (Details Panel)

| Option                       | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| Generate Storm on Game Start | Start automatically or via Verse/event logic.      |
| Use Custom Storm Phases      | Enable to define each phase using beacon devices.  |
| Phase One Radius             | Initial storm radius.                              |
| Delay Time                   | Delay before storm begins.                         |
| Bounds Radius                | Limits maximum storm movement area.                |
| On Finish Behavior           | Options: Stay, Destroy (with optional delay).      |
| Storm Sickness               | Additional damage for prolonged exposure in storm. |

*Note: Configure global settings in the controller's Details panel. Phase-specific settings are managed via **`advanced_storm_beacon_device`**.*

## 🧰 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }

advanced_storm_controller_example := class(creative_device):

    @editable
    StormController : advanced_storm_controller_device = advanced_storm_controller_device{}

    @editable
    StormBeacons : []advanced_storm_beacon_device = array{}

    @editable
    StartButton : button_device = button_device{}

    @editable
    StopButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        StormController.PhaseEndedEvent.Subscribe(OnPhaseEnded)
        StartButton.InteractedWithEvent.Subscribe(OnStartPressed)
        StopButton.InteractedWithEvent.Subscribe(OnStopPressed)

    OnPhaseEnded(PhaseIndex : tuple()) : void =
        Print("Storm phase ended.")

    OnStartPressed(Agent : agent) : void =
        StormController.GenerateStorm()
        Print("Storm generation started.")

    OnStopPressed(Agent : agent) : void =
        StormController.DestroyStorm()
        Print("Storm destroyed.")

    MoveBeaconToIndex(BeaconIndex : int, NewPosition : vector3, NewRotation : rotation)<suspends> : void =
        if (Beacon := StormBeacons[BeaconIndex]):
            Beacon.MoveTo(NewPosition, NewRotation, 1.0)
            Print("Moved beacon {BeaconIndex} to new position.")
```

## ⚖️ How It Works in UEFN

### 1. Place Devices in Level:

- Add an `advanced_storm_controller_device` to your island.
- Add one `advanced_storm_beacon_device` for each storm phase.
- Optionally add `button_device` for runtime storm control.

### 2. Configure Devices:

- In the controller:
  - Set **Use Custom Storm Phases** to **Yes**.
  - Set radius, bounds, phase count, and other settings.
- In each beacon:
  - Assign a unique **Phase** number (1–50).
  - Configure wait/resize time, damage, size, and position.

### 3. Create & Build Verse Script:

- In Verse Explorer, create a new Verse file (e.g., `advanced_storm_controller_example.verse`).
- Paste the provided code and save.
- Build Verse Code (`CTRL+SHIFT+B` or via menu).

### 4. Assign References:

- Drag your Verse device to the level.
- Assign `StormController`, `StormBeacons`, and buttons in the Details panel.

### 5. Test:

- Playtest the island.
- Use buttons or game start to trigger storm.
- Watch phase transitions, movement, and events.

## 🧠 Best Practices

- Always assign unique Phase numbers to beacons.
- Use `PhaseEndedEvent` to trigger effects, drops, or audio cues.
- Combine `GenerateStorm()`/`DestroyStorm()` for round-based gameplay.
- Move/teleport controller or beacons for advanced storm behavior.

## ❌ Common Mistakes & Fixes

| Issue                               | ❌ Wrong                                     | ✅ Correct                              | Explanation                       |
| ----------------------------------- | ------------------------------------------- | -------------------------------------- | --------------------------------- |
| Custom Phases not enabled           | Left default setting                        | Set `Use Custom Storm Phases = Yes`    | Required for beacon phase control |
| Moving controller after storm start | `MoveTo()` called mid-storm                 | Move only **before** `GenerateStorm()` | Only affects **next** storm       |
| Unsubscribed events                 | Used `PhaseEndedEvent` directly             | Use `.Subscribe(OnPhaseEnded)`         | Must subscribe to receive event   |
| Missing assignments                 | Verse `@editable` refs blank                | Assign all refs in Details panel       | Unassigned devices won't work     |
| Using beacon events                 | Subscribed to `StormBeacon.PhaseEndedEvent` | Use only `StormController` events      | Beacons don't emit events         |

## 🔹 Notes

- Combine beacon timing, storm radius, and movement for cinematic storm behavior.
- Use advanced device only for multi-phase storms; use basic version for single-phase.
- Design storm flow early in the map layout to align phases and movement.

---

This documentation provides a comprehensive overview of the `advanced_storm_controller_device` for UEFN, with examples and configuration tips for custom storm behavior in Fortnite Creative maps.

