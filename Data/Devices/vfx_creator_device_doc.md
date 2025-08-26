## VFX Creator Device – UEFN Verse Device Documentation

### 📙 Description
The `vfx_creator_device` is a highly customizable visual effects tool in UEFN (Unreal Editor for Fortnite) that allows creators to build and control their own particle systems or visual effects. Unlike the `vfx_spawner_device`, this device offers extensive flexibility, making it ideal for dynamic, gameplay-driven VFX.

You can:
- Start, stop, pause, or move VFX dynamically
- Bind effects to players (agents) for tailored experiences

**Common Use Cases:**
- Custom ability effects
- Cinematic sequences
- Dynamic combat visuals
- Environmental or hazard-based visuals

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
| Class | Description |
|-------|-------------|
| `creative_object` | Base class for props and devices |
| `creative_device_base` | Adds enable/disable logic |
| `vfx_creator_device` | Enables creation and control of custom VFX in-game |

---

### ↻ Main Event
This device does **not emit listenable events**, but provides full visual control through a **rich set of callable methods**.

---

### 🛠️ Core Methods
| Method | Description |
|--------|-------------|
| `Begin(): void` | Starts effect at device's world location |
| `Begin(Agent: agent): void` | Starts effect at agent's location (requires Stick to Player) |
| `BeginForAll(): void` | Starts effect for all agents (requires Stick to Player) |
| `End(): void` | Stops effect at device location |
| `End(Agent: agent): void` | Stops effect for a specific player |
| `EndForAll(): void` | Stops effect for all players |
| `Toggle(): void` | Toggles effect on/off at device position |
| `Toggle(Agent: agent): void` | Toggles effect for specific agent |
| `ToggleForAll(): void` | Toggles effect for all agents |
| `ToggleEnabled(): void` | Switches between Enable and Disable |
| `TogglePause(): void` | Pauses/resumes effect at device location |
| `TogglePause(Agent: agent): void` | Pauses/resumes for specific player |
| `TogglePauseForAll(): void` | Pauses/resumes for all agents |
| `SpawnAt(Agent: agent): void` | Spawns one-time effect at agent location |
| `Remove(Agent: agent): void` | Detaches from agent but keeps effect active |
| `RemoveFromAll(): void` | Detaches from all agents, resumes at device |
| `Enable(): void` | Enables the device (required before use) |
| `Disable(): void` | Disables the device |
| `GetTransform(): transform` | Returns current transform of device |
| `TeleportTo(...) / MoveTo(...)` | Repositions the device in the world |

---

### ⚙️ Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Stick to Player | Attaches effect to a specific agent |
| Looping Behavior | Sets looping vs one-shot playback |
| Auto Play on Enable | Plays effect automatically when enabled |
| Effect Scale | Controls scale of visual effect |
| Effect Template | Set custom Niagara or particle system |
| Preview in Editor | Enables preview inside UEFN editor |

---

### 🚦 Common Usage: Step-by-Step
```verse
using { /Fortnite.com/Devices }

vfx_handler := class(
    @editable VFX: vfx_creator_device
)

OnBegin<override>()<suspends>: void =
    VFX.Enable()
    VFX.Begin()  # Start effect at device location

TriggerOnPlayer(Player: agent): void =
    VFX.Begin(Player)  # Trigger effect on specific agent

EndEffectOnPlayer(Player: agent): void =
    VFX.End(Player)  # Stop effect for specific agent
```

---

### 🧠 Best Practices
- Use **Stick to Player** when attaching VFX to characters
- Combine with `button_device`, `trigger_device`, or gameplay events
- Use `TogglePause()` for cinematic freeze-frame effects
- Sync VFX with sound using `audio_player_device`
- Use `SpawnAt()` for bursts or one-shot explosions

---

### ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Fix | Explanation |
|-------|------------|----------|-------------|
| Using `Begin(Player)` without Stick to Player | `VFX does nothing` | Enable Stick to Player | Required for agent-based VFX |
| No visible effect after `Enable()` | Device not configured | Set VFX template | Needs Niagara or particle system |
| Forgetting to `Enable()` | `Begin()` fails | Call `Enable()` first | Device must be enabled to function |

---

### 🚀 Ideal Use Cases
- Spell casting and custom abilities
- Impact or explosion effects
- Ambient or area-based storytelling
- Player transformations or power-ups
- Cinematic cutscenes and sequences

