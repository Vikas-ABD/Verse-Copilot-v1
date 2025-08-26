# fire_volume_device – UEFN Verse Device Documentation

## 🔹 Description
The `fire_volume_device` defines a volume in your Fortnite island where objects, buildings, or terrain can be set on fire or prevented from burning. It can be used to:
- Limit or allow wildfire mechanics
- Create fireproof zones
- Choreograph fire spread for quests and puzzles
- Control flammable hazard gameplay

You can ignite/extinguish the area using Verse scripts or event actions. The device allows configuration of size, permissions, and visibility via the details panel.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `effect_volume_device`
- `fire_volume_device`

## 🧩 Functions & Methods
| Name             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `Enable()`       | Activates the fire volume so it can participate in fire/ignition logic.     |
| `Disable()`      | Deactivates fire logic—objects in this area cannot be set on fire.          |
| `Ignite()`       | Ignites all objects inside the volume.                                     |
| `Extinguish()`   | Extinguishes all fires inside the volume.                                  |
| `MoveTo()`/`TeleportTo()` | Move or teleport the volume within the world.                      |
| `GetTransform()` | Gets the world position/rotation/scale of the device.                      |

## 🧹 Events
- No direct Verse events; state is controlled by scripting, wires, or device logic.

## 🎛 Configuration Options (Details Panel)
| Option                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Enabled at Game Start      | Start the volume as active/inactive. Recommended: off for dynamic control. |
| Zone Visible During Game   | Enable to show ember FX for easier visualization.                          |
| Zone Width/Depth/Height    | Define the volume size in creative tiles/meters.                           |
| Allow Objects to Ignite    | Override island-wide settings with Yes/No or follow island defaults.       |

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use fire_volume_device with basic controls
fire_volume_example := class(creative_device):

    @editable
    FireVolume : fire_volume_device = fire_volume_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    IgniteButton : button_device = button_device{}

    @editable
    ExtinguishButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        IgniteButton.InteractedWithEvent.Subscribe(OnIgnitePressed)
        ExtinguishButton.InteractedWithEvent.Subscribe(OnExtinguishPressed)

    OnEnablePressed(Agent : agent) : void =
        FireVolume.Enable()
        Print("Fire volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        FireVolume.Disable()
        Print("Fire volume disabled!")

    OnIgnitePressed(Agent : agent) : void =
        FireVolume.Ignite()
        Print("Fire volume ignited!")

    OnExtinguishPressed(Agent : agent) : void =
        FireVolume.Extinguish()
        Print("Fire volume extinguished!")
```

## 🧠 How It Works in UEFN
1. **Place Devices in Level:**
   - Add `fire_volume_device` to the desired region.
   - Add `button_device` for controls (optional for interactivity).

2. **Configure in Details Panel:**
   - Set size, visibility, and ignition permissions.
   - Decide whether the volume starts enabled.

3. **Create & Build Verse Script:**
   - Use the Verse Explorer to create a new file.
   - Paste the example script and build it using **Verse → Build Verse Code** or `Ctrl+Shift+B`.

4. **Place & Reference Devices:**
   - Drag the Verse device into the world.
   - Assign all `@editable` references in the Details panel.

5. **Test in a Session:**
   - Launch a session and use the buttons to test the fire logic.

## 🧠 Best Practices
- Use multiple volumes for safe and hazard zones.
- Use `Ignite()` and `Extinguish()` in scripted events (e.g., puzzles, bosses).
- Combine with game-phase or player-driven logic.
- Override island settings with “Allow Ignite” in specific volumes.

## ❌ Common Mistakes & Fixes
| Issue                            | ❌ Wrong Example                       | ✅ Correct Example                                  | Explanation                                              |
|----------------------------------|-----------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Fire doesn’t spread automatically| Did not enable fire or volume           | Call `FireVolume.Enable()` before use                    | Fire logic only works when the volume is active.         |
| Trying to ignite when disabled   | `FireVolume.Ignite()` while disabled    | Enable first using `FireVolume.Enable()`                 | Device must be active to respond to ignition commands.   |
| No ember FX visible              | "Zone Visible" set to No                | Enable "Zone Visible" in the Details panel               | FX is off unless enabled explicitly.                     |
| Missing device assignments       | Left `FireVolume`/buttons unassigned    | Assign all devices in the Details panel                  | Verse script needs actual device references to work.     |
| Only using Details permissions   | Only changed “Allow Ignite”             | Use `Ignite()`/`Extinguish()` as well for events         | Details panel sets default, not real-time control.       |

## 📅 Notes
- Use Verse or creative event wires to ignite/extinguish zones dynamically.
- The "Allow Ignite" option overrides global settings but does not replace runtime logic.
- Fire logic is limited to Fortnite’s engine rules on spread and object eligibility.

