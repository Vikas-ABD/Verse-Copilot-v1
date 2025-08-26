📘 wilds_plant_device – UEFN Verse Device Documentation

🔹 Description
The wilds_plant_device generates an interactive plant with an explosive pod that players can launch or detonate in Unreal Editor for Fortnite (UEFN). The plant can be enabled/disabled, forced to grow, or made to explode/launch its pod on command. It’s versatile for environmental hazards, puzzles, powerups, or tactical map features. All launch, explosion, and growth events can be scripted in Verse and the device is highly configurable in the Details panel.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- wilds_plant_device

🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| Enable() | Enables the device; allows growth and interaction. |
| Disable() | Disables the device; prevents growth and player interaction. |
| Grow() | Forces the plant to grow/regrow (if not at max regrowths). |
| Explode() | Forces immediate explosion of the pod (if enabled). |
| SetInfiniteRegrowths(l) | Allows infinite regrowths after launch/destruction (logic true/false). |
| SetMaximumRegrowths(i) | Sets how many regrowths are allowed (when infinite is false; up to 100). |
| MoveTo() / TeleportTo() | Animates or teleports the plant to a new position/rotation. |
| GetTransform() | Returns world transform (location/rotation/scale) for the plant. |

🧹 Events (Data Members)
| Name | Type | When It Fires |
|------|------|----------------|
| ExplodeEvent | listenable(?agent) | When the plant or launched projectile explodes. Sends triggering agent or false. |
| GrowEvent | listenable(tuple()) | When the plant grows (including regrowths). |
| LaunchEvent | listenable(?agent) | When the plant launches a pod. Sends agent if launch was player-triggered. |

🎛 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| Launch on Hit | On/Off; whether hitting launches or explodes pod. |
| Grow Automatically | True/False/Initial Only/Regrowth Only (controls auto regrow). |
| Infinite Regrowths | On/Off; if Off, set Maximum Regrowths (max: 100). |
| Regrowth Delay | Seconds before regrowing after pod is launched/exploded. |
| Can Grow in Storm | On/Off. |
| Hide When Disabled | True/False/Show Leaves. Device disappears when disabled. |

🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

wilds_plant_example := class(creative_device):

    @editable
    PlantDevice : wilds_plant_device = wilds_plant_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ExplodeButton : button_device = button_device{}

    @editable
    GrowButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        PlantDevice.ExplodeEvent.Subscribe(OnPlantExploded)
        PlantDevice.GrowEvent.Subscribe(OnPlantGrew)
        PlantDevice.LaunchEvent.Subscribe(OnPlantLaunched)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ExplodeButton.InteractedWithEvent.Subscribe(OnExplodePressed)
        GrowButton.InteractedWithEvent.Subscribe(OnGrowPressed)

    OnPlantExploded(Agent : ?agent) : void =
        Print("Wilds plant exploded!")

    OnPlantGrew() : void =
        Print("Wilds plant grew!")

    OnPlantLaunched(Agent : ?agent) : void =
        Print("Wilds plant pod launched!")

    OnEnablePressed(Agent : agent) : void =
        PlantDevice.Enable()
        Print("Wilds plant enabled!")

    OnDisablePressed(Agent : agent) : void =
        PlantDevice.Disable()
        Print("Wilds plant disabled!")

    OnExplodePressed(Agent : agent) : void =
        PlantDevice.Explode()
        Print("Wilds plant exploded by agent!")

    OnGrowPressed(Agent : agent) : void =
        PlantDevice.Grow()
        Print("Wilds plant grew by agent!")
```

🔍 Explanation
- **PlantDevice**: Reference to a placed wilds_plant_device.
- **Button Devices**: Used for demonstration and interaction control.
- **Event Subscriptions**: ExplodeEvent, GrowEvent, LaunchEvent are hooked in OnBegin.
- **Event Handlers**: Each handles specific interaction and logs output.

📆 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add a wilds_plant_device and four button_device actors to the map.

2. **Edit Plant in Details Panel**
   - Configure settings like Launch on Hit, regrowth options, storm behavior, etc.

3. **Create and Add Your Verse Script**
   - Open Verse Explorer → Create New Verse File → paste and save the example.
   - Build the project and ensure success.
   - Drag your custom Verse device into the level.

4. **Configure Editable References**
   - In your custom device’s Details panel, assign the buttons and plant.

5. **Test in Play Session**
   - Use the buttons to trigger actions and observe plant behavior.

🧠 Best Practices
- Chain multiple wilds_plant_device actors for combo puzzles or challenges.
- Use events to trigger doors, points, hazards, or wave spawns.
- Control regrowth for escalation or player strategy development.

❌ Common Issues & Fixes
| Problem | Reason | Solution |
|---------|--------|----------|
| Pod won’t regrow | Maximum regrowth reached/infinite off | Use SetInfiniteRegrowths(true) or raise max. |
| Events not firing | Not subscribed in Verse OnBegin | Ensure .Subscribe(handler) is used correctly. |
| Device invisible | "Hide When Disabled" = True | Set Hide When Disabled = False. |

📅 Note
- Use multiple wilds_plant_device actors for advanced sequencing or chain reactions.
- Explosion, growth, and launch logic can be scripted for custom environmental effects.

