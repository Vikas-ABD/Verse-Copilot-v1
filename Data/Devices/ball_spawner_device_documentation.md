## ball_spawner_device – UEFN Verse Device Documentation

### 🔹 Description
The `ball_spawner_device` is used to spawn various ball types (such as generic ball, beach ball) for interactive games and mechanics like dodgeball, soccer, capture zones, and more. It allows control over ball physics, size, color, respawning behavior, and HUD markers. You can spawn, enable/disable, and show/hide HUD markers using Verse logic or Creative wiring.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `ball_spawner_device`

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Activates the device, spawning the ball according to settings. |
| `Disable()` | Deactivates the spawner; disables balls and respawning. |
| `ShowHUD()` | Shows floating HUD icons (if configured on device) to help players locate balls. |
| `HideHUD()` | Hides HUD icons related to spawned balls. |
| `GetTransform()` | Gets device’s world position, rotation, and scale. |
| `MoveTo()` / `TeleportTo()` | Move or teleport device. |

### 🧹 Events
- This device does **not** emit custom events in Verse; all control is by method and device logic.

### 🎠 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Ball Type | Generic Ball, Beach Ball (affects mesh/physics) |
| Base Visible During Game | Show/hide the spawner’s platform visual |
| Enabled During Phase | None/Always/Pre-Game/Game Only/Create Only |
| Ball Size | Set the size (default: 2.28) |
| Gravity | Set gravity override for the ball |
| Maximum Distance Range | Distance before the ball respawns automatically |
| Respawn Delay | Time in seconds before a destroyed/consumed ball respawns |
| Ball Roughness/Metalness | Visual customization for surface effects |
| Ball Color | Color picker, including hex code |
| Ball Logo Brightness | Adjust logo material brightness |
| Mass/Linear Damping/Angular Damping | Modify physical reactions to bumps, rolls, spin, and hits |
| Player Knockback/Impulse | Tweak ball-to-player interactions (on hit, on pickaxe, etc.) |
| Eliminate Player When Touched | Instantly eliminates any player that contacts the ball |

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use ball_spawner_device with button controls
ball_spawner_example := class(creative_device):

    @editable
    BallSpawner : ball_spawner_device = ball_spawner_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    ShowHUDButton : button_device = button_device{}

    @editable
    HideHUDButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to button events
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        ShowHUDButton.InteractedWithEvent.Subscribe(OnShowHUDPressed)
        HideHUDButton.InteractedWithEvent.Subscribe(OnHideHUDPressed)

    # Button control handlers
    OnSpawnPressed(Agent : agent) : void =
        BallSpawner.Enable()
        Print("Ball spawner enabled!")

    OnShowHUDPressed(Agent : agent) : void =
        BallSpawner.ShowHUD()
        Print("Ball HUD shown!")

    OnHideHUDPressed(Agent : agent) : void =
        BallSpawner.HideHUD()
        Print("Ball HUD hidden!")
```

### ⚖️ How it Works in UEFN
1. **Place Devices in Level**:
   - Drag a `ball_spawner_device` into the map.
   - Add any `button_devices` for runtime control.
2. **Configure Options (Details Panel)**:
   - Set ball type, size, color, gravity, respawn behavior, etc.
   - Enable “Eliminate Player When Touched” if needed.
3. **Create & Build Verse Script**:
   - Create new Verse file (e.g., `ball_spawner_example.verse`).
   - Paste example code, save.
   - Click Verse → Build Verse Code or press CTRL+SHIFT+B.
4. **Place & Reference Verse Device**:
   - Drag `ball_spawner_example` into the island.
   - Assign `BallSpawner`, `SpawnButton`, `ShowHUDButton`, and `HideHUDButton` via Details panel.
5. **Test Gameplay**:
   - Use buttons to enable/disable the spawner and toggle HUD icons. Ball spawns per settings.

### 🧠 Best Practices
- Combine with elimination zones for dodgeball/soccer/puzzle games.
- Use `.ShowHUD()` and `.HideHUD()` for on-demand guidance.
- Tweak Ball Size and Gravity for gameplay variety.
- Use elimination on contact for instant-elimination modes.
- Combine with Zone/Capture Area devices for complex logic.

### ❌ Incorrect Usage & How to Fix
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|--------------------|-----------------------|-------------|
| Not calling Enable() | Placed but didn’t call `.Enable()` | `BallSpawner.Enable()` | Balls only spawn when enabled. |
| Wiring HUD directly | Wired ShowHUD, no effect | `BallSpawner.ShowHUD()` | Must be triggered via Verse/event. |
| Unassigned device refs | Left BallSpawner blank | Assign in Details panel | All @editable refs must be linked. |
| No elimination config | Ball didn’t eliminate players | Set "Eliminate Player When Touched" to On | Must configure in Details panel. |
| Runtime color/size | Tried `BallSpawner.SetColor()` | Set color/size in Details panel | Not configurable via Verse methods. |

### 🔹 Note
- This device does not support spawning custom static meshes or coins.
- Use only for supported ball games.
- For advanced mechanics, combine with triggers, captures, and HUD cues.

