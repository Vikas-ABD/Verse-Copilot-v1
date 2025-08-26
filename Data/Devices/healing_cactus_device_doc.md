## Healing Cactus Device – UEFN Verse Device Documentation

### 🔹 Description
The `healing_cactus_device` lets you spawn a cactus with healing fruit that, when burst, heals nearby players. Players can interact with it (shoot, hit, or touch with vehicles) to trigger the healing release. The cactus regrows after a delay and can be fully controlled (enabled/disabled, forced to grow/burst/heal) and scripted for custom objectives, wave defense, or unique item rewards.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `healing_cactus_device`

---

### 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the cactus, so it can interact and regrow. |
| `Disable()` | Disables the cactus; prevents interaction and regrowth, optionally hides the cactus. |
| `Grow()` | Forces the cactus to grow a healing fruit if enabled (subject to regrowth limits/settings). |
| `Burst()` / `Burst(agent)` | Bursts the cactus fruit, healing players nearby (`agent` = instigator, optional). |
| `SetInfiniteRegrowths(l)` | Allows infinite regrowths after bursting (`true`/`false`). |
| `SetMaximumRegrowths(i)` | Sets regrowth limit for this cactus. |
| `GetTransform()` | Returns world position/rotation/scale. |
| `MoveTo()` / `TeleportTo()` | Animates or teleports the cactus in world space. |

---

### 🧹 Events (Data Members)
| Name | Type | When It Fires |
|------|------|----------------|
| `GrowEvent` | `listenable(())` | When cactus grows (regrowth included). |
| `BurstEvent` | `listenable(?agent)` | When cactus is burst (instigator if any, else false). |

---

### 🎮 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| Heal Targets | Instigator Only, Same Team, Everyone (who gets healed) |
| Grow Automatically | Auto-regrow after burst (with delays, etc.) |
| Initial/Regrowth Delay | Delay before first growth/regrowth (seconds) |
| Infinite Regrowths | On/Off — if off, set Maximum Regrowths (per game) |
| Hide When Disabled | Cactus disappears when device is disabled |
| Can Grow in Storm | Cactus can regrow in storm zone |

---

### 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use healing_cactus_device
healing_cactus_example := class(creative_device):

    @editable
    Cactus : healing_cactus_device = healing_cactus_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    BurstButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to cactus events
        Cactus.GrowEvent.Subscribe(OnCactusGrew)
        Cactus.BurstEvent.Subscribe(OnCactusBurst)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        BurstButton.InteractedWithEvent.Subscribe(OnBurstPressed)

    # Event handlers
    OnCactusGrew() : void =
        Print("Healing cactus grew a new fruit!")

    OnCactusBurst(Agent : ?agent) : void =
        if (BurstAgent := Agent?):
            Print("Healing cactus burst by agent!")
        else:
            Print("Healing cactus burst automatically!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        Cactus.Enable()
        Print("Healing cactus enabled!")

    OnDisablePressed(Agent : agent) : void =
        Cactus.Disable()
        Print("Healing cactus disabled!")

    OnBurstPressed(Agent : agent) : void =
        Cactus.Burst()
        Print("Healing cactus burst by agent!")
```

#### Explanation
- **Cactus**: Reference to the placed `healing_cactus_device`.
- **EnableButton, DisableButton, BurstButton**: Button devices placed in the world and set in the Verse device’s Details panel.
- Core cactus events (bursts, regrowths) are subscribable in Verse for scoring, progression, or puzzle logic.
- Code demonstrates manual and event-driven interaction, and the use of `.Burst()`, `.Enable()`, `.Disable()` functions.

---

### 🚀 How to Use in UEFN
1. **Place Devices**
   - Place a `healing_cactus_device` in your world.
   - Optionally, place `button_device` actors for Enable, Disable, and Burst.

2. **Configure in the Details Panel**
   - Set Heal Targets, auto-regrow, delays, infinite regrowths, visibility, etc.

3. **Create & Add Verse Script**
   - Open Verse Explorer from UEFN menu.
   - Create a new Verse file (e.g., `healing_cactus_example.verse`).
   - Paste and save the provided code.
   - Build code (`Ctrl+Shift+B`) until "Build Succeeded."
   - Drag your custom Verse device into the world and assign all `@editable` fields.

4. **Test & Expand**
   - Launch and test cactus behavior.
   - Expand event handlers for advanced gameplay: scoring, VFX/SFX, wave logic, hazards, etc.

---

### 🧠 Best Practices
- Control cactus regrowth/limits for round-based healing and challenge design.
- Subscribe to `BurstEvent` to award points, trigger effects, or advance game states.
- Use `Burst(agent)` to attribute healing to specific players.

---

### ❌ Common Issues & Fixes
| Problem | Reason | Solution |
|---------|--------|----------|
| Won’t regrow | Maximum regrowths reached or device disabled | Enable again and raise limit or set infinite |
| No healing on burst | Targeting not set for team/everyone | Adjust "Heal Targets" in Details panel |
| Device doesn’t respond | References not assigned; Verse not built | Check all assignments and build completion |

---

### 🔎 Notes
- For search-and-destroy or healing puzzles, combine with traps, volumes, triggers, and advanced Verse scripting.
- All cactus behaviors—enable/disable, regrow, burst—are fully programmable and can be controlled via Verse or creative triggers.

