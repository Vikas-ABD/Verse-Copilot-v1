# Skydive Volume Device – UEFN Verse Device Documentation

## 🔹 Description
The `skydive_volume_device` creates a designated zone where players entering are instantly put into a skydive state. This device is highly customizable, supporting the following configurations:

- **Push Force**: Apply a continuous force to players (direction is device-relative).
- **Launch Velocity**: Apply an initial launch speed upon entry.
- **Direction**: Controlled by the rotation of the placed device.
- **Locking**: Optionally trap players inside the zone.
- **Affected Teams/Classes**: Specify which teams or player classes are influenced.
- **Zone Phases**: Control when the device is active (e.g., Pre-Game, Gameplay).
- **Visual FX**: Enable or disable visual effects for skydive.

Use this device to create vertical launch pads, air tubes, sky routes, and dynamic traversal mechanics in your Fortnite Creative map.

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `effect_volume_device`
- `skydive_volume_device`

---

## 🧹 Data Members (Events)
| Name                | Type                  | Description                                      |
|---------------------|-----------------------|--------------------------------------------------|
| AgentEntersEvent    | listenable(agent)     | Triggered when a player enters the volume.       |
| AgentExitsEvent     | listenable(agent)     | Triggered when a player exits the volume.        |
| ZoneOccupiedEvent   | listenable(agent)     | First player enters (empty → occupied).        |
| ZoneEmptiedEvent    | listenable(agent)     | Last player leaves (occupied → empty).         |

---

## 🛠️ Functions & Methods
| Name                         | Description                                                 |
|------------------------------|-------------------------------------------------------------|
| `Enable()`                   | Activates the zone.                                        |
| `Disable()`                  | Deactivates the zone.                                      |
| `EnableVolumeLocking()`      | Locks players inside once they enter.                      |
| `DisableVolumeLocking()`     | Unlocks the volume.                                        |
| `GetAgentsInVolume()`        | Returns players currently inside the volume.               |
| `IsInVolume(agent)`          | Checks if a specific agent is inside the volume.           |
| `MoveTo()` / `TeleportTo()`  | Reposition or teleport the zone in the world.              |
| `GetTransform()`             | Retrieves the zone's position, rotation, and scale.        |

---

## 🎮 Configuration Options (Details Panel)
| Option                        | Description                                                                |
|------------------------------|----------------------------------------------------------------------------|
| Zone Visible During Game     | Toggle visual indicators of the zone.                                     |
| Zone Width/Depth/Height      | Set the physical dimensions of the volume.                                |
| Enabled During Phase         | Define active phases (None, Pre-Game, Gameplay, All).                     |
| Affected Team                | Restrict volume effect to a specific team or all.                          |
| Affected Class               | Restrict to a specific class, all, or none.                               |
| Push Force                   | Continuous directional push; relative to device rotation.                 |
| Lock Affected Players        | If on, traps players inside the zone.                                     |
| Launch Velocity              | Speed applied instantly upon entry.                                       |
| Allow Glider Deploy          | Toggle ability for players to deploy gliders.                             |
| Player Skydive FX            | Control VFX and SFX associated with skydiving.                            |

---

## 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

skydive_volume_example := class(creative_device):

    @editable
    SkydiveVolume : skydive_volume_device = skydive_volume_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    LockButton : button_device = button_device{}

    @editable
    UnlockButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SkydiveVolume.AgentEntersEvent.Subscribe(OnAgentEnters)
        SkydiveVolume.AgentExitsEvent.Subscribe(OnAgentExits)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        LockButton.InteractedWithEvent.Subscribe(OnLockPressed)
        UnlockButton.InteractedWithEvent.Subscribe(OnUnlockPressed)

    OnAgentEnters(Agent : agent) : void =
        Print("Agent entered the skydive volume!")

    OnAgentExits(Agent : agent) : void =
        Print("Agent exited the skydive volume!")

    OnEnablePressed(Agent : agent) : void =
        SkydiveVolume.Enable()
        Print("Skydive volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        SkydiveVolume.Disable()
        Print("Skydive volume disabled!")

    OnLockPressed(Agent : agent) : void =
        SkydiveVolume.EnableVolumeLocking()
        Print("Skydive volume locking enabled!")

    OnUnlockPressed(Agent : agent) : void =
        SkydiveVolume.DisableVolumeLocking()
        Print("Skydive volume locking disabled!")
```

---

## 📊 How It Works in UEFN
1. **Place Devices in Level**:
   - Drag `skydive_volume_device` to desired locations in your map.
   - Rotate to adjust launch direction.

2. **Configure Details Panel**:
   - Set size, FX, phase, launch settings, push force, locking, and affected team/class.

3. **Create & Build Verse Script**:
   - Create a `.verse` file in Verse Explorer, paste the example code, then build.

4. **Place and Assign Verse Device**:
   - Place your custom Verse device.
   - Assign `@editable` references in the Details panel.

5. **Test In-Game**:
   - Launch a play session and test entry, exit, lock/unlock, and events.

---

## 🧠 Best Practices
- Rotate devices to create directional air movement.
- Combine multiple zones to create air tunnels.
- Use runtime enable/disable for puzzles or secret routes.
- Lock agents for challenges or timed traps.
- Subscribe to volume events for gameplay logic (e.g., timers, unlocks).

---

## ❌ Incorrect Usage Examples and Fixes
| Issue                         | ❌ Wrong Example                           | ✅ Correct Example                                      | Explanation                                                  |
|------------------------------|-----------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
| Expecting zone affects all   | Zone placed with no team/class config         | Set "Affected Team/Class" to "Any"                          | Default filters may prevent effect.                         |
| Only visual config set       | Zone set to visible phase only                | Use `.Enable()` or `.Disable()` in Verse                    | Zone needs to be enabled via Verse.                         |
| Tried to set direction value | Edited direction in Details panel             | Rotate the device manually in editor                        | Device rotation controls direction.                         |
| Event not hooked             | Used `AgentEntersEvent` directly              | Use `.Subscribe(OnAgentEnters)`                             | Events must be subscribed in Verse.                         |
| Reference left unassigned    | Didn't assign `@editable` SkydiveVolume       | Assign it via Details panel                                 | Verse needs a reference to function properly.              |

---

## 🔹 Notes
- Chain multiple `skydive_volume_devices` for advanced traversal.
- Use locking features for escape rooms or mini-game logic.
- Integrate with VFX and SFX to enhance immersion.

