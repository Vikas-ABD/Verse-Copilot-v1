## Nitro Hoop Device – UEFN Verse Device Documentation

### 📙 Description
The `nitro_hoop_device` creates a flaming hoop that, when triggered, accelerates players and vehicles and grants them a nitro boost effect. Ideal for racing maps, parkour, or high-speed gameplay. The device can be enabled/disabled and offers full control over cooldown and trigger logic via Verse or in-editor event wiring.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `nitro_hoop_device`

### 🛠️ Key Functions & Methods
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the hoop (accepts triggers and gives boosts). |
| `Disable()` | Disables the hoop (ignores triggers). |
| `AllowCooldown()` | Enables automatic cooldown after a trigger. |
| `DisallowCooldown()` | Disables automatic cooldown; can be re-triggered immediately. |
| `StartCooldown(float)` | Forces cooldown for a specified time (1.0s minimum). |
| `SetDefaultCooldownDuration(float)` | Sets default cooldown time (1–60s). |
| `SetCooldownDelay(float)` | Sets delay (0–5s) before cooldown starts after trigger. |
| `IsEnabled()` | Returns whether the hoop is currently enabled. |
| `GetDefaultCooldownDuration()` | Gets current default cooldown value. |
| `GetCooldownDelay()` | Gets current delay before cooldown. |
| `MoveTo()` / `TeleportTo()` | Changes hoop's position/rotation in the level. |

### 🤩 Events (Data Members)
| Name | Type | When It Fires |
|------|------|----------------|
| `PlayerTriggeredEvent` | `listenable(agent)` | A player runs or drives through the hoop. |
| `VehicleTriggeredEvent` | `listenable(?agent)` | A vehicle (with driver) passes through. |
| `CooldownStartEvent` | `listenable(tuple())` | Hoop enters cooldown. |
| `EnabledEvent` | `listenable(tuple())` | Hoop is re-enabled. |

### 🎛 Device Configuration (Details Panel)
- **Base Type/Columns/Stand** – Adjust hoop's visual style and mount
- **Enable On Phase** – Choose when the hoop is active (Always / Pre-Game / Gameplay Only)
- **Enable Cooldown** – Toggle automatic cooldown after trigger
- **Cooldown Duration** – Duration hoop stays disabled after use
- **Cooldown at Game/Round Start** – Start in cooldown on match begin
- **Velocity/Boost Options** – Boost strength and behavior
- **Visibility/FX** – Configure mesh and effects per game phase

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

nitro_hoop_example := class(creative_device):

    @editable
    NitroHoop : nitro_hoop_device = nitro_hoop_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    CooldownButton : button_device = button_device{}

    var IsEnabled : logic = true

    OnBegin<override>()<suspends> : void =
        NitroHoop.PlayerTriggeredEvent.Subscribe(OnPlayerTriggered)
        NitroHoop.VehicleTriggeredEvent.Subscribe(OnVehicleTriggered)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        CooldownButton.InteractedWithEvent.Subscribe(OnCooldownPressed)

    OnPlayerTriggered(Agent : agent) : void =
        Print("Nitro hoop triggered by player!")

    OnVehicleTriggered(Agent : ?agent) : void =
        Print("Nitro hoop triggered by vehicle!")

    OnEnablePressed(Agent : agent) : void =
        set IsEnabled = true
        NitroHoop.Enable()
        Print("Nitro hoop enabled!")

    OnDisablePressed(Agent : agent) : void =
        set IsEnabled = false
        NitroHoop.Disable()
        Print("Nitro hoop disabled!")

    OnCooldownPressed(Agent : agent) : void =
        if (IsEnabled = true):
            NitroHoop.StartCooldown(3.0)
            Print("Nitro hoop cooldown started!")
```

### 🔎 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add a `nitro_hoop_device` where boost triggers should occur.
   - Optionally, add three `button_device`s for control.

2. **Configure Device Settings**
   - In the Details panel, set:
     - Appearance options (Base, Columns, FX)
     - Cooldown options
     - Velocity and visibility settings

3. **Create & Add Your Verse Script**
   - Use **Verse Explorer** > Create new Verse file
   - Paste and save example code
   - Build (Ctrl+Shift+B)
   - Add Verse device in level

4. **Assign Editable References**
   - In the Verse device's Details:
     - Assign `NitroHoop` to the hoop
     - Assign `EnableButton`, `DisableButton`, `CooldownButton`

5. **Test Your Setup**
   - Playtest and use buttons to control and observe hoop behavior

### 🤔 Best Practices
- Use cooldown logic to manage boost spam
- Combine with scoring/timer/event devices for dynamic gameplay
- Fine-tune velocity for map design and difficulty
- Chain hoops with event triggers for combos

### ❌ Common Issues & Fixes
| Issue | Problem | Solution | Explanation |
|-------|---------|----------|-------------|
| No boost | Hoop disabled / in cooldown | Call `.Enable()` and check cooldown | Must be active and not cooling down |
| Cooldown ignored | Not configured | Set proper duration or use `StartCooldown()` | Cooldown logic must be enabled |
| No trigger reaction | Events not subscribed | Use `.Subscribe()` for triggers | Event hooks required in Verse |
| Invisible hoop | Hidden mesh or FX | Adjust visibility in Details panel | Display options may vary by phase |

### 💡 Notes
- Ideal for racing, escape, or speed-based challenges
- Built-in trigger/boost logic
- Use Verse to extend with scoring, VFX, elimination, or timers

