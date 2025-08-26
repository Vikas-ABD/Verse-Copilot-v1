📘 **effect_volume_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `effect_volume_device` is a **base class** for volume-type devices with unique gameplay effects (such as damage, gravity, or custom areas). It is typically **not placed directly**, but subclassed by other devices like `damage_volume_device` or mutator zone types. However, it may be referenced or interacted with in **Verse** scripts for custom or advanced logic.

### 🧱 Verse Using Statement
```verse
verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `effect_volume_device`

### 🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| AgentEntersEvent | listenable(agent) | Fires when any agent enters the volume. |
| AgentExitsEvent | listenable(agent) | Fires when any agent exits the volume. |
| AgentBeginsEmotingEvent | listenable(agent) | Fires when an agent inside the zone starts emoting. |
| AgentEndsEmotingEvent | listenable(agent) | Fires when an agent in the zone ends emoting. |
| ZoneEmptiedEvent | listenable(agent)* | Fires when the last agent leaves the zone. |
| ZoneOccupiedEvent | listenable(agent)* | Fires when the zone goes from empty to occupied. |
> *Availability may depend on subclass or zone settings.

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| Enable() | Enables the volume—triggers events and applies effects if configured. |
| Disable() | Disables the volume—no effects or event triggers while disabled. |
| GetAgentsInVolume() | Returns array of all agents currently in the zone. |
| IsInVolume(agent) | Returns `true` if agent is inside the area. |
| SetDamage(int)* | Subclass only: sets per-tick damage, clamped [1–500]. |
| GetDamage()* | Subclass only: gets per-tick damage. |
| UpdateSelectedClass(agent) | Sets device to affect agent’s class/team (subclass usage). |
| UpdateSelectedTeam(agent) | Sets device to affect agent’s class/team (subclass usage). |
| MoveTo/TeleportTo/GetTransform | Move, teleport, or get world transform of device. |

### 🎛 Configuration Options
> Set via subclass only (e.g., `damage_volume_device`, `mutator_zone_device`) in the Details panel:
- Width/Height
- Team/Class targeting
- Shape
- Effect type
- Damage amount
- Visual state, etc.

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

effect_volume_example := class(creative_device):

    @editable
    EffectVolume : mutator_zone_device = mutator_zone_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EffectVolume.AgentEntersEvent.Subscribe(OnAgentEnters)
        EffectVolume.AgentExitsEvent.Subscribe(OnAgentExits)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnAgentEnters(Agent : agent) : void =
        Print("Agent entered the effect volume!")

    OnAgentExits(Agent : agent) : void =
        Print("Agent exited the effect volume!")

    OnEnablePressed(Agent : agent) : void =
        EffectVolume.Enable()
        Print("Effect volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        EffectVolume.Disable()
        Print("Effect volume disabled!")
```

### 📌 How it works in UEFN
1. **Place Devices In Level:**
   - Use a subclass (e.g., `damage_volume_device`, `mutator_zone_device`).
   - Size/shape via transform in the editor.

2. **Configure Subclass Settings:**
   - Set effect type, target class/team, tick rate, etc., in the Details panel.

3. **Create and Build Verse Script:**
   - Add a new Verse file (e.g., `effect_volume_example.verse`).
   - Paste and save code, then **Build Verse** (CTRL+SHIFT+B).

4. **Assign References in Editor:**
   - Assign `EffectVolume`, `EnableButton`, and `DisableButton` via Details panel.

5. **Test In-Game:**
   - Launch a session, enter the zone, check logs, and test buttons.

### 🧠 Best Practices
- Use `AgentEntersEvent` / `AgentExitsEvent` for gameplay logic (e.g., eliminations, scoring).
- Use subclasses for actual effects.
- Use `.Enable()` / `.Disable()` for dynamic gameplay logic.
- Query contents with `GetAgentsInVolume()` for zone logic (e.g., capture or scoring).

### ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|----------|------------|-------------|
| Setting effect on base class | `EffectVolume.SetDamage(100)` | Use on a `damage_volume_device` | Only subclass supports it |
| Using events without subscribe | `EffectVolume.AgentEntersEvent` | `EffectVolume.AgentEntersEvent.Subscribe(OnEnter)` | Must subscribe |
| Placing base class | Placing `effect_volume_device` directly | Place via a subclass device | Base is not placeable |
| Missing device references | Left `DamageVolume` blank | Assign all devices in Details panel | Verse requires reference wiring |

---
**Note:**
- Always use subclasses for gameplay effects.
- Consult subclass docs for feature availability.
- Use base class only for advanced scripting or shared logic patterns.

