## Nitro Barrel Spawner Device – UEFN Verse Device Documentation

### 🔹 Description
The `nitro_barrel_spawner_device` spawns a destructible barrel prop that, when destroyed, applies the **Nitro effect** to all nearby players and vehicles. Nitro temporarily boosts movement speed and handling, making this device ideal for races, arena hazards, or dynamic powerup gameplay in Unreal Editor for Fortnite (UEFN). The device can be controlled via Verse or device wiring and includes options for respawn timing, force multipliers, and launch behavior.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `nitro_barrel_spawner_device`

---

### 🛠️ Key Methods & Functions
| Method                     | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `Enable()`                | Enables and spawns the barrel (if it’s not already present).               |
| `Disable()`               | Hides and removes the barrel. Disables the device—no Nitro effect triggered.|
| `AllowRespawn()`          | Allows the barrel to respawn after being destroyed.                         |
| `DisallowRespawn()`       | Prevents the barrel from respawning after destruction.                      |
| `SetRespawnDelay(float)` | Sets time to wait before respawn.                                          |
| `GetRespawnDelay()`       | Gets the current respawn delay in seconds.                                  |
| `SetLaunchForceMultiplier(float)` | Sets launch force when barrel is shot/launched (0.25–3.0).         |
| `GetLaunchForceMultiplier()`     | Returns current launch force multiplier.                       |
| `GetTransform()`          | Returns location/rotation as a transform struct.                            |
| `MoveTo()` / `TeleportTo()` | Animates or instantly moves the barrel to a new location.                |
| `IsEnabled()`             | Returns `true` if barrel is enabled and visible.                            |
| `IsRespawnAllowed()`      | Returns `true` if respawn is enabled.                                       |

---

### 🤩 Events (Data Members)
| Name            | Type               | Description                                        |
|-----------------|--------------------|----------------------------------------------------|
| `LaunchedEvent` | `listenable(?agent)` | Fires when barrel is launched (includes agent).   |
| `ExplodedEvent` | `listenable(?agent)` | Fires when barrel explodes (includes agent).      |

---

### 🎯 Device Configuration (Details Panel)
- **Start Enabled**: Is barrel present at round start?
- **Launch Force Multiplier**: Force applied (range: 0.25–3.0).
- **Should Respawn**: Should the barrel respawn after elimination?
- **Respawn Delay**: Seconds to wait before respawning.

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Characters }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

nitro_barrel_demo := class(creative_device):

    @editable
    NitroBarrel : nitro_barrel_spawner_device = nitro_barrel_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    NitroRadius : float = 500.0

    OnBegin<override>()<suspends> : void =
        NitroBarrel.LaunchedEvent.Subscribe(OnBarrelLaunched)
        NitroBarrel.ExplodedEvent.Subscribe(OnBarrelExploded)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnBarrelLaunched(Agent : ?agent) : void =
        Print("Nitro barrel launched!")

    OnBarrelExploded(Agent : ?agent) : void =
        Print("Nitro barrel exploded!")
        BarrelTransform := NitroBarrel.GetTransform()
        NearbyAgents := GetPlayspace().GetPlayers()
        for (Player : NearbyAgents):
            if (AgentChar := Player.GetFortCharacter[]):
                AgentPos := AgentChar.GetTransform().Translation
                if (Distance(BarrelTransform.Translation, AgentPos) <= NitroRadius):
                    Print("Applying Nitro effect to nearby agent")

    OnEnablePressed(Agent : agent) : void =
        NitroBarrel.Enable()
        Print("Nitro barrel enabled!")

    OnDisablePressed(Agent : agent) : void =
        NitroBarrel.Disable()
        Print("Nitro barrel disabled!")
```

---

### 📄 How to Use in UEFN
1. **Place Devices in Level**
    - Add `nitro_barrel_spawner_device`
    - Add two `button_device`s (Enable/Disable)
2. **Configure Barrel via Details Panel**
    - Set initial state, respawn settings, launch multiplier, etc.
3. **Create and Add Verse Script**
    - In Verse Explorer: Right-click → Create New Verse File
    - Paste the provided code, save, then build (Ctrl+Shift+B)
4. **Assign Editable References**
    - Set `NitroBarrel`, `EnableButton`, `DisableButton` in the details panel
5. **Playtest**
    - Use the buttons to enable/disable barrel, destroy it in-game, and test Nitro effects

---

### 🧠 Best Practices
- Create high-risk/high-reward gameplay areas using Nitro barrels.
- Script advanced logic with `ExplodedEvent` (score, VFX, powerups).
- Adjust `SetRespawnDelay`, `AllowRespawn`, `Disable` for dynamic challenges.

---

### ❌ Common Issues & Fixes
| Issue                  | Cause                               | Solution                                      |
|------------------------|--------------------------------------|-----------------------------------------------|
| Barrel doesn’t respawn | Respawn off or delay set too high   | Set "Should Respawn" on and lower delay       |
| Nitro not applied      | Barrel disabled or players out of range | Enable device and check NitroRadius       |
| No event output        | Events not subscribed in Verse      | Ensure proper event subscriptions             |

---

### 💡 Notes
- Nitro effect auto-applies to players/vehicles in range—no coding needed.
- Use `ExplodedEvent` for additional gameplay logic (VFX, scoring, etc).
- Always fill all `@editable` fields in your Verse device.
- Confirm "Build Succeeded" after code changes.

