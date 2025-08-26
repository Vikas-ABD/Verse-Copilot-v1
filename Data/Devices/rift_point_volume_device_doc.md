# Rift Point Volume Device – UEFN Verse Device Documentation

## 🔹 Description
The `rift_point_volume_device` defines a special volume in Unreal Editor for Fortnite (UEFN) used for search and destroy gameplay. It allows players to plant or defuse the Rift Point item at a defined location. When a player with the Rift Point enters the volume, they can initiate a planting sequence. You can configure this device for teams, classes, timing, damage, detonation radius, and more. All actions such as planting, defusing, detonating, and entering/exiting the zone are programmable via Verse scripting.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `rift_point_volume_device`

## 🛠️ Key Events (Data Members)
| Name              | Type                | When It Fires                                      |
|-------------------|---------------------|----------------------------------------------------|
| PlantStartEvent   | listenable(agent)   | When a player begins planting                      |
| PlantCancelEvent  | listenable(agent)   | When a player cancels planting                    |
| PlantEvent        | listenable(agent)   | When planting is completed                        |
| DefuseStartEvent  | listenable(agent)   | When a player begins defusing                     |
| DefuseCancelEvent | listenable(agent)   | When defusing is cancelled                        |
| DefuseEvent       | listenable(agent)   | When a player completes defusing                  |
| DetonateEvent     | listenable(agent)   | When the Rift Point detonates (pass planter info) |
| OnAgentEntered    | listenable(agent)   | When a player enters the volume                   |
| OnAgentExited     | listenable(agent)   | When a player exits the volume                    |

## 🛠️ Key Methods & Functions
| Method               | Description                                               |
|----------------------|-----------------------------------------------------------|
| Enable()             | Enables the volume for planting/defusing                 |
| Disable()            | Disables all interaction with the volume                 |
| IsEnabled()          | Returns true if the device is currently enabled          |
| GetAgentsInVolume()  | Returns array of agents inside the volume                |
| IsInVolume(Agent)    | Checks if the specified agent is inside the volume       |
| GetTransform()       | Returns world transform (position, rotation, scale)      |
| MoveTo()/TeleportTo()| Moves the volume either instantly or with animation      |

## 🎛 Device Configuration (Details Panel)
| Option            | Description/Default                                      |
|-------------------|-----------------------------------------------------------|
| Plant Time        | How long to plant (default: 4s)                          |
| Defuse Time       | How long to defuse (default: 7s)                         |
| Detonation Time   | Timer from planting to explosion (default: 45s)          |
| Planting Team     | Teams allowed to plant                                   |
| Defusing Team     | Teams allowed to defuse                                  |
| Explosion Radius  | Radius of detonation damage                              |
| Damage            | Damage dealt upon explosion                              |
| Volume Shape/Size | Box, Cylinder, or Sphere with size options               |

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

rift_point_example := class(creative_device):

    @editable
    RiftVolume : rift_point_volume_device = rift_point_volume_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        RiftVolume.Enable()
        Print("Rift point volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        RiftVolume.Disable()
        Print("Rift point volume disabled!")
```

### Explanation:
- **RiftVolume**: Your placed rift_point_volume_device.
- **Enable/Disable Buttons**: Control the device using buttons.
- **Enable/Disable**: Turn interaction logic on/off.
- **Event Subscriptions**: Hook into planting/defusing logic and trigger custom scripts.

## 🔢 How to Use in UEFN
1. **Place Devices**
    - Place the `rift_point_volume_device` at your target objective location.
    - (Optional) Add control buttons.
2. **Configure Device**
    - Set teams, times, explosion damage, volume size/shape via the Details panel.
3. **Add Verse Script**
    - Open Verse Explorer: *Verse → Verse Explorer*
    - Right-click a folder > Create New Verse File (e.g., `rift_point_example.verse`)
    - Paste script, save, and build with `Ctrl+Shift+B`
    - Drag your Verse device into the world and assign fields
4. **Test and Extend**
    - Play your island and test planting.
    - Expand event handlers for objectives, rewards, UI, or progression logic.

## 🧠 Best Practices
- Use event subscriptions for custom effects, scoring, round tracking, and logic.
- Place multiple devices for multi-site gameplay.
- Combine with item granters, scoreboards, etc., for full Search & Destroy mechanics.

## ❌ Common Issues & Fixes
| Problem                   | Cause                                 | Solution                                        |
|---------------------------|----------------------------------------|-------------------------------------------------|
| Plant/defuse not possible | Device disabled or team not allowed   | Call `Enable()` and check team/class settings  |
| Event not firing          | No subscription in Verse              | Add `.Subscribe(...)` in `OnBegin` method      |
| Incorrect volume size     | Shape/size misconfigured              | Adjust in the Details panel                    |

## 📅 Notes
- Assign the Rift Point item to players using Item Granter or similar.
- Fully supports scripted Search and Destroy gameplay.
- For multiple objectives, use multiple volume devices and handle logic individually.

